# Playwright

> **Archivo:** 3 de 4 | **Sección:** Frameworks | **Nivel:** Intermedio

---

## Tabla de Contenidos

1. [Visión General](#visión-general)
2. [Características](#características)
3. [Instalación](#instalación)
4. [Ejemplos](#ejemplos)
5. [API Testing](#api-testing)
6. [Visual Testing](#visual-testing)
7. [Resumen](#resumen)

---

## Visión General

**Playwright**, desarrollado por Microsoft, es un framework moderno para testing de aplicaciones web que soporta múltiples navegadores.

### Características

- ✅ Multi-browser (Chromium, Firefox, WebKit)
- ✅ Multi-lenguaje (TypeScript, JavaScript, Python, Java)
- ✅ Auto-wait
- ✅ Parallel execution
- ✅ Network interception
- ✅ Mobile emulation
- ✅ API testing integrado

---

## Características

### vs Cypress

| Característica | Playwright | Cypress |
|----------------|------------|---------|
| **Browsers** | Multi-browser | Chrome/Electron |
| **Lenguajes** | Multi-language | JavaScript only |
| **API Testing** | Integrado | cy.request() |
| **Mobile** | Emulación real | Limitado |
| **Shadow DOM** | Soporte nativo | Limitado |
| **Parallel** | Nativo | Dashboard paid |

---

## Instalación

```bash
# npm
npm init playwright@latest

# yarn
yarn create playwright
```

### Estructura

```
tests/
├── example.spec.ts
├── login.spec.ts
└── dashboard.spec.ts
playwright.config.ts
```

---

## Ejemplos

### Test Básico

```typescript
import { test, expect } from '@playwright/test';

test('should display title', async ({ page }) => {
  await page.goto('https://example.com');
  await expect(page).toHaveTitle(/Example/);
});
```

### Interacción

```typescript
test('should login', async ({ page }) => {
  await page.goto('/login');
  await page.fill('#email', 'user@example.com');
  await page.fill('#password', 'password');
  await page.click('button[type="submit"]');
  await expect(page).toHaveURL('/dashboard');
});
```

### Selectors

```typescript
// Text
await page.click('text=Login');

// CSS
await page.click('.button-primary');

// Role
await page.click('role=button[name="Submit"]');

// Test ID
await page.click('[data-testid="login-button"]');
```

---

## API Testing

```typescript
import { test, expect } from '@playwright/test';

test('API test', async ({ request }) => {
  const response = await request.get('/api/users');
  expect(response.ok()).toBeTruthy();
  
  const users = await response.json();
  expect(users.length).toBeGreaterThan(0);
});
```

---

## Visual Testing

```typescript
test('visual regression', async ({ page }) => {
  await page.goto('/dashboard');
  await expect(page).toHaveScreenshot('dashboard.png');
});
```

---

## Resumen

- **Playwright** es ideal para testing multi-browser
- **Multi-lenguaje** flexibilidad
- **API + UI** testing integrado
- **Visual testing** para regresión visual

---

## Navegación

- **Anterior:** [02-cypress.md](02-cypress.md)
- **Siguiente:** [04-appium.md](04-appium.md)
- **Volver a Frameworks:** [README.md](README.md)
- **Volver al índice:** [MASTER-README.md](../MASTER-README.md)

---

*Archivo 3 - Playwright*
