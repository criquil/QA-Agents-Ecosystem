---
name: restsharp-api-workflow
description: Usa esta skill para diseñar, generar y revisar pruebas de API con RestSharp, incluyendo configuración de cliente, autenticación, manejo de tokens, assertions y manejo de errores HTTP.
---

# RestSharp API Workflow

## Objetivo
Generar, ejecutar y revisar pruebas de API con RestSharp (.NET/C# + xUnit/NUnit).

## Flujo
1. Define el alcance de la prueba: endpoints, métodos HTTP, datos de entrada.
2. Configura el cliente `RestClient` con base URL, headers default y autenticación (JWT Bearer, OAuth, API Key, Basic) en `[SetUp]`; libera recursos y ejecuta cleanup en `[TearDown]`.
3. Genera tests para cada endpoint (GET, POST, PUT, DELETE) con assertions de status code, body, headers y response time.
4. Implementa data-driven tests con `[TestCase]` o `[TestCaseSource]`; valida schema si hay OpenAPI/Swagger.
5. Ejecuta con `dotnet test` y resume hallazgos: cobertura, fallos, tiempos de respuesta y contract validation.

## Reglas
- Scripts reproducibles: configuración en `appsettings.json`/variables de entorno, nunca valores hardcoded de ambiente.
- Assertions alineados con los criterios de aceptación del test plan.
- Cleanup de datos creados durante los tests (TearDown).
