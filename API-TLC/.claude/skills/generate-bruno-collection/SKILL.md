---
name: generate-bruno-collection
description: Generar una colección de Bruno con requests y pruebas Chai a partir de casos de prueba detallados.
---

# Generar Colección de Bruno con Requests y Pruebas Chai

## 🎯 Objetivo
A partir de los **casos de prueba detallados** (Skill 3), esta skill debe generar una **colección de Bruno**. Cada caso de prueba se convierte en una **request** dentro de la colección, y cada request incluye su respectiva **prueba Chai** para validación automática.

---

## 🔧 Flujo de la Skill

1. **Input**: casos de prueba detallados (Skill 3) — documento con endpoint, método, body, headers, resultado esperado, validaciones y criterios de aceptación.
2. **Transformación**:
   - Crear una request Bruno (`.bru`) por cada caso de prueba.
   - Configurar método HTTP, URL, headers y body según el caso detallado.
   - Incluir script de test con **Chai assertions** que validen código de respuesta, headers y estructura del body.
3. **Output**: colección Bruno (`.bru` files) con múltiples requests y sus respectivos scripts de test (`assert` / `test` blocks).

---

## 📘 Ejemplo de Uso

### Input (caso detallado Skill 3)
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

### Output (archivo `.bru` generado)

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

## ⚙️ Pasos de la Skill

1. **Lectura de los casos detallados** – La skill recibe los casos de la Skill 3 (`develop-detailed-test-cases`) y los interpreta fila por fila.

2. **Creación de requests `.bru`** – Para cada caso de prueba:
   - Se genera un archivo `.bru` con el nombre del caso (`TC02.bru`, `TC03.bru`, etc.).
   - Se configura el método (`GET`, `POST`, `PUT`, `DELETE`, `PATCH`) y la URL del endpoint.
   - Se incluyen los headers (`Content-Type`, `Authorization`, tokens, etc.).
   - Se define el body (`json`, `form`, `multipart`) según los datos de entrada del caso.

3. **Generación del bloque `assert` (Chai)** – Cada `.bru` incluye un bloque de validaciones basado en los criterios de aceptación del caso detallado:
   - **Código HTTP**: `res.status == 201`, `res.status == 200`, `res.status == 404`, etc.
   - **Headers**: `res.headers.has("vnd.bbva.access-token")`, `res.headers.get("vnd.bbva.sso-pkcs7") != null`.
   - **Body**: `res.body.has("id")`, `res.body.name == "Cristian"`, `res.body.id > 0`, `res.body.length > 0`.
   - **Negativos**: `res.status == 400`, `res.body.has("error")`, etc.

4. **Parametrización con variables Bruno** – La skill permite usar variables como `{{baseUrl}}`, `{{dni}}`, `{{token}}`, `{{consumerID}}` para facilitar la ejecución en diferentes entornos (dev, staging, prod).

5. **Organización en colecciones** – Los archivos `.bru` se agrupan en directorios de colección (`tests/api/bruno/` o similar) para ser consumidos por la herramienta **Bruno** o integrados en pipelines.

6. **Salida** – Cada request `.bru` es independiente y contiene:
   - Configuración de la llamada HTTP.
   - Body con los datos de prueba.
   - Script de test con assertions Chai listas para ejecutar.

---

## 📝 Salida Esperada

Una colección Bruno que incluye:

- Un archivo `.bru` por cada caso de prueba detallado.
- Método, endpoint, headers y body configurados según el caso.
- Variables de entorno (`{{baseUrl}}`, `{{dni}}`, etc.) para reutilización.
- Bloque `assert` con validaciones Chai automáticas para código de respuesta, headers y estructura del body.
- Archivos listos para abrir en Bruno o ejecutar en CI/CD.

---

## 💡 Notas
- La skill es **auto-suficiente**; no requiere fuentes externas.
- El formato `.bru` es nativo de **Bruno**, un cliente de API que usa archivos de texto plano (`.bru`) y es compatible con Git.
- Las assertions del bloque `assert` usan sintaxis similar a **Chai** (`==`, `!=`, `.has()`, `.length`) y son interpretadas automáticamente por Bruno.
- La skill genera assertions para todos los criterios de aceptación del caso detallado: código HTTP, headers específicos, propiedades del body, errores y mensajes.
- Se recomienda usar esta colección junto con los casos detallados (Skill 3) y los scripts de ejecución (Skill 2 para la matriz, Skill 5 para Gherkin) para cubrir todos los formatos de entrega.
