---
name: generate-test-artifacts
description: Generar múltiples artefactos de prueba (Bruno, Gherkin, casos individuales, Postman, etc.) a partir de casos de prueba detallados.
---

# Generar Artefactos de Prueba Multi-Formato

## 🎯 Objetivo
A partir de los **casos de prueba detallados** (Skill 4), esta skill genera **múltiples artefactos de prueba** en los formatos que el usuario necesite: colección Bruno (`.bru`), archivos Gherkin (`.feature`), casos individuales (JSON/YAML), colección Postman, scripts de automatización, etc.

---

## 🔧 Flujo de la Skill

1. **Input**: casos de prueba detallados (Skill 4) — documento con endpoint, método, body, headers, resultado esperado, validaciones y criterios de aceptación.
2. **Transformación**: La skill pregunta qué formatos de salida desea el usuario y genera los artefactos correspondientes.
3. **Output**: Uno o múltiples formatos de prueba listos para ejecutar.

---

## 📘 Formatos de Salida Soportados

| Formato | Extensión | Uso Principal |
|---------|-----------|---------------|
| **Bruno** | `.bru` | Cliente API nativo Git-friendly, CI/CD |
| **Gherkin (Coded)** | `.feature` | Cucumber, Serenity, Karate (BDD) |
| **Casos Individuales** | `.json` / `.yaml` | Documentación, trazabilidad, importación a herramientas |
| **Postman Collection** | `.json` | Postman, Newman, CI/CD |
| **Karate Scripts** | `.feature` | Karate Framework (Gherkin extendido) |
| **RestSharp Tests** | `.cs` | .NET / C# con xUnit/NUnit |
| **Playwright Tests** | `.spec.ts` | JavaScript/TypeScript |
| **REST Assured Tests** | `.java` | Java con JUnit/TestNG + Allure |

---

## 📘 Ejemplo de Uso

### Input (caso detallado Skill 4)
**Caso de Prueba: TC02 – Crear usuario válido**

- Endpoint: `/users`
- Método: `POST`
- Headers: `Content-Type: application/json`
- Body:
```json
{
  "name": "Cristian",
  "email": "cristian@example.com"
}
```
- Resultado esperado: `201 Created` con `id` y datos del usuario.
- Validaciones: código HTTP 201, body contiene `id`, `name` y `email` coinciden.

---

### Output 1: Bruno (`.bru`)

```bru
meta {
  name: TC02 – Crear usuario válido
  type: http
  seq: 2
}

post {
  url: {{baseUrl}}/users
  body: json
  auth: none
}

headers {
  Content-Type: application/json
}

body:json {
  {
    "name": "Cristian",
    "email": "cristian@example.com"
  }
}

assert {
  res.status == 201
  res.body.has("id")
  res.body.name == "Cristian"
  res.body.email == "cristian@example.com"
}
```

---

### Output 2: Gherkin Coded (`.feature`)

```gherkin
@TestTotal @TC02 @TIER1 @functional
Feature: Crear usuario válido

  Como desarrollador
  Quiero crear un usuario mediante POST /users
  Para validar que el endpoint retorna 201 con el usuario creado

  @TC02_201 @TIER1
  Scenario Outline: [POST][201] Crear usuario válido
    Given declaro la variable "baseUrl" con valor "{{baseUrl}}"
    And declaro la variable "name" con valor "<name>"
    And declaro la variable "email" con valor "<email>"
    When el usuario envía POST a "/users" con body:
      """
      {
        "name": "<name>",
        "email": "<email>"
      }
      """
    Then compruebo que la respuesta contiene estado 201
    And compruebo que el body contiene "id"
    And compruebo que el body "name" es "<name>"
    And compruebo que el body "email" es "<email>"

    Examples:
      | name      | email                   |
      | Cristian  | cristian@example.com    |
```

---

### Output 3: Caso Individual (`.json`)

```json
{
  "id": "TC02",
  "title": "Crear usuario válido",
  "type": "functional",
  "priority": "TIER1",
  "endpoint": "/users",
  "method": "POST",
  "headers": {
    "Content-Type": "application/json"
  },
  "body": {
    "name": "Cristian",
    "email": "cristian@example.com"
  },
  "expected": {
    "status": 201,
    "validations": [
      { "type": "has_property", "path": "id" },
      { "type": "equals", "path": "name", "value": "Cristian" },
      { "type": "equals", "path": "email", "value": "cristian@example.com" }
    ]
  },
  "tags": ["functional", "TIER1", "create", "user"]
}
```

---

### Output 4: Postman Collection (fragmento)

