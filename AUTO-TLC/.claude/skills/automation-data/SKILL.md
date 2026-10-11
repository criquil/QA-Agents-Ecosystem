---
name: automation-data
description: "Parametrizacion de datos de prueba: DataLoader, arbol data/, externalizacion de input y output esperado. Invocar al disenar los datos de un test o cuando hay credenciales, URLs o mensajes esperados hardcodeados."
---

# Automation Data — Parametrizacion

> **Golden rule**: ningun dato de prueba se escribe en el codigo. Ni de entrada, ni de salida.

## Que cuenta como dato hardcodeado

Todo lo que varia entre entornos, casos o iteraciones:

| Categoria | Ejemplo | Donde vive |
|---|---|---|
| Credenciales | usuario, password, token | `data/users.json` |
| URLs y entornos | baseUrl, timeouts | `data/config.yaml` |
| Datos de formulario | montos, cuentas, fechas | `data/forms.json` |
| Mensajes esperados | texto de exito y de error | `data/messages.json` |
| Estado de pruebas | flags, feature toggles | `data/config.yaml` |
| Datos del caso | input y output de un `TC-[ID]` | `data/cases/TC_<ID>.json` |

El error mas comun: externalizar el **input** y dejar el **output** en un literal.

```typescript
// ❌ input externo, output hardcodeado
const user = await dataLoader.getData('users', 'admin');
await loginPage.login(user.username, user.password);
expect(await loginPage.mensaje()).toBe('Bienvenido');   // <- dato hardcodeado

// ✅ ambos externos
const user  = await dataLoader.getData('users', 'admin');
const msgs  = await dataLoader.getData('messages', 'login');
await loginPage.login(user.username, user.password);
expect(await loginPage.mensaje()).toBe(msgs.success);
```

Un assert contra literal cambia de idioma o de copy y rompe el test sin que haya un bug.

## Estructura de `data/`

```
data/
├── config.yaml          # entornos, timeouts, retries, feature flags
├── users.json           # credenciales por rol y escenario
├── messages.json        # textos esperados por funcionalidad
├── forms.json           # datos de formulario por caso
└── cases/
    ├── TC_001.json      # input + expectedOutput de un caso puntual
    └── TC_002.json
```

## Formatos soportados

| Formato | Uso |
|---|---|
| `.json` | Datos estructurados, datasets de pruebas |
| `.yaml` | Configuracion, ambientes, parametros de ejecucion |
| `.csv` | Tablas grandes, un caso por fila |

## DataLoader

```typescript
export class DataLoader {
  constructor(private readonly dataDir: string) {}

  async loadJson<T>(path: string): Promise<T>
  async loadYaml<T>(path: string): Promise<T>
  async loadCsv<T>(path: string): Promise<T[]>
  async getData<T>(file: string, key: string): Promise<T>   // acceso por clave
}
```

Uso tipico:

```typescript
const loader = new DataLoader({ dataDir: 'data' });
const config = await loader.loadYaml('config');
const env    = config.environments[process.env.QA_ENV ?? 'qa'];

const user = await loader.getData('users', 'validUser');
const msgs = await loader.getData('messages', 'login');

await loginPage.navegar(env.baseUrl);
await loginPage.login(user.username, user.password);
expect(await loginPage.ingresoExitoso()).toBeTruthy();
```

## Formato de `config.yaml`

```yaml
default: qa
environments:
  dev:  { baseUrl: "http://localhost:3000",  timeout: 30000 }
  qa:   { baseUrl: "http://qa.example.com",  timeout: 30000 }
  uat:  { baseUrl: "http://uat.example.com", timeout: 30000 }
  prod: { baseUrl: "http://example.com",    timeout: 60000 }
```

El ambiente se resuelve por variable de entorno. Un test nunca decide en que ambiente corre.

## Datos por caso de prueba

Cuando un caso tiene input y salida esperada propias, se aisan en su archivo:

```json
{
  "testCase": "TC_001",
  "description": "Transferencia con saldo insuficiente",
  "input": {
    "monto": "5000.00",
    "cuentaOrigen": "0000003100010000000001",
    "cuentaDestino": "0000003100010000000002"
  },
  "expectedOutput": {
    "mensaje": "Saldo insuficiente",
    "saldoRestante": "1000.00",
    "urlDestino": "/dashboard"
  }
}
```

Ventaja: el caso es legible sin abrir el test, y el test queda igual para todos los casos.

## Reglas

### Obligatorio

1. Todo dato variable se carga desde `data/` a traves de `DataLoader`.
2. El output esperado tambien se externaliza.
3. La seleccion de ambiente se resuelve por variable, no en el codigo.
4. Un caso con datos propios se aísla en `data/cases/TC_<ID>.json`.
5. Secretos reales no se versionan: se inyectan por variable de entorno o gestor de secretos.

### Prohibido

1. Credenciales, URLs o mensajes esperados en el codigo.
2. Secretos reales en `data/` versionado — placeholders por entorno.
3. Generacion de datos aleatorios sin semilla fija cuando el test debe ser reproducible.
4. Un `assert` contra string literal.

## Checklist de parametrizacion

### Input
- [ ] Credenciales desde `data/users.json`
- [ ] URLs y timeouts desde `data/config.yaml`
- [ ] Datos de formulario desde `data/forms.json`
- [ ] Datos del caso desde `data/cases/TC_<ID>.json`

### Output
- [ ] Mensajes esperados desde `data/messages.json`
- [ ] URLs de destino esperadas parametrizadas
- [ ] Estados esperados parametrizados
- [ ] Ningun assert contra literal

### Configuracion
- [ ] Ambiente resuelto por variable de entorno
- [ ] Sin secretos reales versionados

## Lectura bajo demanda

Este SKILL.md ya trae el arbol `data/`, los formatos, el DataLoader y los patrones.

| Si el SKILL.md no alcanza y necesitás | Leé |
|---|---|
| Catalogo completo de formatos de datos | `docs/knowledge/Automation_QA/Strategy/Data_Parametrization/README.md` |
| Gestion de datos desde la perspectiva del POM | `docs/knowledge/Automation_QA/03-herramientas/02-test-data.md` |

Localiza la seccion antes de leer: `grep -n "^## " <archivo>`

**Stop**: los patrones cubren lo habitual. Para un caso raro, busca con `grep -rn "<termino>" data/` primero.

---

*Automation Data — nada hardcodeado, ni entrada ni salida. Platform: Claude Code.*