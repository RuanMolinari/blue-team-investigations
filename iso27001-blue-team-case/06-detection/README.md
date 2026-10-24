# Detection engineering

As regras deste diretório são ilustrativas e devem ser adaptadas ao schema do SIEM/EDR.

## Ciclo

1. Definir hipótese e risco relacionado.
2. Identificar fonte e campos.
3. Escrever regra/query.
4. Criar teste positivo controlado.
5. Criar teste negativo para falso positivo.
6. Definir severidade, owner e resposta.
7. Medir qualidade e ajustar.
8. Registrar evidência sanitizada.

PowerShell ou autenticação incomum não são prova de ataque isoladamente.
