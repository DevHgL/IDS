1. **Variável Global para Contagem de Alertas**  
   ```python
   alert_count = 0
   ```  
   - Define uma variável global que irá contar quantas vezes a regra de alerta foi acionada.

2. **Função `process_packet`**  
   - Verifica se o pacote possui as camadas TCP e IP.  
   - Aplica a regra: se a porta de destino for 23 (Telnet), imprime uma mensagem de alerta e incrementa a variável `alert_count`.

3. **Função `main`**  
   - Detecta automaticamente a interface de rede padrão usando `conf.iface`.  
   - Inicia a captura de pacotes com um filtro para TCP, limitando a captura a 100 pacotes e sem armazená-los na memória.  
   - Após a captura, verifica o valor de `alert_count`:
     - Se for zero, exibe uma mensagem informando que nenhum alerta foi detectado.
     - Caso contrário, informa o total de alertas encontrados.

4. **Bloco Principal**  
   - Garante que a função `main()` seja executada apenas quando o script for executado diretamente.

Esta versão do script permite saber quando a captura foi concluída e informa ao usuário se não houve nenhuma atividade suspeita durante a captura dos pacotes.
