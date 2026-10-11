# GitHub Actions

> **Archivo:** 2 de 2 | **Sección:** CI/CD | **Nivel:** Intermedio

---

## Definición

**GitHub Actions** es la plataforma CI/CD nativa de GitHub, integrada directamente con repositorios.

## Workflow Example

### .github/workflows/test.yml

```yaml
name: Test Suite

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          
      - name: Install dependencies
        run: npm ci
        
      - name: Run tests
        run: npm test
        
      - name: Upload report
        uses: actions/upload-artifact@v3
        if: always()
        with:
          name: allure-report
          path: allure-results/
          
      - name: Deploy report
        uses: peaceiris/actions-gh-pages@v3
        if: github.ref == 'refs/heads/main'
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./allure-report
```

## Ventajas

- ✅ Nativo de GitHub
- ✅ Gratis para repos públicos
- ✅ Marketplace de actions
- ✅ Matrix builds

## Resumen

- **GitHub Actions** es ideal para proyectos en GitHub
- **YAML** para definir workflows
- **Marketplace** para actions reutilizables

---

## Navegación

- **Anterior:** [01-jenkins.md](01-jenkins.md)
- **Volver a CI/CD:** [README.md](README.md)
- **Siguiente Sección:** [06-mejores-practicas/](../06-mejores-practicas/README.md)
- **Volver al índice:** [MASTER-README.md](../MASTER-README.md)

---

*Archivo 2 - GitHub Actions*
