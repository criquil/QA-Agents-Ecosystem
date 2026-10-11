# BDD-[ID]: [Título funcional del Feature / Escenario]

<!-- REEMPLAZAR:
  - [ID]     : número o código del caso (ej. 077, BDD-01)
  - [Título] : descripción funcional corta (ej. "Verificar límite no habilitado con garantías vencidas")
  NOTA: Keywords de Gherkin siempre en inglés (Feature, Given, When, Then, And...).
        El contenido de los pasos puede estar en español o inglés según BDD_LANG.
-->

## Propósito

<!-- REEMPLAZAR: Una oración que exprese la regla de negocio o comportamiento que se verifica.
     Usar negritas para resaltar estados, campos y valores clave.
     Ejemplo: Verificar que las garantías parciales vencidas sin check **no habilitan** límite de crédito. -->

[Descripción del propósito: qué comportamiento/regla de negocio se verifica.]

## Descripción

<!-- REEMPLAZAR: Párrafo que describe la regla de negocio y el contexto del escenario BDD desde
     la perspectiva del usuario / negocio. Sin tecnicismos de automatización. -->

[Descripción narrativa del comportamiento a validar: contexto, actor, acción y resultado esperado.]

## Data I/O

<!-- REEMPLAZAR: Listar TODOS los datos que la especificación BDD consume (Input / parámetros
     de los steps y Examples) y verifica (Output / assertions en los Then).
     - Tipo   : "Input" para datos de entrada, "Output" para valores verificados.
     - Campo  : nombre técnico/funcional (sin llaves, en camelCase).
     - Descripción: explicación legible del dato.
     Los parámetros de Scenario Outline se reflejan aquí como Input. -->

| Tipo   | Campo             | Descripción                                              |
|--------|-------------------|----------------------------------------------------------|
| Input  | url               | URL de acceso a la aplicación                            |
| Input  | usuario           | Credencial de usuario para login                         |
| Input  | password          | Credencial de contraseña para login                      |
| Input  | [campoInput1]     | [Descripción del dato de entrada 1]                      |
| Input  | [campoInput2]     | [Descripción del dato de entrada 2]                      |
| Output | [campoOutput1]    | [Valor o estado que se verifica en el Then]              |
| Output | resultado         | Estado de la prueba: Pass / Fail                         |

---

## Precondiciones

<!-- OBLIGATORIO — INDEPENDENCIA Y COMPLETITUD DEL ESCENARIO.
     TODO escenario DEBE ser ejecutable de forma independiente.
     El Background de Gherkin SIEMPRE empieza con: URL base + sesión/storage limpio.
     Listar aquí, como checklist verificable antes de ejecutar:
     1. Estado inicial del entorno (qué debe existir / qué debe estar limpio).
     2. Datos de prueba concretos disponibles (IDs, códigos, credenciales).
     3. Autenticación necesaria (o "no requiere autenticación").
     4. Cualquier recurso o configuración previa requerida.
     PROHIBIDO: referenciar otros escenarios ("como en BDD-XXX") o estado asumido. -->

- [ ] [Estado limpio del navegador / storage — ej. "sin sesión activa, sin cookies del sitio"]
- [ ] [Datos de prueba concretos — ej. "cliente con nroDocumento 12345678 en estado Calificada"]
- [ ] [Autenticación requerida — ej. "credenciales en Data I/O"] o [No requiere autenticación]
- [ ] [Recursos / configuración previa adicionales, si aplica]

---

## Especificación Gherkin

<!-- INSTRUCCIONES:
     - Keywords SIEMPRE en inglés: Feature, Background, Scenario, Scenario Outline,
       Examples, Given, When, Then, And, But.
     - Contenido (texto de pasos, tablas, títulos) en el idioma definido por BDD_LANG.
     - Background SIEMPRE: navegar a URL base + limpiar sesión/storage.
     - Escenarios declarativos: perspectiva de negocio, sin detalles de implementación técnica.
     - Tags obligatorios: @BDD-[ID] @[Modulo] y al menos uno de @Smoke / @Regression / @E2E.
     - Si hay múltiples combinaciones de datos: usar Scenario Outline + Examples.
     - Pasos condicionales: usar "And if [condición], [acción]" o expresar como step separado.
     - Los parámetros de Examples se referencian con "<nombre>" dentro de los pasos.        -->

