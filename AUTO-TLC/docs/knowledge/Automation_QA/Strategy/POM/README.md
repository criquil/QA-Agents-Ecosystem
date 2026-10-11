# Page Object Model (POM) - Guía Genérica

> **NOTA**: Este documento es **AGNÓSTICO** - No asume ningún lenguaje de programación ni framework de automatización.

---

## ¿Qué es el Page Object Model?

**Page Object Model (POM)** es un patrón de diseño que crea una capa de abstracción entre los tests y la interfaz de usuario. Cada página de la aplicación se representa como una clase que encapsula:

- **Selectores (locators)**: Elementos de la UI
- **Métodos de acción**: Interacciones con la página
- **Métodos de verificación**: Validaciones de estado

### Beneficios del POM:

| Beneficio | Descripción |
|-----------|-------------|
| **Mantenibilidad** | Cambios en la UI solo afectan a los Page Objects, no a los tests |
| **Reutilización** | Un método puede usarse en múltiples tests |
| **Legibilidad** | Tests expresivos y de alto nivel |
| **Separación de responsabilidades** | Lógica de UI separada de lógica de tests |

---

## Estructura Genérica POM

### Organización de Carpetas

```
/pages
├── BasePage.[ext]              ← Clase base con métodos comunes
└── /[Modulo]
    └── [Nombre]Page.[ext]     ← Una clase por página/módulo
```

### Arquitectura de Clases

```
BasePage (clase padre)
    ↓ hereda
[Pagina1]Page, [Pagina2]Page, [Pagina3]Page, ...
```

---

## BasePage - Clase Base Genérica

La clase `BasePage` contiene métodos comunes utilizados por todos los Page Objects.

### Estructura Conceptual

```pseudocode
class BasePage:
    // Constructor recibe la instancia de la página
    constructor(page)
    
    // Métodos comunes de navegación
    navegar(url)
    recargar()
    ir_atras()
    ir_adelante()
    
    // Métodos comunes de espera
    esperar_elemento(selector, timeout)
    esperar_elemento_oculto(selector, timeout)
    esperar_url(patron, timeout)
    esperar_estado_carga(estado)
    
    // Métodos comunes de interacción
    hacer_click(selector)
    llenar_campo(selector, texto)
    escribir(selector, texto, delay)
    limpiar_campo(selector)
    seleccionar_opcion(selector, valor)
    
    // Métodos comunes de verificación
    elemento_visible(selector)
    elemento_habilitado(selector)
    obtener_texto(selector)
    obtener_atributo(selector, atributo)
```

