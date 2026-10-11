# Umbrales y Criterios de Aceptación (Nivel 3)

## Criterios por disciplina

| Disciplina | PASSED | CONDITIONAL | FAILED |
|---|---|---|---|
| API Testing | 100% endpoints críticos cubiertos, 0 defectos críticos | < 10% no cubiertos | endpoints críticos sin cobertura |
| Manual Testing | ≥ 95% casos ejecutados, 0 P1 abiertos | 90-95% casos, 0 P1 | < 90% o P1 abiertos |
| Automation | coverage ≥ 80%, pass rate ≥ 95%, flaky < 2% | coverage 70-80% | coverage < 70% |
| Performance | p95 dentro de SLA, error rate < 1% | p95 < 10% sobre SLA | p95 > 20% sobre SLA |
| Accessibility | 0 violaciones WCAG nivel A/AA | < 5 violaciones nivel A | ≥ 5 violaciones A o AA |

## Severidad de hallazgos

- **P1 (Crítico)**: bloquea release, viola norma obligatoria, impacto de seguridad.
- **P2 (Alto)**: impacto significativo en calidad, SLA en riesgo.
- **P3 (Medio)**: mejora sugerida, no bloquea.
- **P4 (Bajo)**: cosmético.

## Regla de veredicto

- **PASSED**: todos los criterios en verde.
- **CONDITIONAL**: criterios en amarillo, con plan de mitigación y fecha.
- **FAILED**: algún criterio en rojo.

## Aprobación

- Veredicto CONDITIONAL o FAILED requiere Approval Gate del usuario.