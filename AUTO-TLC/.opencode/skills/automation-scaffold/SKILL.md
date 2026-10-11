---
name: automation-scaffold
description: "Generacion de la estructura base de un proyecto de automatizacion: boilerplate de Page Object, Selectors, TestBase, Test y Config. Invocar al crear un proyecto de tests desde cero o al agregar un modulo nuevo."
---

# Automation Scaffold — Generacion

> **Precondicion**: no generar estructura sin haber resuelto `automation-foundations` (stack),
> `automation-selectors` (selectores reales) y `automation-data` (estructura de datos).
> Un scaffold sin selectores validados produce un proyecto que no corre.

## Flujo de generacion

```
1. Confirmar stack      -> lenguaje, framework, runner
2. Confirmar modulos    -> que paginas se cubren
3. Emitir estructura     -> arbol de carpetas + archivos base
4. Implementar por modulo-> Page Object + test, uno por vez
5. Verificar            -> el test pasa contra la app real
```

## Estructura base generada

```
<proyecto>/
├── pages/
│   ├── BasePage.ts
│   └── <Modulo>/
│       └── <Modulo>Page.ts
├── tests/
│   ├── TestBase.ts
│   └── test_<funcionalidad>.spec.ts
├── helpers/
│   └── data-loader.ts
├── data/
│   ├── config.yaml
│   ├── users.json
│   ├── messages.json
│   ├── forms.json
│   └── cases/
├── reports/
├── playwright.config.ts
├── package.json
└── tsconfig.json
```

## Templates base

### BasePage.ts

```typescript
import { Page, Locator } from '@playwright/test';

export abstract class BasePage {
  constructor(protected readonly page: Page) {}

  protected loc(selector: string): Locator { return this.page.locator(selector); }

  async navegar(url: string)          { await this.page.goto(url); }
  async recargar()                    { await this.page.reload(); }
  async esperarVisible(s: string, t = 30_000) { await this.loc(s).waitFor({ state: 'visible', timeout: t }); }
  async esperarOculto(s: string, t = 30_000)   { await this.loc(s).waitFor({ state: 'hidden', timeout: t }); }
  async click(s: string)              { await this.loc(s).click(); }
  async llenar(s: string, v: string)  { await this.loc(s).fill(v); }
  async texto(s: string)             { return (await this.loc(s).textContent()) ?? ''; }
  async visible(s: string)            { return await this.loc(s).isVisible(); }
}
```

### Selectors por modulo

Los selectores viven como constantes de clase en el Page Object. Si superan ~15 elementos,
separarlos en un archivo `<Modulo>Selectors.ts` que el Page Object compone.

```typescript
export class LoginSelectors {
  readonly INPUT_USUARIO = 'xpath=//*[@id="username"]';
  readonly INPUT_CLAVE   = 'xpath=//*[@id="password"]';
  readonly BTN_INGRESAR  = 'xpath=//button[@id="actionButtonIngresar"]';
  readonly MSG_ERROR     = 'xpath=//*[@class="error-message"]';
}
```

### TestBase.ts

```typescript
import { test as base } from '@playwright/test';

export const test = base.extend({});
export { expect } from '@playwright/test';
```

### Test con tags y datos

```typescript
import { test, expect } from '../TestBase';
import { LoginPage } from '../pages/Login/LoginPage';
import { DataLoader } from '../helpers/data-loader';
import config from '../data/config.yaml';

const TAGS = ['@bank-app', '@qa', '@login', '@login_exitoso', '@smoke'];

test.describe('Login', () => {
  test('ingreso con credenciales validas', { tag: TAGS }, async ({ page }) => {
    const loader = new DataLoader({ dataDir: 'data' });
    const env    = config.environments[process.env.QA_ENV ?? 'qa'];
    const user   = await loader.getData('users', 'validUser');
    const msgs   = await loader.getData('messages', 'login');

    const loginPage = new LoginPage(page);
    await loginPage.navegar(`${env.baseUrl}/login`);
    await loginPage.login(user.username, user.password);

    expect(await loginPage.ingresoExitoso()).toBeTruthy();
  });
});
```

### playwright.config.ts

```typescript
import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  timeout: 30_000,
  retries: process.env.CI ? 2 : 0,
  reporter: [
    ['html', { outputFolder: 'reports/', open: 'never' }],
    ['junit', { outputFile: 'reports/junit.xml' }],
    ['json',  { outputFile: 'reports/results.json' }]
  ],
  use: {
    baseURL: process.env.QA_ENV ? undefined : 'http://localhost:3000',
    trace: 'retain-on-failure',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
    locale: 'es-ES',
    timezoneId: 'America/Bogota'
  },
  projects: [
    { name: 'chromium', use: { browserName: 'chromium' } },
    { name: 'firefox',  use: { browserName: 'firefox' } },
    { name: 'webkit',   use: { browserName: 'webkit' } }
  ]
});
```

Fijar `locale` y `timezoneId` evita fallos que solo aparecen en CI por diferencias regionales.

## Stacks soportados

| Lenguaje | Frameworks | Notas |
|---|---|---|
| TypeScript | Playwright, Cypress, Selenium | Default recomendado |
| Python | Playwright, Selenium, pytest | Sintaxis equivalente, snake_case |
| Java | Selenium, TestNG, JUnit | Cuando la org ya lo estandarizo |
| C# | Selenium, NUnit, xUnit | Cuando la org ya lo estandarizo |

El POM es agnostico: los templates cambian de sintaxis, las reglas no.

## Reglas del scaffold

### Obligatorio

1. No generar un Page Object con selectores inventados.
2. Cada modulo generado incluye su archivo de datos o su entrada en `config.yaml`.
3. Cada test generado incluye los 4 tags obligatorios.
4. `BasePage` presente y todos los Page Object heredan de ella.
5. Verificar que el test generado pasa contra la app real antes de dar por cerrado el scaffold.

### Prohibido

1. Generar la estructura completa de una sola vez sin implementar modulo por modulo.
2. Dejar `# TODO` o placeholders en selectores.
3. Hardcodear credenciales o URLs en el scaffold.
4. Agregar dependencias que el proyecto no usa.

## Checklist de entrega

- [ ] Estructura de carpetas completa segun el estandar
- [ ] `BasePage` con metodos compartidos
- [ ] Al menos un Page Object con selectores **validados**
- [ ] `DataLoader` funcionando y `data/` poblado
- [ ] Al menos un test con los 4 tags que pasa en verde
- [ ] Configuracion con multi-browser y artefactos en fallo
- [ ] `README.md` con el comando de ejecucion

## Lectura bajo demanda

Este SKILL.md ya trae todos los templates base listos para copiar.

| Si el SKILL.md no alcanza y necesitás | Leé |
|---|---|
| Templates oficiales en el repositorio | `docs/knowledge/Automation_QA/Strategy/Boilerplate/README.md` |
| Sintaxis del POM en otro lenguaje | `docs/knowledge/Automation_QA/Strategy/POM/README.md` |
| Estructura de un proyecto por stack | `.opencode/skills/automation-pom/SKILL.md` |

Localiza la seccion antes de leer: `grep -n "^## " <archivo>`

**Stop**: los templates de aca cubren TypeScript + Playwright. Para otro lenguaje, adapta el POM; no descargues boilerplate.

---

*Automation Scaffold — estructura base conforme a las reglas. Platform: OpenCode.*