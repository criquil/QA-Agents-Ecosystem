# Métricas de Calidad (Nivel 3)

## Code Coverage
**Fórmula**: `(líneas_cubiertas / líneas_totales) × 100`
**Umbral**: > 80% (funcional), > 70% (unit)
**Herramienta**: JaCoCo (Java), Istanbul (JS), coverage.py (Python)
**Fuente**: reports de CI/CD.

## Pass Rate
**Fórmula**: `(casos_pasados / casos_ejecutados) × 100`
**Umbral**: > 95% en smoke, > 90% en regresión completa
**Fuente**: Reportes de ejecución (TestRail, Xray, CI).

## Flaky Rate
**Fórmula**: `(pruebas_inestables / total_automatizadas) × 100`
Mide la confiabilidad de la suite.
**Umbral**: < 2%
**Fuente**: histórico de reintentos en CI.

## Defect Density
**Fórmula**: `nº_defectos / KLOC` (o por punto de función)
**Umbral**: por módulo, comparar con baseline histórico.
**Fuente**: Jira + SonarQube.

## Severity Distribution
**Fórmula**: `% de defectos por severidad (P1/P2/P3)`
**Umbral**: P1 < 5%, P2 < 15%
**Fuente**: Jira.