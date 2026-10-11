---
name: manual-project-structure
description: Usa esta skill para crear y hacer respetar la estructura de carpetas estándar de MANUAL-TLC (PRJ-{proyecto}/{ambiente}/...) en todos los artefactos de pruebas manuales.
---

# MANUAL-PROJECT-STRUCTURE — Estructura de Carpetas del Proyecto

<role>

## Rol

Eres el guardián de la estructura de carpetas de MANUAL-TLC. Garantizas que:

1. La estructura estándar **se cree** al iniciar un ciclo de pruebas manuales.
2. **Todos** los artefactos (casos, datos, evidencia, resultados, análisis, defectos y documentos) se guarden **dentro** de esa estructura.
3. Ninguna fase ni skill escriba fuera de ella.

Esta skill es **PRIORITARIA y OBLIGATORIA**. Ninguna otra skill puede definir rutas propias.

</role>

<workflow>

## Estructura canónica

```
RootFolder/                                    ← raíz del workspace/repositorio
│
└── PRJ-{NombreProyecto}/                      ← un solo PRJ-* por proyecto o aplicación
    │
    └── {ambiente}/                            ← un subnivel por ambiente
        │
        ├── DOCs/
        │   └── {TipoDocumento}/               ← una carpeta por cada tipo de documento
        │
        ├── Test_Cases/
        │   ├── TestScript/                    ← casos de prueba ejecutables/manuales
        │   └── BDD/                           ← escenarios Gherkin
        │
        ├── Test_Results/
        │   └── {YYYY-MM-DD}/                  ← una carpeta por fecha de ejecución
        │
        ├── Test_Data/                         ← datos, cuentas y catálogo de selectores
        │
        ├── Test_Results_Analisis_&_RCA/
        │   └── {YYYY-MM-DD}/                  ← una carpeta por fecha de ejecución
        │
        └── Issues&Bugs/
            └── {YYYY-MM-DD}/                  ← una carpeta por fecha de ejecución
```

### Reglas estructurales duras

- Los nombres de carpeta del estándar **se escriben exactamente así**: `DOCs`, `Test_Cases`, `TestScript`, `BDD`, `Test_Results`, `Test_Data`, `Test_Results_Analisis_&_RCA`, `Issues&Bugs`.
- Prohibido crear variantes: `TestResults`, `test_results`, `Bugs`, `Issues`, `Analysis`, `Docs`, `TestScripts`, `TestScript/Manual` ❌.
- `RootFolder` es la raíz del workspace: **no** se crea una carpeta llamada "RootFolder".
- Los únicos elementos permitidos fuera de `PRJ-*` son los de configuración del agente: `.opencode/`, `AGENTS.md`, `opencode.json` y la carpeta `templates/` (plantillas obligatorias de casos de prueba, **solo lectura**).

### Plantillas obligatorias de casos de prueba (`templates/`)

Toda generación, creación o importación de casos de prueba **debe partir de las plantillas estándar** de la carpeta `templates/` en la raíz del repositorio:

| Plantilla | Uso | Destino del artefacto |
|---|---|---|
| `templates/tc_template.md` | Casos de prueba manuales/ejecutables | `Test_Cases/TestScript/TC-{TIPO}-{NNN}.md` |
| `templates/bdd_template.md` | Escenarios BDD/Gherkin | `Test_Cases/BDD/{modulo}.feature` (especificación Gherkin dentro de la plantilla) |
| `templates/tc_example.md` | Ejemplo resuelto de `tc_template.md` | Solo referencia — nunca se copia como caso real |

Reglas:
1. **Ningún caso se escribe desde cero**: se copia la plantilla correspondiente y se conserva su estructura completa de secciones (Propósito, Descripción, Data I/O, Precondiciones, Steps / Especificación Gherkin, Resultado Esperado, Observaciones generales, Postcondiciones / Limpieza, Flujo).
2. Los placeholders se reemplazan y los comentarios guía (`<!-- ... -->`) se eliminan en el artefacto final.
3. **Los casos importados** (Excel, documentos heredados, otros repositorios) **se normalizan a la plantilla** antes de guardarse en `Test_Cases/`; el formato externo nunca se acepta tal cual.
4. Las plantillas son **solo lectura**: nunca se modifican, renombran, mueven ni se copian dentro de `PRJ-*`.

