# Informe de Requisitos — Sistema UGV

*Ref. pliego: CPP 01/2026 AB — CDTI / Ministerio de Defensa de España*
*Presupuesto del proyecto: 11.905.308 € · Duración: 30 meses*

**Equipo:** ______________&nbsp;&nbsp;&nbsp; **Lote:** ☐ 1 (ruedas) ☐ 2 (cadenas)&nbsp;&nbsp;&nbsp; **Integrantes:** ______________________________

## 1. Alcance

Este documento formaliza en requisitos SHALL verificables el contenido técnico de las secciones 1 a 3 del Anexo I (CPP 01/2026 AB), clasificados por subsistema y por verificabilidad mediante simulación. Es la base de partida para la arquitectura del sistema y para la matriz de verificación posteriores.

*Referencia: Anexo I — Requisitos Funcionales, secciones 1 a 3. Las cláusulas administrativas y los anexos II a IX quedan fuera de alcance.*

## 2. Convención de requisitos

**[ID-REQ] El [sujeto] SHALL [verbo de acción] [condición cuantificable]**
Ejemplo: [REQ-MOV-003] El UGV SHALL alcanzar una velocidad máxima en carretera de 75 km/h como mínimo.

| Nivel | Ejemplo en este proyecto | Verificación |
|---|---|---|
| L0 — Misión | El UGV SHALL eliminar el riesgo para el personal en misiones con medios pesados | No verificable por simulación |
| L1 — Sistema | El UGV SHALL operar de forma autónoma sin tripulación a bordo | Tests de autonomía, campo |
| L2 — Subsistema | El sistema de propulsión SHALL proporcionar 140 kW como mínimo | Simulación — verificable |
| L3 — Componente | El pack de baterías SHALL tener capacidad para 2h de autonomía eléctrica | Simulación — verificable |

## 3. Clasificación por verificabilidad

| Verificable por simulación | No verificable (otra evidencia) |
|---|---|
| Velocidad máxima en carretera ≥ 75 km/h | Resistencia balística a disparos de pequeño calibre |
| Potencia de propulsión ≥ 140 kW | Interoperabilidad con comunicaciones del Ejército |
| Pendiente máxima frontal ≥ 60% | Facilidad de mantenimiento de primer escalón |

## 4. Subsistemas del UGV

| Subsistema | Descripción |
|---|---|
| S1 — Propulsión | Motor eléctrico/combustión, transmisión, tracción, ruedas/cadenas |
| S2 — Energía | Baterías, generador, gestión energética, recarga regenerativa |
| S3 — Suspensión y dinámica | Tren de rodaje, suspensión activa, estabilidad, vadeo |
| S4 — Control y autonomía | Modos de operación, navegación autónoma, detección de obstáculos |
| S5 — Sensores y comunicaciones | LIDAR, cámaras, IMU, GNSS, radio, puesto de mando |
| S0 — Sistema (transversal) | Modularidad, masa total, autonomía global |

## 5. Matriz de requisitos

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

*Tabla de trabajo — continuar en la plantilla Excel para el conjunto completo de requisitos.*

## 6. Observaciones e interdependencias

- Subsistema con mayor número de requisitos:

- Subsistema con más requisitos no verificables por simulación:

- Requisitos [OPCIONAL] identificados:

- Requisitos ambiguos o contradictorios detectados:

- Requisitos derivados de RGEN-11 (propulsión híbrida) en otros subsistemas:

## 7. Diagrama de contexto

UGV como caja central; actores externos (puesto de mando, Ejército/UME, entorno físico, otros vehículos del convoy) y flujos entre ellos (órdenes de misión, telemetría, energía, cargas de pago). *[Adjuntar en esta misma carpeta.]*

## 8. Entregables

| Entregable | Formato |
|---|---|
| Matriz de requisitos completa | Excel (plantilla) |
| Observaciones e interdependencias | Este documento |
| Diagrama de contexto | Foto o PDF |

## Anexo — Prefijos del pliego

| Prefijo | Sección | Contenido |
|---|---|---|
| RGEN-XX | §3.1 | Generales — ambos lotes: arquitectura, propulsión, autonomía, modularidad |
| RLT1-XX / RLT2-XX | §3.2 / §3.3 | Específicos del Lote 1 (ruedas) / Lote 2 (cadenas) |
| ROPE-XX | §3.4–3.5 | Modos de operación (teleoperado, autónomo, offline) |
| RPdO-XX | §3.6 | Puesto de Operación |
| RNAV-XX | §3.7 | Sensores de navegación |
| RCOM-XX | §3.8 | Comunicaciones |
