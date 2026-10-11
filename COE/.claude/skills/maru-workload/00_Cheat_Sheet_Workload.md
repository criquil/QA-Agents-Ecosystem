# Cheat Sheet — Workload (decisión rápida)

| Concepto | Fórmula / Regla |
|---|---|
| TPS = usuarios concurrentes × think time | `TPS = VU / think_time(s)` |
| Think time | `= 1 / TPS_objetivo × VU` |
| Duración soak | ≥ 8h (estabilidad), ideal 24-72h (memoria) |
| Ramp-up | 10-20% de la duración total, salvo indicación contraria |
| Capacidad del generador | ≥ 2× carga objetivo |
| Rising load test | Incremento 10-20% hasta saturación |

## Umbrales por defecto

- Error rate: < 1% (pico), < 0.5% (steady state)
- p95 latencia: según SLA del sistema
- CPU del SUT: < 80% sostenido
- Distribución de carga: 60% usuarios reales / 40% sintéticos

## Trampas comunes

- Sin think time → todos los VU golpean a la vez (irreal).
- Ramp-up demasiado rápido → se pierden estados de conexiones.
- Soak corto (< 2h) → no detecta memory leaks.
- Medir p99 con pocos samples (ver cheat sheet de métricas).