---
name: openapi-to-response-example
description: Generar un ejemplo de response JSON a partir de un contrato OpenAPI/Swagger.
---

# OpenAPI a Ejemplo de Response

## 🎯 Objetivo
Transformar un **contrato OpenAPI/Swagger** (YAML/JSON) en un **ejemplo de response JSON** que el usuario pueda usar para validar, probar o documentar el endpoint.

## 🔧 Flujo de la Skill
1. **Input**: contrato OpenAPI/Swagger (provisto por el usuario o generado previamente).
   - La skill pedirá: endpoint (`/users`), método HTTP (`GET`, `POST`…) y código de respuesta (`200`, `201`…) si no están explícitos.
2. **Transformación**:
   - Localizar el `path` y el `method` en el contrato.
   - Resolver el `schema` asociado al código de respuesta.
   - Si usa `$ref`, seguir la referencia en `components.schemas`.
   - Generar valores de ejemplo según el tipo (`integer` → `1`, `string` → `"ejemplo"`, `boolean` → `true`, `array` → `[{...}]`).
3. **Output**: bloque JSON de ejemplo de respuesta.

## 📘 Ejemplo de Uso

### Contrato OpenAPI (fragmento)
```yaml
openapi: 3.0.0
paths:
  /users:
    get:
      responses:
        '200':
          description: Lista de usuarios
          content:
            application/json:
              schema:
                type: array
                items:
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

### Response generado (ejemplo)
```json
[
  {
    "id": 1,
    "name": "Cristian",
    "email": "cristian@example.com"
  }
]
```

## ⚙️ Pasos de la Skill

1. **Recolección de datos** – La skill solicita al usuario:
   - Ruta (`path`) y método HTTP (`GET`, `POST`, etc.).
   - Código de respuesta (`200`, `404`, `201`…).
   - Si el contrato es grande, la skill puede pedir el bloque específico para evitar confusiones.

2. **Navegación del contrato** – Se busca:
   - `paths.{path}.{method}.responses.{code}.content.application/json.schema`
   - Si hay `$ref`, se resuelve a `components.schemas.{nombre}`.

3. **Generación de valores de ejemplo** – Según el tipo detectado:
   - `integer`: `1`
   - `number`: `1.0`
   - `string`: `"ejemplo"` (o un valor representativo si hay `example` o `format`)
   - `boolean`: `true`
   - `object`: se construye con sus propiedades
   - `array`: se construye con un elemento de ejemplo

4. **Salida** – Se devuelve un JSON válido listo para usar como fixture, mock o caso de prueba.

## 📝 Salida Esperada
- Un bloque JSON con el ejemplo de respuesta para el endpoint y código solicitado.
- Valores coherentes con los tipos de datos definidos en el contrato.
- Lista para integrarse en fixtures de prueba (`tests/api/{tool}/data/`) o para validar con Swagger UI.

## 💡 Notas
- La skill es **auto-suficiente**; no requiere fuentes externas.
- Si un campo tiene `example` o `enum` en el contrato, la skill lo respeta y lo usa como valor de referencia.
- Si el contrato tiene múltiples códigos (`200`, `404`, `500`), la skill genera el ejemplo para el código solicitado por el usuario.
