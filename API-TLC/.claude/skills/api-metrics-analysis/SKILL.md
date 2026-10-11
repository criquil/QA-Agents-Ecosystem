---
name: api-metrics-analysis
description: Usa esta skill para analizar métricas de pruebas de API: tiempos de respuesta, throughput, error rates, SLA compliance y contract validation. Incluye los targets numéricos por defecto del proyecto y criterios de veredicto.
---

# API Metrics Analysis

## Objetivo
Analizar métricas de ejecuciones de API testing y generar insights accionables.

## Targets numéricos por defecto

### Cobertura

| Métrica | Fórmula | Target |
|---------|---------|--------|
| Endpoint Coverage | endpoints_tested / total_endpoints | ≥ 80% |
| Line Coverage | lines_covered / total_lines | ≥ 70% |
| Branch Coverage | branches_covered / total_branches | ≥ 60% |
| Scenario Coverage | scenarios_tested / total_scenarios | ≥ 90% |

### Calidad

| Métrica | Fórmula | Target |
|---------|---------|--------|
| Pass Rate | passed_tests / total_tests | ≥ 95% |
| Defect Density | defects / kLOC | ≤ 5 |
| Escape Rate | defects_found_in_prod / total_defects | ≤ 10% |
| MTTR | total_recovery_time / num_incidents | ≤ 4h |

### Performance (API-level)

| Métrica | Fórmula | Target |
|---------|---------|--------|
| Response Time p95 | 95th percentile of response times | ≤ 200ms |
| Response Time p99 | 99th percentile of response times | ≤ 500ms |
| Throughput | requests per second | ≥ 100 req/s |
| Error Rate | errors / total_requests | ≤ 1% |
| Availability | uptime / total_time | ≥ 99.9% |

### Contract

| Métrica | Fórmula | Target |
|---------|---------|--------|
| Schema Compliance | valid_responses / total_responses | 100% |
| Breaking Changes | breaking_changes / total_changes | 0 |
| Backward Compatibility | compatible_versions / total_versions | 100% |

## Criterios de veredicto (Pass/Fail)

- **PASSED**: Todas las métricas dentro del target
- **CONDITIONAL**: Métricas borderline con mitigación propuesta
- **FAILED**: Alguna métrica crítica fuera del target sin mitigación

## Flujo
1. Recopila métricas: response time (p50/p95/p99), throughput (req/s), error rate, SLA compliance.
2. Compara contra los targets por defecto de arriba (o los NFRs definidos en el test plan).
3. Identifica outliers y tendencias.
4. Genera visualizaciones si es posible (tablas, gráficos ASCII).
5. Produce resumen ejecutivo con veredicto: PASSED / CONDITIONAL / FAILED.

## Salida Esperada
- Tabla de métricas vs criterios de aceptación.
- Outliers y tendencias identificados.
- Veredicto: PASSED / CONDITIONAL / FAILED.
- Recomendaciones priorizadas para mejora.
