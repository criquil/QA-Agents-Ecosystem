---
name: automation-selectors
description: "Captura y validación de selectores con Chrome DevTools MCP y jerarquía XPath. Invocar siempre antes de definir cualquier selector en un Page Object o cambiar un selector roto."
---

# Automation Selectors — Captura y Validación

> **Regla de oro**: ningún selector se escribe sin haberlo capturado y validado contra el DOM real.

## El flujo obligatorio

```
1. Playwright MCP      ->  navegar a la URL real del entorno
2. Chrome DevTools MCP ->  take_snapshot (leer el DOM real)
3. DevTools MCP        ->  evaluate_script (confirmar unicidad)
4. Probar interacción  ->  click / fill sobre el elemento
5. Fijar el selector   ->  constante UPPERCASE en el Page Object
6. Documentar          ->  origen + fecha de validación
```

Saltarse el paso 2 es la causa numero uno de tests que no corren nunca.

## Herramientas MCP

| Paso | Tool | Para que |
|---|---|---|
| Navegar | `browser_navigate` | Llevar el browser a la pagina objetivo |
| Inspeccionar | `browser_snapshot` | Leer la estructura accessible del DOM |
| Verificar | `browser_evaluate` | Contar elementos que matchea el selector |
| Interactuar | `browser_click` / `browser_fill` | Confirmar que el elemento responde |
| Evidencia | `browser_take_screenshot` | Dejar registro del estado |

## Jerarquía de prioridad

Usar siempre el primer nivel disponible. Bajar de nivel solo cuando el anterior no existe o no es unico.

| # | Nivel | Ejemplo | Cuando |
|---|---|---|---|
| 1 | `id` | `xpath=//*[@id="login-btn"]` | Siempre que exista |
| 2 | `name` | `xpath=//*[@name="email"]` | Campos de formulario sin id |
| 3 | `data-testid` | `xpath=//*[@data-testid="submit"]` | Atributo pensado para tests |
| 4 | `data-*` | `xpath=//*[@data-action="confirm"]` | Atributos custom |
| 5 | ARIA | `xpath=//button[@aria-label="Submit"]` | Apps accesibles |
| 6 | Texto | `xpath=//button[text()="Aceptar"]` | Texto unico y estable |
| 7 | `class` | `xpath=//*[contains(@class,"btn-primary")]` | Ultimo recurso, siempre con contexto |
| 8 | XPath complejo | `xpath=//*[@id="form"]//input[@name="y"]` | Solo si nada mas funciona |

### Reglas de construccion

1. **Anclar con un atributo estable** (`id`, `name`, `data-*`) y descender desde ahi.
2. **Acotar con contexto** cuando el atributo no es unico: `//*[@id="modal"]//button[...]`.
3. **Combinar condiciones** para aumentar especificidad: `//input[@name="email" and @type="text"]`.
4. **XPath mas corto que funcione.** Cada nivel de anidamiento es fragility.
5. **Normalizar texto**: `normalize-space()` en vez de indices.

## Anti-patrones

```text
❌ /html/body/div[1]/div[2]/span[3]          ruta absoluta, frágil ante cualquier cambio
❌ //div[3]/span[2]                           depende de posicion, sin identidad
❌ //*[@class="active"]                      clase sin contexto, colisiona
❌ //span[text()="OK"]                        texto ambiguo, se repite
❌ //div[@class="css-1a2b3c"]                clase generada dinámicamente
❌ xpath=//button[@id="btn-login"]           inventado sin validar
```

## Selectoresspeciales por tecnologia

| Tecnologia | Como verificar |
|---|---|
| Shadow DOM | El `browser_snapshot` lo expone como shadow-root; anclar por host y entrar con `>>>` |
| iframe | Anclar por `id` o `name` del iframe y cambiar de contexto antes de buscar |
| Canvas | Sin DOM: se interactua por coordenadas relativas al bounding box |
| SVG | Buscar por `id`, `aria-label` o `data-testid`; los paths no son direccionables |
| iFrame dinamico | Esperar a que exista antes de interactuar, no esperar un timeout fijo |

## Checklist antes de fijar un selector

- [ ] Navegue a la pagina real con Playwright MCP
- [ ] Inspeccione el DOM con Chrome DevTools MCP
- [ ] Confirme que matchea **un solo** elemento (`browser_evaluate` con count)
- [ ] Interactue con el elemento y verify que responde
- [ ] Use el nivel mas alto de la jerarquia disponible
- [ ] El selector es corto, con anclaje estable y sin indices
- [ ] Documente origen y fecha de validacion en el Page Object

## Senales de alarma

Si ves esto, el selector no fue validado:

- `TimeoutError` consistente de 30s en un paso concreto
- `strict mode violation: locator resolved to N elements`
- El test funciona manual pero falla automatizado
- Selectores "genericos" tipo `btn_continuar` sin documentacion de origen
- Cambios de selector necesarios en cada iteracion de debugging

## Salida del skill

Tabla de selectores validados, que se pega en el Page Object:

| Elemento | Selector | Nivel | Validado | Notas |
|---|---|---|---|---|
| Input usuario | `xpath=//*[@id="username"]` | 1 | 2026-01-15 | unico en el DOM |
| Btn login | `xpath=//*[@id="login-form"]//button[@type="submit"]` | 1+8 | 2026-01-15 | anidado por contexto |

## Lectura bajo demanda

Este SKILL.md ya trae el flujo MCP, la jerarquia completa y los anti-patrones.

| Si el SKILL.md no alcanza y necesitás | Leé |
|---|---|
| Ejemplos de XPath por framework | `docs/knowledge/Automation_QA/Strategy/Selectors_Strategy/README.md` — seccion `## Framework-Specific Examples` |
| Selectores que fallan y como se arreglan | `.claude/skills/automation-troubleshooting/SKILL.md` |
| Selectores ya validados del proyecto | `automation-plans/*/selectors.md` (usar `Grep` primero) |

Localiza la seccion antes de leer: `grep -n "^## " <archivo>`

**Stop**: la jerarquia y el flujo estan aca. Abrir el knowledge solo si tu caso no esta en la tabla.

---

*Automation Selectors — capturar, validar, fijar. Platform: Claude Code.*