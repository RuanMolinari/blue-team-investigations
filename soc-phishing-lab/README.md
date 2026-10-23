# 🛡️ Lab de SOC: Investigação de Phishing e Execução de Payload

## 🎯 Cenário
Você é um Analista de SOC Tier 1 em uma empresa. Durante o monitoramento de rotina, o sistema de alertas disparou notificações relacionadas a um possível incidente de segurança envolvendo um colaborador do setor financeiro (`Carlos Silva`). 

Sua missão é analisar os logs fornecidos, identificar a cadeia de ataque, extrair os Indicadores de Comprometimento (IOCs) e responder às perguntas de investigação.

---

## 📂 Arquivos Disponíveis
* `logs/splunk_events.log`: Contém os eventos extraídos do SIEM (Splunk) em ordem cronológica.
* `iocs/iocs.txt`: Espaço para você registrar os IOCs descobertos.

---

## ❓ Perguntas de Investigação (Desafio)
Responda às seguintes perguntas com base nos logs:
1. Qual é o endereço de e-mail do remetente fraudulento e qual o assunto da mensagem?
2. Qual foi o nome do arquivo compactado baixado pelo usuário e qual a URL de origem?
3. Qual processo filho foi gerado no endpoint após a execução do arquivo malicioso?
4. Para qual endereço IP externo (Destination IP) o script malicioso tentou estabelecer comunicação (C2)?
5. Qual foi a ação tomada pelo sistema de EDR/Antivírus ao final do incidente?
