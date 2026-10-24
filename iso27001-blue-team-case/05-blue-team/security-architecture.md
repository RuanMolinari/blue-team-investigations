# Arquitetura de segurança — cenário didático

```text
Internet
   |
   v
[API / SaaS] ---- [AWS]
   |                 |
   |                 +---- PostgreSQL
   |                 +---- Backup
   |
   +---- [Identity Provider] ---- [Microsoft 365]
              |
              +---- [GitHub / CI-CD]
              |
              +---- [Windows endpoints + EDR]

Logs -> collectors -> SIEM -> detections -> triage -> incident response -> evidence
```

## Princípios

- identidade como perímetro principal;
- menor privilégio e MFA resistente a phishing;
- logs centralizados e protegidos contra alteração;
- EDR nos endpoints elegíveis;
- segregação de ambientes e deploys;
- backup isolado e testado;
- telemetria orientada aos riscos prioritários.

O diagrama é conceitual e não representa arquitetura real.
