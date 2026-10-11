---
name: automation-foundations
description: "Estrategia de automatización: qué conviene automatizar y qué no, pirámide de testing, selección de stack y framework. Invocar al inicio de un proyecto nuevo o cuando hay que decidir el alcance de la suite."
---

# Automation Foundations — Alcance y Stack

> **Objetivo**: responder dos preguntas antes de escribir una línea de código.
> 1. ¿Qué merece automatizarse?
> 2. ¿Con qué stack se construye la suite?

## Paso 1 — Qué automatizar

El filtro no es "es fácil de automatizar" sino **"es regresión frecuente + crítica + estable"**.

| Señal a favor | Señal en contra |
|---|---|
| Falla a menudo en producción | Cambia cada sprint sin criterio |
| Camino crítico de negocio | UI puramente cosmética |
| Verificable de forma determinista | Resultado depende de timing no controlable |
| Volumen alto de ejecución | Se ejecuta 2 veces al año |
| Requiere setup repetitivo y largo | Setup de 2 minutos |

### Reglas de decisión

1. **Automatizá el camino crítico**, no el exhaustivo. La suite E2E cubre el 20% de los flujos que genera el 80% de los incidentes.
2. **No automatices lo que todavía cambia.** Un test sobre una pantalla en diseño activo es deuda, no cobertura.
3. **Preferí niveles bajos.** La pirámide manda: cada E2E que se puede bajar a integración es tiempo y flakiness recuperados.
4. **No automatices para reemplazar al exploratory testing.** La automatización no explores.

### Salida esperada

Una tabla de funcionalidades con veredicto explícito — no un "depende":

| Funcionalidad | Frecuencia | Criticidad | Estabilidad UI | Nivel | Decisión |
|---|---|---|---|---|---|
| Login | Alta | Crítica | Estable | E2E | AUTOMATIZAR |
| Recuperar password | Media | Alta | Inestable | E2E | DIFERIR |
| Perfil de usuario | Baja | Media | Estable | Integración | AUTOMATIZAR |
| Carrusel de promo | — | Nula | Inestable | — | NO AUTOMATIZAR |

## Paso 2 — Ubicar en la pirámide

```
        /\
       /  \        E2E      ~10%   Pocos, lentos, visibles
      /----\
     /      \      Integr.  ~30%   APIs, DB, servicios
    /--------\
   /          \    Unit     ~60%   Logica pura, rapido
  /____________\
```

Criterio de descenso: si el test no necesita browser, **no debería usar browser**. Cada E2E cuesta ~10-50x un test de integración.

## Paso 3 — Seleccionar el stack

### Web

| Framework | Elegir cuando |
|---|---|
| **Playwright** | Default. Multi-browser, auto-waiting, paralelismo nativo, tracing. |
| **Selenium** | Legado existente, necesidad de un browser grid corporativo estricto. |
| **Cypress** | Equipo JS-centric, feedback en el navegador es prioritario. |
| **Puppeteer** | Solo Chromium, integración Node pura. |

### Móvil

| Framework | Elegir cuando |
|---|---|
| **Appium** | Multi-plataforma (iOS + Android) desde una sola suite. |
| **Maestro** | Flujos moviles simples, YAML, poco mantenimiento. |

### Runner y lenguaje

- **TypeScript** — default recomendado: tipos compartidos entre Page Object y tests.
- **Python** — cuando el equipo es Python o el proyecto ya tiene esa base.
- **Java / C#** — cuando la org ya estandarizó por ecosistema enterprise.

**Regla**: si ya existe una suite, el stack **no se cambia**. Migrar framework es un proyecto, no una decisión.

## Paso 4 — Pirámide de decisión

```
¿El fallo sería costoso en producción?
  NO  -> NO automatizar. Botar en backlog.
  SI  -> ¿La lógica se puede probar sin browser?
           SI  -> Integracion / Unit. Mas barato, mas rapido, menos flaky.
           NO  -> ¿La UI esta estable?
                    NO  -> DIFERIR. Marcar como candidato y revisar en 2 sprints.
                    SI  -> E2E. Con tags para pipeline.
```

## Salida del skill

`automation-plans/plan_[ID]_alcance.md` con:

1. Inventario de funcionalidades y decisiones
2. Nivel asignado por test
3. Stack elegido **con la razón** y las alternativas descartadas
4. Riesgos de la decisión (deuda, curva de aprendizaje, lock-in)

## Lectura bajo demanda

Este SKILL.md ya trae la decision de alcance, la piramide y la tabla de stacks.

| Si el SKILL.md no alcanza y necesitás | Leé |
|---|---|
| Detalle de cuando automatizar | `docs/knowledge/Automation_QA/01-fundamentos/03-cuando-automatizar.md` |
| Comparativa completa de frameworks | `docs/knowledge/Automation_QA/02-frameworks/README.md` |
| Sintaxis de un framework puntual | `docs/knowledge/Automation_QA/02-frameworks/03-playwright.md` (o `01-selenium.md`, `02-cypress.md`, `04-appium.md`) |
| Data-driven / keyword-driven / BDD | `docs/knowledge/Automation_QA/04-estrategias/` |

Localiza la seccion antes de leer: `grep -n "^## " <archivo>`

**Stop**: para decidir que automatizar y con que stack, este archivo basta. No abras el `MASTER-README.md`.

---

*Automation Foundations — alcance y stack. Platform: OpenCode.*