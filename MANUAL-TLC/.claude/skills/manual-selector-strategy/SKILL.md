---
name: manual-selector-strategy
description: Usa esta skill para definir, validar y documentar selectores XPath robustos durante sesiones de prueba manual asistidas, usando exclusivamente el Playwright MCP Server.
---

# MANUAL-SELECTOR-STRATEGY — Estrategia de Localización de Elementos

<role>

## Rol

Eres el especialista en localización de elementos de MANUAL-TLC. Defines, validas y documentas **XPath robustos, legibles y resistentes a cambios** para que las sesiones manuales asistidas sean reproducibles y auditables.

Esta sección es **PRIORITARIA y REQUERIDA** para definir o corregir selectores durante la ejecución de pruebas manuales asistidas.

## Herramienta permitida

- ✅ **Playwright MCP Server** — herramienta única para navegar, localizar y validar selectores.
- 🚫 **PROHIBIDO Chrome DevTools MCP** (o cualquier otro servidor MCP de inspección de DevTools). Toda validación de selectores se realiza **exclusivamente** con el Playwright MCP Server.

### Por qué Playwright MCP Server y no Chrome DevTools MCP

- Expone el **árbol de accesibilidad** (`browser_snapshot`) y búsqueda sobre él (`browser_find`), que es exactamente lo que un selector robusto necesita.
- Permite **evaluar expresiones** (`browser_evaluate`) para contar coincidencias de un XPath sin salir de la sesión.
- Permite **validar funcionalmente** el selector ejecutando la acción real (`browser_click`, `browser_fill_form`, ...).
- Captura evidencia (`browser_take_screenshot`) del elemento localizado, en la misma sesión y sin cambiar de herramienta.
- Mantiene una **única sesión de navegador** para toda la prueba manual.

</role>

<workflow>

## Principio de trabajo

En una sesión asistida el elemento se identifica primero en el **snapshot de accesibilidad** (`browser_snapshot` / `browser_find`). Cuando el elemento debe:

- documentarse en un caso de prueba,
- reutilizarse en sesiones posteriores o en regresión,
- o el snapshot resulta **ambiguo** (varios nodos con el mismo nombre accesible),

entonces se define un **XPath** aplicando la jerarquía de prioridad de esta skill.

## 🎯 Estrategia principal: XPath con atributos prioritarios

**Siempre debe utilizarse XPath** para los selectores que se escriben y documentan.

### 🥇 1. XPath con `id` (máxima prioridad)

Único, rápido y confiable.

```
xpath=//*[@id='login-button']
xpath=//*[@id='form-container']//button
xpath=//input[@id='email-input']
```

### 🥈 2. XPath con `name` (segunda prioridad)

Útil en formularios y campos de entrada, especialmente cuando no hay `id`.

```
xpath=//*[@name='email']
xpath=//input[@name='password' and @type='password']
xpath=//*[@id='login-form']//*[@name='username']
```

### 🥉 3. XPath con `data-testid` o atributos `data-*`

Diseñados específicamente para pruebas; no afectan la UI.

```
xpath=//*[@data-testid='submit-form']
xpath=//*[@data-action='confirm']
xpath=//*[@id='modal']//*[@data-testid='close-button']
```

### 🏷️ 4. XPath con `accessibility id` (roles ARIA y etiquetas accesibles)

Mejora la accesibilidad y la semántica; ideal para aplicaciones inclusivas. Se lee directamente del snapshot.

```
xpath=//button[@role='button' and @aria-label='Enviar']
xpath=//*[@aria-describedby='help-text']
xpath=//*[@role='dialog' and @aria-labelledby='modal-title']
```

### 📝 5. XPath con texto visible (solo si es único y estable)

**Riesgo:** se rompe ante cambios de idioma o de contenido. Siempre combinado con contexto.

```
xpath=//button[text()='Aceptar']
xpath=//span[contains(text(), 'términos y condiciones')]
xpath=//div[normalize-space()='Mensaje de éxito']
xpath=//*[@id='modal']//button[text()='Confirmar']
```

### 🎨 6. XPath con `class` (solo si es única y no se genera dinámicamente)

**Riesgo:** puede cambiar con el diseño o con el framework CSS.

```
xpath=//*[@class='btn-confirmar']
xpath=//*[contains(@class, 'btn-primary')]
xpath=//button[contains(@class, 'submit')]
xpath=//*[@id='form']//input[contains(@class, 'input-field') and @type='text']
```

### ⚙️ 7. XPath complejo (último recurso)

Extremadamente flexible pero frágil ante cambios estructurales. Construir siempre **desde un ancla única**.

```
xpath=//*[@id='container']//div[@class='row'][2]/span
xpath=//*[@id='label']/following-sibling::input
xpath=//*[@name='email']/parent::div
xpath=//button[@type='submit' and contains(@class, 'primary')]
xpath=//*[@id='btn-save' or @name='save-button']
xpath=//input[@name='city']/ancestor::form[@id='address-form']
```

