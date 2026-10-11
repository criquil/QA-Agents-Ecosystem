# 08 - Reglas estrictas

> **Misión:** Establecer reglas obligatorias que deben seguirse en todo el proceso de automatización de testing.

---

## Reglas Generales

### 1. Uso Obligatorio de Playwright MCP Server para navegación y validación funcional

**Regla:** Todos los tests funcionales con UI/Web DEBEN ser navegados y validados utilizando el Playwright MCP Server.

**Razón:** Garantiza que los flujos se ejecuten en un browser real, las evidencias sean capturadas y los pasos documentados correspondan al comportamiento real de la aplicación.

**Proceso obligatorio:**
1. Usar Playwright MCP para navegar a la URL del entorno
2. Ejecutar cada paso del caso de prueba via Playwright MCP
3. Capturar screenshot al finalizar cada fase crítica
4. Verificar visualmente el Resultado Esperado antes de documentarlo

**Herramientas clave:** `navigate_page`, `click`, `fill`, `take_screenshot`, `wait_for`, `press_key`

**Referencia completa:** `docs/knowledge/Agentic_QA/06-referencia/04-regla-mcp-servers.md`

---

### 2. Uso Obligatorio de Chrome DevTools MCP para captura y validación de Selectores

**Regla:** TODOS los selectores DEBEN ser capturados y validados utilizando Chrome DevTools MCP ANTES de ser definidos en cualquier Page Object.

**Razón:** Asegura que los selectores sean correctos, únicos y estables en el DOM real — no inferidos o copiados sin validar.

**Proceso obligatorio:**
1. Navegar a la página con Chrome DevTools MCP (`navigate_page`)
2. Capturar snapshot del DOM (`take_snapshot`)
3. Identificar el elemento target y verificar jerarquía (id > name > data-testid > ARIA > text > class)
4. Validar que el selector funciona (`evaluate_script`)
5. Definirlo como constante `UPPERCASE` en el Page Object

**Herramientas clave:** `navigate_page`, `take_snapshot`, `evaluate_script`, `take_screenshot`, `get_console_message`

**Referencia completa:** `docs/knowledge/Agentic_QA/06-referencia/04-regla-mcp-servers.md`

---

### 3. Evitar Código Redundante

**Regla:** Nunca duplicar código que ya existe. Siempre buscar reutilización.

**Razón:** El código redundante dificulta el mantenimiento y aumenta el riesgo de inconsistencias.

**Antes de crear código:**
- [ ] ¿Ya existe una función que haga esto?
- [ ] ¿Existe un Page Object que ya tenga este método?
- [ ] ¿Puedo reutilizar una función existente?

---

### 4. Antes de Crear Código, SIEMPRE Validar si Ya Existe

**Regla:** SIEMPRE buscar código existente antes de crear nuevo código.

**Razón:** Evita duplicación y promueve consistencia.

**Proceso:**
1. Buscar en Page Objects existentes
2. Buscar en helpers/utilidades
3. Buscar en tests anteriores
4. Solo crear nuevo si no existe nada equivalente

---

### 5. Evitar Declarar un Selector Múltiples Veces

**Regla:** Cada selector debe ser declarado UNA sola vez y reutilizarse.

**Razón:** Evita inconsistencias y dificultad de mantenimiento.

**Implementación:**
```typescript
// ✅ CORRECTO - Declarar una vez en Page Object
class LoginPage {
  readonly INPUT_USERNAME = '#username';
  readonly INPUT_PASSWORD = '#password';
  readonly BTN_LOGIN = '#login-button';
}

// ❌ INCORRECTO - Declarar múltiples veces
const INPUT_USERNAME = '#username';  // En test 1
const INPUT_USERNAME = '#username';  // En test 2
```

---

### 6. Nunca Hardcodear Datos

**Regla:** NUNCA hardcodear datos directamente en el código de tests o Page Objects.

**Razón:** Los datos hardcodeados son difíciles de mantener, no son reutilizables y presentan riesgos de seguridad.

**❌ INCORRECTO:**
```typescript
// ❌ Datos hardcodeados
await page.fill('#username', 'admin');
await page.fill('#password', 'password123');
await page.goto('http://example.com/login');
```

**✅ CORRECTO:**
```typescript
// ✅ Datos desde archivos externos
const user = await dataLoader.getData('users', 'admin');
await page.fill('#username', user.username);
await page.fill('#password', user.password);

const config = await dataLoader.loadYaml('config');
await page.goto(config.environments.qa.baseUrl);
```

---

### 7. SIEMPRE Parametrizar Datos

**Regla:** SIEMPRE cargar datos desde archivos externos (JSON, YAML, CSV).

**Razón:** Permite reutilización, mantenimiento fácil y ejecución en múltiples entornos.

**Tipos de datos a parametrizar:**
- Credenciales de usuario
- URLs y configuración de entornos
- Mensajes de validación
- Datos de formularios
- Datos específicos de casos de prueba

