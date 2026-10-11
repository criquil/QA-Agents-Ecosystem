# Cheat Sheet — Métricas y KPIs de Calidad

Fórmulas y umbrales estándar para gobernanza QA.

## Métricas de Proceso (Process)
- **Lead Time**: tiempo desde requerimiento hasta entrega.
- **Defect Escape Rate**: % defectos encontrados en producción / total de defectos.
- **Cycle Time**: tiempo desde inicio de desarrollo hasta completado.
- **MTTR** (Mean Time To Repair): tiempo promedio para corregir defectos.
- **Coverage**: % código/funcionalidades cubiertas por pruebas.

## Métricas de Producto (Quality)
- **Defect Density**: defectos por KLOC o puntos de función.
- **Severity Distribution**: % P1, P2, P3.
- **Pass Rate**: % casos de prueba pasados / total ejecutados.
- **Flaky Rate**: % pruebas inestables / total automatizadas.

## Umbrales de Calidad (ejemplos)
- Defect Escape Rate < 5%
- Coverage > 80% (funcional), > 70% (unit)
- Flaky Rate < 2%
- MTTR < 24h (P1), < 72h (P2), < 5 días (P3)
