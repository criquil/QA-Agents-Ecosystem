---
name: generate-api-test-matrix
description: Generar una matriz de casos de prueba de API a partir de requerimientos, un archivo OpenAPI y/o ejemplos.
---

# Generar Matriz de Casos de Prueba de API

## 🎯 Objetivo
A partir de **requerimientos funcionales**, un **archivo OpenAPI** y/o **ejemplos de input**, la skill debe crear una **matriz de casos de prueba** que cubra todos los requerimientos del input.

---

## 🔧 Flujo de la Skill

1. **Input**:
   - Requerimientos escritos (funcionales o técnicos).
   - Archivo OpenAPI (YAML/JSON).
   - Ejemplos de requests/responses.
2. **Transformación**:
   - Parsear endpoints, métodos, parámetros y respuestas del OpenAPI.
   - Mapear cada requerimiento a un caso de prueba.
   - Generar matriz con columnas: `ID`, `Endpoint`, `Método`, `Requerimiento`, `Tipo de prueba`, `Resultado esperado`.
3. **Output**: matriz de casos de prueba en formato tabular (Markdown, CSV o Excel).

---

## 📘 Ejemplo de Uso

### Input
Archivo OpenAPI con endpoint `/users` (GET, POST).

### Matriz generada

| ID   | Endpoint | Método | Requerimiento                  | Tipo de prueba | Resultado esperado    |
|------|----------|--------|--------------------------------|----------------|-----------------------|
| TC01 | /users   | GET    | Listar usuarios existentes     | Funcional      | Retorna lista JSON    |
| TC02 | /users   | POST   | Crear usuario válido           | Funcional      | Retorna 201 con ID    |
| TC03 | /users   | POST   | Crear usuario sin `email`      | Negativo       | Retorna 400 error     |

---

## ⚙️ Pasos de la Skill

1. **Recolección de entradas** – La skill recoge:
   - El archivo OpenAPI del servicio (si está disponible).
   - Los requerimientos funcionales o técnicos del usuario.
   - Ejemplos de request/response que ilustren el comportamiento esperado.

2. **Análisis del contrato OpenAPI** – Se extraen:
   - Endpoints, métodos HTTP y parámetros (`paths`).
   - Respuestas por código (`responses`).
   - Modelos definidos en `components.schemas`.

3. **Mapeo requerimientos → casos** – Cada requerimiento se traduce en:
   - Un ID único (`TC001`, `TC002`...).
   - El endpoint y método HTTP correspondiente.
   - El tipo de prueba: funcional, negativo, boundary, validación de contrato, error, etc.
   - El resultado esperado según el contrato o el requerimiento.

4. **Generación de la matriz** – Se construye la tabla con cobertura total:
   - Todos los endpoints y métodos quedan representados.
   - Los escenarios positivos, negativos y de error están incluidos.

5. **Exportación** – La matriz se entrega en uno de los formatos:
   - **Markdown** (tabla para documentación).
   - **CSV** (fácil de importar a Excel/Google Sheets).
   - **Excel** (archivo `.xlsx` listo para compartir con el equipo).

---

## 📝 Salida Esperada

Una matriz completa que:
- Cubra todos los endpoints y escenarios del servicio.
- Sirva como base para diseñar los casos de prueba detallados y automatizarlos.
- Asegure trazabilidad entre los requerimientos y las pruebas ejecutadas.
- Se exporte en el formato elegido por el usuario (Markdown, CSV o Excel).

---

## 💡 Notas
- La skill es **auto-suficiente**; no requiere fuentes externas.
- Si el OpenAPI no está disponible, la skill puede construir la matriz solo a partir de los requerimientos escritos y los ejemplos provistos.
- Los IDs de casos se generan de forma secuencial para facilitar la trazabilidad y el seguimiento de la ejecución.
- Se recomienda revisar la matriz con el equipo antes de pasar a la fase de implementación de scripts.
