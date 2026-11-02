# ISO/IEC 27001:2022 + Blue Team — Case Study

> **Portfolio demonstration project.** FinSecure Tecnologia Ltda., including its assets, risks, incidents, timelines, metrics, and outcomes, is entirely fictional. This repository does not document an implementation at a real organization, a compliance audit, or an ISO/IEC 27001 certification.

## Executive summary

This case study demonstrates how an Information Security Management System (ISMS) can be connected to Blue Team operations: governance, risk assessment, control selection, telemetry, detection, incident response, evidence management, internal audit, and continual improvement.

The scenario describes a fictional financial-technology SaaS company using AWS, Microsoft 365, Windows, GitHub, CI/CD, and PostgreSQL. A tabletop exercise simulates phishing and possible identity compromise.

## What this project demonstrates

- Definition of ISMS context, scope, and objectives.
- Risk-assessment methodology and an initial risk register.
- Illustrative gap assessment and Statement of Applicability (SoA).
- Security architecture, logging, and monitoring.
- Sigma rules and investigation queries.
- Incident response and root-cause analysis.
- MITRE ATT&CK mapping based on available evidence.
- Simulated internal audit and security metrics.
- Clear separation of assumptions, hypotheses, synthetic data, and actual evidence.

## Fictional organization

| Attribute | Scenario assumption |
|---|---|
| Organization | FinSecure Tecnologia Ltda. |
| Industry | B2B SaaS / financial services |
| Size | 180 employees |
| Infrastructure | AWS, Microsoft 365, Windows, GitHub, CI/CD, PostgreSQL |
| Security team | 3 people |
| Objective | Establish an ISMS and prevention, detection, and response capabilities |

## Repository structure

```text
01-governance/          context, scope, policy, and objectives
02-risk-management/     risks, methodology, and treatment
03-iso27001/            gap assessment, SoA, and control mapping
04-asset-management/    synthetic asset inventory
05-blue-team/           architecture, logging, and vulnerability management
06-detection/            Sigma rules, queries, and validation
07-incident-response/   tabletop, playbook, and root-cause analysis
08-mitre-attack/        evidence-based mapping and confidence
09-audit/               internal audit
10-metrics/             KPIs and methodology
11-evidence/            evidence index
12-lab/                 controlled lab exercises
```

## ISO/IEC 27001 considerations

ISO/IEC 27001 specifies requirements for an ISMS. Controls should be determined according to the organization's context, risks, and applicable obligations; Annex A should not be treated as an automatic checklist.

This case study considers Amendment 1:2024 and records an assessment of whether climate change is a relevant issue in the context of the ISMS. The repository does not reproduce the full text of copyrighted standards.

## Simulated incident

**INC-2026-001 — possible identity compromise through phishing.** The scenario begins with a fake login link and credentials submitted by a user. The response exercise covers containment, session revocation, OAuth review, log investigation, and recovery.

Data exfiltration, malware, persistence, and privilege escalation are **not assumed**. They should only be classified as confirmed when sufficient evidence is available.

## Validation

```bash
python scripts/validate_repo.py
```

Sigma rules and queries should be validated in the relevant SIEM/backend and authorized lab environment. Synthetic metrics must not be presented as real-world results.

## Disclaimer

All organization names, incidents, assets, metrics, timelines, and outcomes are fictional. This is an educational portfolio case study; it is not a certification, real audit, or production implementation.
