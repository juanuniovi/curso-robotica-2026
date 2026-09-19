# Estudio de Conceptos y Selección — Sistema UGV

**Equipo:** ______________&nbsp;&nbsp;&nbsp; **Integrantes:** ______________________________

## 1. Alcance

Este documento es el Doc.04 de `docs/metodologia-mbse.md`: antes de modelar la arquitectura en
SysML (Fase 5), el equipo identifica **concepciones alternativas** de la solución y selecciona
una de forma justificada y trazable a los requisitos. Sin este paso, la arquitectura de la Fase 5
sería una elección arbitraria en vez de una decisión de ingeniería.

*Referencia: Anexo I — Requisitos Funcionales, RLT1-02.*

## 2. El problema de decisión

RLT1-02 permite tres configuraciones de tren de tracción para el UGV de ruedas:

> «Tren de tracción de ruedas en configuración **4×4, 6×6 u 8×8**, con elevadas capacidades
> todoterreno de dificultad promedio y mayores velocidades en terrenos llanos y consolidados.»

Elegir entre ellas no es un detalle de implementación: condiciona la masa en vacío (RLT1-06), la
capacidad de carga (RLT1-07), la potencia necesaria (RLT1-09), la complejidad del sistema de
propulsión y suspensión (RLT1-04, RLT1-05), y en última instancia el coste y el plazo. Esta es la
decisión de concepto que este documento formaliza.

## 3. Alternativas consideradas

| Concepto | Descripción | Ventaja principal | Riesgo principal |
|---|---|---|---|
| A — 4×4 | | | |
| B — 6×6 | | | |
| C — 8×8 | | | |

*Describe cada configuración con tus palabras: número de ejes motrices, implicaciones en tren de
rodaje y suspensión (S3), y cómo afecta a los puntos de interfaz de cargas de pago (RGEN-28).*

## 4. Criterios de decisión

Define entre 4 y 6 criterios, cada uno trazado a un requisito, con un peso (que sume 100%). Para
cada criterio, indica también **qué posibilidad concreta** generaría la evidencia con la que vas
a puntuarlo — no hace falta ejecutarla ahora, solo identificarla; sin esto, la puntuación de la
matriz AoA es una opinión, no una decisión de ingeniería.

| Criterio | Requisito que lo justifica | Posible medio de evidencia para puntuar | Peso |
|---|---|---|---|
| Capacidad de carga | RLT1-07, RLT1-08 | Cálculo analítico de reparto de carga por eje | |
| Movilidad todoterreno | RLT1-03 | Simulación de tracción/pendiente por configuración | |
| Complejidad / coste del sistema de propulsión | RLT1-09, RGEN-11 | Comparación de número de motores/actuadores por configuración | |
| Facilidad de integración de Puntos de Interfaz | RGEN-28 | Boceto/croquis de la disposición de puntos de interfaz por configuración | |
| | | | |
| **Total** | | | **100%** |

## 5. Matriz de decisión ponderada (AoA — Analysis of Alternatives)

Puntúa cada alternativa en cada criterio (escala 1–5, 5 = mejor) apoyándote en el medio de
evidencia identificado en la tabla anterior, y calcula la puntuación ponderada.

| Criterio | Peso | A — 4×4 | B — 6×6 | C — 8×8 |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| **Puntuación ponderada total** | | | | |

## 6. Concepto seleccionado

**Configuración elegida:** ______________

**Justificación** (por qué esta y no las otras, apoyándote en la matriz — 5-8 líneas):

[respuesta]

**Consecuencias para la Fase 5 (Arquitectura):** qué implica esta elección para los bloques y
propiedades de `sistema.yaml` (p. ej. número de conjuntos de rueda-motor, propiedades del bloque
`MovilidadTrenRodaje`).

[respuesta]

## 7. Entregables de esta fase

| Entregable | Formato | Dónde |
|---|---|---|
| Este documento (alternativas, criterios, matriz AoA, decisión justificada) | Markdown, rellenar directamente | esta carpeta |
