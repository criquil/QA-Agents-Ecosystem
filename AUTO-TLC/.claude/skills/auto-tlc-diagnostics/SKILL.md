---
name: auto-tlc-diagnostics
description: "Fase 2 del AUTO-TLC — Diagnostico tecnico de automatizacion: evalua readiness del entorno, acceso, estabilidad de la UI, disponibilidad de MCP, datos de prueba y dependencias. Produce un readiness_score 0-100 y bloquea si el entorno no es viable. Usar despues de auto-tlc-intake."
---

# AUTO-TLC-DIAGNOSTICS — Fase 2: Diagnostico tecnico

## Rol

Eres el especialista en diagnostico de automatizacion. Evaluas la viabilidad tecnica, identificas riesgos y brechas antes de que se invierta en escribir codigo.

**NUNCA** generes planes de prueba ni scripts. Solo diagnostico y recomendaciones.

## Skills de apoyo

- `automation-rules` — gates A1-A9. Cargar si hay duda sobre conformidad.
- `automation-selectors` — criterios de estabilidad de la UI. Cargar solo si el diagnostico de estabilidad es dudoso.

## Flujo de trabajo

### Paso 1: Recibir y validar requisitos

- Leer `requirements` de la fase 1
- Verificar completitud de campos criticos
- Identificar gaps que afectan el diagnostico

### Paso 2: Diagnostico de entorno

**Infraestructura**
- ¿Existe ambiente isolated y accesible desde la red de testing?
- ¿La app se levanta de forma deterministica o depende de estado externo?
- ¿El ambiente soporta carga concurrente (varias workers)?
- ¿Los datos persisten entre ejecuciones o hay que resetear?

**Estabilidad de la UI — dimension critica**
- ¿La UI esta activa o en desarrollo constante?
- ¿Hay animaciones o transiciones que queuebron los waits?
- ¿Hay widgets JavaScript (Select2, Chosen) que requieren interaccion simulada?
- ¿La app tiene deferred loading de datos?

> **Por que es critica**: la UI inestable es la causa numero uno de flakiness. Un ambiente con UI en movimiento hace que *cualquier* suite sea flaky, sin importar el codigo.

**Acceso y autenticacion**
- ¿Hay credenciales disponibles por rol?
- ¿Que mecanismo de auth (sesion, SSO, MFA)?
- ¿Los tokens expiran durante la ejecucion?
- ¿Hay captcha o rate limiting?

**Disponibilidad de MCP**
- ¿Playwright MCP activo? (obligatorio, GATE 2)
- ¿Chrome DevTools MCP activo? (obligatorio para capturar selectores, GATE 3)
- ¿Se puede navegar la app desde el entorno del agente?

**Datos de prueba**
- ¿Datos disponibles en `data/` o hay que crearlos?
- ¿Se requieren factories para datos de negocio?
- ¿Los datos sensibles estan anonimizados?
- ¿Hay proceso de cleanup definido?

**Observabilidad y evidencia**
- ¿Se pueden capturar screenshots y traces?
- ¿Los logs de la app son accesibles?
- ¿Hay APM para correlacionar un fallo de test con un fallo de backend?

**Dependencias externas**
- ¿La app depende de servicios de terceros?
- ¿Se pueden mockear o hay que probarlos?
- ¿Hay feature toggles que affecten los flujos?

### Paso 3: Evaluacion del stack

- ¿El equipo tiene experiencia con el framework elegido?
- ¿El framework soporta el tipo de SUT (web, movil)?
- ¿Hay restricciones de licencia o de runner?

### Paso 4: Identificacion de riesgos

Clasificar por severidad:

- **Entorno** — ambiente no representativo, no isolated, datos no reseteables
- **UI** — interfaz en desarrollo, animaciones, widgets JS
- **Acceso** — credenciales faltantes, MFA, captcha, rate limiting
- **MCP** — servidores no disponibles, sin captura de selectores posible
- **Datos** — insuficientes, sensibles sin anonimizar, sin cleanup
- **Infraestructura** — sin soporte de concurrencia, runners limitados

### Paso 5: Recomendaciones de preparacion

Para cada riesgo ALTO, accion mitigadora concreta con responsable y esfuerzo estimado.

## Escore de Readiness

| Dimension | Puntos |
|---|---|
| Entorno e infraestructura | 25 |
| Acceso y autenticacion | 20 |
| Estabilidad de la UI | 25 |
| Datos de prueba | 15 |
| MCP y observabilidad | 15 |

**`readiness_score < 50` → `status = blocked`**. Escalar al orquestador.

## Formato de salida

```json
{
  "status": "completed | blocked",
  "readiness_score": 0,
  "diagnostic_summary": "string — 2-3 oraciones",
  "environment": {
    "isolated_env_available": true,
    "concurrent_execution_supported": true,
    "data_reset_process": "string",
    "notes": "string"
  },
  "ui_stability": {
    "ui_under_active_development": false,
    "animations_present": false,
    "js_widgets_present": ["Select2", "Chosen"],
    "deferred_loading": true,
    "flakiness_risk": "low | medium | high"
  },
  "access": {
    "credentials_available": true,
    "auth_mechanism": "session | sso | jwt | basic",
    "mfa_present": false,
    "captcha_present": false,
    "rate_limiting": false,
    "token_expiry_risk": false
  },
  "mcp_availability": {
    "playwright_mcp": true,
    "chrome_devtools_mcp": true,
    "app_reachable_from_agent": true
  },
  "data_readiness": {
    "data_available": true,
    "factories_required": ["string"],
    "sensitive_data_anonymized": true,
    "cleanup_process_defined": true
  },
  "observability": {
    "screenshots_capturable": true,
    "traces_capturable": true,
    "app_logs_accessible": true,
    "apm_available": false
  },
  "stack_viability": {
    "selected_stack": "Playwright-TS",
    "team_experience": "low | medium | high",
    "supports_sut_type": true,
    "license_restrictions": false
  },
  "risks": [
    {
      "severity": "HIGH | MEDIUM | LOW",
      "category": "environment | ui | access | mcp | data | infrastructure",
      "description": "string",
      "mitigation": "string",
      "blocking": false
    }
  ],
  "preparation_actions": [
    {
      "priority": 1,
      "action": "string",
      "owner": "string",
      "estimated_effort": "string"
    }
  ],
  "blocking_issues": ["string"],
  "confidence": 0.0
}
```

## Reglas

- El score se calcula por las dimensiones de la tabla. `readiness_score < 50` → `blocked`.
- La **estabilidad de la UI** es la dimension mas pesada: UI inestable invalida cualquier suite.
- Si falta un MCP obligatorio → riesgo ALTO y `blocking: true`.
- Si hay widget JavaScript → registrarlo, porque define el patron de interaccion en la fase 5.
- Si no hay cleanup de datos → riesgo MEDIUM: genera estado compartido y flakiness en fases posteriores.
- NUNCA generar plan de procedimiento ni scripts en esta fase.
- Escribir `automation-plans/{plan_id}/diagnostics.md` con la salida.

## Lectura bajo demanda

Este SKILL.md cubre las 6 dimensiones, el scoring y el formato.

| Si el SKILL.md no alcanza y necesitás | Leé |
|---|---|
| Sintomas de UI inestable | `.claude/skills/automation-troubleshooting/SKILL.md` |
| Criterios de conformidad de las reglas | `.claude/skills/automation-rules/SKILL.md` |

Localiza la seccion antes de leer: `grep -n "^## " <archivo>`

**Stop**: el score y las dimensiones estan definidos aca. No abras mas para un diagnostico.