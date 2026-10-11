# TC-01: Verificar garantías parciales vencidas no habilitan límite

## Propósito

Verificar que las garantías parciales vencidas sin check *no habilitan* límite de crédito para el cliente en el sistema SCACS.

## Descripción

El caso navega por SCACS desde el login hasta la sección de Límites Vigentes de una solicitud preaprobada en estado "Calificada". Se aplica un flujo de búsqueda por documento del cliente, se filtran las propuestas por flujo "Solicitud Preaprobada" y estado "Calificada", se ingresa al detalle de la solicitud y se valida que el monto habilitado sea 0,00, confirmando que las garantías parciales vencidas sin check no generan habilitación de límite.

## Data Input / Output

| Tipo | Campo | Descripción |
|------|-------|-------------|
| Input | url | URL de acceso a SCACS |
| Input | usuario | Credencial de usuario para login |
| Input | password | Credencial de contraseña para login |
| Input | nroDocumento | Número de documento del cliente |
| Output | montoHabilitado | Valor de "Habilitado" en Límites Vigentes |
| Output | resultado | Estado de la prueba: Pass / Fail |

---

## Steps

### 1. Navegar a SCACS

| Step | Title | Description | Expected Result | Data Input | Data Output |
|------|-------|-------------|-----------------|------------|-------------|
| 1.1 | Abrir navegador | Iniciar el navegador web | Navegador abierto | — | Instancia del navegador |
| 1.2 | Ir a URL de SCACS | Navegar a la dirección de la app | Se carga página de login | url | Página de login visible |

---

### 2. Iniciar sesión

| Step | Title | Description | Expected Result | Data Input | Data Output |
|------|-------|-------------|-----------------|------------|-------------|
| 2.1 | Completar usuario | Ingresar nombre de usuario | Campo completado | usuario | Campo con valor |
| 2.2 | Completar contraseña | Ingresar contraseña | Campo completado | password | Campo con valor |
| 2.3 | Click en LOGIN | Presionar botón de inicio | Pantalla principal visible | — | Sesión activa |

---

### 3. Navegar a Búsqueda de Propuestas

| Step | Title | Description | Expected Result | Data Input | Data Output |
|------|-------|-------------|-----------------|------------|-------------|
| 3.1 | Abrir menú lateral | Click en ícono hamburguesa | Menú desplegado | — | Menú visible |
| 3.2 | Seleccionar Búsqueda | Click en "Búsqueda de Propuestas" | Pantalla de búsqueda abierta | — | Pantalla visible |

---

### 4. Abrir panel de filtros

| Step | Title | Description | Expected Result | Data Input | Data Output |
|------|-------|-------------|-----------------|------------|-------------|
| 4.1 | Expandir filtros | Click en "Rueda Filtro Propuestas" | Panel de filtros desplegado | — | Panel expandido |

---

### 5. Buscar cliente por documento

| Step | Title | Description | Expected Result | Data Input | Data Output |
|------|-------|-------------|-----------------|------------|-------------|
| 5.1 | Abrir buscador | Click en "Lupa para buscar Cliente" | Modal de búsqueda abierto | — | Modal visible |
| 5.2 | Ingresar documento | Completar "Número Documento" | Campo completado | nroDocumento | Campo con valor |
| 5.3 | Ejecutar búsqueda | Click en "Buscar" | Resultados en tabla | — | Tabla de resultados |
| 5.4 | Seleccionar cliente | Click en primera fila | Cliente seleccionado | — | Cliente seleccionado |

---

### 6. Aplicar filtro de Flujo

| Step | Title | Description | Expected Result | Data Input | Data Output |
|------|-------|-------------|-----------------|------------|-------------|
| 6.1 | Seleccionar flujo | En "Flujo" elegir "Solicitud Preaprobada" | Flujo filtrado | Flujo = "Solicitud Preaprobada" | Campo filtrado |
| 6.2 | Ejecutar búsqueda | Click en "Buscar" | Tabla con preaprobadas | — | Lista filtrada |

---

### 7. Aplicar filtro de Estado

| Step | Title | Description | Expected Result | Data Input | Data Output |
|------|-------|-------------|-----------------|------------|-------------|
| 7.1 | Seleccionar estado | En "Estado Propuesta" elegir "Calificada" | Estado filtrado | Estado = "Calificada" | Campo filtrado |
| 7.2 | Ejecutar búsqueda | Click en "Buscar" | Tabla con calificadas | — | Lista filtrada |

---

### 8. Ingresar a solicitud calificada

| Step | Title | Description | Expected Result | Data Input | Data Output |
|------|-------|-------------|-----------------|------------|-------------|
| 8.1 | Ubicar fila | Identificar fila con Estado "Calificada" | Fila encontrada | — | Fila localizada |
| 8.2 | Abrir solicitud | Click en "Calificada" de esa fila | Detalle de solicitud abierto | — | Detalle abierto |

---

### 9. Acceder al Resumen

| Step | Title | Description | Expected Result | Data Input | Data Output |
|------|-------|-------------|-----------------|------------|-------------|
| 9.1 | Ir a Resumen | Click en "Resumen" | Resumen de propuesta visible | — | Pantalla Resumen |

---

### 10. Consultar solicitud

| Step | Title | Description | Expected Result | Data Input | Data Output |
|------|-------|-------------|-----------------|------------|-------------|
| 10.1 | Click en Consultar | Click en "Consultar" | Detalle con pestañas abierto | — | Detalle con pestañas |
| 10.2 | Consultar (condicional) | Si aparece "Inicio Solicitud Garantías", click en "CONSULTAR SOLICITUD" | Detalle accesible | — | Detalle accesible |

---

### 11. Navegar a pestaña Límites

| Step | Title | Description | Expected Result | Data Input | Data Output |
|------|-------|-------------|-----------------|------------|-------------|
| 11.1 | Seleccionar pestaña | Click en "Límites" | Sección de Límites visible | — | Pestaña activa |

---

### 12. Verificar monto habilitado

| Step | Title | Description | Expected Result | Data Input | Data Output |
|------|-------|-------------|-----------------|------------|-------------|
| 12.1 | Abrir Límites Vigentes | Click en "LÍMITES VIGENTES" | Tabla de límites desplegada | — | Tabla visible |
| 12.2 | Validar monto | Leer "Habilitado" en última fila | Valor igual a 0,00 | — | montoHabilitado = 0,00 |

---

## Resultado Esperado

| Verificación | Valor Esperado |
|--------------|----------------|
| Monto "Habilitado" en Límites Vigentes (última fila) | 0,00 |

---

## Flujo


Navegar a SCACS
  → Login
    → Menú → Búsqueda de Propuestas
      → Abrir filtros → Buscar cliente por documento
        → Filtro Flujo: "Solicitud Preaprobada"
          → Filtro Estado: "Calificada"
            → Seleccionar solicitud
              → Resumen → Consultar
                → [Condicional: CONSULTAR SOLICITUD]
                  → Pestaña "Límites"
                    → "LÍMITES VIGENTES"
                      → Verificar: Habilitado == 0,00