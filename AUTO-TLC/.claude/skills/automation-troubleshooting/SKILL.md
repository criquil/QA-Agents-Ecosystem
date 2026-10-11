---
name: automation-troubleshooting
description: "Diagnostico de tests rojos y flaky: selectores rotos, timeouts, dropdowns JavaScript, condiciones de carrera, video y screenshots costosos. Invocar ante cualquier fallo de ejecucion o test intermitente."
---

# Automation Troubleshooting — Diagnostico

> **Metodo**: reproducir -> clasificar -> causa raiz -> fix minimo -> verificar. Sin skip como solucion.

## Flujo de diagnostico

```
1. Reproducir el fallo de forma aislada      npx playwright test -g "<caso>" --repeat-each 3
2. Leer el error literal                     no asumir la causa
3. Clasificar en una categoria              ver tabla abajo
4. Aplicar el patron de la categoria
5. Verificar con ejecucion repetida         --repeat-each 10
6. Documentar la leccion                    -> automation-assets
```

## Categorias de error

| # | Categoria | Sintoma tipico | Causa raiz | Fix |
|---|---|---|---|---|
| 1 | **Selector** | `element not found`, `strict mode violation` | Selector no validado o duplicado | Recapturar con DevTools MCP |
| 2 | **Timing** | Falla 1 de cada 3 corridas | Condicion de carrera, espera implicita | Auto-wait, no sleep fijo |
| 3 | **Datos** | Falla solo con un dataset | Valor hardcodeado o fixture mutable | Externalizar a `data/` |
| 4 | **Dropdown JS** | Timeout de 20 s en un `<select>` | Widget Select2/Chosen ignora `selectOption` | Patron click + type + Enter |
| 5 | **Ambiente** | Falla solo en CI | Timeouts, locale o timezone distintos | Alinear config con `config.yaml` |
| 6 | **Orden/estado** | Falla segun el test anterior | Estado compartido entre tests | Aislar: un usuario y datos por test |
| 7 | **Infraestructura** | Falla massiva y sincrona | Backend o red caidos | Verificar endpoint antes de culpar al test |

Orden de verificacion: **7 antes que 1**. Una caida de backend produce timeouts que parecen
problemas de selector, yiagnosticar el selector lleva a "arreglar" codigo que estaba bien.

## Categoria 1 — Selector

```text
❌ Locator timeout 30s exceeded
❌ strict mode violation: locator resolved to 3 elements
```

1. Navegar a la pagina exacta con Playwright MCP.
2. `browser_snapshot` para ver el DOM real.
3. `browser_evaluate` para contar cuantos elementos matchea el selector.
4. Si matchea mas de uno: agregar contexto (`//*[@id="form"]//button`).
5. Si matchea cero: el selector esta mal. Recapturar, no parchear a ojo.

## Categoria 2 — Timing

```text
❌ Element is not visible (pero esta en el DOM)
❌ Falla en la primera corrida, pasa en la segunda
```

| Sintoma | Fix |
|---|---|
| Elemento en DOM pero invisible | Esperar estado `visible`, no `attached` |
| Datos cargados por AJAX | Esperar el elemento que depende de los datos |
| Animacion de transicion | `await expect(locator).toBeVisible()` — auto-wait |
| Falla 1 de cada 3 | Condicion de carrera: falta una espera |

**Prohibido**: `waitForTimeout(3000)` como solucion. Es adivinar. Si el framework auto-espera, el
tiempo explicito solo hace el test lento. Si hace falta una espera, que sea por condicion:

```typescript
await expect(this.loc(this.MSG_ERROR)).toBeVisible();   // ✅ espera por condicion
await this.page.waitForTimeout(3000);                   // ❌ espera a ciegas
```

## Categoria 4 — Dropdown JavaScript

Select2, Chosen y Bootstrap Select ignoran `selectOption` y cuelgan hasta el timeout.

**Identificar**: clase `select2` en el `<select>`, contenedor `select2-container`, input `select2-search__field`.

