# Plano de tratamento de riscos

| Risco | Tratamento | Ações principais | Owner | Evidência de conclusão |
|---|---|---|---|---|
| R-001 | Mitigar | MFA resistente a phishing, revisão de contas privilegiadas, revogação de sessões e alertas | IAM Lead | Política, amostra de autenticações e teste |
| R-002 | Mitigar | EDR, hardening, backups isolados e exercício de recuperação | Endpoint/Infra | Cobertura EDR e restore test |
| R-003 | Mitigar | Classificação, acesso mínimo, criptografia e monitoramento | Data Owner | ACL/configuração e teste |
| R-004 | Mitigar | PAM/JIT, segregação e recertificação | IAM Lead | Aprovações e logs |
| R-005 | Mitigar | Proteção de branch, revisão de dependências, secret scanning e deploy controlado | Engineering Lead | Configuração CI/CD e teste |
| R-006 | Mitigar | Trilhas de auditoria, segregação e revisão periódica | GRC/IAM | Evidências de revisão |
| R-007 | Mitigar | Proteção DDoS, rate limiting e monitoramento | Cloud Lead | Testes controlados e alertas |
| R-008 | Mitigar | Imutabilidade, isolamento e testes de restauração | Infra Lead | Relatório de restore |
| R-009 | Mitigar | MFA resistente a phishing, conscientização e detecção | Security Lead | Política, campanha e alertas |
| R-010 | Mitigar | Inventário, cobertura EDR e health checks | Endpoint Lead | Relatório de cobertura |

Nenhum risco foi aceito por órgão de gestão real neste case. Risco residual deve ser calculado após implementação e teste dos controles.
