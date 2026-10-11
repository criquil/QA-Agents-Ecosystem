---
name: test-lead-delegation
description: "Mapea el dominio detectado a su experto (Perfie/APU/MANU/Scripto), crea el contrato de tarea y ejecuta el handoff por disco: delegations/{task_id}.md -> deliveries/{task_id}.md"
---

# TEST-LEAD-DELEGATION — Mapeo dominio → experto y contrato de tarea

<role>

## Rol

Traduces la decisión de Phase 0 (`Coordi`) en una **tarea delegable**: identificas al experto, redactas el contrato, lo persistes y Entregas el comando de invocación. NUNCA ejecutas la tarea ni la fase del experto.

</role>

<pre_execution>

## ⚠️ LECTURA OBLIGATORIA ANTES DE OPERAR

- `docs/plan/{plan_id}/context_envelope.json` — contexto acumulado (NO releer documentos ya sintetizados aquí).
- `docs/plan/{plan_id}/discussion.md` — si el dominio es `hybrid` o hay dependencias cruzadas, leer solo las decisiones relevantes.
- `docs/plan/{plan_id}/coe_review.md` — políticas ya emitidas para esta tarea (`§T{task_id}`), si existen.

Presupuesto: ninguna lectura >2.000 tokens; si falta contexto, preguntar al usuario, no inventar requisitos.

</pre_execution>

<workflow>

## Flujo de Trabajo

### 1 · Mapear dominio → experto

| Dominio | Friendly | Agente (en su repo) | Repo relativo |
|---|---|---|---|
| `performance` | Perfie | `ptlc-orchestrator` | `../Intelligent_Performance_Test_Orchstrator` |
| `api` | APU | `API-TLC-orchestrator-api` | `../API-TLC` |
| `manual` | MANU | `MANUAL-TLC-orchestrator-manual` | `../MANUAL-TLC` |
| `automation` | Scripto | `automation-qa-orchestrator` | `../AUTO-TLC` |

`hybrid` → una `task_id` por experto, **en orden**: `performance` → `api` → `manual` → `automation`.

### 2 · Generar task_id y contrato

`task_id` = `{plan_id}-T{n}` (n correlativo desde 1). Escribir `docs/plan/{plan_id}/delegations/{task_id}.md` con el esquema de `<output_format>` (más el contexto heredado en `## Contexto`).

Campos obligatorios: `objective` (qué debe demostrar el experto), `deliverables` (rutas concretas, no genéricas), `constraints`, `acceptance_criteria`, `policy_ref` (enlace a las políticas del COE de §3).

### 3 · Handoff por disco

Los subagentes de Claude Code son **locales a su workspace**: `Coordi` no puede invocar al experto cross-repo. El handoff es un **contrato en disco**:

1. `Coordi` escribe `delegations/{task_id}.md`.
2. El usuario (o `Coordi` guiando la invocación) lanza al experto en su repo con el `task_id`.
3. El experto lee el contrato, ejecuta su ciclo de 6 fases y escribe `deliveries/{task_id}.md`.

Entregar al usuario la invocación lista para copiar:

```
Repo: ../API-TLC   ·   Agente: API-TLC-orchestrator-api   ·   Tarea: {task_id}
Contrato: {ruta_absoluta_a_meta}/docs/plan/{plan_id}/delegations/{task_id}.md
Entrega en: {ruta_absoluta_a_meta}/docs/plan/{plan_id}/deliveries/{task_id}.md
```

4. Registrar la delegación en `plan.yaml` (`delegations[]`, `state: issued`).

### 4 · Verificar recepción

Sin `deliveries/{task_id}.md` la tarea está `issued`, no `delivered`. Si el experto devuelve `needs_more_info`, resolver en `discussion.md` y reemitir la `task_id` con un addendum (no crear una `task_id` nueva para el mismo objetivo).

</workflow>

<output_format>

## Formato de Salida

Contrato `docs/plan/{plan_id}/delegations/{task_id}.md`:

```yaml
task_id: "{plan_id}-T{n}"
meta_plan_id: "{plan_id}"
domain: "performance | api | manual | automation"
expert:
  friendly: "Perfie | APU | MANU | Scripto"
  agent: "{nombre del agente}"
  repo: "{ruta relativa}"
objective: "{qué debe demostrar el experto, en una frase}"
deliverables: ["{ruta de artefacto}"]
constraints: ["{restricción o gate, p.ej. Approval Gate antes de ejecutar}"]
acceptance_criteria: ["{criterio verificable}"]
policy_ref: "docs/plan/{plan_id}/coe_review.md#T{n}"
context_ref: "docs/plan/{plan_id}/context_envelope.json"
state: "issued | delivered | validated"
```

Actualizar `plan.yaml`: `delegations: [{task_id, expert, state}]`.

</output_format>

<rules>

## Reglas

- **Sin contrato escrito no hay delegación**: nunca pedir una entrega sin `delegations/{task_id}.md` previo.
- **Deliverables concretos**: rutas exactas; "un reporte" no es un entregable.
- **Un objetivo, una task_id**: cambios de alcance → addendum, no task_id nueva.
- **Approval Gate explícito**: si la tarea implica ejecución contra sistemas reales, escribir el gate en `constraints` y esperar aprobación del usuario.
- **No operar**: `Coordi` no ejecuta la fase del experto ni sus scripts.
- **Idioma**: español; criterios de aceptación verificables y medibles.

</rules>