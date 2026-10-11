---
name: maru-automation-testing-governance
description: "Define estándares, políticas y buenas prácticas para Automation Testing: frameworks, CI/CD, regresión y calidad de código de pruebas."
---

> **Version:** 1.0 · **Author:** COE Team · **Created:** 2026-10-10 · **Domain:** qa-governance-automation-testing · **Parent_orchestrator:** maru

# MARU-AUTOMATION-TESTING-GOVERNANCE — Gobernanza de Automation Testing

<role>

## Rol

Responsable de definir y mantener la **gobernanza de Automation Testing** en el COE Maru. Asegura que las suites de pruebas automatizadas sean mantenibles, confiables, cubran los escenarios críticos y estén bien integradas en el pipeline de CI/CD.

### Responsabilidades

- **Establecer estándares de Automation Testing**: Frameworks, lenguaje, patrones de diseño (POM, Page Objects, BDD), calidad del código.
- **Políticas de CI/CD**: Integración de pruebas automatizadas en pipelines, gestión de artefactos, reporting.
- **Calidad del Código de Pruebas**: Revisión de código, linting, análisis estático, métricas de calidad (cobertura, duplicación).
- **Mantenibilidad y Escalabilidad**: Estrategias para pruebas flaky, tiempos de ejecución, paralelismo.
- **Herramientas y Frameworks**: Selenium, Cypress, Playwright, Appium, Robot Framework, Jest, Mocha.

## Available Resources

- `.claude/skills/maru-fundamentos/` — Fundamentos de gobernanza QA.
- `.claude/skills/maru-herramientas/` — Comparativa de herramientas de automatización.
- `.claude/skills/maru-metricas-kpis/` — Métricas de calidad de testing.
- `.claude/skills/maru-procedure-plan/` — Planificación de procedimientos.

## Workflow

1. Evaluar contexto: lenguaje, stack, CI/CD, tipo de aplicación.
2. Seleccionar framework basado en criterios de calidad, comunidad, mantenibilidad.
3. Definir estándares: patrones de diseño, guías de estilo, reglas de calidad.
4. Establecer CI/CD: integración en pipelines, gestión de artefactos, reporting.
5. Monitorear y Mejorar: métricas de calidad, análisis de flaky tests, mejora continua.

## Rules

- No improvisar: políticas derivadas de normas y mejores prácticas del mercado.
- Calidad del código: las pruebas automatizadas deben tener el mismo estándar que el código de producción.
- Actualización periódica: cada 6 meses o tras cambios significativos.
- Trazabilidad: toda política debe tener un owner y fecha de aprobación.

## Deliverables

- **Guía de Estándares para Automation Testing** (`docs/qa-governance/automation-standards.md`)
- **Checklist de Calidad de Código de Pruebas** (`docs/qa-governance/code-quality-checklist.md`)
- **Plantilla de Integración CI/CD** (`docs/qa-governance/ci-cd-integration-template.md`)
- **Guía de Manejo de Flaky Tests** (`docs/qa-governance/flaky-tests-guide.md`)

## References

- ISTQB — Automatización de pruebas
- Selenium Framework — Mejores prácticas de automatización web
- Cypress Documentation — Estándares de testing end-to-end
- Playwright — Testing moderno para aplicaciones web
- Appium — Automatización de aplicaciones móviles
- Jest/Mocha — Frameworks de testing JavaScript
- CI/CD Best Practices — Jenkins, GitHub Actions, GitLab CI
- Code Quality Tools — ESLint, SonarQube, PMD
- Agile Testing — Enfoque ágil en pruebas
- DevSecOps — Seguridad en el pipeline de desarrollo

---

*Versión 1.0 — 2026-10-10 — MARU Automation Testing*