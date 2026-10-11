# Cypress

> **Archivo:** 2 de 4 | **Sección:** Frameworks | **Nivel:** Intermedio

---

## Tabla de Contenidos

1. [Visión General](#visión-general)
2. [Características](#características)
3. [Instalación](#instalación)
4. [Ejemplos](#ejemplos)
5. [Comandos Custom](#comandos-custom)
6. [Cypress Dashboard](#cypress-dashboard)
7. [Resumen](#resumen)

---

## Visión General

**Cypress** es un framework de testing moderno diseñado para desarrolladores front-end. Ejecuta tests en el mismo ciclo de vida que la aplicación.

### Características

- ✅ Time-travel debugging
- ✅ Automatic waiting
- ✅ Screenshots y videos
- ✅ Network traffic control
- ✅ Real browser testing
- ✅ Chrome DevTools integration

---

## Características

### vs Selenium

| Característica | Cypress | Selenium |
|----------------|---------|----------|
| **Arquitectura** | In-browser | Out-of-browser |
| **Ejecución** | Síncrona | Asíncrona |
| **Debugging** | Time-travel | Console logs |
| **Waiting** | Automático | Manual |
| **Network** | Intercept | Proxy |
| **Setup** | Mínimo | Configuración |

---

## Instalación

```bash
# npm
npm install cypress --save-dev

# yarn
yarn add cypress --dev

# Abrir Cypress
npx cypress open
```

### Estructura

```
cypress/
├── e2e/                    # Tests
│   ├── login.cy.js
│   └── dashboard.cy.js
├── fixtures/               # Test data
│   └── users.json
├── support/                # Commands
│   ├── commands.js
│   └── e2e.js
├── downloads/
└── screenshots/
```

---

## Ejemplos

### Test Básico

```javascript
describe('Login', () => {
  it('should login successfully', () => {
    cy.visit('/login');
    cy.get('#email').type('user@example.com');
    cy.get('#password').type('password');
    cy.get('button[type="submit"]').click();
    cy.url().should('include', '/dashboard');
  });
});
```

### assertions

```javascript
// Element assertions
cy.get('.title').should('be.visible');
cy.get('.title').should('have.text', 'Welcome');
cy.get('.title').should('contain', 'Welcome');
cy.get('input').should('have.value', 'John');

// Length assertions
cy.get('.items').should('have.length', 5);

// Class assertions
cy.get('.button').should('have.class', 'active');

// Property assertions
cy.get('.link').should('have.attr', 'href', '/about');
```

---

## Comandos Custom

### Definición

```javascript
// support/commands.js
Cypress.Commands.add('login', (email, password) => {
  cy.visit('/login');
  cy.get('#email').type(email);
  cy.get('#password').type(password);
  cy.get('button[type="submit"]').click();
});

Cypress.Commands.add('createUser', (user) => {
  cy.request('POST', '/api/users', user);
});
```

### Uso

```javascript
it('should access dashboard', () => {
  cy.login('user@example.com', 'password');
  cy.url().should('include', '/dashboard');
});
```

---

## Cypress Dashboard

### Configuración

```javascript
// cypress.config.js
module.exports = defineConfig({
  projectId: 'your-project-id',
  video: true,
  screenshotOnRunFailure: true,
});
```

### Reportes

```bash
# Subir a Dashboard
cypress run --record --key your-key

# Ver reportes
open https://dashboard.cypress.io
```

---

## Resumen

- **Cypress** es ideal para frontend testing
- **Time-travel debugging** para desarrollo
- **Automatic waiting** reduce flakiness
- **Dashboard** para reportes y monitoreo

---

## Navegación

- **Anterior:** [01-selenium.md](01-selenium.md)
- **Siguiente:** [03-playwright.md](03-playwright.md)
- **Volver a Frameworks:** [README.md](README.md)
- **Volver al índice:** [MASTER-README.md](../MASTER-README.md)

---

*Archivo 2 - Cypress*
