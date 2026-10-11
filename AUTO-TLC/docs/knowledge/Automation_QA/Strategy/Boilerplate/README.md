# Boilerplate - Plantillas de Código

> **Misión:** Proveer plantillas base para empezar rápidamente con automatización

---

## Estructura

```
Boilerplate/
├── README.md                    # Este archivo
├── PageObject.ts               # Template de Page Object
├── Selectors.ts                # Template de Selectors
├── TestBase.ts                 # Template de TestBase
├── Test.ts                     # Template de Test
└── Config.ts                   # Template de configuración
```

---

## Agente: qa-boilerplate-generator

**Polyglot Agent** para generar estructura base de proyectos de automatización.

### Soporte

| Lenguaje | Frameworks |
|----------|------------|
| Python | Playwright, Selenium, pytest |
| JavaScript | Playwright, Selenium, Cypress, Puppeteer |
| TypeScript | Playwright, Selenium, Cypress, Puppeteer |
| Java | Selenium, TestNG, JUnit |
| C# | Selenium, NUnit, xUnit |
| Go | Selenium |
| Ruby | Selenium, Capybara |

### Uso

```bash
# Generar boilerplate
"Generate boilerplate for Python + Playwright"
"Create project structure for TypeScript + Cypress"
"Setup Selenium + Java project"
```

### Workflow del Agente

1. **Pregunta** lenguaje, framework, funcionalidad y preferencias
2. **Muestra** estructura genérica propuesta
3. **Espera** confirmación antes de generar
4. **Genera** código completo con templates

---

## Templates

### 1. PageObject.ts

```typescript
import { Page } from '@playwright/test';
import { BasePage } from '../Pages/BasePage';
import { [Page]Selectors } from './[Page].selectors';

export class [Page]Page extends BasePage {
  private selectors = new [Page]Selectors();
  
  constructor(page: Page) {
    super(page);
  }
  
  // Métodos específicos de la página
  async [action](): Promise<void> {
    // Implementar acción
  }
  
  async [getter](): Promise<string> {
    // Implementar getter
  }
}
```

### 2. Selectors.ts

```typescript
export class [Page]Selectors {
  // Inputs
  readonly [inputName] = '[data-testid="[input-name]"]';
  
  // Buttons
  readonly [buttonName] = '[data-testid="[button-name]"]';
  
  // Text
  readonly [textName] = '[data-testid="[text-name]"]';
  
  // Containers
  readonly [containerName] = '[data-testid="[container-name]"]';
}
```

### 3. TestBase.ts

```typescript
import { test as base } from '@playwright/test';
import { [Page]Page } from '../Pages/[Page]/[Page]Page';

export const test = base.extend<{
  [page]Page: [Page]Page;
}>({
  [page]Page: async ({ page }, use) => {
    await use(new [Page]Page(page));
  },
});

export { expect } from '@playwright/test';
```

### 4. Test.ts

```typescript
import { test, expect } from '../TestBase';

test.describe('[Feature]', () => {
  test('[scenario]', async ({ [page]Page }) => {
    // Arrange
    // ...
    
    // Act
    // ...
    
    // Assert
    // ...
  });
});
```

### 5. Config.ts

```typescript
import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './Test',
  timeout: 30000,
  retries: 2,
  use: {
    baseURL: 'http://localhost:3000',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },
  projects: [
    { name: 'chromium', use: { browserName: 'chromium' } },
    { name: 'firefox', use: { browserName: 'firefox' } },
    { name: 'webkit', use: { browserName: 'webkit' } },
  ],
});
```

---

## Uso

### 1. Copiar Template

```bash
# Copiar template deseado
cp Boilerplate/PageObject.ts Pages/NewPage/NewPage.ts
cp Boilerplate/Selectors.ts Pages/NewPage/NewPage.selectors.ts
cp Boilerplate/TestBase.ts Test/TestBase.ts
cp Boilerplate/Test.ts Test/NewFeature/new-feature.test.ts
```

### 2. Reemplazar Placeholders

```bash
# Reemplazar [Page] por nombre real
sed -i 's/\[Page\]/Login/g' Pages/Login/LoginPage.ts
sed -i 's/\[Page\]/Login/g' Pages/Login/Login.selectors.ts
```

### 3. Implementar

```typescript
// 1. Definir selectores
// 2. Implementar page methods
// 3. Crear tests
// 4. Ejecutar y verificar
```

---

## Navegación

- **Volver a Strategy:** [../README.md](../README.md)
- **POM:** [../POM/README.md](../POM/README.md)
- **Selectors:** [../Selectors_Strategy/](../Selectors_Strategy/)

---

*Boilerplate Documentation*
