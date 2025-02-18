from scapy.all import sniff, TCP, IP, conf

# Variável global para contar alertas
alert_count = 0

# Função que processa cada pacote capturado
def process_packet(packet):
    global alert_count
    # Verifica se o pacote possui a camada TCP
    if packet.haslayer(TCP):
        tcp_layer = packet.getlayer(TCP)
        # Verifica se o pacote possui a camada IP para obter os endereços de origem e destino
        if packet.haslayer(IP):
            ip_layer = packet.getlayer(IP)
            # Regra de exemplo: se a porta de destino for 23 (Telnet), alerta sobre atividade suspeita
            if tcp_layer.dport == 23:
                print("ALERTA: Atividade suspeita detectada!")
                print(f"IP de origem: {ip_layer.src}, IP de destino: {ip_layer.dst}, Porta de destino: {tcp_layer.dport}")
                alert_count += 1

# Função principal que inicia a captura dos pacotes
def main():
    # Detecta automaticamente a interface de rede padrão
    iface = conf.iface
    print(f"Iniciando a captura de pacotes na interface: {iface}")
    
    # Inicia a captura dos pacotes:
    # - Filtra apenas pacotes TCP
    # - Limita a captura a 100 pacotes
    # - Não armazena os pacotes na memória
    sniff(filter="tcp", prn=process_packet, iface=iface, count=100, store=False)
    
    # Mensagem final indicando se algum alerta foi encontrado
    if alert_count == 0:
        print("Captura concluída. Nenhuma atividade suspeita foi detectada.")
    else:
        print(f"Captura concluída. Total de alertas: {alert_count}")

# Executa a função principal somente se o script for executado diretamente
if __name__ == "__main__":
    main()
