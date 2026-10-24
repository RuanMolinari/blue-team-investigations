# ISO/IEC 27001:2022 + Blue Team — Estudo de Caso

> **Projeto demonstrativo de portfólio.** A FinSecure Tecnologia Ltda., seus ativos, riscos, incidentes, prazos, métricas e resultados são inteiramente fictícios. Este repositório não comprova implementação em uma organização real, não é uma auditoria de conformidade e não representa certificação ISO/IEC 27001.

## Resumo executivo

Este case demonstra como conectar requisitos de um Sistema de Gestão de Segurança da Informação (SGSI) a operações de Blue Team: governança, avaliação de riscos, seleção de controles, telemetria, detecção, resposta a incidentes, evidências, auditoria interna e melhoria contínua.

O cenário é uma empresa SaaS fictícia de tecnologia financeira com AWS, Microsoft 365, Windows, GitHub, CI/CD e PostgreSQL. Um exercício de mesa simula phishing e possível comprometimento de identidade.

## O que este projeto demonstra

- definição de contexto, escopo e objetivos do SGSI;
- metodologia de riscos e registro inicial de riscos;
- gap assessment e Statement of Applicability ilustrativos;
- arquitetura de segurança, logging e monitoramento;
- regras Sigma e consulta de triagem;
- resposta a incidentes e análise de causa-raiz;
- mapeamento MITRE ATT&CK condicionado à evidência;
- auditoria interna simulada e métricas;
- separação explícita entre premissas, hipóteses, dados sintéticos e evidências reais.

## Organização fictícia

| Atributo | Premissa |
|---|---|
| Organização | FinSecure Tecnologia Ltda. |
| Setor | SaaS / serviços financeiros B2B |
| Porte | 180 pessoas |
| Infraestrutura | AWS, Microsoft 365, Windows, GitHub, CI/CD, PostgreSQL |
| Equipe de segurança | 3 pessoas |
| Objetivo | Estruturar SGSI e capacidade de prevenção, detecção e resposta |

## Estrutura

```text
01-governance/          contexto, escopo, política e objetivos
02-risk-management/     riscos, metodologia e tratamento
03-iso27001/            gap assessment, SoA e mapeamento
04-asset-management/    inventário sintético
05-blue-team/           arquitetura, logging e vulnerability management
06-detection/           Sigma, queries e validação
07-incident-response/   tabletop, playbook e RCA
08-mitre-attack/        mapeamento com confiança/evidência
09-audit/               auditoria interna
10-metrics/             KPIs e metodologia
11-evidence/            índice de evidências
12-lab/                 laboratório seguro
```

## Precisão ISO/IEC 27001

A ISO/IEC 27001 especifica requisitos para um SGSI; controles devem ser determinados com base no contexto, riscos e obrigações aplicáveis. O Annex A não deve ser tratado como checklist automático.

Este case considera a Emenda 1:2024 e registra a análise da relevância de mudanças climáticas no contexto do SGSI. O repositório não reproduz o texto integral de normas protegidas por direitos autorais.

## Incidente simulado

**INC-2026-001 — possível comprometimento de identidade por phishing.** O cenário começa com um link de login falso e credenciais fornecidas pelo usuário. A equipe simula contenção, revogação de sessões, revisão de OAuth, investigação de logs e recuperação.

Exfiltração, malware, persistência e elevação de privilégio **não são presumidos**. Só devem ser classificados como confirmados quando houver evidência suficiente.

## Validação

```bash
python scripts/validate_repo.py
```

As regras Sigma e consultas devem ser validadas no SIEM/backend e no laboratório autorizado. Métricas sintéticas não devem ser apresentadas como resultados reais.

## Disclaimer

Todos os nomes, incidentes, ativos, métricas, prazos e resultados são fictícios. Este projeto é um estudo de caso educacional e de portfólio; não representa certificação, auditoria real ou implementação em produção.
