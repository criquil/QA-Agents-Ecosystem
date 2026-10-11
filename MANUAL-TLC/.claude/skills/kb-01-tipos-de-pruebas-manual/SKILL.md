---
name: kb-01-tipos-de-pruebas-manual
description: Skill autónoma de conocimiento sobre los tipos de pruebas manuales: funcionales, sistema, regresión, smoke, sanity, exploratorias y aceptación. No depende de archivos externos.
---

# Tipos de Pruebas Manuales

Los siete tipos que cubre MANUAL-TLC v1.0, con su objetivo, alcance y criterio de salida.

## 1. Pruebas Funcionales

**Objetivo:** verificar que cada función cumple su requisito funcional.

**Alcance:** cada pantalla, campo, botón y regla de negocio visible al usuario.

**Casos típicos:**
- Flujo feliz por cada requisito (crear, consultar, editar, eliminar).
- Validaciones de formulario: obligatorios, formato, longitud, rangos.
- Filtros, ordenamientos, paginación y búsqueda.
- Reglas de negocio (descuentos, cupones, límites, estados).
- Persistencia del dato tras guardar, recargar y volver a entrar.
- Roles y visibilidad de acciones por perfil.

**Criterio de salida:** 100% de casos ejecutados; ≥ 95% PASS; evidencia por caso.

---

## 2. Pruebas de Sistema (System Testing)

**Objetivo:** validar el sistema completo e integrado contra los requisitos de sistema.

**Alcance:** flujos end-to-end que atraviesan varios módulos, roles y servicios.

**Casos típicos:**
- Alta de cliente → alta de producto → compra → pago → facturación → notificación.
- Flujos que cruzan módulos con distintos permisos.
- Coherencia de datos entre módulos (lo vendido aparece en el inventario y en el reporte).
- Comportamiento del sistema ante una dependencia externa caída.
- Estados globales: sesión expirada a mitad de un flujo, timeout, error transversal.

**Criterio de salida:** todos los flujos críticos ejecutados de punta a punta sin bloqueantes.

---

## 3. Pruebas de Regresión

**Objetivo:** confirmar que los cambios no rompieron funcionalidad previamente validada.

**Alcance:** suite congelada de casos estables y representativos (P1 y P2 principalmente).

**Casos típicos:**
- Repetición exacta de casos ya validados, con los mismos datos y el mismo rol.
- Comparación de resultado contra el baseline del ciclo anterior.
- Re-ejecución de casos ligados a defectos ya corregidos.

**Criterio de salida:** 0 regresiones P1/P2 abiertas.

---

## 4. Smoke Testing

**Objetivo:** gate mínimo de aceptación del build — ¿el sistema es testeable?

**Alcance:** amplio y superficial. Pocos casos, las pantallas y flujos vitales.

**Casos típicos:**
- La aplicación carga y responde.
- El login funciona con cada rol principal.
- El menú principal y las pantallas clave abren sin error.
- Una operación de escritura básica se puede completar.

**Criterio de salida:** 100% PASS. Si el smoke falla, se detiene todo el ciclo.

---

## 5. Sanity Testing

**Objetivo:** verificación estrecha y profunda de un fix o cambio puntual.

**Alcance:** el módulo afectado y sus dependencias inmediatas.

**Casos típicos:**
- Reproducir el defecto reportado y confirmar que ya no ocurre.
- Ejecutar las variantes cercanas al defecto (el mismo campo, otros valores límite).
- Confirmar que el fix no rompió la función directamente relacionada.

**Criterio de salida:** fix verificado y sin regresión directa. No sustituye a la regresión.

---

## 6. Pruebas Exploratorias

**Objetivo:** aprender, diseñar y ejecutar simultáneamente para descubrir lo no anticipado.

**Alcance:** dirigido por **charters** (área + recursos + riesgo a descubrir) y **timeboxeado**.

**Casos típicos:**
- Módulos nuevos, recién integrados o inestables.
- Áreas con requisitos ambiguos o incompletos.
- Comportamientos no documentados: interrupciones, doble submit, sesión expirada.
- Combinaciones de datos, roles y estados poco probables.

**Criterio de salida:** charters ejecutados, reporte SBTM por sesión, hallazgos registrados.

---

## 7. Pruebas de Aceptación (UAT)

**Objetivo:** validación del negocio contra los criterios de aceptación.

**Alcance:** escenarios de negocio end-to-end, ejecutados o conducidos por el usuario de negocio.

**Casos típicos:**
- Cada criterio de aceptación firmado previamente.
- Escenarios reales de operación diaria del negocio.
- Verificación de reportes, comprobantes y notificaciones.

**Criterio de salida:** aceptación formal (Aceptado / Aceptado con condiciones / Rechazado).

---

## Tabla comparativa

| Tipo | Amplitud | Profundidad | Momento | Ejecutor |
|---|---|---|---|---|
| Smoke | Amplia | Superficial | Al recibir el build | QA |
| Sanity | Estrecha | Profunda | Tras un fix | QA |
| Funcionales | Media | Profunda | Durante el ciclo | QA |
| Sistema | Amplia | Profunda | Al integrar | QA |
| Regresión | Amplia | Media | Antes del release | QA |
| Exploratorias | Variable | Variable | Continuo | QA |
| UAT | Media | Profunda (negocio) | Previo al release | Negocio |
