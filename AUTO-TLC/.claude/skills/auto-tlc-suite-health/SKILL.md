---
name: auto-tlc-suite-health
description: "Targets numericos, metricas y criterios de veredicto de salud de suite. Skill de apoyo de las fases 4 y 6 del AUTO-TLC. Cargar cuando se necesiten umbrales por defecto o el calculo de una metrica de salud."
---

# AUTO-TLC-SUITE-HEALTH — Targets, metricas y veredicto

> Skill transversal de apoyo. No es una fase. Se carga desde `auto-tlc-test-plan` (fase 4) y `auto-tlc-analysis` (fase 6).

## Targets por defecto

Si el usuario no define umbrales propios, usar estos. **Declararlos explicitamente** en el plan formal.

| Metrica | Target | Severidad | Justificacion |
|---|---|---|---|
| `pass_rate_smoke_pct` | 100 | Critica | El smoke es la garantia de acceso; cualquier fallo bloquea |
| `pass_rate_full_pct` | ≥ 98 | Critica | 2% es el margen de flakiness asumible |
| `flakiness_pct` | < 2 | Critica | Por encima, la suite pierde credibilidad |
| `smoke_duration_min` | ≤ 5 | Alta | Si no entra en el ciclo del commit, no se ejecuta |
| `full_regression_duration_min` | ≤ 45 | Media | Nightly; mas alla, deja de correr a diario |
| `feature_coverage_pct` | ≥ 80 | Alta | El resto se justifica o se descarta explicitamente |
| `code_coverage_pct` | ≥ 70 | Media | Indicador de apoyo, no de calidad directa |
| `unvalidated_selectors` | 0 | Critica | Selector sin validar es bomba de tiempo |
| `hardcoded_data` | 0 | Critica | Bloquea el multi-entorno |
| `tests_without_tags` | 0 | Critica | Sin tags, el pipeline no ejecuta el test |
| `orphan_scenarios` | 0 | Alta | Escenario sin requisito o requisito sin escenario |
| `js_widget_failures` | 0 | Alta | El patron click+type+enter esta definido; fallar es deuda |

## Calculo de cada metrica

### `pass_rate_pct`

```
passed / total × 100
```

`total = passed + failed + skipped`. Los skipped por `@wip` **no cuentan** como fallo pero tampoco como cobertura: reportarlos aparte.

### `flakiness_pct`

El calculo clave de la suite, y el mas facil de medir mal.

```
flakiness_pct = (tests que fallaron y pasaron en el reintento) / total × 100
```

**No** confundir con la tasa de fallo: un test que falla 1 de cada 5 corridas es 100% flaky aunque su tasa de fallo sea baja.

Medicion directa:

```bash
npx playwright test --repeat-each 5 --reporter=json | <procesar>
```

### `feature_coverage_pct`

```
funcionalidades con al menos 1 test automatizado / funcionalidades candidatas × 100
```

El denominador sale de `scope.md` (fase 1). **Las funcionalidades descartadas explicitamente no cuentan como candidatas** — si no, el ratio premia la omision.

### `smoke_duration_min`

Wall clock del stage completo en CI, no la suma de duraciones de tests. Incluye arranque de runner, setup y subida de artefactos.

### `unvalidated_selectors`

```bash
grep -rn "TODO\|FIXME\|PLACEHOLDER\|<placeholder>" tests/*/*/*/*/scripts/
```

Resultado debe ser **0**. Cualquier coincidencia es un selector sin validar.

### `hardcoded_data`

```bash
grep -rn "fill('.*')\|goto('http\|toBe('.*')" tests/*/*/*/*/scripts/
```

Resultado debe ser **0**. Credenciales, URLs y mensajes esperados salen de `data/`.

### `tests_without_tags`

Cruzar el filtro real del pipeline contra el listado de tests:

```bash
npx playwright test --grep "@qa" --list
```

Si el resultado no coincide con lo esperado para ese stage, hay tests sin tags.

## Criterios de veredicto

| Veredicto | Condicion |
|---|---|
| **PASSED** | Todas las metricas `Critica` en target |
| **CONDITIONAL** | Criticas en target, alguna `Alta` o `Media` fuera, con mitigacion propuesta |
| **FAILED** | Algun `Critica` fuera, o smoke rojo sin causa de infraestructura documentada |

### Matriz de severidad

| Severidad | Que significa | Efecto |
|---|---|---|
| `Critica` | Rompe el ciclo: el pipeline no ejecuta, o el resultado no es confiable | Bloquea veredicto |
| `Alta` | Degrada la suite: cobertura, mantenibilidad, velocidad | Bloquea a `PASSED` |
| `Media` | Mejora Continua | Observacion, no bloquea |

## Reporte de salud

```markdown
## Salud de Suite — {plan_id} — {fecha}

| Metrica | Valor | Target | Estado |
|---|---|---|---|
| pass_rate_smoke_pct | 100 | 100 | OK |
| pass_rate_full_pct | 97.2 | ≥ 98 | FALLA |
| flakiness_pct | 3.4 | < 2 | FALLA |
| smoke_duration_min | 3.1 | ≤ 5 | OK |
| feature_coverage_pct | 84 | ≥ 80 | OK |
| unvalidated_selectors | 0 | 0 | OK |
| hardcoded_data | 0 | 0 | OK |
| tests_without_tags | 0 | 0 | OK |

**Metricas criticas fuera de target:** pass_rate_full_pct, flakiness_pct
**Impacto:** veredicto limitado a CONDITIONAL hasta cerrar los 2 puntos.
```

## Reglas

- Un target declarado por el usuario **gana** al de esta tabla. Documentar la diferencia.
- Toda metrica se reporta con su denominador. Un porcentaje sin denominador no es auditable.
- `flakiness_pct` se mide con ejecucion repetida, no se estima.
- Las funcionalidades excluidas en `scope.md` salen del denominador de cobertura.
- Los valores por defecto son un punto de partida, no dogma: un proyecto con suite E2E pesada puede necesitar `smoke_duration_min ≤ 8`. Declarar la desviacion y el motivo.

## Lectura bajo demanda

Este SKILL.md contiene todos los targets y formulas necesarios.

| Si el SKILL.md no alcanza y necesitás | Leé |
|---|---|
| Sintaxis para medir cada metrica | `.claude/skills/automation-cicd/SKILL.md` |
| Sintomas de flakiness por categoria | `.claude/skills/automation-troubleshooting/SKILL.md` |

**Stop**: para calcular el veredicto, esta tabla completa es suficiente. No abras mas.