</workflow>

## 🔧 Cómo se entrega el XPath al Playwright MCP Server

El parámetro `target` de toda herramienta de interacción acepta una **referencia del snapshot** o un **selector único**. Para XPath se usa el prefijo explícito `xpath=`:

| Necesidad | Herramienta | `target` |
|---|---|---|
| Clic en un elemento | `browser_click` | `xpath=//*[@id='login-button']` |
| Escribir en un campo | `browser_type` | `xpath=//input[@name='email']` |
| Rellenar un formulario | `browser_fill_form` | `xpath=//*[@id='user-form']` |
| Seleccionar en lista | `browser_select_option` | `xpath=//*[@data-testid='country-select']` |
| Marcar un check/radio | `browser_check` | `xpath=//*[@name='terms']` |
| Esperar un elemento | `browser_wait_for` | texto/estado esperado del elemento |
| Verificar visibilidad | `browser_verify_element_visible` | `role` + `accessibleName` del snapshot |

El parámetro `element` (descripción legible, ej. `"botón Iniciar sesión"`) se acompaña siempre para dejar claro qué se está operando.

## ✅ Protocolo de validación de un selector (obligatorio)

**Ningún selector puede usarse ni documentarse sin haber sido validado con el Playwright MCP Server.** Está prohibido "inventar" selectores.

### Para validar un selector nuevo

1. **Navegar** hasta la sección involucrada: `browser_navigate`.
2. **Localizar el nodo** y leer sus atributos:
   - `browser_snapshot` (árbol de accesibilidad completo), o
   - `browser_find` con el texto/regex del elemento (más económico que el snapshot completo).
3. **Construir el XPath** aplicando la jerarquía de prioridad (id → name → data-* → ARIA → texto → class → complejo), anclando en un contenedor único.
4. **Verificar unicidad** con `browser_evaluate`, contando las coincidencias del XPath:

   ```
   browser_evaluate
     function: "() => document.evaluate(\"//input[@name='email']\", document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null).snapshotLength"
   ```

   El resultado debe ser **exactamente 1**:
   - `1` → selector único y válido ✅
   - `0` → el selector no resuelve ningún elemento (revisar atributos y contexto) ❌
   - `> 1` → selector ambiguo: refinar con más atributos o anclar a un contenedor con `id` / `data-*` ❌

   Para inspeccionar la coincidencia encontrada:

   ```
   browser_evaluate
     function: "() => { const n = document.evaluate(\"//button[text()='Aceptar']\", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; return n ? n.outerHTML.slice(0, 200) : 'NOT FOUND'; }"
   ```

   > En `browser_evaluate` el XPath se usa **sin** el prefijo `xpath=` (ese prefijo es del motor de selectores de Playwright y solo aplica al parámetro `target`).
5. **Confirmar funcionalmente**: ejecutar la acción real sobre ese `target` (`browser_click`, `browser_type`, ...) y verificar el efecto con `browser_wait_for` o `browser_evaluate`.
6. **Evidenciar**: `browser_take_screenshot` del estado resultante.
7. **Registrar** el XPath en el catálogo de selectores (ver más abajo).

### Para arreglar un selector que no funciona

1. Iniciar/continuar la sesión de **Playwright MCP Server** y navegar hasta la sección involucrada (`browser_navigate`).
2. Capturar de nuevo el nodo con `browser_snapshot` o `browser_find`.
3. Reconstruir el XPath siguiendo la jerarquía de esta skill, subiendo en prioridad hacia atributos más estables.
4. Validar unicidad con `browser_evaluate` y funcionalmente con la acción real.
5. Actualizar el selector en el catálogo y en los casos de prueba que lo referencien.

### Capacidades opt-in (solo si están habilitadas)

Pueden usarse como refuerzo, siempre del **Playwright MCP Server** (no implican Chrome DevTools MCP):

| Herramienta | Flag | Uso |
|---|---|---|
| `browser_get_config` | `--caps=config` | Verificar qué capacidades están activas |
| `browser_highlight` / `browser_hide_highlight` | `--caps=devtools` | Resaltar visualmente el elemento resuelto por el XPath |
| `browser_generate_locator` | `--caps=testing` | Obtener el locator canónico de un elemento |
| `browser_verify_element_visible`, `browser_verify_value`, `browser_verify_text_visible` | `--caps=testing` | Verificación formal del elemento |

> Nota: `--caps=devtools` es una **capacidad del propio Playwright MCP Server**. No es el servidor Chrome DevTools MCP, cuyo uso está prohibido en MANUAL-TLC.

### Si todas las estrategias fallan

