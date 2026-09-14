# Semana 1 — Ficha de Extracción de Requisitos

*Sistema Terrestre No Tripulado (UGV) · CPP 01/2026 AB — CDTI / Ministerio de Defensa de España*
*Presupuesto real del proyecto: 11.905.308 € · Duración: 30 meses*

**Equipo:** ______________&nbsp;&nbsp;&nbsp; **Lote:** ☐ 1 (ruedas) ☐ 2 (cadenas)&nbsp;&nbsp;&nbsp; **Integrantes:** ______________________________

Sois el equipo de ingeniería que acaba de recibir el pliego técnico de una licitación real del CDTI. Antes de diseñar nada hay que entender qué pide el cliente: leer el pliego como ingenieros de sistemas y transformar sus exigencias en requisitos formales y verificables. Eso es esta ficha.

*Material: Anexo I — Requisitos Funcionales (secciones 1 a 3, ~25 páginas; el resto es material contractual que no necesitáis) + plantilla Excel de tabla de requisitos.*

## 1. El requisito SHALL

Un requisito formal se expresa siempre con el verbo **SHALL** (deberá): es una obligación verificable, no una descripción ni una sugerencia.

**[ID-REQ] El [sujeto] SHALL [verbo de acción] [condición cuantificable]**
Ejemplo: [REQ-MOV-003] El UGV SHALL alcanzar una velocidad máxima en carretera de 75 km/h como mínimo.

| Nivel | Ejemplo en este proyecto | Verificación |
|---|---|---|
| L0 — Misión | El UGV SHALL eliminar el riesgo para el personal en misiones con medios pesados | No verificable por simulación |
| L1 — Sistema | El UGV SHALL operar de forma autónoma sin tripulación a bordo | Tests de autonomía, campo |
| L2 — Subsistema | El sistema de propulsión SHALL proporcionar 140 kW como mínimo | Simulación — verificable |
| L3 — Componente | El pack de baterías SHALL tener capacidad para 2h de autonomía eléctrica | Simulación — verificable |

*El pliego contiene sobre todo requisitos L1/L2. Los descompondréis hasta L3 más adelante en el curso.*

## 2. ¿Verificable por simulación?

| Verificable | No verificable (otra evidencia) |
|---|---|
| Velocidad máxima en carretera ≥ 75 km/h | Resistencia balística a disparos de pequeño calibre |
| Potencia de propulsión ≥ 140 kW | Interoperabilidad con comunicaciones del Ejército |
| Pendiente máxima frontal ≥ 60% | Facilidad de mantenimiento de primer escalón |

## 3. Subsistemas del UGV

| Subsistema | Descripción |
|---|---|
| S1 — Propulsión | Motor eléctrico/combustión, transmisión, tracción, ruedas/cadenas |
| S2 — Energía | Baterías, generador, gestión energética, recarga regenerativa |
| S3 — Suspensión y dinámica | Tren de rodaje, suspensión activa, estabilidad, vadeo |
| S4 — Control y autonomía | Modos de operación, navegación autónoma, detección de obstáculos |
| S5 — Sensores y comunicaciones | LIDAR, cámaras, IMU, GNSS, radio, puesto de mando |
| S0 — Sistema (transversal) | Modularidad, masa total, autonomía global |

## 4. Tareas

**Tarea 1 — Lectura activa (45 min).** Leed las secciones 1-3 del Anexo I marcando: **verde** = requisito con valor numérico, **amarillo** = requisito funcional sin valor numérico, **naranja** = restricción/condición de diseño. Contad cuántos requisitos numerados hay (RGEN, RLT1/RLT2, ROPE, RNAV, RCOM — unos 80 en total) y repartíoslos.

**Tarea 2 — Extracción a formato SHALL (60 min).** Para cada requisito: registrad su ID original, transformadlo a SHALL sin inventar nada, asignadlo a un subsistema, e indicad si es verificable por simulación (Sí/No/Parcial). Rellenad la tabla (podéis añadir filas; usad la plantilla Excel si preferís trabajar ahí):

