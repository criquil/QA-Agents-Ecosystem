---
name: kb-01-metricas-manual-exhaustivas
description: Skill autónoma de conocimiento sobre métricas y kpis de pruebas manuales. No depende de archivos externos.
---

# Métricas y KPIs de Pruebas Manuales

## Métricas de Cobertura

| Métrica | Fórmula | Target |
|---------|---------|--------|
| Requirement Coverage | requisitos_cubiertos / total_requisitos | 100% |
| Case Execution Coverage | casos_ejecutados / casos_diseñados | >= 95% |
| Module Coverage | módulos_ejecutados / total_módulos | >= 90% |
| Type Coverage | tipos_de_prueba_ejecutados / tipos_planificados | 100% |
| Browser Coverage | navegadores_ejecutados / navegadores_de_matriz | 100% |
| Charter Coverage (exploratorio) | áreas_cubiertas / áreas_del_alcance | >= 80% |

## Métricas de Calidad

| Métrica | Fórmula | Target |
|---------|---------|--------|
| Pass Rate | casos_pass / casos_ejecutados | >= 95% |
| Defect Density | defectos / módulo | <= 5 |
| Defect Detection Effectiveness | defectos_válidos / defectos_reportados | >= 90% |
| Reopen Rate | defectos_reabiertos / defectos_cerrados | <= 10% |
| Escape Rate | defectos_en_producción / total_defectos | <= 10% |
| MTTR | tiempo_total_de_resolución / nº_de_incidentes | <= 8 h |

## Métricas de Performance Percibida

| Métrica | Fórmula | Target |
|---------|---------|--------|
| Page Load P95 | percentil 95 del tiempo de carga | <= 3000 ms |
| Page Load P99 | percentil 99 del tiempo de carga | <= 5000 ms |
| Transactional Error Rate | transacciones_con_error / total_transacciones | <= 1% |
| Environment Availability | tiempo_disponible / tiempo_planificado | >= 99.9% |
| Perceived Responsiveness | acciones_con_feedback_en < 1 s / total_acciones | >= 95% |

## Métricas de Eficiencia de Sesión

| Métrica | Fórmula | Target |
|---------|---------|--------|
| Cases per Hour | casos_ejecutados / horas_efectivas | informativo |
| Blocked Rate | casos_blocked / casos_ejecutados | <= 5% |
| Evidence Completeness | casos_pass_con_evidencia / casos_pass | 100% |
| Session Duration Variance | duración_real / duración_planificada | 0.8 – 1.2 |
| Rework Rate | casos_repetidos_por_error_de_datos / total_casos | <= 5% |

## Métricas de UAT

| Métrica | Fórmula | Target |
|---------|---------|--------|
| Acceptance Criteria Pass | criterios_aceptados / total_criterios | 100% |
| Blocking Defects at Sign-off | defectos_P1_abiertos_en_la_firma | 0 |
| UAT Participant Coverage | participantes_que_ejecutaron / participantes_planificados | >= 90% |
| Sign-off Timeliness | firma_a_tiempo / total_firmas | 100% |

## Criterios Pass/Fail

- **PASSED**: todas las métricas dentro del target y evidencia completa.
- **CONDITIONAL**: métricas borderline con mitigación propuesta y plazo.
- **FAILED**: alguna métrica crítica fuera del target sin mitigación (defectos P1 abiertos, evidencia faltante, UAT rechazada).

## Reglas

1. Los umbrales definitivos provienen del plan de pruebas del proyecto.
2. Sin evidencia asociada, un PASS no computa para ninguna métrica.
3. Reportar siempre desagregado por tipo de prueba manual.
4. Las métricas de eficiencia nunca deben usarse para presionar reducción de calidad (evidencia y exploración no son negociables).
