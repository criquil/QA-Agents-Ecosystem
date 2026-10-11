# Cheat Sheet — Herramientas (decisión rápida)

| Disciplina | Primera opción | Alternativa | Cuándo usar alternativa |
|---|---|---|---|
| API | Postman/Newman | Pact (contratos) | Equipe distributed / contract-first |
| API Java | RestAssured | Karate | Karate si se busca DSL declarativo |
| Manual | TestRail / Xray | Jira nativo | Equipos pequeños sin herramienta dedicada |
| Automation web | Playwright | Cypress / Selenium | Selenium si hay legado W3C |
| Automation mobile | Appium | Detox (React Native) | Detox solo si RN puro |
| Performance | k6 | JMeter / Gatling / Locust | JMeter si multi-protocolo o GUI |
| Accessibility | axe-core + Lighthouse | Pa11y | Pa11y en CI, axe en navegador |
| Calidad de código | SonarQube | ESLint/PMD | ESLint si solo JS/TS |

## Reglas rápidas

- No introducir dos herramientas que cubran lo mismo.
- Priorizar open source salvo necesidad regulatoria de trazabilidad.
- Toda herramienta debe integrarse en CI/CD.