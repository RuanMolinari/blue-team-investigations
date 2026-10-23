# 📝 Gabarito e Resolução do Lab

## Respostas das Perguntas:
1. **Remetente e Assunto:** `rh-beneficios@update-beneficios-rh.com` / `Urgente: Atualizacao de Beneficios 2026` (Evento 1).
2. **Arquivo e URL:** `Atualizacao_Beneficios.zip` baixado de `http://update-beneficios-rh.com/download/Atualizacao_Beneficios.zip` (Evento 2).
3. **Processo Gerado:** `powershell.exe` (chamado a partir do executável descompactado na pasta Downloads) (Evento 3).
4. **IP de Comando e Controle (C2):** `203.0.113.88` na porta `443` (Evento 4).
5. **Ação do EDR:** O alerta foi classificado como severidade "High" e o processo malicioso foi **Bloqueado** (`action=Blocked`) (Evento 5).

---

## 🔍 IOCs Extraídos
* **Domínio/URL Maliciosa:** `http://update-beneficios-rh.com/download/Atualizacao_Beneficios.zip`
* **IP de C2:** `203.0.113.88`
* **Hash SHA-256 do Payload:** `4a5f8b2c9e1d3f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a`
