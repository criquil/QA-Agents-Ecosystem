---
name: kb-02-pruebas-de-sistema-manual
description: Skill autónoma de conocimiento sobre pruebas de sistema (system testing) manuales. No depende de archivos externos.
---

# Pruebas de Sistema (System Testing) Manuales

## Definición

Validación del **sistema completo e integrado** contra los requisitos de sistema, ejecutada desde la perspectiva del usuario final sobre el entorno desplegado, con todos los módulos y dependencias activos.

## Diferencia con Pruebas Funcionales

| | Pruebas Funcionales | Pruebas de Sistema |
|---|---|---|
| Alcance | Una función o pantalla | Un flujo completo que cruza módulos |
| Base | Requisito funcional | Requisito de sistema y flujo de negocio |
| Dependencias | Aisladas o simuladas | Reales y activas |
| Enfoque | ¿Función correcta? | ¿Sistema coherente y operativo? |
| Datos | Por validación | De punta a punta, persistidos |

## Tipos de validación

### 1. Flujo end-to-end
Recorrer el flujo completo con un rol real y verificar la coherencia del resultado en cada etapa y en cada módulo implicado.

```
Ejemplo e-commerce:
1. Alta de cliente                   -> cliente registrado
2. Verificación de correo            -> cuenta activada
3. Búsqueda y agregado al carrito    -> carrito correcto
4. Checkout y pago                   -> pago aprobado
5. Confirmación de pedido            -> pedido y estado correctos
6. Notificación por correo           -> correo recibido con los datos del pedido
7. Facturación                       -> factura generada con el monto correcto
8. Inventario                        -> stock descontado correctamente
9. Reporte de ventas                 -> la venta aparece en el reporte
```

### 2. Integración entre módulos
Verificar que el dato creado en un módulo se refleje correctamente en los demás (coherencia, no sólo presencia).

### 3. Integración con servicios externos
- Pasarela de pago: aprobación, rechazo y timeout explícitos.
- Correo/SMS: recepción, contenido y enlace válido.
- SSO: alta, baja y expiración de sesión.
- Comportamiento del sistema cuando el servicio externo está caído.

### 4. Estados globales del sistema
```
Sesión expirada a mitad de un flujo        -> redirección y datos no perdidos
Timeout de una operación larga             -> mensaje claro y estado consistente
Doble submit del mismo formulario          -> sin duplicados
Dos pestañas editando el mismo registro    -> comportamiento definido
Conectividad perdida durante el guardado   -> sin corrupción de datos
```

### 5. Compatibilidad del sistema
Repetir el flujo crítico en la matriz de navegadores y resoluciones acordada, comprobando paridad funcional.

### 6. Volumen y estados límite del sistema
- Listado con una sola página y con muchas páginas.
- Reportes con el máximo rango de fechas permitido.
- Usuario con muchos registros históricos.

## Escenarios que siempre deben existir

1. El flujo comercial principal de punta a punta.
2. El flujo de alta y baja de usuario.
3. El flujo con la dependencia externa más crítica caída.
4. El flujo de recuperación (reinicio, reingreso, reintento).
5. El flujo de consulta de información histórica y reportes.

## Criterios de éxito

- Los flujos críticos se completan sin bloqueantes.
- Los datos son coherentes entre todos los módulos implicados.
- Los servicios externos integrados responden y se comportan ante fallo.
- Los estados globales del sistema son manejados de forma explícita.
- Hay paridad funcional en la matriz de navegadores acordada.

## Best Practices

1. Ejecutar el sistema con las dependencias reales, no simuladas.
2. Usar un usuario de negocio real (no un usuario de prueba con permisos especiales).
3. Verificar el dato en todos los módulos donde debería aparecer.
4. Probar con el volumen representativo del negocio, no sólo con dos registros.
5. Registrar la versión del build y de cada servicio externo durante la ejecución.
6. Reiniciar el estado entre flujos para evitar contaminación cruzada.
