---
name: automation-tagging
description: "Categorizacion de tests: los 4 tags obligatorios, tags opcionales y ejecucion selectiva por filtro. Invocar al crear tests, al conectarlos a un pipeline o cuando un test no se ejecuta en CI."
---

# Automation Tagging — Categorizacion

> **Por que importa**: los pipelines filtran por tags. Un test sin tags correctos **no se ejecuta nunca**. No es un problema de estilo, es funcional.

## Los 4 tags obligatorios

Todo test debe tener estos cuatro. Sin excepcion.

| # | Tag | Valores | Que habilita |
|---|---|---|---|
| 1 | `@project` | nombre del proyecto | Filtro en repos compartidos |
| 2 | `@environment` | `dev` `qa` `uat` `prod` | Decide en que entorno corre |
| 3 | `@functionality` | lowercase del modulo | Deploy selectivo por funcionalidad |
| 4 | `@specific_case` | `{funcionalidad}_{variante}` | Debug granular de un caso |

```typescript
test('transferencia con saldo insuficiente', {
  tag: ['@bank-app', '@qa', '@transfer', '@transfer_saldo_insuficiente']
}, async ({ page }) => { /* ... */ });
```

## Que pasa sin cada tag

| Tag ausente | Consecuencia concreta |
|---|---|
| `@project` | El filtro de repositorio compartido no encuentra el test |
| `@environment` | **El test no corre en ningun entorno** |
| `@functionality` | Imposible hacer deploy parcial por funcionalidad |
| `@specific_case` | No se puede aislar el caso para depurar |

## Tags opcionales

Controlan la ejecucion por stage sin cambiar el codigo.

| Tag | Significado | Uso tipico |
|---|---|---|
| `@smoke` | Camino critico, rapido | En cada commit |
| `@regression` | Regresion completa | Nightly o semanal |
| `@critical` | Bloquea deploy si falla | Gate de produccion |
| `@slow` | Lento, excluido de corridas rapidas | Fuera del smoke |
| `@wip` | En desarrollo, no ejecutar | Evita ruido en el pipeline |
| `@skip` | Deshabilitado temporalmente | Test roto conocido |

## Ejecucion selectiva

```bash
# Por ambiente
npx playwright test --grep "@qa"
npx playwright test --grep "@prod"

# Por criticidad
npx playwright test --grep "@smoke and not @slow"
npx playwright test --grep "@critical and @prod"

# Por funcionalidad (deploy parcial)
npx playwright test --grep "@transfer and @prod"
npx playwright test --grep "@login and not @wip"

# Suite completa de regresion
npx playwright test --grep "@regression and not @slow"
```

## Verificacion obligatoria

Despues de crear un test, comprobar que el filtro lo encuentra:

```bash
npx playwright test --grep "@transfer_saldo_insuficiente" --list
```

Si `--list` no devuelve el test, **el tag esta mal escrito** y en el pipeline no se ejecutara.
Esta verificacion es parte del checklist, no opcional.

## Como se declaran

```typescript
// Playwright — recommended
test('titulo', { tag: ['@bank-app', '@qa', '@login', '@login_exitoso', '@smoke'] }, fn);

// Alternativa con anotaciones
test('titulo', {
  annotations: [
    { type: 'project',     description: 'bank-app' },
    { type: 'environment', description: 'qa' },
    { type: 'feature',     description: 'login' },
    { type: 'case',        description: 'login_exitoso' }
  ]
}, fn);
```

## Reglas de escritura

### Obligatorio

1. Los 4 tags obligatorios en todo test.
2. `@project` identico en todos los tests del proyecto.
3. `@environment` de la lista cerrada `dev|qa|uat|prod`.
4. `@functionality` en `kebab-case` o `lowercase`.
5. `@specific_case` con formato `{funcionalidad}_{variante}`, unico por caso.
6. Verificar con `--list` que el filtro encuentra el test.

### Prohibido

1. Tags genericos o ambiguos: `@test1`, `@prueba`, `@nuevo`.
2. Espacios en el nombre del tag.
3. Mayusculas en los tags.
4. Tags duplicados en el mismo test.
5. Omitir `@environment`.

## Checklist

- [ ] Los 4 tags obligatorios presentes
- [ ] `@project` correcto y uniforme
- [ ] `@environment` de la lista cerrada
- [ ] `@functionality` descriptiva y en minusculas
- [ ] `@specific_case` unica y con formato `{funcionalidad}_{variante}`
- [ ] Tags opcionales agregados segun criticidad (`@smoke`, `@critical`, `@slow`)
- [ ] `npx playwright test --grep "<tag>" --list` devuelve el test

## Lectura bajo demanda

Este SKILL.md ya trae los 4 tags obligatorios, los opcionales y los filtros de ejecucion.

| Si el SKILL.md no alcanza y necesitás | Leé |
|---|---|
| Catalogo completo de tags y uso en pipeline | `docs/knowledge/Automation_QA/Strategy/Test_Categorization/README.md` |
| Donde se aplica cada filtro | `.opencode/skills/automation-cicd/SKILL.md` |

Localiza la seccion antes de leer: `grep -n "^## " <archivo>`

**Stop**: para escribir los tags de un test, aca alcanza. No abras el catalogo.

---

*Automation Tagging — sin tags, no hay ejecucion. Platform: OpenCode.*