## Convenciones de nombres

| Marcador | Regla | Ejemplo |
|---|---|---|
| `PRJ-{NombreProyecto}` | Prefijo literal `PRJ-` + nombre sin espacios ni acentos, PascalCase | `PRJ-CheckoutEcommerce`, `PRJ-PortalProveedores` |
| `{ambiente}` | Minúsculas de la lista controlada | `local`, `dev`, `qa`, `staging`, `preprod`, `prod` |
| `{TipoDocumento}` | PascalCase con guion bajo, del catálogo de tipos documentales | `Test_Plan`, `Test_Strategy`, `UAT` |
| `{YYYY-MM-DD}` | Fecha ISO de la **ejecución** (o de reporte del defecto) | `2026-09-21` |
| `{YYYY-MM-DD}_r{NN}` | Segunda y siguientes corridas del mismo día | `2026-09-21_r02` |
| `TC-{TIPO}-{NNN}` | Caso de prueba; TIPO ∈ `SMK`, `SAN`, `FUNC`, `SYS`, `REG`, `EXP`, `UAT` | `TC-FUNC-003` |
| `DEF-{NNNN}` | Defecto | `DEF-0341` |
| `S-{NN}` | Sesión exploratoria (SBTM) | `S-03` |

**Prohibido** en cualquier nombre: espacios, acentos, `#`, `?`, `*`, `<`, `>`, `|`, comillas y puntos suspensivos.

> El carácter `&` pertenece al estándar (`Test_Results_Analisis_&_RCA`, `Issues&Bugs`). En PowerShell hay que **entrecomillar** toda ruta que lo contenga: `Join-Path $base "Issues&Bugs/$fecha"`.

## Catálogo de tipos documentales (`DOCs/{TipoDocumento}`)

| TipoDocumento | Contenido |
|---|---|
| `Test_Plan` | Plan formal de pruebas (IEEE-829/ISTQB) y estado del plan (`plan.yaml`) |
| `Test_Strategy` | Estrategia, tipos de prueba, matriz de cobertura, priorización |
| `Requirements` | Requisitos, criterios de aceptación, alcance |
| `Test_Design` | Diseño de casos, técnicas aplicadas, matriz de trazabilidad |
| `Environment` | Configuración de entornos, URLs, accesos (sin credenciales), matriz de navegadores |
| `Session_Reports` | Reportes de sesión exploratoria (SBTM) |
| `UAT` | Guiones UAT, criterios de aceptación y actas de aceptación |
| `Sign_Off` | Aprobaciones, actas de cierre y firmas |
| `Metrics` | Tableros de métricas y KPIs por ciclo |
| `Manuals` | Manuales de usuario, guías de operación y de soporte |

El catálogo es **extensible**: se puede agregar un tipo nuevo sólo si ningún tipo existente lo cubre, respetando PascalCase con guion bajo. Las carpetas se crean **a demanda**, cuando se produce el primer documento de ese tipo.

## Mapa de artefactos → rutas

