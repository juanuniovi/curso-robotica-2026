# Documento de Requisitos de las Partes Interesadas (StRD) — Sistema UGV

**Equipo:** ______________&nbsp;&nbsp;&nbsp; **Integrantes:** ______________________________

## 1. Alcance

Este documento formaliza en requisitos SHALL verificables el contenido técnico de la sección 3
del Anexo I (CPP 01/2026 AB), clasificados por subsistema y por verificabilidad mediante
simulación. Es el Doc.03 de `docs/metodologia-mbse.md`: parte del Análisis de la Necesidad y el
CONOPS (Fases 1 y 2) y es la base de partida para el Estudio de Conceptos (Fase 4) y la
arquitectura del sistema (Fase 5).

*Referencia: Anexo I — Requisitos Funcionales, sección 3 (el UGV de tracción de ruedas). Las
cláusulas administrativas y los anexos II a IX quedan fuera de alcance.*

## 2. Convención de requisitos

**[ID-REQ] El [sujeto] SHALL [verbo de acción] [condición cuantificable]**
Ejemplo: [REQ-MOV-003] El UGV SHALL alcanzar una velocidad máxima en carretera de 75 km/h como mínimo.

| Nivel | Ejemplo en este proyecto | Verificación |
|---|---|---|
| L0 — Misión | El UGV SHALL eliminar el riesgo para el personal en misiones peligrosas o penosas | No verificable por simulación |
| L1 — Sistema | El UGV SHALL operar de forma autónoma sin tripulación a bordo | Tests de autonomía, campo |
| L2 — Subsistema | El sistema de propulsión SHALL proporcionar 140 kW como mínimo | Simulación — verificable |
| L3 — Componente | El pack de baterías SHALL tener capacidad para 2h de autonomía eléctrica | Simulación — verificable |

## 3. Clasificación por verificabilidad

| Verificable por simulación | No verificable (otra evidencia) |
|---|---|
| Velocidad máxima en carretera ≥ 75 km/h | Resistencia de los subsistemas a agentes ambientales en campo |
| Potencia de propulsión ≥ 140 kW | Facilidad real de mantenimiento de primer escalón |
| Pendiente máxima frontal ≥ 60% | Ergonomía del Puesto de Operación en condiciones de estrés |

## 4. Subsistemas del UGV

| Subsistema | Descripción |
|---|---|
| S1 — Propulsión | Motor eléctrico/combustión, transmisión, tracción, ruedas |
| S2 — Energía | Baterías, generador, gestión energética, recarga regenerativa |
| S3 — Suspensión y dinámica | Tren de rodaje, suspensión activa, estabilidad, vadeo |
| S4 — Control y autonomía | Modos de operación, navegación autónoma, detección de obstáculos |
| S5 — Sensores y comunicaciones | LIDAR, cámaras, IMU, GNSS, radio, puesto de mando |
| S0 — Sistema (transversal) | Modularidad, masa total, autonomía global |

## 5. Matriz de requisitos

| ID propio | ID pliego | Texto SHALL | Subsistema | Fuente (§) | ¿Simulable? |
|---|---|---|---|---|---|
| REQ-MOV-001 | RLT1-03 | El UGV SHALL alcanzar una velocidad máxima en carretera de al menos 75 km/h. | S1 | §3.2.1 | Sí |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

*Tabla de trabajo — continuar en la plantilla Excel para el conjunto completo de requisitos.*

## 6. Observaciones e interdependencias

- Subsistema con mayor número de requisitos:

- Subsistema con más requisitos no verificables por simulación:

- Requisitos [OPCIONAL] identificados:

- Requisitos ambiguos o contradictorios detectados:

- Requisitos derivados de RGEN-11 (propulsión híbrida) en otros subsistemas:

## 7. Entregables

| Entregable | Formato |
|---|---|
| Matriz de requisitos completa | Excel (plantilla) |
| Observaciones e interdependencias | Este documento |
| 15 requisitos ancla consolidados | `recursos/requisitos_ancla.csv` |

## Anexo — Prefijos del pliego

| Prefijo | Sección | Contenido |
|---|---|---|
| RGEN-XX | §3.1 | Generales: arquitectura, propulsión, autonomía, modularidad |
| RLT1-XX | §3.2 | Específicos del UGV de tracción de ruedas |
| ROPE-XX | §3.4–3.5 | Modos de operación (teleoperado, autónomo, offline) |
| RPdO-XX | §3.6 | Puesto de Operación |
| RNAV-XX | §3.7 | Sensores de navegación |
| RCOM-XX | §3.8 | Comunicaciones |
| RSW-XX | §3.9 | Software |
| RPVyA-XX | §3.10 | Pruebas |
| RDOC-XX | §3.11 | Documentación |
