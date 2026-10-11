---
name: manual-metrics-analysis
description: Usa esta skill para analizar métricas de pruebas manuales: cobertura, pass rate, densidad de defectos, tiempos de sesión, tiempos de carga y cumplimiento de SLAs.
---

# Manual Metrics Analysis

## Objetivo

Analizar métricas de sesiones de prueba manual y generar insights accionables con veredicto.

## Métricas a recopilar

### Cobertura
| Métrica | Fórmula | Target |
|---------|---------|--------|
| Requirement Coverage | requisitos_con_caso / total_requisitos | 100% |
| Case Execution Coverage | casos_ejecutados / casos_diseñados | ≥ 95% |
| Module Coverage | módulos_con_caso_ejecutado / total_módulos | ≥ 90% |
| Type Coverage | tipos_de_prueba_ejecutados / tipos_planificados | 100% |
| Browser Coverage | navegadores_ejecutados / navegadores_de_la_matriz | 100% |

### Calidad
| Métrica | Fórmula | Target |
|---------|---------|--------|
| Pass Rate | casos_pass / casos_ejecutados | ≥ 95% |
| Defect Density | defectos / módulo | ≤ 5 |
| Defect Detection Effectiveness | defectos_validos / defectos_reportados | ≥ 90% |
| Severity Mix | defectos_P1 / total_defectos | informativo |
| Reopen Rate | defectos_reabiertos / defectos_cerrados | ≤ 10% |
| Escape Rate | defectos_en_producción / total_defectos | ≤ 10% |

### Performance percibida
| Métrica | Fórmula | Target |
|---------|---------|--------|
| Page Load p95 | percentil 95 del tiempo de carga | ≤ 3000 ms |
| Page Load p99 | percentil 99 del tiempo de carga | ≤ 5000 ms |
| Transactional Error Rate | transacciones_con_error / total_transacciones | ≤ 1% |
| Environment Availability | tiempo_disponible / tiempo_planificado | ≥ 99.9% |

### Eficiencia de la sesión
| Métrica | Fórmula | Target |
|---------|---------|--------|
| Cases per Hour | casos_ejecutados / horas | informativo |
| Blocked Rate | casos_blocked / casos_ejecutados | ≤ 5% |
| Evidence Completeness | casos_con_evidencia / casos_pass | 100% |

## Flujo

1. Recopila las métricas de la sesión (resultados + evidencia + registro de defectos).
2. Compara contra los criterios de aceptación y umbrales del plan de pruebas.
3. Identifica outliers y tendencias (por módulo, rol, navegador, franja horaria).
4. Genera visualizaciones simples (tablas, gráficos ASCII) cuando aporten claridad.
5. Produce un resumen ejecutivo con veredicto: PASSED / CONDITIONAL / FAILED.

## Criterios de veredicto

- **PASSED**: todas las métricas dentro del target y Evidence Completeness 100%.
- **CONDITIONAL**: métricas en el borde, con defectos menores y mitigación propuesta.
- **FAILED**: alguna métrica crítica fuera del target sin mitigación (especialmente defectos P1 abiertos o evidencia faltante).

## Salida Esperada

- Tabla de métricas vs criterios de aceptación.
- Outliers y tendencias identificados.
- Veredicto: PASSED / CONDITIONAL / FAILED.
- Recomendaciones priorizadas para mejora.

## Reglas

- Nunca declarar PASS sin verificar la existencia de la evidencia asociada.
- Reportar por separado las métricas de cada tipo de prueba manual.
- Los umbrales usados deben ser los declarados en el plan de pruebas, no valores inventados.
