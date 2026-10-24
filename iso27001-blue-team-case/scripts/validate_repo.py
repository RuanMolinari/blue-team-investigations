#!/usr/bin/env python3
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'README.md',
    '01-governance/scope.md',
    '02-risk-management/risk-register.csv',
    '03-iso27001/soa-template.csv',
    '03-iso27001/soa-exemplo.csv',
    '06-detection/sigma/suspicious-powershell-download.yml',
    '07-incident-response/incident-001.md',
    '08-mitre-attack/attack-mapping.csv',
    '10-metrics/security-kpis.csv',
]
errors=[]
for rel in REQUIRED:
    if not (ROOT/rel).is_file(): errors.append(f'Missing: {rel}')
for p in ROOT.rglob('*.csv'):
    try:
        with p.open(encoding='utf-8-sig', newline='') as f:
            rows=list(csv.reader(f))
        if not rows or len(rows[0])<2: errors.append(f'Invalid CSV: {p.relative_to(ROOT)}')
    except Exception as e: errors.append(f'CSV error {p}: {e}')
if errors:
    for e in errors: print(e)
    raise SystemExit(1)
print('OK: required files and CSV structure validated')