| Artefacto | Ruta canónica |
|---|---|
| Estado del plan activo | `PRJ-{proyecto}/{ambiente}/DOCs/Test_Plan/plan.yaml` |
| Plan de pruebas formal | `PRJ-{proyecto}/{ambiente}/DOCs/Test_Plan/Test_Plan_{proyecto}_{ambiente}_{YYYY-MM-DD}.md` |
| Estrategia y cobertura | `PRJ-{proyecto}/{ambiente}/DOCs/Test_Strategy/Test_Strategy_{YYYY-MM-DD}.md` |
| Requisitos y criterios | `PRJ-{proyecto}/{ambiente}/DOCs/Requirements/Requirements_{YYYY-MM-DD}.md` |
| Casos de prueba | `PRJ-{proyecto}/{ambiente}/Test_Cases/TestScript/TC-{TIPO}-{NNN}.md` |
| Índice de casos | `PRJ-{proyecto}/{ambiente}/Test_Cases/TestScript/README.md` |
| Escenarios BDD | `PRJ-{proyecto}/{ambiente}/Test_Cases/BDD/{modulo}.feature` |
| Cuentas y datos de prueba | `PRJ-{proyecto}/{ambiente}/Test_Data/accounts_{ambiente}.yaml`, `test_data_{modulo}.{ext}` |
| Configuración de sesión | `PRJ-{proyecto}/{ambiente}/Test_Data/session-config.yaml` |
| Catálogo de selectores (XPath) | `PRJ-{proyecto}/{ambiente}/Test_Data/Selectors/{modulo}.md` |
| Evidencia de la ejecución | `PRJ-{proyecto}/{ambiente}/Test_Results/{YYYY-MM-DD}/Evidence/{CASE-ID}/` |
| Resumen de ejecución | `PRJ-{proyecto}/{ambiente}/Test_Results/{YYYY-MM-DD}/Execution_Summary.yaml` |
| Reporte de sesión exploratoria | `PRJ-{proyecto}/{ambiente}/Test_Results/{YYYY-MM-DD}/Sessions/S-{NN}.md` |
| Análisis de resultados | `PRJ-{proyecto}/{ambiente}/Test_Results_Analisis_&_RCA/{YYYY-MM-DD}/Analysis_{YYYY-MM-DD}.md` |
| RCA por defecto | `PRJ-{proyecto}/{ambiente}/Test_Results_Analisis_&_RCA/{YYYY-MM-DD}/RCA_{DEF-NNNN}.md` |
| Reporte final | `PRJ-{proyecto}/{ambiente}/Test_Results_Analisis_&_RCA/{YYYY-MM-DD}/Test_Report_{proyecto}_{ambiente}_{YYYY-MM-DD}.md` |
| Documentación de métricas del ciclo | `PRJ-{proyecto}/{ambiente}/DOCs/Metrics/Metrics_{YYYY-MM-DD}.md` |
| Registro de defectos | `PRJ-{proyecto}/{ambiente}/Issues&Bugs/{YYYY-MM-DD}/Issues_Bugs_{YYYY-MM-DD}.md` |
| Evidencia propia de un defecto | `PRJ-{proyecto}/{ambiente}/Issues&Bugs/{YYYY-MM-DD}/{DEF-NNNN}/` |

**Regla de no duplicación**: la evidencia se guarda **una sola vez** en `Test_Results/{fecha}/Evidence/{CASE-ID}/` y los defectos y el análisis la **referencian por ruta relativa**. Sólo se copia a `Issues&Bugs/{fecha}/{DEF-NNNN}/` si la evidencia se genera después del cierre del ciclo.

## Procedimiento de creación (idempotente)

### Paso 1: Resolver los marcadores
- `{proyecto}` y `{ambiente}` provienen del intake (Fase 1). **Si faltan, no se inventan: se pregunta al usuario.**
- `{fecha}` = fecha de ejecución en formato `YYYY-MM-DD`.

### Paso 2: Crear la estructura base

```powershell
$proyecto = "{NombreProyecto}"      # sin "PRJ-" y sin espacios
$ambiente = "{ambiente}"            # local | dev | qa | staging | preprod | prod
$fecha    = "{YYYY-MM-DD}"

$base = Join-Path (Get-Location) (Join-Path "PRJ-$proyecto" $ambiente)

$carpetas = @(
  "Test_Cases/TestScript",
  "Test_Cases/BDD",
  "Test_Results/$fecha/Evidence",
  "Test_Results/$fecha/Sessions",
  "Test_Data",
  "Test_Data/Selectors",
  "Test_Results_Analisis_&_RCA/$fecha",
  "Issues&Bugs/$fecha"
)

foreach ($c in $carpetas) {
  New-Item -ItemType Directory -Force -Path (Join-Path $base $c) | Out-Null
}

Write-Output "Estructura lista en: $base"
```

`New-Item -Force` es idempotente: **nunca** borra ni sobrescribe, sólo crea lo que falta.

