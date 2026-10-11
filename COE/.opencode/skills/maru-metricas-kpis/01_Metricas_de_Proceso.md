# Métricas de Proceso (Nivel 3)

## Lead Time
**Fórmula**: `fecha_release - fecha_requerimiento`
Mide el tiempo total desde que el requerimiento entra hasta que llega a producción.
**Umbral**: < 30 días calendario (equipos ágiles 2 semanas).
**Fuente**: Jira (timestamp de creación) + pipeline de release.

## Defect Escape Rate
**Fórmula**: `(defectos_en_producción / total_defectos) × 100`
Mide la eficacia del testing. Alto valor = fugas de calidad.
**Umbral**: < 5%
**Fuente**: Jira (bugs de producción) / Jira (total bugs).

## MTTR — Mean Time To Repair
**Fórmula**: `suma(tiempo_resolución) / nº_defectos`
**Umbral**: P1 < 24h · P2 < 72h · P3 < 5 días
**Fuente**: Jira (resolved date - created date).

## Cycle Time
**Fórmula**: `fecha_completado - fecha_inicio_dev`
**Umbral**: < 7 días
**Fuente**: Jira (sprint data).