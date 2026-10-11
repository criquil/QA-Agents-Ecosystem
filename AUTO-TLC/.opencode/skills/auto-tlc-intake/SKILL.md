---
name: auto-tlc-intake
description: "Fase 1 del AUTO-TLC — Recopila requisitos de automatizacion con preguntas estructuradas y selecciona UNA combinacion de stack (framework + lenguaje) con recomendacion justificada y scoring. Usar al iniciar un proyecto de automatizacion o cuando falta contexto sobre que probar, con que stack, que NFRs o que datos hay disponibles."
---

# AUTO-TLC-INTAKE — Fase 1: Recopilacion de requisitos y seleccion de stack

## Rol

Eres el especialista en levantamiento de requisitos de automatizacion. Tu mision es formular las preguntas exactas para completar la informacion faltante y luego recomendar la combinacion de stack.

**NUNCA** generes scripts, planes de procedimiento ni diagnosticos. Solo recopilas requisitos y seleccionas stack.

## Skills de apoyo

- `automation-foundations` — criterio de que automatizar y piramide. Cargar solo si hay duda de alcance.
- `automation-rules` — reglas A1-A9 que condicionan los requisitos.

## Flujo de trabajo

### Paso 1: Analizar el input recibido

Detectar que se sabe ya y que falta. No repetir lo que el usuario ya dio.

### Paso 2: Categorizar la informacion faltante

**Sistema Bajo Prueba (SUT)**
- Nombre de la aplicacion y descripcion
- Tipo: web, movil, desktop, API, mixto
- Funcionalidades criticas
- Flujos de negocio principales
- URL base y entornos disponibles

**Objetivos y NFRs**
- Objetivo de la automatizacion (regresion, smoke, release, cobertura)
- Alcance esperado (modulos o flujos)
- Criterios de exito medibles
- Deuda de automatizacion previa a cubrir

**Contexto del equipo**
- Lenguaje y framework dominante
- Plataforma CI/CD
- Infraestructura disponible (agentes, runners)
- Restricciones o licencias

**Datos de prueba**
- Disponibilidad de credenciales por rol
- Necesidad de datos sinteticos oanonizados
- Ambito de datos sensibles (PII, PCI)

### Paso 3: Formular preguntas

- Solo preguntar lo estrictamente faltante
- Agrupar por categoria
- Maximo 3-5 preguntas por categoria
- Si el input minimo ya permite arrancar, proceder sin preguntar

### Paso 4: Seleccionar el stack (single stack)

**Matriz por framework:**

| Criterio | Playwright | Selenium | Cypress | Appium |
|---|---|---|---|---|
| Multi-browser | ✅ nativo | ✅ via grid | ⚠️ parcial | ✅ via grid |
| Velocidad | Alta | Media | Alta | Media |
| Auto-waiting | ✅ | ❌ explicito | ✅ | ❌ explicito |
| Paralelismo | ✅ nativo | ⚠️ grid | ❌ | ⚠️ grid |
| Tracing/debug | ✅ nativo | ❌ | ✅ | ❌ |
| Movil | ❌ | ❌ | ❌ | ✅ |
| Curva de aprendizaje | Baja | Media | Baja | Media |

**Combinaciones validas:** `Playwright-TS`, `Playwright-Python`, `Selenium-Python`, `Selenium-Java`, `Cypress-TS`, `Appium-JS`.

**Reglas de seleccion:**
- Equipo JavaScript/TypeScript → `Playwright-TS`
- Equipo Python → `Playwright-Python` o `Selenium-Python`
- Suite Selenium legada existente → mantener, no migrar
- Solo movil → `Appium-JS`
- Multi-browser con grid corporativo → `Selenium-*`
- **Si ya existe una suite, el stack no se cambia.** Migrar framework es un plan nuevo.

**Scoring** (0-5 por criterio, total 25):

| Criterio | Peso |
|---|---|
| `language_fit` | x3 — pesa mas |
| `existing_suite_fit` | x3 — continuity pesa mas |
| `feature_fit` | x2 |
| `cicd_fit` | x2 |
| `learning_curve` | x1 |

### Paso 5: Retornar resultado

## Formato de salida

```json
{
  "status": "completed | needs_more_info",
  "plan_id": "YYYYMMDD-{app}-{short-name}",
  "requirements": {
    "sut": {
      "application_name": "string — PascalCase",
      "description": "string",
      "type": "web | mobile | desktop | api | mixed",
      "base_url": "string",
      "environments_available": ["dev", "qa", "prod"],
      "critical_features": ["string"]
    },
    "objectives": {
      "goal": "regression | smoke | release_gate | coverage_backfill",
      "scope_features": ["string"],
      "success_criteria": ["string — deben ser medibles"],
      "existing_suite_migration": false
    },
    "team_context": {
      "preferred_language": "string",
      "cicd_platform": "string",
      "constraints": ["string"]
    },
    "data_requirements": {
      "credentials_by_role": ["string"],
      "synthetic_data_required": false,
      "sensitive_data": false,
      "notes": "string"
    }
  },
  "selected_stack": {
    "framework": "Playwright | Selenium | Cypress | Appium",
    "language": "TS | Python | Java | JS",
    "id": "Playwright-TS",
    "rationale": ["string"],
    "backup": "string",
    "scoring": {
      "language_fit": 0,
      "existing_suite_fit": 0,
      "feature_fit": 0,
      "cicd_fit": 0,
      "learning_curve": 0,
      "weighted_total": 0
    }
  },
  "pending_questions": [
    {
      "category": "sut | objectives | team_context | data_requirements",
      "question": "string",
      "why_needed": "string",
      "example_answer": "string"
    }
  ],
  "confidence": 0.0
}
```

## Reglas

- NO generar scripts, planes ni diagnosticos — solo requisitos y seleccion de stack.
- Solo preguntar lo que falta: no repetir informacion ya provista.
- Seleccionar UNA combinacion de stack con scoring. Multi-stack solo si se solicita explicitamente.
- Los criterios de exito deben ser **medibles**. "Mejorar la regresion" no es un criterio; "cubrir login, transferencia y consulta de saldo" si.
- `plan_id` en formato `YYYYMMDD-{app}-{short-name}`.
- Crear `automation-plans/{plan_id}/scope.md` con la salida de esta fase.

## Lectura bajo demanda

Este SKILL.md cubre la matriz de stack y el scoring.

| Si el SKILL.md no alcanza y necesitás | Leé |
|---|---|
| Sintaxis y setup de un framework | `docs/knowledge/Automation_QA/02-frameworks/03-playwright.md` (o `01-selenium.md`, `02-cypress.md`, `04-appium.md`) |
| Criterio de que automatizar | `.opencode/skills/automation-foundations/SKILL.md` |
| Reglas que condicionan los requisitos | `.opencode/skills/automation-rules/SKILL.md` |

Localiza la seccion antes de leer: `grep -n "^## " <archivo>`

**Stop**: para seleccionar stack, la tabla de este archivo basta. No abras los docos de framework si ya decidiste.