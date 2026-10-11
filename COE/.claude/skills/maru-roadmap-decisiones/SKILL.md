---
name: maru-roadmap-decisiones
description: "Contiene el PRD del COE (requisitos de producto), registro de decisiones de arquitectura (ADR) y roadmap de adopción de estándares."
---

> **Version:** 1.0 · **Author:** COE Team · **Created:** 2026-10-10 · **Domain:** qa-governance-roadmap · **Parent_orchestrator:** maru

# MARU-ROADMAP-DECISIONES — Roadmap y Decisiones

<pre_execution>

Leer `PRD.yaml` para requisitos de producto. Leer `decisiones/` (ADR) solo cuando la tarea requiera el contexto de una decisión previa. No cargar el roadmap completo salvo planificación.

</pre_execution>

## Estructura

- `PRD.yaml` — requisitos del COE (visión, alcance, stakeholders, no-objetivos).
- `decisiones/ADR-NNN_Titulo.md` — Architecture Decision Records: contexto, decisión, consecuencias.
- `roadmap.yaml` — fases de adopción de estándares con fechas y responsables.

## Workflow

1. Nueva necesidad → evaluar si requiere decisión (ADR) o solo ejecución.
2. ADR: redactar contexto, opciones evaluadas, decisión, consecuencias.
3. Actualizar `roadmap.yaml` con el impacto y el owner.

## Rules

- Toda decisión que afecte estándares requiere ADR.
- Los ADR son inmutables: se superseden, no se editan.
- Actualizar `.claude/skills/README.md` al crear una skill nueva desde este roadmap.

## Deliverables

- `.claude/skills/maru-roadmap-decisiones/PRD.yaml`
- `.claude/skills/maru-roadmap-decisiones/roadmap.yaml`
- `.claude/skills/maru-roadmap-decisiones/decisiones/ADR-001_*.md`

---
*Versión 1.0 — 2026-10-10 — MARU Roadmap*