### Paso 3: Crear los tipos documentales a demanda

Cuando una fase produce un documento, crear su carpeta si no existe:

```powershell
$docType = "Test_Plan"              # del catálogo de tipos documentales
New-Item -ItemType Directory -Force -Path (Join-Path $base "DOCs/$docType") | Out-Null
```

### Paso 4: Confirmar la estructura al usuario

Informar la ruta raíz creada y el listado de carpetas, para que quede explícito dónde se guardará todo.

## Verificación y gate de cumplimiento

### Antes de escribir cualquier artefacto

1. Verificar que `{proyecto}` y `{ambiente}` estén resueltos.
2. Verificar que exista la carpeta destino; si no existe, crearla (idempotente).
3. Verificar que la ruta destino esté **dentro** de `PRJ-{proyecto}/{ambiente}/`.

### Script de verificación de la estructura

```powershell
$proyecto = "{NombreProyecto}"
$ambiente = "{ambiente}"
$base = Join-Path (Get-Location) "PRJ-$proyecto/$ambiente"

$requeridas = @(
  "DOCs",
  "Test_Cases",
  "Test_Cases/TestScript",
  "Test_Cases/BDD",
  "Test_Results",
  "Test_Data",
  "Test_Data/Selectors",
  "Test_Results_Analisis_&_RCA",
  "Issues&Bugs"
)

$faltantes = $requeridas | Where-Object { -not (Test-Path (Join-Path $base $_)) }
if ($faltantes) {
  Write-Output "ESTRUCTURA INCOMPLETA - faltan: $($faltantes -join ', ')"
} else {
  Write-Output "ESTRUCTURA COMPLETA - OK ($base)"
}
```

### Detector de desviaciones (artefactos fuera del estándar)

```powershell
$permitidos = @('AGENTS.md','opencode.json','.opencode','.git','.gitignore','node_modules')
Get-ChildItem -Force | Where-Object {
  $permitidos -notcontains $_.Name -and -not $_.Name.StartsWith('PRJ-')
} | Select-Object -ExpandProperty Name
```

Si este comando devuelve algo, hay **deriva estructural**: migrar el contenido a `PRJ-{proyecto}/{ambiente}/` y eliminar la carpeta suelta.

## Integración con las fases

| Fase | Responsabilidad |
|---|---|
| **1. Intake** | Obtener `{proyecto}` y `{ambiente}` (bloqueante) y **crear la estructura** |
| **2. Diagnostics** | Verificar que la estructura exista y sea escribible; reportar como riesgo si no lo es |
| **3. Procedure Plan** | Declarar en `evidence_plan` y `test_data_strategy` las rutas canónicas |
| **4. Test Plan** | Escribir en `DOCs/Test_Plan/` y `DOCs/Test_Strategy/` |
| **5. Execution** | Escribir casos en `Test_Cases/`, datos en `Test_Data/` y evidencia en `Test_Results/{fecha}/Evidence/` |
| **6. Analysis** | Escribir en `Test_Results_Analisis_&_RCA/{fecha}/` y defectos en `Issues&Bugs/{fecha}/` |

## Ejemplo completo de árbol resultante

```
PRJ-CheckoutEcommerce/
└── qa/
    ├── DOCs/
    │   ├── Test_Plan/
    │   │   ├── plan.yaml
    │   │   └── Test_Plan_CheckoutEcommerce_qa_2026-09-21.md
    │   ├── Test_Strategy/
    │   │   └── Test_Strategy_2026-09-21.md
    │   └── UAT/
    │       └── Guion_UAT_Checkout_2026-09-21.md
    ├── Test_Cases/
    │   ├── TestScript/
    │   │   ├── README.md
    │   │   ├── TC-SMK-001.md
    │   │   ├── TC-FUNC-003.md
    │   │   └── TC-REG-008.md
    │   └── BDD/
    │       └── checkout.feature
    ├── Test_Results/
    │   └── 2026-09-21/
    │       ├── Evidence/
    │       │   ├── TC-FUNC-003/TC-FUNC-003-paso3-20260921T1042.png
    │       │   └── TC-REG-008/TC-REG-008-paso2-20260921T1105.png
    │       ├── Sessions/
    │       │   └── S-03.md
    │       └── Execution_Summary.yaml
    ├── Test_Data/
    │   ├── accounts_qa.yaml
    │   ├── session-config.yaml
    │   ├── test_data_checkout.json
    │   └── Selectors/
    │       └── checkout.md
    ├── Test_Results_Analisis_&_RCA/
    │   └── 2026-09-21/
    │       ├── Analysis_2026-09-21.md
    │       ├── RCA_DEF-0341.md
    │       └── Test_Report_CheckoutEcommerce_qa_2026-09-21.md
    └── Issues&Bugs/
        └── 2026-09-21/
            ├── Issues_Bugs_2026-09-21.md
            └── DEF-0341/
                └── evidence-console-20260921T1042.log
```

