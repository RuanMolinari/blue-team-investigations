# Análise de causa-raiz — INC-2026-001

**Natureza:** hipótese de RCA para exercício fictício.

## 5 Whys

1. **Por que** uma conta poderia ter sido comprometida? Porque credenciais/sessão podem ter sido expostas em phishing.
2. **Por que** a exposição poderia produzir impacto? Porque a conta pode possuir acesso a serviços relevantes.
3. **Por que** o impacto pode ser ampliado? Porque privilégio excessivo e sessões persistentes podem aumentar a superfície.
4. **Por que** esses riscos podem permanecer? Porque controles de identidade e sua eficácia podem não ser revisados/testados com frequência suficiente.
5. **Por que** a eficácia pode não ser validada? Porque governança, telemetria e testes de controles podem estar desalinhados com o risco.

## Hipótese de causa sistêmica

Possível fragilidade no gerenciamento de risco de identidade e na validação de eficácia dos controles, potencialmente combinando autenticação suscetível a phishing, privilégio excessivo e telemetria insuficiente.

Isso **não atribui culpa ao usuário** e não declara fatos sem evidência.

## Ações corretivas propostas

- MFA resistente a phishing para perfis críticos;
- revisão de privilégios e sessões;
- testes periódicos de detecção;
- cobertura de logs e EDR;
- exercícios de resposta;
- revisão do risco residual após testes.
