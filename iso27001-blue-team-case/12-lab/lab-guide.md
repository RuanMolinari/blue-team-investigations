# Guia de laboratório seguro

## Objetivo
Validar detecções, telemetria e resposta sem tocar em ativos de terceiros ou produção.

## Ambiente sugerido

- VM Windows isolada;
- Sysmon/EDR de laboratório;
- SIEM local ou tenant de teste;
- máquina Linux para apoio;
- snapshots e rede controlada.

## Exercícios

1. gerar evento benigno de PowerShell;
2. gerar comando com flag encoded em ambiente isolado;
3. produzir evento de autenticação sintético;
4. validar alertas e falsos positivos;
5. registrar timestamps, regras e resultados;
6. destruir/reverter VMs ao final.

Atomic Red Team ou ferramentas similares só devem ser usadas em máquinas próprias e autorizadas. Não baixar payloads reais nem executar testes em produção.
