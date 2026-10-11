# Perfiles de Carga (Nivel 3)

## Tipos de perfil

| Perfil | Forma | Uso | Duración típica |
|---|---|---|---|
| Baseline | Constante baja | Medir referencia | 5-10 min |
| Load test | Rampa → steady state | Validar SLA con carga esperada | 15-30 min |
| Stress test | Rampa ascendente hasta saturación | Hallar punto de ruptura | 20-40 min |
| Spike test | Salto brusco y retorno | Comportamiento ante eventos | 5-10 min |
| Soak/endurance | Steady state largo | Memory leaks, degradación | 8-72 h |
| Capacity test | Escalado progresivo | Máximo usuarios antes de degradar | 30-60 min |
| Smoke | Carga mínima | Valida setup antes de la prueba | 1-2 min |

## Estructura de una prueba típica

```
[smoke 2min] → [baseline 10min] → [load 20min] → [stress 20min] → [recovery 10min]
```

## Ramp-up

- 10-20% de la duración total.
- Razones: conexiones TCP/TLS, JIT warmup, caché frío.
- Si el ramp-up es demasiado rápido, el SUT no refleja comportamiento real.

## Cool-down (recuperación)

- Reducir carga a 0 en 5-10 min.
- Verificar que el sistema vuelve a su línea base.
- Si no vuelve → **cuello de botella confirmado**.

## Criterio de parada

- Error rate >5% sostenido 2 min → abortar.
- Latencia p95 >200% del baseline → abortar.
- CPU >90% en SUT por >5 min → anotar saturación, continuar si el objetivo es encontrarla.