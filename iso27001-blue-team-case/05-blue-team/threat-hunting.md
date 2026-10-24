# Threat hunting — cenário seguro

## Hipóteses

- autenticação anômala seguida de atividade administrativa;
- criação de OAuth/app credential inesperada;
- PowerShell com parâmetros de download;
- alterações de mailbox ou grupo fora do padrão.

## Método

1. Definir hipótese e janela temporal.
2. Selecionar fontes e campos necessários.
3. Executar consulta somente em dados autorizados.
4. Correlacionar usuário, asset, IP, sessão e timestamp.
5. Separar sinal de evidência de comprometimento.
6. Registrar achados, negativos e limitações.

Hunting não deve presumir que um comportamento suspeito seja ataque sem evidência contextual.
