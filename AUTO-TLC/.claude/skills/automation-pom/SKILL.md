---
name: automation-pom
description: "Page Object Model: BasePage, jerarquia de clases, separacion entre metodos de accion y de verificacion, convenciones de nombres. Invocar al disenar la arquitectura de pages o al crear/modificar un Page Object."
---

# Automation POM — Page Object Model

> **Proposito**: que un cambio de UI rompa un archivo, no veinte tests.

## Capas y responsabilidades

```
BasePage        -> metodos compartidos (navegacion, esperas, interaccion, lectura)
Pages           -> interaccion con la UI. Sin logica de negocio
Tests           -> logica de negocio y orquestacion. Sin selectores
data/           -> datos de entrada y salida esperada
```

Regla de lectura: si el test contiene un selector, el POM esta roto. Si el Page Object contiene una regla de negocio, el POM esta roto.

## Estructura obligatoria

```
pages/
├── BasePage.ts
└── <Modulo>/
    └── <Modulo>Page.ts        una clase por pagina o modulo

tests/
├── TestBase.ts
└── test_<funcionalidad>.spec.ts

helpers/
└── data-loader.ts

data/
├── config.yaml
├── users.json
├── messages.json
├── forms.json
└── cases/
    └── TC_<ID>.json
```

## BasePage — el contrato comun

```typescript
export abstract class BasePage {
  constructor(protected readonly page: Page) {}

  // Navegacion
  async navegar(url: string): Promise<void>
  async recargar(): Promise<void>

  // Esperas
  async esperarVisible(selector: string, timeout?: number): Promise<void>
  async esperarOculto(selector: string, timeout?: number): Promise<void>

  // Interaccion
  async click(selector: string): Promise<void>
  async llenar(selector: string, valor: string): Promise<void>
  async escribir(selector: string, valor: string): Promise<void>

  // Lectura
  async texto(selector: string): Promise<string>
  async atributo(selector: string, attr: string): Promise<string | null>
  async visible(selector: string): Promise<boolean>
}
```

Todo Page Object hereda de `BasePage`. Sin excepcion. El metodo `click` se implementa una vez.

## Anatomia de un Page Object

```typescript
export class LoginPage extends BasePage {
  // Selectores: constantes UPPERCASE, validados con DevTools
  readonly INPUT_USUARIO = 'xpath=//*[@id="username"]';
  readonly INPUT_CLAVE   = 'xpath=//*[@id="password"]';
  readonly BTN_INGRESAR  = 'xpath=//button[@id="actionButtonIngresar"]';
  readonly MSG_ERROR     = 'xpath=//*[@class="error-message"]';

  constructor(page: Page) { super(page); }

  // --- Metodos de ACCION: hacen, no verifican ---
  async ingresarUsuario(valor: string): Promise<void>
  async ingresarClave(valor: string): Promise<void>
  async hacerClickIngresar(): Promise<void>
  async login(usuario: string, clave: string): Promise<void>

  // --- Metodos de VERIFICACION: leen, no hacen ---
  async mensajeError(): Promise<string>
  async ingresoExitoso(): Promise<boolean>
  async validarMensajeError(esperado: string): Promise<boolean>
}
```

### Por que separar accion de verificacion

Un metodo que hace y verifica no se puede reutilizar. `login(usuario, clave, verificar)` obliga a pasar
`verificar=false` en el flujo negativo. Con metodos separados, el test compone:

```typescript
await loginPage.login(credenciales.username, credenciales.password);
expect(await loginPage.ingresoExitoso()).toBeTruthy();
```

Cada metodo hace una sola cosa, se prueba sola y se lee como una frase.

## Convenciones de nombres

| Elemento | Patron | Ejemplo |
|---|---|---|
| Page Object | `<Funcionalidad>Page` | `TransferenciasPage` |
| Selector | `UPPERCASE` con prefijo por rol | `BTN_CONFIRMAR`, `MSG_ERROR` |
| Metodo de accion | verbo + objeto | `ingresarUsuario`, `confirmarPago` |
| Metodo de verificacion | `verificar*` / `es*` / `obtener*` | `verificarSaldoInsuficiente` |
| Test | `test_<funcionalidad>.spec.ts` | `test_transferencias.spec.ts` |
| Caso | `test_<descripcion_caso>` | `test_transferencia_saldo_insuficiente` |

Prefijos de selector por rol: `INPUT_`, `BTN_`, `LNK_`, `TBL_`, `ROW_`, `COL_`, `MSG_`, `LBL_`, `DDL_`, `CHK_`, `ICO_`, `TAB_`, `FLD_`, `DIV_`.

## Reglas del POM

### Obligatorio

1. Todo Page Object hereda de `BasePage`.
2. Selectores como constantes de clase en `UPPERCASE`, con prefijo de rol.
3. Una clase por pagina o modulo.
4. Buscar y reutilizar antes de crear.
5. Documentar los metodos publicos.
6. Separar metodos de accion y de verificacion.

### Prohibido

1. Selectores dentro de los tests.
2. Selectores o metodos duplicados.
3. Datos de prueba hardcodeados en el Page Object.
4. Metodos que mezclan accion y verificacion.
5. Nombres genericos: `button1`, `inputField`, `click`.

## Checklist de un Page Object nuevo

- [ ] Hereda de `BasePage`
- [ ] Todos los selectores validados con DevTools MCP y documentados
- [ ] Selectores en `UPPERCASE` con prefijo de rol
- [ ] Ningun selector declarado fuera de esta clase
- [ ] Ningun dato hardcodeado — todo por parametro o `DataLoader`
- [ ] Metodos de accion separados de los de verificacion
- [ ] Nombre del archivo igual al de la clase
- [ ] Busca equivalente existente antes de crearse (A3)

## Lectura bajo demanda

Este SKILL.md ya trae la estructura, la anatomia de un Page Object y las reglas del POM.

| Si el SKILL.md no alcanza y necesitás | Leé |
|---|---|
| Variantes por lenguaje (Java, C#, Python) | `docs/knowledge/Automation_QA/Strategy/POM/README.md` — seccion `## Estructura Generica POM` |
| Plantilla lista para copiar | `docs/knowledge/Automation_QA/Strategy/Boilerplate/README.md` |
| Parametrizacion de los datos que recibe | `.claude/skills/automation-data/SKILL.md` |

Localiza la seccion antes de leer: `grep -n "^## " <archivo>`

**Stop**: el patron completo esta aca. No leas el POM generico si ya sabes el lenguaje.

---

*Automation POM — Playwright + TypeScript como referencia; adaptable a cualquier lenguaje. Platform: Claude Code.*