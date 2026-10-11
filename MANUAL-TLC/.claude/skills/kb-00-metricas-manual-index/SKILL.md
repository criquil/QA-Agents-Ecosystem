---
name: kb-00-metricas-manual-index
description: Skill autónoma de conocimiento sobre métricas y kpis de pruebas manuales. No depende de archivos externos.
---

# Métricas y KPIs de Pruebas Manuales

> **Rol de este archivo:** Índice del catálogo de métricas y KPIs para MANUAL-TLC v1.0.
> **Cuándo leer este archivo:** Cuando necesitas definir métricas, KPIs o criterios de aceptación para un ciclo de pruebas manuales.

---

## Contenido del Dominio

| Skill | Descripción |
|-------|-------------|
| `kb-01-metricas-manual-exhaustivas` | Catálogo completo de métricas: cobertura, calidad, performance percibida, eficiencia de sesión, UAT |
| `manual-metrics-analysis` | Skill operativa de análisis de métricas y veredicto |

---

## Resumen de Métricas Principales

### Métricas de Cobertura
- Requirement Coverage: 100%
- Case Execution Coverage: >= 95%
- Module Coverage: >= 90%
- Type Coverage: 100% (los 7 tipos planificados)
- Browser Coverage: 100% de la matriz de compatibilidad

### Métricas de Calidad
- Pass Rate: >= 95%
- Defect Density: <= 5 por módulo
- Defect Detection Effectiveness: >= 90%
- Reopen Rate: <= 10%
- Escape Rate: <= 10%

### Métricas de Performance Percibida
- Page Load P95: <= 3000 ms
- Page Load P99: <= 5000 ms
- Transactional Error Rate: <= 1%
- Environment Availability: >= 99.9%

### Métricas de Eficiencia de Sesión
- Cases per Hour: informativo (baseline por equipo)
- Blocked Rate: <= 5%
- Evidence Completeness: 100%

### Métricas de UAT
- Acceptance Criteria Pass: 100%
- Blocking Defects at Sign-off: 0
- Sign-off obtenido: Sí/No

---

## Reglas de uso

1. Los umbrales definitivos los define el plan de pruebas de cada proyecto; los valores aquí son los defaults recomendados.
2. Sin evidencia no hay métrica válida: cada PASS debe estar respaldado por un archivo de evidencia.
3. Reportar siempre por tipo de prueba, no sólo agregado.
