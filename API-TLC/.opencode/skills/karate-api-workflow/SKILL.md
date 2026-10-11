---
name: karate-api-workflow
description: Usa esta skill para diseñar, generar y revisar pruebas de API con Karate Framework, incluyendo feature files, scenario outlines, call ods, matchers y reportes HTML.
---

# Karate API Workflow

## Objetivo
Generar, ejecutar y revisar pruebas de API con Karate Framework (Gherkin/BDD, multi-protocolo).

## Flujo
1. Define el alcance: endpoints, métodos, datos de entrada y dependencias entre escenarios.
2. Escribe feature files Gherkin con `Scenario Outline` y `Examples` para datos parametrizados.
3. Configura `karate-config.js` para entornos (baseUrl por env), variables globales y hooks.
4. Ejecuta con `mvn test` o `karate -Denv=...` y revisa el reporte HTML (`target/karate-reports/karate-summary.html`).
5. Resume hallazgos: cobertura, fallos, tiempos de respuesta y contract validation.

## Patrones clave
- **Matchers** para validación de schema/contratos: `match response.id == '#number'`, `'#regex'`, `'#contains'`, `'#notnull'`
- **Call/reutilización**: `call read('classpath:auth.feature')` para auth y escenarios compartidos
- **Def**: capturar valores de respuesta (`def userId = response.id`) para encadenar escenarios
- **Organización**: features por dominio, helpers reutilizables, runners por feature

## Reglas
- Nunca hardcodear baseUrl/credenciales en features — usar `karate.properties` o `karate-config.js`.
- Naming descriptivo de scenarios: "Get user by valid ID returns user data".