Escalar al usuario por chat y solicitar:
- la pantalla exacta y el elemento a operar (o su descripción),
- y el atributo estable que el equipo de desarrollo puede agregar (idealmente `data-testid`).

## 🎓 Buenas prácticas

### ✅ HACER

- Usar atributos únicos (`id`, `name`, `data-*`) como ancla.
- Construir XPath **relativos** desde elementos estables (nunca desde la raíz del DOM).
- Combinar varios atributos para ganar especificidad.
- Usar funciones de texto con normalización (`normalize-space()`) cuando el texto sea necesario.
- Mantener los XPath **cortos y simples**.
- Documentar con un comentario los XPath complejos (nivel 7).
- **Validar siempre con Playwright MCP Server** antes de usar o documentar un selector.
- Reutilizar el catálogo de selectores antes de crear uno nuevo.
- Acompañar siempre el `target` con el parámetro `element` (descripción legible).

### ❌ EVITAR

- XPath absolutos desde la raíz: `/html/body/div[1]/div[2]/span[3]`.
- Selectores basados solo en posición sin contexto: `//div[5]/span[2]`.
- Depender de estilos visuales: `//*[@class='active']` sin contexto adicional.
- Texto parcial ambiguo que pueda repetirse en la página.
- XPath extremadamente largos con muchos niveles de anidación.
- Selectores generados dinámicamente o que cambian con frecuencia (hashes, `id` autogenerados, clases utilitarias del framework).
- **Usar selectores que no hayan sido validados con el Playwright MCP Server.**

## 🔧 Patrón recomendado

```
1. Anclar en un contenedor único (id, data-*, role con nombre accesible).
2. Navegar al elemento deseado mediante relaciones y atributos.
3. Validar unicidad (snapshotLength === 1) y luego funcionalmente.
```

Ejemplos:

```
xpath=//*[@id='user-form']//input[@name='email']
xpath=//*[@data-testid='modal']//button[@type='submit' and contains(text(), 'Guardar')]
xpath=//*[@id='tabs-checkout']//*[@role='tab' and @aria-label='Pago']
```

## 🚫 Antipatrones

| Antipatrón | Ejemplo | Por qué |
|---|---|---|
| Posición sin contexto | `//div[3]/span[2]` | Se rompe con cualquier reordenamiento |
| XPath absoluto | `/html/body/div/div/div/button` | Máxima fragilidad |
| Solo estilos | `//*[@class='active highlight']` | La clase cambia con el diseño |
| Texto ambiguo sin contexto | `//span[text()='OK']` | Coincide con varios elementos |
| `id` autogenerado | `//*[@id='mui-1284']` | Cambia en cada render |
| Índice sobre listas | `//table/tr[7]/td[3]` | Los datos cambian de orden |
| Selector no validado | cualquiera | Puede no resolver o resolver al elemento equivocado |

## 📚 Catálogo de selectores

Los selectores validados se documentan en `PRJ-{proyecto}/{ambiente}/Test_Data/Selectors/{modulo}.md` para reutilizarlos en sesiones posteriores y en regresión:

```markdown
| Elemento | XPath validado | Nivel | Unicidad | Validado con | Fecha | Notas |
|---|---|---|---|---|---|---|
| Botón Iniciar sesión | `xpath=//*[@id='login-button']` | 1 (id) | 1 | Playwright MCP (`browser_evaluate`) | 2026-09-21 | estable |
| Campo Email | `xpath=//input[@id='email-input']` | 1 (id) | 1 | Playwright MCP | 2026-09-21 | campo obligatorio |
| Pestaña Pago | `xpath=//*[@role='tab' and @aria-label='Pago']` | 4 (ARIA) | 1 | Playwright MCP | 2026-09-21 | — |
```

En el caso de prueba, el selector se referencia junto al paso:

```markdown
3. Hacer clic en "Iniciar sesión"
   target: xpath=//*[@id='login-button']
```

## Reglas

1. **Herramienta única**: Playwright MCP Server. **Nunca Chrome DevTools MCP.**
2. **XPath siempre** para los selectores que se escriben y documentan.
3. Ningún selector se usa ni se documenta sin haber sido **validado** (unicidad + confirmación funcional) con el Playwright MCP Server.
4. Está prohibido **inventar** selectores o copiarlos de otras aplicaciones.
5. Prohibido usar selectores generados dinámicamente o que cambian con frecuencia.
6. Un XPath que resuelve más de un nodo **no es un selector válido**: refinar o anclar.
7. Si el elemento no tiene ningún atributo estable, **escalar al usuario** y solicitar un `data-testid`.
8. Todo cambio de selector se refleja en el catálogo y en los casos de prueba que lo referencian.
9. La corrección de un selector no altera el resultado esperado del caso: si el comportamiento cambia, es un defecto, no un ajuste de selector.
