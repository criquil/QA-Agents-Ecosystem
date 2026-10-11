---
name: automation-rules
description: "Reglas obligatorias A1-A9 de la automatización de pruebas y gates MCP. Skill transversal: se invoca SIEMPRE antes de generar cualquier artefacto (Page Object, test, datos, pipeline)."
---

# Automation Rules — Reglas Obligatorias A1-A9

> **Cuándo**: primera skill de cualquier ciclo. Si no la invocaste, el artefacto generado no es conforme.

## Tabla maestra

| Regla | Resumen | Severidad |
|---|---|---|
| **A1 — Validación de selectores** | Ningún selector se define sin capturar y validar contra el DOM real | CRITICA |
| **A2 — Navegación real** | Todo flujo UI/Web se ejecuta contra la app real antes de generar código | CRITICA |
| **A3 — Sin código redundante** | Antes de crear, buscar si ya existe | ALTA |
| **A4 — Selector declarado una vez** | Constante en el Page Object, nunca re-declarado en el test | ALTA |
| **A5 — Sin datos hardcodeados** | Todo dato de prueba se externaliza a `data/` | CRITICA |
| **A6 — Parametrización obligatoria** | Input **y** output esperado se cargan de archivos externos | CRITICA |
| **A7 — Tags obligatorios** | `@project @environment @functionality @specific_case` en todo test | CRITICA |
| **A8 — Template de caso** | Todo caso de prueba usa `docs/templates/tc_template.md` con ID `TC-[ID]` | CRITICA |
| **A9 — Almacenamiento por tipo** | Cada artefacto se guarda con el template de su tipo | ALTA |

## Gates (bloqueantes)

```
GATE 1 — Conocimiento   ¿Se consultó la skill del dominio antes de actuar?
GATE 2 — Playwright MCP ¿Se navegó la app real?                (UI/Web, siempre)
GATE 3 — DevTools MCP   ¿Se validó cada selector en el DOM?   (Page Object nuevo)
GATE 4 — Reuso          ¿Se buscó un activo equivalente?        (antes de crear)
GATE 5 — Codigo         ¿El código compila y el test corre sin placeholders?
```

**Si un gate falla → BLOCKED.** No hay tarea "demasiado simple" que lo salte. Reanudar desde contexto comprimido no exime.

Secuencia: GATE 1 → 2 → 3 → 4 → 5. No se saltea a GATE 5 sin pasar por 2, 3 y 4.

## A1 + A2 — La regla que más tiempo ahorra

Ningún selector se inventa. El flujo obligatorio es:

1. **Playwright MCP** — navegar a la URL real del entorno.
2. **Chrome DevTools MCP** — `take_snapshot` para inspeccionar el DOM real.
3. Verificar unicidad con `evaluate_script`.
4. Probar la interacción antes de fijarla.
5. Registrar el selector con su origen y fecha de validación.

**Por qué es crítica**: un selector inventado produce timeouts de 30s por paso, ciclos de
depuración y una tasa de éxito de 0%. Un selector validado a priori produce un test que pasa a la
primera. La diferencia medida es de horas por caso.

Detalle: `.claude/skills/automation-selectors/SKILL.md`

## A5 + A6 — Golden rule de datos

Nunca hardcodear. Ni credenciales, ni URLs, ni mensajes esperados, ni datos de formulario.

```
❌ await page.fill('#username', 'admin');
❌ await page.goto('http://qa.example.com/login');
✅ const user  = await dataLoader.getData('users', 'admin');
✅ const cfg   = await dataLoader.loadYaml('config');
   await page.goto(cfg.environments[env].baseUrl);
```

El **output esperado también se parametriza**. Un `assert` contra un string literal es un dato
hardcodeado con distinto disfraz.

Detalle: `.claude/skills/automation-data/SKILL.md`

## A7 — Tags que el pipeline depende

```text
@project @environment @functionality @specific_case
```

Sin estos tags, los filtros de CI/CD no encuentran el test y **nunca se ejecuta**. No es un problema
de estilo: es funcional. Verificá siempre que el comando de filtro devuelve resultados.

Detalle: `.claude/skills/automation-tagging/SKILL.md`

## A8 — Template de caso de prueba

Todo caso, creado o importado, usa `docs/templates/tc_template.md`:

- ID único con patrón `TC-[ID]`
- Secciones obligatorias completas: Propósito, Descripción, Data I/O, Steps, Resultado Esperado, Flujo
- Steps en tabla de 3 columnas: `# | Acción | Resultado esperado`

Referencia de implementación: `docs/templates/tc_example.md`

## Checklist de salida

Antes de entregar cualquier artefacto, verificá:

- [ ] ¿Consulté la skill del dominio correspondiente?
- [ ] ¿Navegué la app real con Playwright MCP?
- [ ] ¿Validé cada selector con Chrome DevTools MCP?
- [ ] ¿Busqué un activo equivalente antes de crear?
- [ ] ¿El Page Object hereda de `BasePage` y tiene selectores en MAYÚSCULAS?
- [ ] ¿Ningún dato hardcodeado — input ni output?
- [ ] ¿Los 4 tags obligatorios están presentes?
- [ ] ¿El caso usa el template oficial con ID `TC-[ID]`?
- [ ] ¿No quedan `# TODO`, placeholders ni selectores sin validar?

## Lectura bajo demanda

Este SKILL.md ya contiene las reglas A1-A9 completas. Para el detalle:

| Si el checklist no alcanza y necesitás | Leé |
|---|---|
| Fundamento de las reglas del dominio | `docs/knowledge/Automation_QA/08-rules/README.md` |
| Como capturar un selector con MCP | `.claude/skills/automation-selectors/SKILL.md` |
| Ejemplos de parametrizacion | `.claude/skills/automation-data/SKILL.md` |
| Formato de los 4 tags | `.claude/skills/automation-tagging/SKILL.md` |

**Stop**: para *aplicar* una regla no hace falta leer mas — invocá la skill del dominio y listo.

---

*Automation Rules — reglas A1-A9. Platform: Claude Code.*