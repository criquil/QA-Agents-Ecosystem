---
name: import-collection
id: import-collection
description: Importar una colección de cualquier tipo (OpenAPI/Swagger, Bruno, Postman) y transformarla en casos test coded usando los frameworks del API-TLC (RestSharp, Karate, Playwright, REST Assured).
---

# Importar Colección a Casos Coded

## 🎯 Objetivo
Esta skill **independiente** toma un **input de colección** en cualquier formato soportado (OpenAPI/Swagger, Bruno, Postman) y la **transforma automáticamente** en **casos test coded** listos para ejecución usando los **cuatro frameworks principales del API-TLC v1.0**:

- **RestSharp** (.NET/C# + xUnit/NUnit)
- **Karate** (Gherkin/BDD + multi-protocolo)
- **Playwright** (JS/TS + API + browser testing)
- **REST Assured** (Java + Given/When/Then + Allure)

La skill es *independiente* — puede usarse sin depender de las fases anteriores del API-TLC y soporta múltiples formatos de entrada para máxima flexibilidad.

---

## 🔧 Formatos de Input Soportados

### 1. OpenAPI/Swagger
**`openapi.yaml` / `swagger.json`** (versión 3.0+)
- Endpoints, métodos HTTP, parámetros, requests/responses
- Esquemas (`components.schemas`)
- Tokens de seguridad (`securitySchemes`)

### 2. Colección Bruno
**`coleccion.bruno`** (formato nativo de Bruno)
- Requests con métodos, URLs, headers, body
- Scripts `assert` / `test` opcionalmente incluidos

### 3. Colección Postman
**`coleccion.json`** (formato v2.1 de Postman)
- Item requests, URL, headers, body, tests `pm.test`
- Variables de entorno, global variables

La skill **detecta automáticamente** el formato de input basándose en la estructura del archivo y el contenido.

---

## 📘 Flujo de Transformación

### Paso 1: Detección y Parseo
- **Input** → La colección del usuario (formato detectado automáticamente)
- **Parsear** todos los endpoints, métodos HTTP, parámetros, datos de request y expectativas de response
- **Normalizar** los datos a un modelo común interno

### Paso 2: Selección de Frameworks
- La skill pregunta al usuario: **"¿En qué frameworks quieres generar casos test?"**
- Opciones (seleccionar una o más):
  - `restsharp` (REST Assured-style para .NET/C#)
  - `karate` (Gherkin-BDD multi-protocolo)
  - `playwright` (JavaScript/TypeScript)
  - `restassured` (Java + Allure)

### Paso 3: Generación Codificada
Por cada endpoint/elemento en la colección, la skill genera **casos test coded**:

| Framework | Punto de entrada | Sintaxis típica | Casos típicos generados |
|-----------|-------------|---------------|--------------------|
| **RestSharp** | `.cs` (test .NET) | `response.StatusCode == HttpStatusCode.Created` | `GET /users`, `POST /users`, `PUT /users/{id}`, etc. |
| **Karate** | `.feature` (Gherkin) | `Given url baseUrl`, `When method`, `Then status`, `And match` | `Feature: usuarios`, `Scenario: obtener usuario`, `Examples: datos` |
| **Playwright** | `.spec.ts` (test JS/TS) | `await request.get(url)`, `await expect(response.status()).toBe(200)` | `test('GET /users', ...)` con `expect`/`assert` |
| **REST Assured** | `.java` (JUnit + Allure) | `given().when().get().then().statusCode(200)` | `public class UsersTests { @Test void testGetUsers() { ... } }` |

### Paso 4: Adaptación Específica por Framework
Cada framework recibe tratamiento especial para:

- **RestSharp**: Genera `TestCaseSource`, `Theory`, `Fact` con `RestClient` de RestSharp, `HttpRequest` + `HttpResponse`, `Assert.Equal`, `Assert.True`.

- **Karate**: Genera `Feature` con `Background`, `Scenario Outline`, `Examples`, `Given url baseUrl`, `And header`, `When method`, `Then status`, `And match`

- **Playwright**: Genera `test.describe`, `test('title', async () => { await request.get(...) })`, `expect(response.status()).toBe(200)`

- **REST Assured**: Genera `class { @Test public void testGetUsers() { given().when().get().then().statusCode(200) } }` y reporte Allure opcional.

### Paso 5: Organizar en Directorios por Framework

```
tests/api/imported/
├── restsharp/
│   ├── OpenAPI_Users_Spec.cs
│   └── Coleccion_Postman_Snippets.cs
├── karate/
│   ├── OpenAPI_Users_Spec.feature
│   └── Coleccion_Bruno_Snippets.feature
├── playwright/
│   ├── OpenAPI_Users_Spec.spec.ts
│   └── Coleccion_Postman_Snippets.spec.ts
└── restassured/
    ├── OpenAPI_Users_Spec.java
    └── Coleccion_Bruno_Snippets.java
```

---

## 📘 Ejemplo de Uso

### Input (Colección OpenAPI)
```yaml
openapi: 3.0.0
paths:
  /users:
    get:
      summary: Listar usuarios
      responses:
        '200':
          description: Lista exitosa
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/User'
    post:
      summary: Crear usuario
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/User'
      responses:
        '201':
          description: Creado
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: integer
        name:
          type: string
        email:
          type: string
```

### Selección de Frameworks
> En qué frameworks quieres generar casos test?
> 
> - [x] restsharp
> - [x] karate
> - [x] playwright
> - [x] restassured

### Output: Multi-Framework Codificado

#### RestSharp (`Users_Created.cs`)
```csharp
[Test]
[Category("POST /users")]
public async Task TestPostUsers()
{
    using var client = new RestClient("{{baseUrl}}");
    var request = new RestRequest("/users", Method.Post)
        .AddHeader("Content-Type", "application/json")
        .AddJsonBody(new { name = "Cristian", email = "cristian@example.com" });
    
    var response = await client.ExecuteAsync<User>(request);
    
    // Validaciones
    Assert.Equal(HttpStatusCode.Created, response.StatusCode);
    Assert.NotNull(response.Data.Id);
    Assert.Equal("Cristian", response.Data.Name);
    Assert.Equal("cristian@example.com", response.Data.Email);
}
```

#### Karate (`users_created.feature`)
```gherkin
Feature: Colección importada / POST /users

  Background:
    Given url baseUrl
    And header Content-Type = "application/json"

  @imported
  Scenario: POST /users (Importado desde OpenAPI)
    When request { "name": "Cristian", "email": "cristian@example.com" }
    And url baseUrl + "/users"
    And request
    Then status 201
    And match response contains { "id": #number }
    And match response.name == "Cristian"
    And match response.email == "cristian@example.com"
```

#### Playwright (`users_created.spec.ts`)
```typescript
// tests/users_created.spec.ts

import { test, expect } from '@playwright/test';

test.describe('Colección importada', () => {
  test('POST /users (Importado desde OpenAPI)', async ({ request }) => {
    const payload = { name: 'Cristian', email: 'cristian@example.com' };
    const response = await request.post('/users', {
      data: payload,
      headers: { 'Content-Type': 'application/json' }
    });
    
    // Validaciones
    expect(response.status()).toBe(201);
    const body = await response.json();
    expect(body).toHaveProperty('id');
    expect(body.name).toBe('Cristian');
    expect(body.email).toBe('cristian@example.com');
  });
});
```

#### REST Assured (`Users_Created.java`)
```java
package tests.api.imported;

import io.qameta.allure.Description;
import io.qameta.allure.Epic;
import io.qameta.allure.Feature;
import org.junit.Test;
import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.notNullValue;

@Epic("API Testing")
@Feature("Imported Collections")
public class Users_Created {

    @Test
    @Description("POST /users (Importado desde OpenAPI)")
    public void testPostUsers() {
        String payload = "{\"name\": \"Cristian\", \"email\": \"cristian@example.com\"}";
        
        given()
            .baseUri("{{baseUrl}}")
            .contentType("application/json")
            .body(payload)
        .when()
            .post("/users")
        .then()
            .statusCode(201)
            .body("id", notNullValue())
            .body("name", equalTo("Cristian"))
            .body("email", equalTo("cristian@example.com"));
    }
}
```

---

## ⚙️ Casos Avanzados y Características

### 1. Soporte Multi-Protocolo
- **Karate** puede generar casos para HTTP + gRPC + GraphQL automáticamente si el contrato original lo especifica.

### 2. Datos Parametrizados
- La skill extrae `Examples` de OpenAPI (`examples` section) y `postman.collection` (`item[*].request.body.raw`).

### 3. Mapeo de Seguridad
- OpenAPI `securitySchemes` se convierten a llamadas `given().auth().oauth2()` (Karate), `client.AddHeader("Authorization", "Bearer {{token}}")` (RestSharp), `request.setAuth(OAuth2_10_Jwt_Bearer(...))` (Playwright), `given().auth().oauth2()` (REST Assured).

### 4. Variables de Entorno
- Las variables globales de la colección (`variables globales`) se convierten a `{{variableName}}` en todos los frameworks.

### 5. Falta de native-to-framework-mapping

| OpenAPI/Bruno/Postman | RestSharp | Karate | Playwright | REST Assured |
|-----------------------|-----------|--------|------------|--------------|
| **GET /users** | `GetAsync("/users")` | `Given url baseUrl + "/users"` | `await request.get("/users")` | `when().get("/users")` |
| **POST /users** | `PostAsync<User>(request)` | `When request({ ... })` | `await request.post("/users", data)` | `when().post("/users")` |
| **PUT /users/{id}** | `PutAsync<UpdateUser>(id, request)` | `And request({ ... })` | `await request.put(`/users/${id}`, data)` | `when().put(`/users/${id}`)` |
| **DELETE /users/{id}** | `DeleteAsync("/users/{id}")` | `And url = baseUrl + "/users/{id}"` | `await request.delete(`/users/${id}`)` | `when().delete(`/users/${id}`)` |
| **Headers** | `AddHeader("X-API-Key", "value")` | `And header "X-API-Key": "value"` | `options.headers = { 'X-API-Key': 'value' }` | `header("X-API-Key", "value")` |
| **JSON Body** | `AddJsonBody(payload)` | `request { ... }` | `data: payload` | `body(payload)` |
| **Query Params** | `AddQueryParameter("param", "value")` | `params { "param": "value" }` | `params: { param: "value" }` | `queryParam("param", "value")` |
| **Assertions** | `Assert.Equal`, `Assert.Contains` | `Then status`, `And match` | `expect(response.status()).toBe(200)` | `then().statusCode(200)` |
| **Paths Params** | `AddUrlSegment("id", id)` | `path("/users/{id}")` | `route: `/users/${id}` | `pathParam("id", id)` |

### 6. Orden de Ejecución por Defecto

```mermaid
flowchart TD
    A[Input Collection] --> B{¿Qué frameworks?]}
    B -->|RestSharp| C[*.cs - .NET Unit Tests]
    B -->|Karate| D[*.feature - BDD Scenarios]
    B -->|Playwright| E[*.spec.ts - JS/TS Tests]
    B -->|REST Assured| F[*.java - Java JUnit]
    
    C --> G[API-TLC Integration]
    D --> G
    E --> G
    F --> G
```

La skill **consulta al usuario** por los frameworks de salida para dar flexibilidad y evitar la generación innecesaria.

---

## 📝 Salida Esperada

Un **conjunto completo de test scripts coded** para cada framework seleccionado:

- **RestSharp** (`*.cs`) – Tests de unitarios .NET con RestSharp, Assertion, Naming y Naming por categorias
- **Karate** (`*.feature`) – Features Gherkin con Background, Scenario Outline, Examples
- **Playwright** (`*.spec.ts`) – Tests de Playwright con imports, fixtures y expect Chai
- **REST Assured** (`*.java`) – Tests de JUnit + Allure con Given/When/Then

Todos los scripts:
- Mantienen la trazabilidad de los IDs originales (si la colección incluye `id`)
- Usan variables reutilizables `{{baseUrl}}`, `{{token}}`, `{{param}}`
- Son listos para importación en un pipeline de CI/CD
- Se pueden ejecutar independientemente del API-TLC (usando frameworks nativos)

---

## 💡 Notas

- La skill es **auto-suficiente** — usa detección automática de formato (`.yaml`, `.json`, `.bru`).
- Si la colección es **inválida o vacía**, la skill detiene con un error claro.
- Los **datos de ejemplo** son generados automáticamente si la colección no los tiene.
- La skill **no** ejecuta los tests generados; simplemente los crea para ser ejecutados posteriormente.
- La **resiliencia** incluye manejo de referencias circulares, definición de esquemas faltantes y resolución de tokens de seguridad.
- Los **artefactos** mantienen la conformidad con los estándares API-TLC y están listos para integrarse en workflows CI/CD existentes.

La habilidad de `import-collection` amplía el API-TLC desde **API-TLC v1.0** a admitir **entrada pre-existente** (importaciones de JSON) y **producción multi-framework** (REST Assured, Playwright, etc.).