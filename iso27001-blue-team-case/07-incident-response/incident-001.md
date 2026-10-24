# INC-2026-001 — Tabletop de phishing

**Classificação:** cenário fictício / exercício de mesa.

## Cenário

Um usuário acessa um link de login falso e informa credenciais e um código de autenticação. O IdP registra uma autenticação incomum. O time precisa determinar se houve uso indevido da conta e conter o risco.

## Linha do tempo simulada

| Hora | Evento | Estado |
|---|---|---|
| 08:12 | Mensagem de phishing entregue | Simulado |
| 08:17 | Usuário acessa página falsa | Simulado |
| 08:19 | Autenticação incomum observada | Hipótese a validar |
| 08:23 | Alerta de identidade | Hipótese de alerta |
| 08:25 | Revogação de sessões e bloqueio temporário | Resposta esperada |
| 08:40 | Revisão de OAuth, mailbox e grupos | Investigação |
| 09:10 | Isolamento de endpoint, se aplicável | Condicional |
| 10:00 | Impacto preliminar documentado | Resultado do exercício |

Os horários não são métricas reais.

## Evidências mínimas

- eventos do IdP com timestamp e timezone;
- cabeçalhos e logs de entrega do e-mail;
- logs de acesso aos serviços;
- trilha das ações de contenção;
- queries e janelas de busca;
- evidências preservadas e sanitizadas.

## Contenção

1. Confirmar o usuário por canal alternativo.
2. Bloquear conta se necessário.
3. Revogar sessões/tokens.
4. Redefinir credenciais e revisar MFA.
5. Revisar OAuth, mailbox, grupos e privilégios.
6. Investigar extensão somente com logs.

## Encerramento

Encerrar quando credenciais/sessões expostas estiverem invalidadas, impacto documentado, lacunas registradas, recuperação validada e ações corretivas atribuídas.

O cenário não presume exfiltração, malware, persistência ou elevação de privilégio.
