# Introducción a la ingeniería de sistemas y al MBSE

> Lectura previa de la **Semana 1**. Objetivo: llegar a la Semana 2 con el vocabulario
> mínimo para construir un modelo de arquitectura sin que "BDD", "bloque" o "trazabilidad"
> suenen a chino. ~15 minutos de lectura.

---

## 1. ¿Qué es la ingeniería de sistemas?

Un robot terrestre no tripulado lo diseñan a la vez ingenieros de mecánica, de potencia,
de control, de software, de comunicaciones… Cada uno domina su parte, pero **nadie domina
el conjunto**. La ingeniería de sistemas es la disciplina que se ocupa de ese conjunto:

- traducir lo que necesita el cliente en **requisitos** claros y verificables;
- repartir esos requisitos entre subsistemas y definir **cómo encajan** entre sí (las
  interfaces);
- mantener la **trazabilidad**: saber en todo momento por qué existe cada pieza y qué
  requisito la justifica;
- comprobar al final que el sistema **hace lo que tenía que hacer**.

El ingeniero de sistemas no es el que más sabe de motores ni de código: es **el dueño de
las interfaces y de la coherencia del todo**.

## 2. ¿Por qué "basada en modelos" (MBSE)?

Tradicionalmente todo esto se hacía con **documentos**: un Word de requisitos, un Excel de
interfaces, un PowerPoint de arquitectura, un PDF de pruebas… Al primer cambio, esos
documentos dejan de estar de acuerdo entre sí y nadie sabe cuál vale.

**MBSE** (*Model-Based Systems Engineering*) sustituye esa pila de documentos por **un
único modelo**: una base de datos gráfica donde los bloques, las interfaces, los requisitos
y sus enlaces viven juntos y consistentes. El modelo es la **fuente de verdad**; los
documentos, si hacen falta, se generan desde él.

En este curso el modelo se construye con **MATLAB System Composer** (arquitectura) y se
verifica con **Simscape** (simulación física).

## 3. El ciclo en V

El trabajo de sistemas se organiza en forma de **V**:

```
 Necesidades                                         Validación
   \                                                   /
    Requisitos                                 Verificación
      \                                           /
       Arquitectura  ───────────────────  Integración
         \                                   /
          Diseño de detalle  ──────  Pruebas de subsistema
                     \                /
                      Implementación
```

- **Rama izquierda (bajada):** de lo abstracto a lo concreto — necesidades → requisitos →
  arquitectura → diseño.
- **Fondo:** se construye.
- **Rama derecha (subida):** de lo concreto a lo abstracto — se prueba cada nivel contra lo
  que se definió en el nivel equivalente de la izquierda. La **trazabilidad** cruza la V de
  un lado al otro (cada test verifica un requisito).

Las 14 semanas del curso recorren la V: **Semanas 1–3** bajan por la rama izquierda
(entender el encargo, nombrar la arquitectura, formalizarla); **Semanas 4–8** trabajan el
fondo y empiezan a subir (ingeniería inversa del modelo, calibración, verificación);
**Semanas 9–14** completan la subida (fallos, integración, optimización, defensa).

## 4. Vocabulario SysML mínimo

**SysML** es el lenguaje gráfico estándar para modelar sistemas. No hace falta dominarlo;
basta con estos términos:

| Término | Qué es |
|---|---|
| **Bloque** (*block*) | Una "caja" que representa un elemento del sistema: el UGV, el subsistema de propulsión, el Puesto de Mando… Puede contener otros bloques. |
| **Propiedad de valor** (*value property*) | Un dato numérico del bloque, **con tipo y unidad**: `masa_orden_mision = 9000 kg`, `potencia_min = 140 kW`. |
| **Puerto** (*port*) | El punto por el que un bloque se conecta con otro. |
| **Interfaz** (*interface*) | Qué fluye por una conexión: energía eléctrica, un par mecánico, un mensaje de control, un flujo de vídeo… |
| **BDD** (*Block Definition Diagram*) | El diagrama que dice **qué bloques hay**, sus propiedades y cómo se componen unos dentro de otros (la "lista de piezas" jerárquica). Es lo que se construye en la **Semana 2**. |
| **IBD** (*Internal Block Diagram*) | El diagrama que dice **cómo se conectan por dentro** los bloques de un nivel: puertos, interfaces y líneas de conexión. Se trabaja en la **Semana 3**. |
| **Enlace de trazabilidad** | Una flecha que une un elemento del modelo con el requisito que lo justifica (*satisfy*), o un test con el requisito que verifica (*verify*). |

**BDD = qué hay** (bloques y propiedades). **IBD = cómo se conecta** (puertos e interfaces).

## 5. La regla de oro del curso

> **Todo valor numérico del modelo lleva el ID del requisito que lo justifica.**

Si en un bloque escribes `velocidad_max = 75 km/h`, en su descripción debe aparecer
`RLT1-03`. Una propiedad sin requisito que la respalde **no entra en el modelo**. Esta
regla es lo que separa "usar una herramienta" de "hacer ingeniería de sistemas".

## 6. Los cuatro roles del equipo

El equipo se organiza en cuatro roles funcionales, definidos **por el tipo de evidencia
que producen**, no por subsistema del vehículo. Los roles **rotan** en el punto medio del
ciclo en V, de modo que cada alumno recorre la rama de diseño y la de verificación.

| Rol | De qué se ocupa | Evidencia que produce |
|---|---|---|
| **IS — Ingeniería de Sistemas** | Requisitos, arquitectura, trazabilidad, coordinación | Modelo SysML y matriz de verificación |
| **Simulación** | Modelo físico en Simscape (propulsión, dinámica) | Resultados de simulación |
| **Taller** | Banco físico y medidas reales | Evidencia física (medidas) |
| **Software** | Adquisición de datos e integración hardware ↔ modelo | Integración y contraste hw ↔ modelo |

El rol de IS coordina a los otros tres y reporta al Cliente (el profesor).

---

*Siguiente paso: leer el [Anexo I anonimizado](anexo-I_anonimizado.html) con el guion de la
Semana 1 y rellenar la ficha de comprensión.*
