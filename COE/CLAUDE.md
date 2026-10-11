# COE Maru — Gobernanza de Buenas Prácticas de QA

Guía persistente para agentes Claude Code — COE Maru.

---

## Qué es

**COE Maru** (Center of Excellence) — Agente orquestador de **Gobernanza de Buenas Prácticas de QA**. Responsabilidad cross-team multidisciplinar: API Test, Manual Test, Automation Test, Performance Test, Accessibility Test, y todos los tipos de test disponibles, además de la calidad de procesos del ciclo de vida de desarrollo (SDLC).

El conocimiento vive como skills en `.claude/skills/`; Maru es el entry point y orquesta la gobernanza cargando una skill por disciplina solo cuando se necesita.

**Idioma primario: español** en documentación, output y navegación.

---

## Entry point

`maru` es el **entry point obligatorio** de todo request (agente en `.claude/agents/`).

- Detecta la disciplina en Phase 0 (API, Manual, Automation, Performance, Accessibility, Procesos, Auditoría, Consulta).
- Ejecuta el workflow de gobernanza cargando la skill correspondiente **solo la sección requerida** (`<pre_execution>` → fragmento exacto).
- Lo no-gobernanza se resuelve con subagentes integrados (`general-purpose`/`Explore`) o desde el knowledge base local.

---

## Reglas obligatorias

- **`<pre_execution>`**: todo skill con esa sección DEBE leer con `Read` lo que lista antes de producir output.
- **3 niveles**: `.claude/skills/README.md` (índice maestro) → `SKILL.md` de la skill → `NN_Tema.md` (autoritativo). Leer el Nivel 2 antes de editar un Nivel 3.
- **Edición**: Nivel 3 usa naming `NN_Topic_Name.md`. No duplicar docs: actualizar el existente. Al mover o renombrar, actualizar referencias en `.claude/skills/README.md` y el `SKILL.md` padre.
- **Catálogo**: el índice de skills (y herramientas en `maru-herramientas/`) está en `.claude/skills/README.md`.

---

## Presupuesto de tokens

- **Índice antes que documento**: dudas → `SKILL.md`/índice; detalle → sección con `grep -n "^## "` + `Read` por offset/limit. Nunca leer completo un doc >2.000 tokens.
- **Cheat sheets primero**: fórmulas/umbrales en `maru-metricas-kpis/00_Cheat_Sheet_Metricas.md`, `maru-workload/00_Cheat_Sheet_Workload.md` y `maru-herramientas/00b_Cheat_Sheet_Herramientas.md` (bajo `.claude/skills/`); el doc completo, para API/sintaxis/ejemplos.
- **Envelope acumulado**: cada fase de gobernanza persiste su bloque en `docs/qa-governance/{plan_id}/context_envelope.json`; las siguientes lo cargan y no releen lo ya sintetizado.
- **Límites de tamaño (verificados a mano)**: `agents/*.md` ≤3.200 tokens; `SKILL.md` ≤2.000; Nivel 3 ≤6.000. Al agregar una sección, revisar que el archivo no exceda su límite.

---

## Entregables

Plantilla base en `docs/qa-governance/_plantilla/` (`plan.yaml`, `context_envelope.json`, `qa-quality-plan.md`, `governance-checklist.md`, `audit-report.md`, `improvement-plan.md`). Cada gobernanza real crea su carpeta `docs/qa-governance/{plan_id}/` copiando esa plantilla.

- `docs/qa-governance/{plan_id}/qa-quality-plan.md` — plan de calidad activo (workflows resumibles)
- `docs/qa-governance/{plan_id}/governance-checklist.md` — checklist por disciplina
- `docs/qa-governance/{plan_id}/audit-report.md` — reporte de auditoría con hallazgos
- `docs/qa-governance/{plan_id}/improvement-plan.md` — plan de mejora (CAPA, responsables, plazos)

---

## Rutas clave

- `.claude/skills/README.md` — índice maestro
- `.claude/agents/maru.md` — entry point y pipeline de gobernanza
- `.claude/settings.json` — permisos del proyecto
- `docs/qa-governance/` — artefactos de gobernanza