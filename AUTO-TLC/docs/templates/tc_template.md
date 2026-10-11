# TC-[ID]: [Título funcional del caso de prueba]

<!-- REEMPLAZAR:
  - [ID]     : número o código del caso (ej. 077, TC-01)
  - [Título] : descripción funcional corta (ej. "Verificar límite habilitado al calificar solicitud")
-->

## Propósito

<!-- REEMPLAZAR: Una oración que exprese el objetivo de verificación del caso.
     Usar negritas para resaltar estados, campos y valores clave.
     Ejemplo: Verificar que las garantías parciales vencidas sin check **no habilitan** límite de crédito. -->

[Descripción del propósito del caso de prueba.]

## Descripción

<!-- REEMPLAZAR: Párrafo que describe el flujo de punta a punta: punto de entrada, navegación principal,
     acciones clave y la verificación final. Sin tecnicismos de automatización. -->

[Descripción narrativa del flujo completo del caso: desde dónde inicia, qué navega, qué filtra, qué valida.]

## Data Input / Output

<!-- REEMPLAZAR: Listar TODOS los datos que el caso consume (Input) y produce/verifica (Output).
     - Tipo: "Input" para datos que se ingresan, "Output" para valores que se verifican.
     - Campo: nombre técnico/funcional del parámetro (sin llaves, en camelCase).
     - Descripción: explicación legible del dato.
     Excluir variables internas {B[...]} y técnicas de control. -->

| Tipo   | Campo             | Descripción                                              |
|--------|-------------------|----------------------------------------------------------|
| Input  | url               | URL de acceso a la aplicación                            |
| Input  | usuario           | Credencial de usuario para login                         |
| Input  | password          | Credencial de contraseña para login                      |
| Input  | [campoInput1]     | [Descripción del dato de entrada 1]                      |
| Input  | [campoInput2]     | [Descripción del dato de entrada 2]                      |
| Output | [campoOutput1]    | [Valor o estado que se verifica al final del caso]       |
| Output | resultado         | Estado de la prueba: Pass / Fail                         |

---

## Steps

<!-- INSTRUCCIONES GENERALES PARA PASOS:
     FORMATO: cada sección tiene UNA tabla de 3 columnas: # | Acción | Resultado esperado
     - Columna #: número de sub-paso (ej. 1.1, 1.2). Alineado a la derecha.
     - Columna Acción: qué hace el usuario. Incluir inline el elemento UI y el valor ({CP[...]}).
       Max ~55 chars por línea; el texto hace wrap automático en la celda.
     - Columna Resultado esperado: qué se observa tras la acción. Conciso y verificable.
     - Pasos condicionales: prefijo *(Condicional)* en la celda Acción.
     - NO usar tablas de 5-6 columnas. NO repetir información ya en Data I/O.
     - Nombrar los elementos de UI tal como aparecen en el sistema (ej. "Menu Hamburguesa").
     - El documento debe leerse sin scroll horizontal en 1366×768. -->

### 1. [Nombre de la primera fase — ej. Login]

| #   | Acción                                                   | Resultado esperado                                  |
|----:|:---------------------------------------------------------|:----------------------------------------------------|
| 1.1 | [Qué se hace — elemento UI — valor si aplica]            | [Lo que se debe ver/obtener tras la acción]         |
| 1.2 | *(Condicional)* Si aparece [X], [qué se hace]            | [X] cerrado / descartado                            |
| 1.3 | Ingresar `{CP[usuario]}` en el campo `Usuario`           | Campo completado con el valor ingresado             |

---

### 2. [Nombre de la segunda fase — ej. Navegación]

<!-- Copiar este bloque para cada fase adicional. -->

| #   | Acción                                                   | Resultado esperado                                  |
|----:|:---------------------------------------------------------|:----------------------------------------------------|
| 2.1 | [Acción]                                                 | [Resultado]                                         |
| 2.2 | [Acción]                                                 | [Resultado]                                         |

---

### N. [Fase de validación final]

| #   | Acción                                                   | Resultado esperado                                  |
|----:|:---------------------------------------------------------|:----------------------------------------------------|
| N.1 | [Verificar campo / condición]                            | [Valor esperado — ej. `Habilitado` == **0,00**]     |

---

## Resultado Esperado

<!-- REEMPLAZAR: Tabla de verificaciones críticas. Máx 2-3 filas.
     - Verificación: qué se comprueba.
     - Valor esperado: valor, estado o condición que debe cumplirse. -->

| Verificación                              | Valor esperado      |
|:------------------------------------------|:--------------------|
| [Campo o condición verificada]            | [Valor — ej. 0,00]  |
| [Campo o condición verificada 2]          | [Valor esperado 2]  |

---

## Observaciones generales

<!-- OPCIONAL. Incluir si hay:
     - Popups opcionales que pueden o no aparecer.
     - Tiempos de espera relevantes (TBox Wait).
     - Ramas condicionales que dependen del estado de datos.
     - Comportamientos variables por entorno. -->

- [Observación 1: ej. "Puede aparecer popup de descarga; cerrarlo antes de continuar."]
- [Observación 2: ej. "Los waits de 8-15 s tras cada búsqueda son necesarios para que la tabla se recargue."]

## Postcondiciones / Limpieza

<!-- OPCIONAL. Estado final esperado del entorno tras la ejecución.
     Solo incluir acciones funcionales (no desktop/SO ni cierre forzado de procesos). -->

- [Postcondición 1: ej. "La sesión puede permanecer abierta para nuevas ejecuciones."]
- [Postcondición 2: ej. "No se realizan modificaciones al estado de los datos; solo se consultan."]

---

## Flujo

<!-- REEMPLAZAR: Diagrama ASCII que muestra la secuencia de navegación de punta a punta.
     Usar sangría con → para indicar el avance de pasos.
     Usar [Condicional: ...] para ramas opcionales.
     Ejemplo de formato:

     Punto de entrada
       → Fase 1
         → Fase 2
           → [Condicional: acción si aparece X]
             → Fase 3
               → Verificación final
-->

[Punto de entrada / Pantalla inicial]
  → [Fase 1]
    → [Fase 2]
      → [Fase 3]
        → [Condicional: acción opcional]
          → [Fase N — validación]
            → Verificar: [campo] == [valor esperado]
