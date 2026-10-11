---
name: maru-workload
title: "Modelado de Carga — COE Maru"
description: "Guía de modelado de workloads para performance testing: dimensionamiento de usuarios virtuales, TPS, perfiles de carga y cálculo de arriving rate."
version: 1.0
author: "COE Team"
created: "2026-10-10"
domain: "qa-governance-workload"
entry_point: false
parent_orchestrator: "maru"
---

# MARU-WORKLOAD — Modelado de Carga

<pre_execution>

## Cheat sheet primero
- `.opencode/skills/maru-workload/00_Cheat_Sheet_Workload.md` — fórmulas y umbrales

## Lecturas por sección (Nivel 3)
- `01_Dimensionamiento.md` — cómo calcular VUs, TPS, arriving rate
- `02_Perfiles_de_Carga.md` — ramp-up, steady state, spikes, soak

Presupuesto: ninguna lectura >2.000 tokens.

</pre_execution>

## Dimensiones del modelo

- **Usuarios virtuales (VU)**: concurrencia simulada.
- **TPS (arriving rate)**: transacciones por segundo sostenidas.
- **Think time**: pausa entre transacciones del usuario.
- **Ramp-up**: tiempo de incremento de carga.
- **Perfil**: forma de la carga a lo largo del tiempo (step, ramp, spike, soak).

## Reglas

- El modelo debe derivarse de datos reales de producción (analytics, APM).
- Sin datos de producción → declarar supuestos explícitos.
- La capacidad del generador debe ser ≥2× la carga objetivo.

## Deliverables

- `docs/qa-governance/workload-model.md`

---
*Versión 1.0 — 2026-10-10 — MARU Workload*