---
name: export-response-to-openapi
description: Transformar un response JSON validado en un contrato OpenAPI/Swagger (YAML/JSON).
---

# Exportar Response a Contrato OpenAPI/Swagger

## 🎯 Objetivo
Convertir un **response JSON** (provisto por el usuario) previamente validado en un **contrato OpenAPI 3.0** que documente el endpoint y su respuesta.

## 🔧 Flujo de la Skill
1. **Input**: response JSON validado (ejemplo: resultado de un test o runner).
   - La skill pedirá los datos necesarios no provistos en el input original (como el nombre del endpoint, método HTTP, etc.).
2. **Transformación**:
   - Detectar tipo de datos (object, array, string, integer, boolean, null).
   - Mapear propiedades a `components.schemas`.
   - Generar `paths` con método y respuesta.
3. **Output**: contrato OpenAPI 3.0 en YAML/JSON listo para documentar el servicio.

## 📘 Ejemplo de Uso

### Response validado
```json
[
  {
    "id": 1,
    "name": "Cristian",
    "email": "cristian@example.com"
  }
]
```

### Contrato generado (YAML)
YAML
openapi: 3.0.0
info:
  title: Exported API Contract
  version: 1.0.0
paths:
  /users:
    get:
      summary: Obtener lista de usuarios
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

## ⚙️ Pasos de la Skill

1. **Recolección de datos** – La skill solicita al usuario:
   - Nombre del endpoint (p.ej. `/users`)
   - Método HTTP (GET, POST, PUT, DELETE, etc.)
   - Código de respuesta esperado (p.ej. `200`)
   - Tipo de contenido (p.ej. `application/json`)

2. **Análisis de tipos** – Para cada propiedad del response JSON:
   - `id`: entero → `type: integer`
   - `name`: cadena → `type: string`
   - `email`: cadena → `type: string`
   - Se detectan arrays, objetos, booleanos y null.

3. **Generación de esquemas** – Cada propiedad se convierte en un esquema en `components.schemas`.

4. **Construcción de paths** – Se crea la ruta con el método HTTP correspondiente y se añade la respuesta con el schema apropiado.

5. **Salida** – Se devuelve un bloque OpenAPI 3.0 (YAML o JSON) listo para integrar en Swagger UI, generar clientes/servidores automáticos o usar como base para pruebas.

## 📝 Salida Esperada
- Un archivo con contrato OpenAPI 3.0 (YAML o JSON) que documenta el endpoint y su respuesta.
- Esquemas definidos en `components.schemas`.
- Rutas (`paths`) con método, summary y respuestas.
- Documentación lista para Swagger UI y generación de clientes.

## 💡 Notas
- La skill es **auto-suficiente** en términos de conocimiento; no requiere fuentes externas.
- Si el response JSON contiene estructuras complejas (nested objects, arrays), la skill las mapeará recursivamente.
- El formato de salida puede ser YAML (por defecto) o JSON según la preferencia del usuario.
