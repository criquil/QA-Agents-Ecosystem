---
name: maru-test-types
title: "Catálogo de Tipos de Prueba — COE Maru"
description: "Referencia completa de todos los tipos de prueba disponibles para gobernanza: funcionales, no funcionales, exploratorios, seguridad, compatibilidad, recuperación."
version: 1.0
author: "COE Team"
created: "2026-10-10"
domain: "qa-governance-test-types"
entry_point: false
parent_orchestrator: "maru"
---

# MARU-TEST-TYPES — Catálogo de Tipos de Prueba

<pre_execution>

Leer primero `.opencode/skills/README.md` (Nivel 1). Para umbrales/criterios de paso usar `.opencode/skills/maru-metricas-kpis/00_Cheat_Sheet_Metricas.md`. No leer más de 2.000 tokens de una sola vez.

</pre_execution>

## Tipos disponibles

- Funcionales (unit, integración, sistema, regresión, smoke, sanity)
- No funcionales (performance, seguridad, accesibilidad, usabilidad, confiabilidad)
- Exploratorios (charter-based, session-based)
- De seguridad (penetración, vulnerabilidad, OWASP Top 10)
- De compatibilidad (navegadores, dispositivos, sistemas operativos)
- De recuperación (disaster recovery, backup restore)
- Contract testing (consumer-driven, provider verification)
- A/B testing, canary releases, blue-green

## Invocación

Invocar solo cuando Maru detecta que debe definir o validar qué tipo de prueba aplica a la disciplina en curso. Leer la sección específica (`grep -n "^## "`) y no el archivo completo.

---
*Versión 1.0 — 2026-10-10 — MARU Test Types*