```json
{
  "info": { "name": "API Test Collection", "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json" },
  "item": [
    {
      "name": "TC02 – Crear usuario válido",
      "request": {
        "method": "POST",
        "header": [{ "key": "Content-Type", "value": "application/json" }],
        "body": { "mode": "raw", "raw": "{\n  \"name\": \"Cristian\",\n  \"email\": \"cristian@example.com\"\n}", "options": { "raw": { "language": "json" } } },
        "url": { "raw": "{{baseUrl}}/users", "host": ["{{baseUrl}}"], "path": ["users"] }
      },
      "event": [
        {
          "listen": "test",
          "script": {
            "exec": [
              "pm.test('Status 201', () => pm.response.to.have.status(201));",
              "pm.test('Body has id', () => pm.expect(pm.response.json()).to.have.property('id'));",
              "pm.test('Name matches', () => pm.expect(pm.response.json().name).to.equal('Cristian'));",
              "pm.test('Email matches', () => pm.expect(pm.response.json().email).to.equal('cristian@example.com'));"
            ]
          }
        }
      ]
    }
  ]
}
```

---

## ⚙️ Pasos de la Skill

1. **Lectura de los casos detallados** – La skill recibe los casos de la Skill 4 (`develop-detailed-test-cases`) y los interpreta caso por caso.

2. **Selección de formatos de salida** – La skill pregunta al usuario qué formatos necesita (puede seleccionar uno o varios):
   - `bruno` → Colección Bruno (`.bru` files)
   - `gherkin` → Archivos Gherkin coded (`.feature`)
   - `individual` → Casos individuales (`.json` / `.yaml`)
   - `postman` → Colección Postman (`.json`)
   - `karate` → Scripts Karate (`.feature` con sintaxis extendida)
   - `restsharp` → Tests RestSharp (`.cs`)
   - `playwright` → Tests Playwright (`.spec.ts`)
   - `restassured` → Tests REST Assured (`.java`)

3. **Generación por formato** – Para cada caso de prueba, la skill genera los artefactos en los formatos seleccionados:
   - **Bruno**: `.bru` con `meta`, `method`, `headers`, `body`, `assert` (Chai)
   - **Gherkin**: `.feature` con `Feature`, `Scenario Outline`, `Examples`, tags `@TestTotal @TIER1 @tipo`
   - **Individual**: `.json` con estructura completa del caso (id, título, endpoint, método, headers, body, expected, validations, tags)
   - **Postman**: Collection v2.1 con `pm.test` scripts usando Chai/Postman assertions
   - **Karate**: `.feature` con `Given url`, `And header`, `When method`, `Then status`, `And match`
   - **RestSharp/Playwright/REST Assured**: Scripts completos con assertions nativas de cada framework

4. **Parametrización y variables** – Todos los formatos usan variables reutilizables:
   - `{{baseUrl}}` / `baseUrl` — URL base del entorno
   - `{{dni}}`, `{{consumerID}}`, `{{token}}` — Variables de datos de prueba
   - `{{env}}` — Entorno (dev, staging, prod)

5. **Organización en directorios** – Los archivos se organizan por formato:
   ```
   tests/
   ├── api/
   │   ├── bruno/           # .bru files
   │   ├── gherkin/         # .feature files
   │   ├── individual/      # .json/.yaml files
   │   ├── postman/         # collection.json
   │   ├── karate/          # .feature files
   │   ├── restsharp/       # .cs files
   │   ├── playwright/      # .spec.ts files
   │   └── restassured/     # .java files
   ```

6. **Salida** – Entrega los archivos en los formatos solicitados, listos para:
   - Ejecutar en Bruno / Postman / Newman
   - Correr en pipelines CI/CD (GitHub Actions, Azure DevOps, Jenkins)
   - Importar en Cucumber, Serenity, Karate
   - Usar como documentación viva y trazabilidad

---

## 📝 Salida Esperada

Uno o múltiples directorios con artefactos de prueba:

- **Colección Bruno** completa con requests y assertions Chai
- **Archivos Gherkin** por caso con `Scenario Outline` y `Examples`
- **Casos individuales** en JSON/YAML para trazabilidad y documentación
- **Colección Postman** con tests `pm.test` listos para Newman
- **Scripts de automatización** para la herramienta seleccionada (Karate, RestSharp, Playwright, REST Assured)

---

## 💡 Notas
- La skill es **auto-suficiente**; no requiere fuentes externas.
- El usuario puede elegir **uno o varios formatos** en la misma ejecución.
- Los tags `@TestTotal`, `@TIER1/2/3`, `@functional`, `@negative`, `@contract`, `@security` se generan automáticamente según el tipo de prueba.
- Las validaciones se traducen al lenguaje nativo de cada formato:
  - Bruno: `assert { res.status == 201; res.body.has("id") }`
  - Gherkin: `Then compruebo que la respuesta contiene estado 201`
  - Postman: `pm.test('Status 201', () => pm.response.to.have.status(201))`
  - Karate: `Then status 201`, `And match response.id == '#number'`
  - RestSharp: `Assert.Equal(201, response.StatusCode); Assert.NotNull(response.Data.id);`
- Se recomienda usar esta skill como **paso final de preparación** antes de la fase de ejecución (Skill 5 `api-tlc-execution-api`).
- La trazabilidad se mantiene mediante el `ID` del caso (`TC01`, `TC02`...) en todos los formatos generados.