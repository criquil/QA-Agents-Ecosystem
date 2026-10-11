---
name: automation-assets
description: "Catalogo y reuso de activos de automatizacion: registro de Page Objects, helpers, datasets y selectores validados, mas captura de lecciones aprendidas. Invocar al inicio (reuso antes que creacion) y al cierre de cada ciclo."
---

# Automation Assets — Catalogo, Reuso y Memoria

> **Principio**: reuso antes que creacion. Un activo reutilizado es un activo que nadie tiene que volver a depurar.

## Dos modos

| Modo | Cuando | Accion |
|---|---|---|
| **Discovery** | Antes de crear cualquier artefacto | Buscar activo equivalente |
| **Capture** | Despues de generar o resolver un fallo | Registrar el activo o la leccion |

## Discovery — antes de crear

Decision en orden. No saltear directo a "crear".

```
1. REUSE   -> ¿Ya existe y serve tal cual?          Usar.
2. EXTEND  -> ¿Existe algo parecido que pueda ampliar?  Extender.
3. CREATE  -> ¿No hay nada equivalente?               Crear, y capturar.
```

### Donde buscar

| Tipo de activo | Donde |
|---|---|
| Page Object | `pages/**/<Modulo>Page.ts` |
| Selector validado | `automation-plans/*/selectors.md` |
| Helper / utilidad | `helpers/` |
| Datos de prueba | `data/` y `data/cases/` |
| Patron reutilizable | `docs/knowledge/Automation_QA/Strategy/Troubleshooting/` |
| Boilerplate | `docs/knowledge/Automation_QA/Strategy/Boilerplate/` |

```bash
grep -r "ingresarUsuario" pages/ --include=*.ts
grep -r "xpath=//\*\[@id=\"login" tests/ automation-plans/ --include=*.ts --include=*.md
```

Si el resultado no esta vacio, **no crear**. Extender el activo existente.

## Capture — que registrar

### 1. Activos creados

```markdown
### Page Object — LoginPage
- Ruta: pages/Login/LoginPage.ts
- Modulo: Login
- Selectores: 4 (validados 2026-01-15 con DevTools MCP)
- Tests que lo usan: test_login.spec.ts
- Reutilizable en: cualquier flujo que autenticacion con usuario/clave
```

### 2. Selectores validados

Tabla acumulativa, la mas consultada del proyecto:

| Elemento | Modulo | Selector | Fecha | Notas |
|---|---|---|---|---|
| Input usuario | Login | `xpath=//*[@id="username"]` | 2026-01-15 | unico en el DOM |
| Btn ingresar | Login | `xpath=//button[@id="actionButtonIngresar"]` | 2026-01-15 | dentro de `#login-form` |

Un selector validado no se vuelve a capturar. Es el activo mas barato de reusar.

### 3. Lecciones aprendidas

Solo lo que **no es obvio**. Registrar la causa raiz, no el sintoma.

```markdown
### Leccion — dropdowns Select2
- Sintoma: timeout de 20 s al seleccionar opciones
- Causa: el widget Select2 ignora selectOption; requiere simulacion de usuario
- Fix: patron click + type + Enter
- Impacto: 12 dropdowns, 92 s -> 31 s
- Aplicar a: cualquier <select> con clase select2
```

Criterio de inclusion: si el mismo error vuelve a aparecer en otro proyecto, la leccion vale.
Si solo servio para ese archivo, no.

### 4. Salud de la suite

| Metrica | Como se mide | Objetivo |
|---|---|---|
| Tasa de tests flaky | tests que pasan en el reintento / total | < 2% |
| Duracion de smoke | tiempo del stage de smoke | < 5 min |
| Selectores sin validar | grep de `TODO` en `pages/` | 0 |
| Datos hardcodeados | grep de literales en `tests/` | 0 |
| Tests sin tags | `--list` cruzado con los filtros del pipeline | 0 |
| Reutilizacion |(Page Objects usados / creados) | > 2 |

## Reporte de cierre de ciclo

```markdown
## Ciclo [ID] — [funcionalidad]

### Activos
- Creados: N Page Objects, M helpers, K datasets
- Extendidos: X activos existentes (en lugar de crear)
- Reusados en otros modulos: Y

### Selectores
- Capturados y validados: N
- Reutilizados del catalogo: M

### Lecciones
- Registradas: Z

### Salud
- Tests nuevos: N, pasando: N/N
- Flakiness detectada: N
- Deuda cerrada: ...

### Deuda abierta
- Selectores pendientes de revalidar por cambio de UI
- Tests marcados @wip y su fecha de revision
```

## Checklist de fin de ciclo

- [ ] Page Objects nuevos registrados en el catalogo
- [ ] Selectores validados agregados a la tabla
- [ ] Lecciones no obvias documentadas con causa raiz
- [ ] Metricas de salud actualizadas
- [ ] Deuda abierta explicitada con fecha de revision
- [ ] Todo `@wip` tiene fecha de compromiso

## Lectura bajo demanda

Este SKILL.md ya define el flujo Discovery/Capture y las metricas de salud.

| Si el SKILL.md no alcanza y necesitás | Leé |
|---|---|
| Buscar activos existentes en el proyecto | `grep -rn "<termino>" pages/ data/ helpers/` — no leas los directorios |
| Patrones reutilizables | `docs/knowledge/Automation_QA/Strategy/Troubleshooting/README.md` |
| Metricas de mantenimiento de la suite | `docs/knowledge/Automation_QA/06-mejores-practicas/` |

**Stop**: la tabla de este SKILL.md es el indice. Para localizar algo concreto, `grep` primero; nunca recorrer `pages/` ni `data/` leyendo archivo por archivo.

---

*Automation Assets — reuso antes que creacion. Platform: OpenCode.*