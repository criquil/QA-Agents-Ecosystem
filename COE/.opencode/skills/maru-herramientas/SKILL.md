---
name: maru-herramientas
title: "Catálogo de Herramientas — COE Maru"
description: "Comparativa y catálogo de herramientas de testing y gobernanza QA por disciplina: API, Manual, Automation, Performance, Accessibility."
version: 1.0
author: "COE Team"
created: "2026-10-10"
domain: "qa-governance-herramientas"
entry_point: false
parent_orchestrator: "maru"
---

# MARU-HERRAMIENTAS — Catálogo de Herramientas

<pre_execution>

Usar `.opencode/skills/maru-herramientas/00b_Cheat_Sheet_Herramientas.md` primero (decisión rápida). Para detalle de API/sintaxis, cargar el doc de la herramienta específica (`01_*.md`, `02_*.md`). No leer el catálogo completo salvo que se necesite.

</pre_execution>

## Por disciplina

| Disciplina | Herramientas |
|---|---|
| API | Postman/Newman, Pact, RestAssured, Karate, SoapUI, Insomnia |
| Manual | TestRail, Zephyr, Xray, Jira, TestFlink |
| Automation | Selenium, Cypress, Playwright, Appium, Robot Framework, Jest, Mocha |
| Performance | k6, JMeter, Gatling, Locust |
| Accessibility | axe-core, Lighthouse, WAVE, Pa11y, JAWS, NVDA, VoiceOver |
| Gestión | Jira, Azure DevOps, GitLab, Confluence, SonarQube |

## Criterios de selección

- Lenguaje del equipo y stack tecnológico.
- Protocolo (HTTP, gRPC, WebSocket, JDBC).
- Curva de aprendizaje.
- Integración CI/CD disponible.
- Costo (open source vs. licencia).
- Soporte de la comunidad.

## Deliverables

- `docs/qa-governance/tool-selection-matrix.md`

---
*Versión 1.0 — 2026-10-10 — MARU Herramientas*