</workflow>

<rules>

## Reglas de cumplimiento

1. **La estructura se crea al inicio del ciclo** (Fase 1) y antes de escribir cualquier artefacto.
2. **Todo** artefacto de MANUAL-TLC vive dentro de `PRJ-{proyecto}/{ambiente}/`. Ninguna fase inventa rutas propias.
3. Los nombres de las carpetas del estándar **no se alteran, no se traducen y no se renombran**.
4. Si `{proyecto}` o `{ambiente}` no están definidos, **se pregunta al usuario**; no se generan valores por defecto inventados.
5. La creación es **idempotente**: se usa `New-Item -Force` y nunca se borra ni se sobrescribe contenido existente.
6. Antes de escribir, se crea la carpeta destino si falta. Nunca se asume que existe.
7. Los tipos documentales nuevos deben justificarse (que ningún tipo existente los cubra) y respetar PascalCase con guion bajo.
8. Toda fecha en nombres de carpeta es **ISO `YYYY-MM-DD`**; varias corridas del mismo día usan el sufijo `_r{NN}`.
9. La evidencia **no se duplica**: se guarda una vez y se referencia por ruta relativa.
10. Si aparece una ruta heredada (`docs/`, `tests/`, `evidence/` en la raíz), se migra el contenido a la estructura y se elimina la carpeta suelta.
11. No se crean carpetas vacías "por si acaso": los tipos documentales y los subniveles de fecha se crean cuando se necesitan.
12. Las únicas excepciones fuera de `PRJ-*` son `.opencode/`, `AGENTS.md`, `opencode.json` y la carpeta `templates/` (plantillas obligatorias de casos de prueba, solo lectura).

## Antipatrones

| Antipatrón | Por qué está mal | Corrección |
|---|---|---|
| `docs/manual-test-plan.md` | Ruta suelta fuera del estándar | `DOCs/Test_Plan/Test_Plan_{...}.md` |
| `tests/manual/evidence/` | Ruta heredada, no pertenece al estándar | `Test_Results/{fecha}/Evidence/` |
| `PRJ-x/qa/TestResults/` | Variante en CamelCase | `Test_Results/` |
| `PRJ-x/Produccion/` | Ambiente inventado y acentuado | `prod` |
| `PRJ-x/qa/Bugs/` | Carpeta del estándar renombrada | `Issues&Bugs/` |
| `PRJ-x/qa/Test_Results/21-09-2026/` | Fecha no ISO | `2026-09-21/` |
| `PRJ-x/qa/Test_Data/creds.txt` | Credenciales en el repositorio | Variables de entorno o gestor de secretos |
| Crear todas las carpetas de fecha del año | Ruido y carpetas vacías | Crear la fecha al ejecutar |
| Duplicar evidencia en `Issues&Bugs` y `Test_Results` | Dos fuentes de verdad | Referenciar por ruta relativa |
| Escribir un caso de prueba sin partir de `templates/tc_template.md` o `templates/bdd_template.md` | Caso fuera del estándar, con secciones incompletas | Copiar la plantilla y completarla |
| Copiar las plantillas dentro de `PRJ-*` o modificar `templates/` | Se rompe la única fuente de verdad de casos | Las plantillas viven solo en `templates/` y son de solo lectura |

</rules>
