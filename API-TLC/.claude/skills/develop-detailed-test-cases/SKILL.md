---
name: develop-detailed-test-cases
description: Desarrollar casos de prueba detallados a partir de la matriz generada en la Skill 2.
---

# Desarrollar Casos de Prueba Detallados

## 🎯 Objetivo
A partir de la **matriz de casos de prueba de API** generada en la Skill 2 (`generate-api-test-matrix`), esta skill desarrolla los **casos de prueba detallados** con pasos, datos de entrada y validaciones.

---

## 🔧 Flujo de la Skill

1. **Input**: matriz de casos de prueba (Skill 2) — en formato Markdown, CSV, Excel o texto tabular.
2. **Transformación**:
   - Expandir cada fila en un caso detallado completo.
   - Definir pasos de ejecución (request, headers, body).
   - Especificar datos de prueba y validaciones.
   - Incluir resultado esperado y criterios de aceptación.
3. **Output**: documento de casos de prueba detallados (Markdown, JSON, o formato de Test Suite).

---

## 📘 Ejemplo de Uso

### Input (matriz Skill 2)
| ID   | Endpoint | Método | Requerimiento                  | Tipo de prueba | Resultado esperado    |
|------|----------|--------|--------------------------------|----------------|-----------------------|
| TC02 | /users   | POST   | Crear usuario válido           | Funcional      | Retorna 201 con ID    |

### Caso detallado generado

**Caso de Prueba: TC02 – Crear usuario válido**

- **Precondiciones**: API disponible, base de datos limpia, servicio corriendo.
- **Endpoint**: `/users`
- **Método**: `POST`
- **Headers**:
  - `Content-Type: application/json`
- **Body** (datos de prueba):
  ```json
  {
    "name": "Cristian",
    "email": "cristian@example.com"
  }
  ```
- **Pasos de ejecución**:
  1. Enviar request `POST /users` con el body definido.
  2. Validar que la respuesta tiene código `201`.
  3. Validar que el body de respuesta contiene un campo `id`.
  4. Validar que el campo `email` coincide con el enviado.
- **Resultado esperado**: `201 Created` con objeto JSON que incluye `id` y los datos del usuario creado.
- **Criterios de aceptación**:
  - Código HTTP `201`.
  - Response contiene `id` (entero, mayor que 0).
  - Respuesta incluye los datos enviados (`name`, `email`).

---

## ⚙️ Pasos de la Skill

1. **Lectura de la matriz** – La skill recibe la matriz de la Skill 2 (`generate-api-test-matrix`) y la interpreta fila por fila.

2. **Desarrollo por fila** – Para cada caso (`TC01`, `TC02`, `TC03`...):
   - Se crea un título con el ID y el requerimiento.
   - Se definen las **precondiciones** (estado del sistema antes de la prueba).
   - Se describe el **endpoint**, **método HTTP**, **headers** y **body**.
   - Se listan los **pasos de ejecución** en orden secuencial.
   - Se especifica el **resultado esperado** con código HTTP, estructura del response y datos clave.
   - Se definen los **criterios de aceptación** que deben cumplirse para considerar la prueba como pasada.

3. **Clasificación por tipo de prueba** – Cada caso mantiene su tipo (funcional, negativo, boundary, validación de contrato, error, seguridad) para facilitar la priorización de la ejecución.

4. **Formato de salida** – El documento se puede entregar como:
   - **Markdown** (documento legible para el equipo).
   - **JSON** (estructura lista para ser consumida por herramientas de automatización).
   - **Test Suite** (formato compatible con herramientas como Karate, RestSharp, Playwright o REST Assured).

5. **Cobertura y trazabilidad** – Se verifica que cada fila de la matriz original esté representada en los casos detallados y que los IDs coincidan para asegurar trazabilidad completa.

---

## 📝 Salida Esperada

Un documento completo con:
- Cada caso detallado expandido con pasos, datos y validaciones.
- Precondiciones claras para cada escenario.
- Datos de entrada específicos (body, parámetros, headers).
- Resultado esperado con código HTTP, estructura del response y validaciones.
- Criterios de aceptación explícitos para la evaluación de la prueba.
- Formato exportable a Markdown, JSON o Test Suite.

---

## 💡 Notas
- La skill es **auto-suficiente**; no requiere fuentes externas.
- Si la matriz incluye casos negativos (`400`, `404`, `500`), los pasos detallados incluyen datos incorrectos, parámetros faltantes o situaciones de error.
- Se recomienda usar los casos detallados como base para la Skill 5 (`api-tlc-execution-api`) y los workflows de herramientas (`restsharp-api-workflow`, `karate-api-workflow`, etc.).
- La trazabilidad entre la matriz (Skill 2) y los casos detallados es directa a través del campo `ID` (`TC01`, `TC02`...).
