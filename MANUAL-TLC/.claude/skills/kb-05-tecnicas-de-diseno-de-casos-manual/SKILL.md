---
name: kb-05-tecnicas-de-diseno-de-casos-manual
description: Skill autónoma de conocimiento sobre técnicas de diseño de casos de prueba manuales: particiones de equivalencia, valores límite, tablas de decisión, transición de estados y casos de uso. No depende de archivos externos.
---

# Técnicas de Diseño de Casos de Prueba Manuales

## Definición

Las técnicas de diseño permiten obtener el máximo de cobertura con el mínimo de casos, sustituyendo la intuición por un método repetible y trazable.

---

## 1. Particiones de Equivalencia

Dividir el dominio de entrada en clases donde el sistema debe comportarse igual. Un caso por clase basta.

**Ejemplo — campo "edad" (18 a 65):**

| Partición | Valores | Resultado esperado |
|---|---|---|
| Inválida inferior | 10, 17 | Error de validación |
| Válida | 18, 40, 65 | Aceptado |
| Inválida superior | 66, 90 | Error de validación |
| Vacío / no numérico | "", "abc" | Error de validación |

Casos: 4 (en lugar de probar cada valor posible).

---

## 2. Análisis de Valores Límite

Los defectos se concentran en los bordes. Probar siempre: límite inferior, mínimo-1, límite superior, máximo+1, y un valor interior representativo.

**Campo numérico (1 a 100):**

| Valor | Clase | Esperado |
|---|---|---|
| 0 | Bajo el mínimo | Error |
| 1 | Mínimo | Aceptado |
| 2 | Justo sobre el mínimo | Aceptado |
| 50 | Interior | Aceptado |
| 99 | Justo bajo el máximo | Aceptado |
| 100 | Máximo | Aceptado |
| 101 | Sobre el máximo | Error |

**Campo texto (máximo 100 caracteres):**

| Valor | Esperado |
|---|---|
| "" (vacío) | Error "campo obligatorio" |
| " " (sólo espacios) | Error o trim según requisito |
| "a" | Aceptado |
| "a" × 100 | Aceptado |
| "a" × 101 | Error de longitud |
| "!@#$%^&*()" | Definido por requisito |
| con acentos y emojis | Definido por requisito |
| `<script>alert(1)</script>` | Debe ser escapado o rechazado |

**Colecciones (1 a 10 elementos):** vacía, 1, 5, 10, 11.

**Fechas:** mínima, anterior a la mínima, máxima, posterior a la máxima, formato inválido, zona horaria, cambio de mes/año, año bisiesto.

---

## 3. Tabla de Decisión

Para reglas de negocio con varias condiciones combinadas. Cada columna es un caso.

**Ejemplo — descuento por tipo de cliente y monto:**

| Condición / Regla | R1 | R2 | R3 | R4 |
|---|---|---|---|---|
| Cliente es premium | Sí | Sí | No | No |
| Monto > 1000 | Sí | No | Sí | No |
| **Descuento** | 15% | 5% | 5% | 0% |

**Ejemplo — cupón:**

| Condición | R1 | R2 | R3 | R4 |
|---|---|---|---|---|
| Cupón existe | Sí | Sí | Sí | No |
| Cupón vigente | Sí | No | Sí | — |
| Carrito elegible | Sí | — | No | — |
| **Resultado** | Aplicado | Rechazado: expirado | Rechazado: no elegible | Rechazado: inexistente |

---

## 4. Transición de Estados

Para entidades con ciclo de vida. Probar transiciones válidas e inválidas.

**Ejemplo — pedido:**

```
Borrador --confirmar--> Confirmado --pagar--> Pagado --enviar--> Enviado --entregar--> Entregado
   |                        |                    |
   +---cancelar--> Cancelado +--cancelar--> Cancelado
```

Casos: cada transición válida, cada transición inválida (ej. Entregado → Borrador debe ser rechazada) y cada acción desde un estado no permitido.

---

## 5. Casos de Uso / Flujos

Diseñar a partir de escenarios de negocio completos, incluyendo:
- Flujo principal
- Flujos alternativos
- Flujos de excepción

**Ejemplo — "Pagar un pedido":**
- Principal: pedido confirmado → pago aprobado → pedido pagado
- Alternativo: pago rechazado → reintentar con otro medio
- Excepción: timeout de la pasarela → pedido sin cambio de estado y mensaje claro

---

## 6. Pairwise / Combinaciones

Cuando hay muchas variables con varios valores, probar todas las combinaciones es inviable. Elegir un conjunto reducido que cubra todos los pares de variables al menos una vez.

**Ejemplo — 3 variables (navegador × rol × idioma):** la combinación total es N×M×K; con pairwise se reduce drásticamente manteniendo la detección de defectos de interacción.

---

## 7. Error Guessing (como complemento)

Basado en la experiencia del tester: histórico de defectos del módulo, cambios recientes, zonas complejas, cálculos, fechas, importaciones/exportaciones, permisos.

Se usa **como complemento** de las técnicas formales, nunca como sustituto.

---

## Checklist de cobertura de un caso de prueba

```
[ ] Flujo principal cubierto
[ ] Particiones de equivalencia cubiertas
[ ] Valores límite cubiertos (mínimo-1, mínimo, máximo, máximo+1)
[ ] Entradas inválidas y vacías
[ ] Reglas de negocio combinadas (tabla de decisión)
[ ] Transiciones de estado válidas e inválidas
[ ] Permisos por rol
[ ] Persistencia verificada
[ ] Mensajes de error verificados (texto, claridad, ubicación)
[ ] Compatibilidad en la matriz
[ ] Accesibilidad básica (teclado, foco, etiquetas)
```

## Reglas

1. Un caso por partición o por regla, no por valor.
2. Siempre los bordes antes que el centro.
3. Toda tabla de decisión debe cubrir todas las reglas, incluidas las de rechazo.
4. Las transiciones inválidas son tan importantes como las válidas.
5. Documentar el dato exacto de cada caso: sin dato no hay reproducibilidad.
6. No sustituir el método por la intuición: la intuición complementa, no reemplaza.
