---
name: maru-metricas-kpis
description: "Catálogo autoritativo de métricas de calidad: definiciones, fórmulas, umbrales de aceptación y cálculo de NFRs y KPIs."
---

> **Version:** 1.0 · **Author:** COE Team · **Created:** 2026-10-10 · **Domain:** qa-governance-metricas · **Parent_orchestrator:** maru

# MARU-METRICAS-KPIS — Métricas y KPIs

<pre_execution>

## Documentos completos (2)
- `.claude/skills/maru-metricas-kpis/SKILL.md` — este archivo (catálogo de métricas)

## Cheat sheet primero (preferir sobre el doc completo)
- `.claude/skills/maru-metricas-kpis/00_Cheat_Sheet_Metricas.md` — fórmulas y umbrales

## Lecturas por sección (Nivel 3)
- `01_Metricas_de_Proceso.md` — lead time, escape rate, MTTR
- `02_Metricas_de_Calidad.md` — coverage, pass rate, flaky rate
- `03_Umbrales_y_Criterios.md` — umbrales de aceptación por disciplina

Presupuesto: ninguna lectura >2.000 tokens.

</pre_execution>

## Métricas de proceso
Lead Time · Cycle Time · Defect Escape Rate · MTTR · Review Time

## Métricas de calidad
Code Coverage · Pass Rate · Flaky Rate · Defect Density · Severity Distribution

## Métricas de rendimiento
p95 · p99 · Throughput · Error Rate · Saturation Point

## Métricas de accesibilidad
Violaciones WCAG · Cobertura de pruebas manuales de accesibilidad

## Reglas

- Toda métrica debe tener definición formal, fórmula, fuente de datos y umbral.
- Si no hay umbral acordado, la métrica no se reporta.
- Métricas sin owner no se publican.

## Deliverables

- `docs/qa-governance/metrics-dashboard.md`

---
*Versión 1.0 — 2026-10-10 — MARU Métricas*