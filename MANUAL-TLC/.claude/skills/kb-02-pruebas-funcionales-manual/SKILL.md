---
name: kb-02-pruebas-funcionales-manual
description: Skill autónoma de conocimiento sobre pruebas funcionales manuales. No depende de archivos externos.
---

# Pruebas Funcionales Manuales

## Definición

Verificación manual de que cada función del sistema produce el resultado esperado para entradas válidas, inválidas y límite, según lo definido en los requisitos funcionales.

## Tipos de Pruebas Funcionales

### 1. Positive Testing
El sistema funciona correctamente con datos válidos.

```
Login con credenciales válidas            -> ingresa y muestra el dashboard
Alta de cliente con datos válidos         -> cliente creado y visible en el listado
Edición de un registro existente          -> cambios persistidos y visibles
Eliminación de un registro permitido      -> registro desaparece del listado
```

### 2. Operaciones CRUD
- **Create**: formulario completo y válido → registro creado y listado.
- **Read**: consulta y detalle → datos completos y correctos.
- **Update**: modificación → cambios persistidos tras recargar.
- **Delete**: eliminación → registro removido y sin efectos colaterales.

### 3. Validaciones de formulario

| Validación | Qué verificar |
|---|---|
| Campo obligatorio | Mensaje claro, foco en el campo, no se envía el formulario |
| Formato | Email, teléfono, documento, tarjeta: rechazo de formatos inválidos |
| Longitud | Mínima y máxima: aceptación en el límite, rechazo fuera de él |
| Rangos numéricos | Mínimo, máximo, fuera de rango, negativo, decimales |
| Fechas | Pasado/futuro cuando aplique, formato y locales |
| Archivos | Tipo, tamaño, cantidad |
| Coherencia | Confirmar contraseña, fecha inicio < fecha fin, cantidad > 0 |

### 4. Reglas de negocio
- Descuentos, cupones y promociones con sus condiciones y exclusiones.
- Límites por rol, por plan o por tipo de cliente.
- Transiciones de estado permitidas y prohibidas.
- Cálculos: subtotales, impuestos, redondeos, moneda y formato.

### 5. Filtros, búsqueda y ordenamiento
```
Búsqueda exacta, parcial, sin resultados y con caracteres especiales
Filtros combinados y su limpieza
Ordenamiento ascendente/descendente por cada columna ordenable
Paginación: primera, intermedia, última página, cambio de tamaño de página
```

### 6. Navegación y estado de la UI
- Menú, breadcrumbs y retorno desde el detalle.
- Botón atrás del navegador y recarga de página.
- Acciones mostradas/ocultas según el rol.
- Estados vacíos, de carga y de error de cada pantalla.

## Flujo funcional completo de ejemplo

```
1. Ingresar con rol cliente              -> dashboard del cliente
2. Buscar un producto                    -> resultados correctos
3. Agregar al carrito                    -> carrito con el ítem y el subtotal
4. Modificar cantidad                    -> total recalculado
5. Aplicar cupón válido                  -> descuento aplicado al total
6. Aplicar cupón inválido                -> mensaje de error, total sin cambios
7. Completar checkout con datos válidos  -> número de pedido generado
8. Consultar el pedido en "Mis pedidos"  -> pedido con estado correcto
9. Recargar la página                    -> estado persistido
```

## Assertions observables

- **Mensajes**: texto esperado, específico y accionable.
- **Estados visuales**: campo marcado en rojo, botón deshabilitado, spinner.
- **Datos**: valor, formato, unidades, moneda y zona horaria.
- **Persistencia**: el dato sobrevive a recarga, navegación y re-login.
- **Permisos**: la acción no permitida no está disponible o es rechazada.

## Best Practices

1. **Un requisito, al menos un caso**: sin trazabilidad no hay cobertura demostrable.
2. **Datos definidos por caso**: la reproducibilidad depende del dato.
3. **Evidencia por caso**: sin evidencia el PASS no es auditable.
4. **Probar el límite, no sólo el centro**: los defectos viven en los bordes.
5. **Validar la persistencia, no sólo la respuesta en pantalla**.
6. **Verificar el mensaje, no sólo que el error ocurra**.

## Anti-patrones

- Probar sólo el happy path.
- Aceptar cualquier mensaje de error como válido.
- No validar el dato tras recargar la página.
- Repetir exactamente el mismo caso con distintos datos triviales.
- Reportar un defecto sin pasos de reproducción.
