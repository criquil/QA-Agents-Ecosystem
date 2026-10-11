# Plan de Calidad QA — {plan_id}

> **Estado**: plantilla — completar en cada revisión.
> **Owner**: {responsable} · **Aprobado por**: {aprobador} · **Fecha**: {YYYY-MM-DD}

## 1. Objetivo

{Qué se busca lograr con este plan de gobernanza. Alcance y límites.}

## 2. Alcance

| Incluido | Excluido |
|---|---|
| {disciplinas/equipos cubiertos} | {fuera de alcance} |

## 3. Estándares aplicables

| Estándar | Versión | Aplicación |
|---|---|---|
| ISO/IEC 25010 | 2011 | Características de calidad del producto |
| ISO/IEC 29148 | 2011 | Procesos de ciclo de vida y requisitos |
| ISO 9001 | 2015 | Gestión de calidad organizacional |
| WCAG | 2.2 | Accesibilidad nivel AA |
| OWASP API Security Top 10 | 2023 | Seguridad de APIs |

## 4. Métricas y umbrales

| Métrica | Objetivo | Fuente | Frecuencia |
|---|---|---|---|
| Defect Escape Rate | < 5% | Jira | Trimestral |
| Code Coverage | ≥ 80% | CI | Por release |
| p95 latencia | {SLA} | APM | Diario |
| WCAG violaciones AA | 0 | axe + auditoría | Por release |

## 5. Roles y responsabilidades

| Rol | Nombre | Responsabilidad |
|---|---|---|
| QA Lead | {} | Adopción de estándares |
| Dev Lead | {} | Shift-Left, quality gates |
| Product Owner | {} | Criterios de aceptación |

## 6. Entregables

- [ ] Checklist de gobernanza por disciplina
- [ ] Reporte de auditoría con hallazgos P1/P2/P3
- [ ] Plan de mejora (CAPA)
- [ ] Evidencia de cumplimiento

## 7. Revisión

**Próxima revisión**: {fecha} · **Veredicto anterior**: {PASSED | CONDITIONAL | FAILED}