```gherkin
@BDD-[ID] @[Modulo/Funcionalidad] @[Smoke|Regression|E2E]
Feature: [Nombre descriptivo de la funcionalidad bajo prueba]
  As a [Rol de usuario / actor del negocio]
  I want to [Acción o funcionalidad que se ejecuta]
  So that [Beneficio o resultado de negocio esperado]

  Background:
    Given the user navigates to the base URL "<url>"
    And the browser session and storage are clean

  # --- Escenario principal (caso nominal / happy path) ---

  @TC-[ID] @[Smoke|Regression]
  Scenario: [Nombre descriptivo del escenario principal]
    Given [Precondición de negocio — ej. "the user is logged in as '<usuario>'"]
    And [Estado inicial adicional si aplica]
    When [Acción principal del usuario o evento desencadenante]
    And [Acción secundaria / selección de filtros si aplica]
    Then [Resultado esperado / comportamiento del sistema verificado]
    And [Aserción adicional sobre "<campoOutput1>"]
```

<!-- OPCIONAL — Copiar y descomentar este bloque si el escenario es data-driven
     (se ejecuta con múltiples combinaciones de datos de prueba).

```gherkin
  @DataDriven @[Regression]
  Scenario Outline: [Nombre del escenario parametrizado]
    Given [Precondición con "<campoInput1>"]
    When [Acción con "<campoInput2>"]
    Then [Resultado con "<campoOutput1>"]

    Examples:
      | campoInput1 | campoInput2 | campoOutput1 |
      | [Valor 1A]  | [Valor 1B]  | [Resultado 1]|
      | [Valor 2A]  | [Valor 2B]  | [Resultado 2]|
```
-->

---

## Resultado Esperado

<!-- Tabla de verificaciones críticas definidas en los pasos Then. Máx 2-3 filas.
     - Verificación: qué se comprueba (extraído del Then).
     - Valor esperado: valor, estado o condición que debe cumplirse. -->

| Verificación                              | Valor esperado      |
|:------------------------------------------|:--------------------|
| [Campo o condición verificada]            | [Valor — ej. 0,00]  |
| [Campo o condición verificada 2]          | [Valor esperado 2]  |

---

## Observaciones generales

<!-- OPCIONAL. Incluir si hay:
     - Steps condicionales que pueden o no ejecutarse según el estado de datos.
     - Tiempos de espera relevantes para la automatización (explicit wait steps).
     - Ramas del flujo que dependen del estado del entorno.
     - Sugerencias de reutilización de Step Definitions para el equipo de automatización.
     - Comportamientos variables por entorno (QA vs Staging). -->

- [Observación 1: ej. "El step 'And if the popup appears, close it' es condicional."]
- [Observación 2: ej. "Reutilizar el step 'the user is logged in' del shared steps catalog."]

## Postcondiciones / Limpieza

<!-- OBLIGATORIO. Estado final esperado del entorno tras la ejecución.
     Incluir acciones concretas de restauración para que el siguiente escenario
     parta de un estado limpio.
     Incluir SOLO acciones funcionales (no cierre forzado de procesos ni SO). -->

- [Postcondición 1: ej. "Cerrar sesión del usuario (logout)."]
- [Postcondición 2: ej. "Limpiar localStorage / cookies del sitio."]

---

## Flujo BDD

<!-- REEMPLAZAR: Diagrama ASCII que muestra la secuencia Given → When → Then de punta a punta.
     - Usar sangría con → para indicar el avance de cada bloque.
     - Usar [Condicional: ...] para pasos opcionales.
     - La secuencia SIEMPRE inicia en Background (URL base + estado limpio)
       y termina en la limpieza.
     Ejemplo de formato:

     Background (Given: URL base + sesión limpia)
       → Given: [Precondición de negocio]
         → When: [Acción principal]
           → [Condicional: paso opcional]
             → Then: [Verificación del comportamiento]
               → Limpieza / Postcondiciones
-->

[Background — URL base + sesión limpia]
  → [Given: Precondición de negocio / autenticación]
    → [Given: Estado inicial adicional]
      → [When: Acción o evento principal]
        → [When: Filtros / sub-acciones]
          → [Condicional: paso opcional]
            → [Then: Verificación del resultado esperado]
              → Verificar: [campoOutput1] == [valor esperado]
                → Limpieza / Postcondiciones
