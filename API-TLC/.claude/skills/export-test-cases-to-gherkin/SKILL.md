---
name: export-test-cases-to-gherkin
description: Exportar casos de prueba detallados a formato Gherkin coded para frameworks BDD (Cucumber, Serenity, Karate).
---

# Exportar Casos de Prueba a Gherkin (Coded)

## 🎯 Objetivo
A partir de los **casos de prueba detallados** (Skill 3), esta skill debe exportarlos en formato **Gherkin** con estilo **coded** (incluyendo tags, Feature, Scenario Outline, Examples), para integrarse en frameworks BDD como **Cucumber, Serenity, Karate** o pipelines de QA automation.

---

## 🔧 Flujo de la Skill

1. **Input**: casos de prueba detallados (Skill 3) — documento con precondiciones, pasos, validaciones y resultado esperado.
2. **Transformación**:
   - Convertir cada caso en un `Feature` o `Scenario Outline`.
   - Incluir tags de clasificación (`@TestTotal`, `@TIER1`, `@sso`, etc.).
   - Mapear pasos a sintaxis Gherkin (`Given`, `When`, `Then`).
   - Generar `Examples` para parametrización con variables del caso.
3. **Output**: archivo `.feature` en formato Gherkin listo para ejecución.

---

## 📘 Ejemplo de Uso

### Input (caso detallado Skill 3)
**Caso de Prueba: Login GloMo exitoso retorna pkcs7 y access-token**

- Endpoint: `/login`
- Método: `POST`
- Datos: DNI válido, consumerID válido
- Validaciones: status 200, headers no nulos

### Output (archivo Gherkin)

```gherkin
@TestTotal @PA0PQRS859 @sso @jws
Feature: Single Sign-On JWS ASO — Preparar Cobro

  Como consumidor del flujo de autenticación GloMo Tap on Phone
  Quiero obtener un token JWS (tsec) mediante el flujo de Single Sign-On
  Para autenticarme en las operaciones de cobro Tap on Phone contra Symbiotic

  # =========================================================
  # STEP 1 — Login GloMo (customer-password/validations)
  # Base URL: glomo-play.bbva.com.ar  (fuera del ASO Platform)
  # =========================================================

  @ssoLogin200 @TIER1
  Scenario Outline: [POST][200] login GloMo exitoso retorna pkcs7 y access-token
    Given declaro la variable "dni" con valor "<dni>"
    And declaro la variable "consumerID" con valor "<consumerID>"
    When el usuario realiza el login GloMo con DNI "<dni>"
    Then compruebo que la respuesta contiene estado 200
    Then compruebo que el header de respuesta "vnd.bbva.sso-pkcs7" no sea nulo
    Then compruebo que el header de respuesta "vnd.bbva.access-token" no sea nulo

    Examples:
      | dni      | consumerID |
      | 10003350 | 16000001   |

  @ssoLogin401 @TIER3
  Scenario Outline: [POST][401] login GloMo con credenciales inválidas
    Given declaro la variable "dni" con valor "<dni>"
    When el usuario realiza el login GloMo con DNI "<dni>"
    Then compruebo que la respuesta contiene estado 401

    Examples:
      | dni         |
      | 00000000    |
      | INVALIDO    |
```

---

## ⚙️ Pasos de la Skill

1. **Lectura de la matriz** – La skill recibe los casos detallados de la Skill 3 (`develop-detailed-test-cases`) y los interpreta caso por caso.

2. **Generación de Feature** – Para cada caso se construye:
   - Un `Feature` con descripción del negocio (rol, acción, beneficio).
   - Tags de clasificación: `@TestTotal` (identificador único), `@TIER1/@TIER2/@TIER3` (prioridad), `@sso`, `@jws`, etc.
   - Un `Scenario Outline` con el nombre `[MÉTODO][CÓDIGO] descripción del escenario`.

3. **Mapeo de pasos Gherkin** – Cada caso se traduce a pasos estandarizados:
   - **Given**: Para declarar variables y precondiciones (`declaro la variable "dni" con valor "<dni>"`).
   - **When**: Para la acción principal (`el usuario realiza el login GloMo con DNI "<dni>"`).
   - **Then**: Para validaciones (`compruebo que la respuesta contiene estado 200`, `compruebo que el header ... no sea nulo`).

4. **Parametrización con Examples** – Se generan tablas `Examples` con las variables usadas en el escenario (DNI, consumerID, credenciales, etc.).

5. **Tags por escenario** – Cada `Scenario Outline` recibe tags que identifican:
   - El código de respuesta esperada (`@ssoLogin200`, `@ssoLogin401`).
   - La prioridad o TIER (`@TIER1`, `@TIER2`, `@TIER3`).
   - El tipo de flujo (`@sso`, `@jws`, `@api`, `@ui`, etc.).

6. **Salida** – El archivo `.feature` generado está listo para ser consumido por:
   - **Cucumber** (Java, JavaScript, .NET).
   - **Serenity BDD** (integrado con Cucumber).
   - **Karate Framework** (compatible con sintaxis Gherkin extendida).
   - **Pipelines de QA automation** que consumen `.feature` files.

---

## 📝 Salida Esperada

Un archivo `.feature` por cada caso de prueba detallado, con:

- **Feature** descriptivo con rol/acción/beneficio.
- **Tags** de identificación y prioridad.
- **Scenario Outline** parametrizado con `Examples`.
- **Pasos Given/When/Then** en estilo coded (con referencias a variables).
- Estructura lista para ejecución en frameworks BDD.

---

## 💡 Notas
- La skill es **auto-suficiente**; no requiere fuentes externas.
- Los tags `@TestTotal`, `@TIER1/2/3`, `@sso`, `@jws` son ejemplos — la skill permite al usuario definir o modificar los tags según su nomenclatura interna.
- Si el caso detallado incluye múltiples validaciones, la skill genera múltiples `Then` steps cubriendo cada una.
- El `Scenario Outline` con `Examples` permite ejecutar el mismo escenario con diferentes conjuntos de datos (válidos, inválidos, boundary cases).
- Los pasos usan un estilo "coded" que mezcla Gherkin natural con referencias a variables y validaciones específicas, facilitando la traducción a implementaciones reales en los frameworks BDD.