> **NOTA**: La sintaxis específica (Python, Java, JavaScript, C#, etc.) se adaptará según el proyecto.

---

## Creación de Page Objects

### Paso 1: Definir la Clase

Cada Page Object hereda de `BasePage`:

```pseudocode
class [Nombre]Page hereda de BasePage:
    constructor(page)
        invocar super(page)
```

### Paso 2: Definir Selectores como Atributos de Clase

Los selectores se definen como **constantes de clase** al inicio:

```pseudocode
class LoginPage hereda de BasePage:
    // Selectores - Formato: MAYÚSCULAS
    INPUT_USERNAME = "xpath=//*[@id='username']"
    INPUT_PASSWORD = "xpath=//*[@name='password']"
    BTN_LOGIN = "xpath=//button[@id='login-form']"
    LBL_BIENVENIDA = "xpath=//*[@class='welcome-message']"
    MSG_ERROR = "xpath=//*[@class='error-message']"
```

### Paso 3: Implementar Métodos de Acción

Métodos que representan **acciones del usuario**:

```pseudocode
class LoginPage:
    // Métodos de acción
    navegar_a_login(url)
        invocar page.goto(url)
    
    ingresar_usuario(usuario)
        invocar page.locator(INPUT_USERNAME).fill(usuario)
    
    ingresar_password(password)
        invocar page.locator(INPUT_PASSWORD).fill(password)
    
    hacer_click_login()
        invocar page.locator(BTN_LOGIN).click()
    
    login(usuario, password)
        invocar self.ingresar_usuario(usuario)
        invocar self.ingresar_password(password)
        invocar self.hacer_click_login()
```

### Paso 4: Implementar Métodos de Verificación

Métodos que **validan el estado** de la página:

```pseudocode
class LoginPage:
    verificar_login_exitoso()
        retornar page.locator(LBL_BIENVENIDA).is_visible()
    
    verificar_error(mensaje_esperado)
        mensaje_actual = page.locator(MSG_ERROR).text_content()
        retornar mensaje_esperado in mensaje_actual
    
    obtener_mensaje_error()
        retornar page.locator(MSG_ERROR).text_content()
```

---

## Reglas de POM

### ✅ OBLIGATORIO

1. **Todos los Page Objects heredan de `BasePage`**
2. **Selectores como atributos de clase** (convención: MAYÚSCULAS)
3. **Una clase por página/módulo**
4. **Buscar y reutilizar** antes de crear nuevos
5. **Documentar todos los métodos públicos**
6. **Separar métodos de acción y verificación**

### ❌ PROHIBIDO

1. **Usar selectores directamente en tests**
2. **Duplicar selectores o métodos**
3. **Hardcodear datos de prueba en Page Objects**
4. **Crear métodos que mezclen acción y verificación**
5. **Usar nombres genéricos** (button1, input_field, test)

---

## Integración con Tests

### Flujo de Uso

```pseudocode
// En el test
class TestLogin:
    test_login_exitoso(page):
        // 1. Crear Page Object
        login_page = LoginPage(page)
        
        // 2. Ejecutar acciones usando Page Object
        login_page.navegar_a_login(url_base)
        login_page.ingresar_usuario(usuario)
        login_page.ingresar_password(password)
        login_page.hacer_click_login()
        
        // 3. Verificar usando Page Object
        assert login_page.verificar_login_exitoso() == true
```

### Ventajas de esta Integración

| Ventaja | Descripción |
|---------|-------------|
| **Tests legibles** | Se lee como lenguaje natural |
| **Tests mantenibles** | Cambios en UI solo afectan a Page Objects |
| **Tests reutilizables** | Mismos Page Objects en múltiples tests |
| **Separación clara** | Tests (QUÉ) vs Page Objects (CÓMO) |

---

## Estructura del Proyecto

```
/proyecto_qa
├── /pages                          ← Page Objects (POM)
│   ├── BasePage.[ext]             ← Clase base
│   ├── /Login
│   │   └── LoginPage.[ext]        ← Page Object
│   ├── /Dashboard
│   │   └── DashboardPage.[ext]    ← Page Object
│   └── /[Modulo]
│       └── [Nombre]Page.[ext]     ← Page Object
│
├── /tests                          ← Tests
│   ├── TestBase.[ext]             ← Clase base de tests
│   └── test_[funcionalidad].[ext]  ← Tests
│
├── /helpers                        ← Utilidades
│   └── data_loader.[ext]          ← Carga de datos
│
├── /data                           ← Datos parametrizados
│   ├── config.[json|yaml]         ← Configuración
│   ├── usuarios.json               ← Usuarios
│   └── /[feature]                 ← Datos por feature
│
├── /reports                        ← Reportes
│
├── /config                        ← Configuración extra
│
└── [archivo de dependencias]       ← package.json/requirements.txt/etc
```

---

## Convenciones de Nombres

### Page Objects
```
[Funcionalidad]Page.[ext]

Ejemplos:
- LoginPage.py / .java / .ts
- DashboardPage.py / .java / .ts
- TransferenciasPage.py / .java / .ts
```

### Tests
```
test_[funcionalidad].[ext]

Ejemplos:
- test_login.py / .java / .ts
- test_transferencias.py / .java / .ts
```

### Métodos de Test
```
test_[descripcion_del_caso]

Ejemplos:
- test_login_con_credenciales_validas
- test_transferencia_con_saldo_insuficiente
- test_pago_servicio_exitoso
```

---

## Resumen de Reglas POM

### ✅ OBLIGATORIO

1. Todos los Page Objects heredan de `BasePage`
2. Selectores como atributos de clase en MAYÚSCULAS
3. Una clase por página/módulo
4. Buscar y reutilizar antes de crear
5. Documentar todos los métodos públicos
6. Separar métodos de acción y verificación

### ❌ PROHIBIDO

1. Usar selectores directamente en tests
2. Duplicar selectores o métodos
3. Hardcodear datos de prueba
4. Crear métodos que mezclen acción y verificación
5. Usar nombres genéricos

---

## Referencias

- **Estrategia de Selectors**: Ver `Selectors_Strategy/README.md`
- **Categorización de Tests**: Ver `test-categorization.md`
- **Parametrización de Datos**: Ver `data-parametrization.md`
