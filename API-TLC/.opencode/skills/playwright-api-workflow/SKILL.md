---
name: playwright-api-workflow
description: Usa esta skill para diseñar, generar y revisar pruebas de API con Playwright (APITesting), incluyendo request context, fixtures, assertions y test generation.
---

# Playwright API Workflow

## Objetivo
Generar, ejecutar y revisar pruebas de API con Playwright (JS/TS).

## Flujo
1. Define el alcance: endpoints, métodos, body fixtures y dependencias.
2. Configura `playwright.config.ts` con baseURL, timeouts, retries y `extraHTTPHeaders` (Accept, Authorization).
3. Escribe tests usando el fixture `request` (request context) y fixtures reutilizables para auth.
4. Ejecuta con `npx playwright test` y revisa el HTML report.
5. Resume hallazgos: cobertura, fallos, tiempos de respuesta y contract validation.

## Patrones clave
- **Tests**: `test.describe()` para agrupar, `test()` por escenario; naming "GET /users/:id - returns user when exists"
- **Contract validation**: schemas JSON (zod o validación manual de propiedades/tipos) contra el response body
- **Assertions**: `expect(response.status())`, `await response.json()`, headers, response time (`Date.now()` delta)
- **Data-driven**: arrays de datos o CSV/JSON leídos con `fs` + `csv-parse`
- **Parallel execution**: seguro con aislamiento de datos por test; projects en config para separar suites

## Reglas
- Sin valores hardcoded de ambiente: `process.env.API_BASE_URL` / `process.env.AUTH_TOKEN`.
- Assertions alineados con los criterios de aceptación del test plan.