| ID propio | ID pliego | Texto SHALL | Subsistema | Fuente (§) | ¿Simulable? |
|---|---|---|---|---|---|
| REQ-MOV-001 | RLT1-03a | El UGV (Lote 1) SHALL alcanzar una velocidad máxima en carretera de al menos 75 km/h. | S1 | §3.2.1 | Sí |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

*[Continuad añadiendo filas hasta cubrir todos los requisitos identificados — o usad la plantilla Excel proporcionada.]*

**Tarea 3 — Análisis (30 min).** Responded en grupo, preparando la puesta en común:

1. ¿Cuántos requisitos tiene el subsistema con más requisitos? ¿Es razonable?

   _(respuesta)_

2. ¿Qué subsistema tiene más requisitos NO verificables por simulación? ¿Por qué?

   _(respuesta)_

3. Los requisitos [OPCIONAL], ¿cómo los habéis tratado?

   _(respuesta)_

4. ¿Algún requisito ambiguo o contradictorio? Identificadlo.

   _(respuesta)_

5. **RGEN-11 dice que la propulsión será híbrida. ¿Genera requisitos derivados en otros subsistemas? ¿Cuáles?** — la más importante: la interdependencia entre subsistemas es el núcleo de la ingeniería de sistemas.

   _(respuesta)_

**Tarea 4 — Diagrama de contexto (30 min).** A mano o con cualquier herramienta: el UGV como caja central, los actores externos (operador/puesto de mando, Ejército/UME, entorno físico, otros vehículos del convoy) y los flujos entre ellos (órdenes de misión, telemetría, energía, cargas de pago). *[Adjuntad la foto o PDF en esta misma carpeta.]*

## 5. Entregables y evaluación

| Entregable | Formato | Peso |
|---|---|---|
| E1.1 — Tabla de requisitos completa | Excel (plantilla) | 60% |
| E1.2 — Respuestas Tarea 3 | Word, máx. 1 página | 20% |
| E1.3 — Diagrama de contexto | Foto o PDF, máx. 1 página | 20% |

*Entrega antes del inicio de la Semana 2. Criterio transversal: cobertura >85% de los requisitos numerados, formato SHALL correcto, asignación a subsistema coherente, columna "¿Simulable?" bien identificada, y análisis de la Tarea 3 con ejemplos concretos del pliego (no respuestas superficiales).*

## Consejos rápidos

- ~80 requisitos numerados en total (RGEN, RLT1, RLT2, ROPE, RNAV, RCOM) — repartidlos por rangos antes de empezar.
- RGEN-11 a RGEN-15 (propulsión híbrida) son el corazón técnico: generan requisitos derivados en casi todos los subsistemas.
- Los [OPCIONAL] se registran igualmente, con nota, pero no cuentan en el recuento de obligatorios.
- "deberá" / "se requiere que" / "tendrá que" → todo se transforma en SHALL; incluid siempre el valor numérico si el pliego lo da.
- No confundáis descripción de arquitectura con requisito: "el sistema incluye un UAV de Apoyo" describe; "el UAV de Apoyo SHALL teleoperarse de forma independiente del UGV" es un requisito.

## Referencia rápida de prefijos

| Prefijo | Sección | Contenido |
|---|---|---|
| RGEN-XX | §3.1 | Generales — ambos lotes: arquitectura, propulsión, autonomía, modularidad |
| RLT1-XX / RLT2-XX | §3.2 / §3.3 | Específicos del Lote 1 (ruedas) / Lote 2 (cadenas) |
| ROPE-XX | §3.4–3.5 | Modos de operación (teleoperado, autónomo, offline) |
| RPdO-XX | §3.6 | Puesto de Operación |
| RNAV-XX | §3.7 | Sensores de navegación |
| RCOM-XX | §3.8 | Comunicaciones |

*Para este ejercicio, los más relevantes son RGEN, RLT1/RLT2, ROPE y RNAV.*