```typescript
// ❌ se cuelga ~20 s y a veces selecciona mal
await page.locator(SELECT).selectOption({ label: tipo, timeout: 20_000 });

// ✅ patron correcto: CLICK abrir + TYPE filtrar + ENTER seleccionar
await page.locator(SELECT).click();
await page.keyboard.type(tipo);
await page.waitForTimeout(300);        // el widget procesa el filtro
await page.keyboard.press('Enter');
```

Medido: 12 dropdowns pasaron de **92 s a 31 s** (~65% mas rapido) con este patron.

## Categoria 6 — Estado compartido

```
❌ El test pasa solo, falla en la suite completa
```

Causas: datos de negocio creados por un test que otro asume, sesion de usuario reutilizada, orden de ejecucion.

```typescript
// ✅ un contexto limpio por test
test.beforeEach(async ({ browser }) => {
  const context = await browser.newContext();
  page = await context.newPage();
});
```

Cada test debe poder correr solo y en cualquier orden.

## Flakiness — cuando falla a veces

**Sintoma**: pasa en local, falla en CI. O falla 1 de cada 5 corridas.

```
1. Reproducir con --repeat-each 10 --repeat-each-each ...
2. Si necesita siempre reintentos -> no es ruido, es un bug. Ve a la categoria 2 o 6.
3. Si falla por red -> timeout de red explicito, no el timeout global
4. Si falla solo en CI -> comparar locale, timezone, timeouts y disponibilidad de datos
5. Si falla por orden -> aislar el estado por test
```

**Regla**: un test que requiere reintentos para pasar no esta terminado. Agregar `retries` para
tapar flakiness convierte un bug de calidad en un bug invisible.

## Evidencia por escenario

Activar video y screenshots siempre cuesta ~4 MB y +3-5 s **por test**.

| Escenario | Video | Screenshots | Tiempo | Uso |
|---|---|---|---|---|
| Desarrollo local | si | si | ~30 s | Debug visual |
| Debug de un fallo | no | si | ~33 s | Foto del momento exacto |
| Smoke en CI | **no** | si | ~6 s | Rapido |
| `@critical` | si | si | ~32 s | Evidencia de release |

En smoke, video y screenshots son overhead puro: deshabilitalos.

## Anti-patrones de debugging

```text
❌ Agregar retries hasta que pase            tapa el bug
❌ Subir el timeout a 60 s                    hides un problema de timing
❌ Usar waitForTimeout para "arreglar"        espera a ciegas
❌ Comentar el test hasta que "se estabilice" pierde cobertura
❌ Cambiar el selector a ojo sin validar      falla en la siguiente iteracion
✅ Reproducir aislado y leer el error literal
✅ Clasificar la causa, aplicar el patron, verificar con ejecucion repetida
```

## Checklist de cierre

- [ ] Fallo reproducido de forma aislada
- [ ] Error literal leido, causa clasificada
- [ ] Causa raiz identificada, no el sintoma
- [ ] Fix minimo aplicado (el menor que resuelve la causa)
- [ ] Verificado con `--repeat-each 10` sin fallos
- [ ] Leccion documentada via `automation-assets`

## Lectura bajo demanda

Este SKILL.md ya trae las 7 categorias de error con su fix y los anti-patrones de debugging.

| Si el SKILL.md no alcanza y necesitás | Leé |
|---|---|
| Caso real documentado de cada fallo | `docs/knowledge/Automation_QA/Strategy/Troubleshooting/README.md` |
| Estrategias anti-flakiness | `docs/knowledge/Automation_QA/06-mejores-practicas/01-flaky-tests.md` |
| Errores de selector especificamente | `.claude/skills/automation-selectors/SKILL.md` |

Localiza la seccion antes de leer: `grep -n "^## " <archivo>`

**Stop**: clasificar por la tabla y aplicar el fix es lo habitual. Abrir el detalle solo si tu sintoma no esta en las 7 categorias.

---

*Automation Troubleshooting — reproducir, clasificar, corregir, verificar. Platform: Claude Code.*