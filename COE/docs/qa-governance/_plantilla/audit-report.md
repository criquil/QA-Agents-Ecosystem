# Reporte de Auditoría QA — {plan_id}

**Alcance**: {disciplinas auditadas}
**Periodo**: {fecha} — {fecha}
**Auditor**: {} · **Owner**: {}

## Resumen ejecutivo

{2-3 frases: estado general, número de hallazgos P1/P2/P3 y veredicto.}

**Veredicto**: {PASSED | CONDITIONAL | FAILED}

## Hallazgos

| ID | Severidad | Disciplina | Hallazgo | Normativa | Acción |
|---|---|---|---|---|---|
| F-001 | P1 | API | Endpoints sin contract test | ISO/IEC 25010 | Crear Pact |
| F-002 | P2 | Automation | Flaky rate 4% | Criterios internos | Aislar tests |
| F-003 | P3 | Accessibility | Falta VPAT | WCAG, Section 508 | Publicar VPAT |

## Métricas

| Métrica | Valor | Objetivo | Estado |
|---|---|---|---|
| Defect Escape Rate | {} | < 5% | {🟢|🟡|🔴} |
| Coverage | {} | ≥ 80% | {🟢|🟡|🔴} |
| WCAG violaciones AA | {} | 0 | {🟢|🟡|🔴} |

## Evidencia

- {enlace a reporte de ejecución}
- {enlace a quality gate de CI}
- {capturas o exports}

## Conclusión

{Recomendación y siguiente paso: aprobar plan de mejora o repetir auditoría en {fecha}.}