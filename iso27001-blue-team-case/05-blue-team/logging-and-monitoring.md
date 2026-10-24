# Logging e monitoramento

## Fontes prioritárias

| Fonte | Eventos | Uso |
|---|---|---|
| IdP | login, MFA, sessão, mudança de privilégio | detecção de identidade |
| Microsoft 365 | mailbox, OAuth, admin | investigação de conta |
| AWS | CloudTrail, IAM, console | atividade cloud |
| Endpoint/EDR | processo, rede, isolamento | execução e resposta |
| GitHub | autenticação, branch, secrets | risco CI/CD |
| API | autenticação, erros, abuso | disponibilidade e acesso |

## Requisitos de qualidade

- timestamp e timezone consistentes;
- identificação de origem e usuário/asset quando disponível;
- retenção proporcional ao risco e obrigações aplicáveis;
- acesso aos logs restrito e auditável;
- monitoramento da saúde das fontes;
- testes positivos e negativos para regras críticas.

Cobertura deve ser medida com inventário de fontes, não estimada.
