---
name: rest-assured-api-workflow
description: Usa esta skill para diseñar, generar y revisar pruebas de API con REST Assured, incluyendo Given/When/Then, matchers, filters y reportes Allure.
---

# REST Assured API Workflow

## Objetivo
Generar, ejecutar y revisar pruebas de API con REST Assured (Java + JUnit/TestNG).

## Flujo
1. Define el alcance: endpoints, métodos, body y dependencias.
2. Configura el proyecto Maven/Gradle con REST Assured, json-schema-validator y allure-rest-assured; define `RestAssured.baseURI`/`basePath` y request specification global en `@BeforeAll`.
3. Escribe tests con Given/When/Then, validación de schema con `body(matchesJsonSchema())` y Hamcrest matchers.
4. Ejecuta con `mvn test` y revisa el reporte Allure.
5. Resume hallazgos: cobertura, fallos, tiempos de respuesta y contract validation.

## Patrones clave
- **Auth**: `.auth().oauth2(token)` (Bearer), `.auth().basic(...)`, `.auth().digest(...)`
- **Assertions**: Hamcrest — `equalTo`, `greaterThan`, `containsString`, `hasItems`; JSONPath — `body("users[0].name", ...)`
- **Extract**: `extract().path(...)`, `extract().as(Class.class)` para encadenar escenarios
- **Specs reutilizables**: `RequestSpecBuilder` / `ResponseSpecBuilder`
- **Logging/filtros**: `.log().ifValidationFails()`; filtro `AllureRestAssured` para reportes
- **Data-driven**: `@ParameterizedTest` / `@Parameterized`

## Reglas
- Configuración por entorno vía variables de entorno / sistema, nunca hardcoded.
- Assertions alineados con los criterios de aceptación del test plan.