**Estructura de datos:**
```
data/
├── config.yaml          # Configuración general
├── users.json           # Credenciales
├── messages.json        # Mensajes de validación
├── forms.json           # Datos de formularios
└── cases/               # Datos específicos
    ├── TC_001.json
    └── TC_002.json
```

---

### 8. Uso Obligatorio del Template de Caso de Prueba

**Regla:** Todo caso de prueba creado o importado DEBE utilizar el template oficial ubicado en `docs/templates/tc_template.md`.

**Razón:** Garantiza consistencia, trazabilidad y legibilidad en todos los casos de prueba del proyecto, independientemente del tipo de testing (manual, automatizado, API, performance).

**Proceso obligatorio:**
1. Copiar `docs/templates/tc_template.md` como base del nuevo caso
2. Asignar un ID único con patrón `TC-[ID]`
3. Completar **todas** las secciones obligatorias (Propósito, Descripción, Data I/O, Steps, Resultado Esperado, Flujo)
4. Usar tablas de 3 columnas en Steps: `# | Acción | Resultado esperado`
5. Consultar `docs/templates/tc_example.md` como referencia de implementación

**Aplica a:**
- Creación de casos nuevos desde cero
- Importación desde tickets, user stories, especificaciones externas
- Migración de casos existentes en otros formatos

**Referencia completa:** `docs/knowledge/Agentic_QA/06-referencia/02-regla-template-caso-prueba.md`

---

### 9. Almacenamiento Obligatorio con Template por Tipo de Artefacto

**Regla:** Todo artefacto que se ingrese al framework (caso de prueba, test script, plan de prueba, datos de prueba) DEBE ser almacenado usando el template oficial para su tipo. No se aceptan artefactos en formato libre.

**Razón:** Garantiza trazabilidad, consistencia y legibilidad en todos los artefactos del proyecto, independientemente del tipo de testing o del equipo que lo genere.

**Templates obligatorios por tipo:**

| Tipo | Template | Ubicación |
|------|----------|-----------|
| Caso de prueba | tc_template.md | `docs/templates/tc_template.md` |
| Test script | POM Boilerplate | `docs/knowledge/Automation_QA/Strategy/Boilerplate/` |
| Plan de prueba | Formato plan formal | Skill `qa-formal-planning` |
| Datos de prueba | DataLoader pattern | `docs/knowledge/Automation_QA/Strategy/Data_Parametrization/` |

**Proceso obligatorio para test scripts:**
1. Usar el boilerplate oficial como estructura base del archivo
2. Page Object hereda de `BasePage` — POM obligatorio
3. Selectores como constantes `UPPERCASE` en el Page Object
4. `DataLoader` para todos los datos — nunca inline
5. 4 tags obligatorios: `@project`, `@environment`, `@functionality`, `@specific_case`

**Checklist de ingreso:**
- [ ] ¿Usa el template oficial de su tipo?
- [ ] ¿Tiene identificador único?
- [ ] ¿Secciones obligatorias completas?
- [ ] ¿Sin datos hardcodeados?

**Referencia completa:** `docs/knowledge/Agentic_QA/06-referencia/03-regla-almacenamiento-template.md`

---

## Resumen de Reglas

| # | Regla | Prioridad |
|---|-------|-----------|
| 1 | Uso Obligatorio de Playwright MCP Server | 🔴 CRÍTICA |
| 2 | Uso Obligatorio de Chrome DevTools MCP | 🔴 CRÍTICA |
| 3 | Evitar Código Redundante | 🟠 ALTA |
| 4 | SIEMPRE Validar si Ya Existe | 🟠 ALTA |
| 5 | Evitar Declarar Selector Múltiples Veces | 🟠 ALTA |
| 6 | Nunca Hardcodear Datos | 🔴 CRÍTICA |
| 7 | SIEMPRE Parametrizar Datos | 🔴 CRÍTICA |
| 8 | Uso Obligatorio del Template de Caso de Prueba | 🔴 CRÍTICA |
| 9 | Almacenamiento Obligatorio con Template por Tipo de Artefacto | 🔴 CRÍTICA |

---

## Referencias

- **POM Strategy:** Ver `../Strategy/POM/README.md`
- **Selectors Strategy:** Ver `../Strategy/Selectors_Strategy/README.md`
- **Data Parametrization:** Ver `../Strategy/Data_Parametrization/README.md`
- **Troubleshooting:** Ver `../Strategy/Troubleshooting/README.md`
- **Template de Caso de Prueba:** Ver `docs/templates/tc_template.md`
- **Ejemplo de Caso de Prueba:** Ver `docs/templates/tc_example.md`
- **Regla Template (referencia completa):** Ver `docs/knowledge/Agentic_QA/06-referencia/02-regla-template-caso-prueba.md`
- **Regla Almacenamiento con Template:** Ver `docs/knowledge/Agentic_QA/06-referencia/03-regla-almacenamiento-template.md`

---

*Reglas estrictas - Intelligent QA Manager*
