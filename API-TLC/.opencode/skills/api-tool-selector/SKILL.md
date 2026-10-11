---
name: api-tool-selector
description: Usa esta skill cuando necesites elegir entre RestSharp, Karate Framework, Playwright o REST Assured para un caso de API testing. Aplica criterios de stack tecnológico, tipo de prueba, CI/CD y curva de aprendizaje.
---

# API Tool Selector

## Objetivo
Elegir la herramienta adecuada para un escenario de pruebas de API y justificar la decisión con criterios técnicos.

## Matriz de decisión

| Criterio | RestSharp | Karate | Playwright | REST Assured |
|----------|-----------|--------|------------|--------------|
| **Lenguaje** | C# / .NET | Gherkin (multi) | JS/TS | Java |
| **Tipo** | Library | Framework | Framework | Library |
| **HTTP** | ✅ | ✅ | ✅ | ✅ |
| **gRPC** | ❌ | ✅ | ❌ | ✅ |
| **GraphQL** | Manual | ✅ | ❌ | Manual |
| **BDD** | ❌ | ✅ | ❌ | ❌ |
| **Contract** | ❌ | ✅ | ❌ | ❌ |
| **Reportes** | xUnit/NUnit | HTML nativo | HTML Playwright | Allure |
| **CI/CD** | GitHub Actions | Maven/Gradle | GitHub Actions | Maven/Gradle |
| **Curva aprendizaje** | Baja (familiar .NET) | Media | Baja (familiar JS) | Media |

## Recomendaciones por stack

- **Equipo .NET/C# → RestSharp**: integración natural con xUnit/NUnit, HTTP/REST completo
- **Equipo Java → REST Assured**: integración con JUnit/TestNG, reportes Allure, soporte gRPC/GraphQL
- **Equipo JavaScript/TypeScript → Playwright**: API + browser testing en una herramienta, fixtures modernos
- **Multi-lenguaje / BDD / multi-protocolo → Karate**: Gherkin legible, HTTP/gRPC/GraphQL/WebSocket, reportes HTML nativos, mock server integrado
- **Contract-first development → Karate**: validación de contrato nativa

## Flujo
1. Identifica el objetivo principal: functional, integration, contract, E2E, BDD.
2. Confirma stack tecnológico y restricciones (.NET, Java, JavaScript, multi-lenguaje).
3. Evalúa restricciones del equipo: lenguaje, curva de aprendizaje, integración CI/CD.
4. Compara opciones con la matriz de decisión (pros, contras, riesgos).
5. Devuelve recomendación final y alternativa de respaldo.

## Salida Esperada
- Herramienta recomendada.
- Razones técnicas en bullets.
- Riesgos de implementación.
- Siguiente skill a cargar: la skill de workflow de la herramienta elegida (`restsharp-api-workflow`, `karate-api-workflow`, `playwright-api-workflow` o `rest-assured-api-workflow`).
