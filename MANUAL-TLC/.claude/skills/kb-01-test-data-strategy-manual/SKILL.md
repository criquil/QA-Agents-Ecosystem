---
name: kb-01-test-data-strategy-manual
description: Skill autónoma de conocimiento sobre test data management para pruebas manuales. No depende de archivos externos.
---

# Test Data Management para Pruebas Manuales

## Estrategias de Datos

### 1. Datos semilla (seeds)
Estado conocido y repetible cargado antes del ciclo.

**Ventajas:** resultados comparables entre ciclos, base para la regresión.
**Riesgos:** acoplamiento al proceso de carga; se desactualiza si el modelo cambia.

### 2. Catálogo de cuentas por rol
Un usuario por rol (admin, operador, cliente, auditor) con permisos y datos asociados.

**Ventajas:** permite validar autorización y visibilidad desde el primer caso.
**Riesgos:** cuentas que caducan, se bloquean o acumulan datos de sesiones previas.

### 3. Datos creados en la sesión
El propio tester crea el dato que necesita (cliente nuevo, pedido nuevo).

**Ventajas:** no depende de datos preexistentes, refleja el uso real.
**Riesgos:** consume tiempo de sesión y requiere cleanup posterior.

### 4. Datos sintéticos
Datos generados para cubrir casos límite (nombres largos, caracteres especiales, montos extremos).

**Ventajas:** cubre límites difíciles de encontrar en datos reales.
**Riesgos:** puede no reflejar la distribución real de los datos de negocio.

### 5. Datos anonimizados de producción
Copia con PII enmascarada.

**Ventajas:** realismo y volumen representativo.
**Riesgos:** proceso de anonimización incompleto o desactualizado.

## Datos por tipo de prueba

| Tipo | Necesidad de datos |
|---|---|
| Smoke | Un usuario por rol y una entidad mínima que exista |
| Sanity | El dato exacto que disparaba el defecto |
| Funcionales | Datos variados por regla de negocio y por validación |
| Sistema | Datos que atraviesan todos los módulos del flujo |
| Regresión | Mismos datos del baseline (indispensable para comparar) |
| Exploratorias | Datos raros, extremos y combinaciones inusuales |
| UAT | Datos realistas del negocio, provistos o aprobados por el negocio |

## Casos límite obligatorios

```
Texto    : vacío, un carácter, máximo permitido, máximo+1, con acentos, con emojis, con <script>
Números  : 0, negativo, mínimo, máximo, máximo+1, decimales, notación científica
Fechas   : hoy, pasado, futuro lejano, formato distinto, fecha inválida, zona horaria
Listas   : vacía (0), con un elemento, con el máximo permitido, con máximo+1
Archivos : sin archivo, formato inválido, tamaño máximo, tamaño máximo+1, nombre con caracteres especiales
```

## Mejores Prácticas

1. **Separar datos de casos** — el caso referencia el dato, no lo embebe.
2. **Versionar el catálogo** — cuentas y datos semilla en `PRJ-{proyecto}/{ambiente}/Test_Data/`.
3. **Resetear antes del ciclo** — un entorno con datos residuales produce falsos positivos.
4. **Cleanup después de la sesión** — dejar el entorno como estaba o mejor documentado.
5. **No usar datos reales de clientes** sin anonimización aprobada.
6. **Registrar el dato usado** en el caso ejecutado: es lo que hace reproducible el resultado.
7. **Un dato, un propósito** — evitar cadenas de dependencia entre casos.

## Riesgos típicos

| Riesgo | Consecuencia | Mitigación |
|---|---|---|
| Cuenta de prueba bloqueada | Casos BLOCKED | Cuentas alternas registradas en el catálogo |
| Datos residuales | Falsos positivos y duplicados | Reset del entorno antes del ciclo |
| PII en el entorno de pruebas | Incumplimiento de privacidad | Anonimización y enmascarado |
| Dato caducado o inconsistente | Defecto fantasma | Datos semilla versionados y validados |
| Datos no compartidos con negocio | UAT con datos irreales | Datos de UAT definidos junto al negocio |
