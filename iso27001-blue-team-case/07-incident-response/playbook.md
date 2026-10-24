# Playbook — comprometimento de identidade

## Detectar

- validar alerta e origem;
- identificar usuário, sessão, IP, dispositivo e timestamp;
- preservar eventos relevantes.

## Conter

- bloquear conta quando justificado;
- revogar sessões/tokens;
- revisar MFA e credenciais;
- remover OAuth/app credentials suspeitos;
- elevar para incident commander.

## Investigar

- IdP, Microsoft 365, cloud, GitHub e endpoint;
- mailbox rules, grupos e privilégios;
- acessos a dados;
- persistência e exfiltração somente se sustentadas por evidência.

## Recuperar

- corrigir causa;
- revalidar endpoint e identidade;
- restaurar acesso controlado;
- monitorar reforçadamente.

## Pós-incidente

- RCA;
- ações corretivas com owner e prazo;
- atualização de riscos/SoA;
- teste de eficácia;
- lições aprendidas.
