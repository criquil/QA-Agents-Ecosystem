# ADR-001: Adopción de Playwright como estándar de automatización web

**Estado**: Aceptado
**Fecha**: 2026-10-10
**Deciders**: COE Team
**Owner**: QA Lead

## Contexto

Se requiere un estándar único para automatización de pruebas web (E2E). El equipo
actualmente mezcla Selenium (legado), Cypress (proyectos nuevos) y pruebas
manuales E2E sin estandarizar.

## Opciones evaluadas

| Opción | Pros | Contras |
|---|---|---|
| Selenium WebDriver | Estándar de facto, multi-navegador | Curva de aprendizaje, API verbosa, paralelismo complejo |
| Cypress | DX excelente, debugging integrado | Solo Chromium/Firefox/WebKit, sin soporte multi-navegador nativo |
| Playwright | Multi-navegador nativo, paralelismo, espera automática | Ecosistema más nuevo que Selenium |

## Decisión

Adoptar **Playwright** como estándar para automatización web E2E.
Selenium se mantiene solo para suites legadas en fase de migración.
Cypress queda descontinuado para nuevos proyectos.

## Consecuencias

- **Positivas**: un solo framework, multi-navegador, mejor manejo de async.
- **Negativas**: migración de suites existentes requiere esfuerzo.
- **Acción**: plan de migración de 3 meses documentado en roadmap Fase 2.

## Referencias

- Playwright docs: https://playwright.dev
- ISO/IEC 25010 — mantenibilidad del código de prueba