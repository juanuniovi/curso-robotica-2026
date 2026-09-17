# Introducción a la ingeniería de sistemas y al MBSE

> Lectura previa de la **Fase 1 — Ingeniería inversa**. Objetivo: llegar a la Fase 2 con el
> vocabulario mínimo para construir un modelo de arquitectura sin que "BDD", "bloque" o
> "trazabilidad" suenen a chino. ~15 minutos de lectura.

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

En este curso el modelo de arquitectura se escribe como **texto plano** (YAML: bloques,
propiedades, interfaces) y se visualiza generando diagramas BDD/IBD con un script — ver
`modelos/sysml/`. Se verifica con **simulación por computador** (un simulador físico, por
determinar).

## 3. La metodología: OOSEM sobre el ciclo en V

SysML es un **lenguaje** — dice cómo se dibuja un bloque o una interfaz. No dice en qué
orden hacer las cosas. Eso lo da una **metodología**, y la que usa este curso (sin haberla
nombrado hasta ahora) es **OOSEM** (*Object-Oriented Systems Engineering Method*): la
metodología que INCOSE empareja con SysML en su libro de referencia. No es una elección
nuestra — es el estándar de facto para trabajar con SysML, tool-agnóstica.

**Importante: este curso recorre solo la rama descendente de la V, y ni siquiera llega a
Implementación.** El encargo real es preparar una **oferta técnica** para una licitación —
no construir ni verificar el sistema completo. Eso sería ya ejecutar un contrato
adjudicado, y queda fuera del alcance del curso:

| Fase OOSEM (Sols, Fig. 3.5) | Fase del curso | Documento | Qué se hace |
|---|---|---|---|
| Necesidad, problema, stakeholders | 1 — Análisis de la Necesidad | Doc.01 | Leer el pliego, deducir necesidad, problema y stakeholders, diagrama de contexto |
| Concepto de Operaciones (ConOps) | 2 — CONOPS | Doc.02 | Modos de operación, misiones, ciclo de vida, escenario |
| Requisitos de stakeholder | 3 — Requisitos de las Partes Interesadas | Doc.03 | Matriz SHALL, clasificación por verificabilidad |
| Identificación y selección de conceptos de diseño | 4 — Estudio de Conceptos y Selección | Doc.04 | Alternativas, criterios ponderados, matriz AoA, decisión |
| Requisitos de sistema y métodos de verificación, análisis funcional, arquitectura | 5 — Arquitectura | Doc.05 + Doc.06 | BDD + IBD, trazabilidad, baseline de arquitectura |
| Métodos de verificación (consolidación) — (no es una fase OOSEM estándar; planificación de apoyo a la oferta) | 6 — Plan de Verificación e Integración | Doc.07 | Matriz de trazabilidad requisito↔método, esquema de integración — sin ejecutar |
| — (consolidación final, no una fase OOSEM estándar) | 7 — Optimización y cierre | Doc.08 + oferta final | Plan de gestión (EDT/WBS, cronograma, presupuesto), síntesis de la oferta |

Visualmente, la metodología completa se dibuja como una **V**:

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

Este curso solo baja por la **rama izquierda** (necesidades → requisitos → arquitectura),
sin llegar a Diseño de detalle completo ni a Implementación. La rama derecha (Pruebas de
subsistema → Integración → Verificación → Validación) se muestra arriba como referencia de
la metodología general — **no la recorremos**. Lo que sí hacemos en su lugar es reunir
**evidencia de viabilidad** (simulación de los subsistemas críticos, medidas sobre un banco
de pruebas físico) que demuestre que el diseño cumple los requisitos, y volcarla en el
documento de oferta técnica que cierra el curso.

## 4. Vocabulario SysML mínimo

**SysML** es el lenguaje gráfico estándar para modelar sistemas. No hace falta dominarlo;
basta con estos términos:

| Término | Qué es |
|---|---|
| **Bloque** (*block*) | Una "caja" que representa un elemento del sistema: el UGV, el subsistema de propulsión, el Puesto de Mando… Puede contener otros bloques. |
| **Propiedad de valor** (*value property*) | Un dato numérico del bloque, **con tipo y unidad**: `masa_orden_mision = 9000 kg`, `potencia_min = 140 kW`. |
| **Puerto** (*port*) | El punto por el que un bloque se conecta con otro. |
| **Interfaz** (*interface*) | Qué fluye por una conexión: energía eléctrica, un par mecánico, un mensaje de control, un flujo de vídeo… |
| **BDD** (*Block Definition Diagram*) | El diagrama que dice **qué bloques hay**, sus propiedades y cómo se componen unos dentro de otros (la "lista de piezas" jerárquica). Es lo que se construye en la **Fase 5**. |
| **IBD** (*Internal Block Diagram*) | El diagrama que dice **cómo se conectan por dentro** los bloques de un nivel: puertos, interfaces y líneas de conexión. También se trabaja en la **Fase 5**. |
| **Enlace de trazabilidad** | Una flecha que une un elemento del modelo con el requisito que lo justifica (*satisfy*), o un test con el requisito que verifica (*verify*). |

**BDD = qué hay** (bloques y propiedades). **IBD = cómo se conecta** (puertos e interfaces).

## 5. La regla de oro del curso

> **Todo valor numérico del modelo lleva el ID del requisito que lo justifica.**

Si en un bloque escribes `velocidad_max = 75 km/h`, en su descripción debe aparecer
`RLT1-03`. Una propiedad sin requisito que la respalde **no entra en el modelo**. Esta
regla es lo que separa "usar una herramienta" de "hacer ingeniería de sistemas".

## 6. Los cuatro roles del equipo

El equipo se organiza en cuatro roles funcionales, definidos **por el tipo de evidencia
que producen**, no por subsistema del vehículo. Los roles **rotan de forma flexible**: cada
alumno pasa por tantos como quiera, en coordinación con sus compañeros. Simulación, Taller
y Software no verifican un sistema ya construido — generan la evidencia de viabilidad
(simulaciones, medidas de banco, esquemas de integración) que sostiene la oferta técnica.

| Rol | De qué se ocupa | Evidencia que produce |
|---|---|---|
| **IS — Ingeniería de Sistemas** | Requisitos, arquitectura, trazabilidad, coordinación | Modelo SysML y estructura de la oferta técnica |
| **Simulación** | Modelo físico por computador (propulsión, dinámica) | Resultados de simulación |
| **Taller** | Banco físico y medidas reales | Evidencia física (medidas) |
| **Software** | Adquisición de datos e integración hardware ↔ modelo | Integración y contraste hw ↔ modelo |

El rol de IS coordina a los otros tres y reporta al Cliente (el profesor).

---

*Siguiente paso: leer el [Anexo I anonimizado](anexo-I_anonimizado.html) con el guion de la
Fase 1 y rellenar la ficha de comprensión.*
