# Informe de Arquitectura — BDD del Sistema UGV

*Ref. pliego: CPP 01/2026 AB — CDTI / Ministerio de Defensa de España*
*RDOC-13 — Vista de Sistemas y Subsistemas*

**Equipo:** ______________&nbsp;&nbsp;&nbsp; **Lote:** ☐ 1 (ruedas) ☐ 2 (cadenas)

## 1. Alcance

Este documento formaliza el Block Definition Diagram (BDD) de primer y segundo nivel del Sistema UGV a partir del modelo base (`modelos/sysml/SistemaUGV.slx`): confirma la jerarquía de bloques, asigna propiedades de valor (tipo, valor, unidad) y traza cada una al requisito del pliego que la justifica. Es la base sobre la que la Semana 3 construye las interfaces y el IBD.

## 2. Bloques de nivel 1 — Sistema UGV

| Bloque | Contenido | Referencias |
|---|---|---|
| `UGV` | Vehículo terrestre no tripulado de tracción de ruedas. Masa en orden de misión ≤ 9000 kg; autonomía ≥ 8 h o 400 km; autonomía eléctrica ≥ 2 h o 100 km. | RLT1-08, RGEN-14, RGEN-15 |
| `PuestoMandoPortable` | Puesto de operación + comunicaciones + alimentación. 3 interfaces independientes (conducción, misión, carga útil). | RPdO-06 |
| `DispositivoTelemandoPortable` | Tipo tablet con joystick, para teleoperación cercana. | ROPE-03 |
| `SubsistemaComunicaciones` | 3 módulos (5G, radio, satélite); alcance BLOS ≥ 20 km. | RCOM-01, RCOM-02 |
| `UAVApoyo` | Apoyo a teleoperación y consciencia situacional; modos TELEOPERADO y CAUTIVO VIRTUAL. | ROPE-04 |

## 3. Bloques de nivel 2 — desglose interno de `UGV`

| Bloque | Contenido | Referencias |
|---|---|---|
| `PropulsionEnergia` | Propulsión híbrida: motor eléctrico + combustión (biocombustible 100%) + baterías. Potencia total ≥ 140 kW. | RGEN-11 a RGEN-13, RLT1-09 |
| `MovilidadTrenRodaje` | Tren de ruedas 4x4/6x6/8x8, tracción independiente por rueda, suspensión neumática regulable. v_carretera ≥ 75 km/h, pendiente frontal ≥ 60%. | RLT1-04, RLT1-05, RLT1-03 |
| `PercepcionNavegacion` | Detección de obstáculos (LiDAR/radar/visión) con modo SIGILOSO; navegación alternativa al GNSS, ≥ 3 tecnologías, ≥ 5 km sin señal. | RGEN-09, RNAV-01 |
| `ControlComputacion` | Computación embarcada y control drive-by-wire. Frenado automático anticolisión. Modos TELEOPERADO / AUTÓNOMO / FUERA DE LÍNEA. | RGEN-17, ROPE-01 |
| `PuntosInterfazCargas` | Puntos de interfaz mecánicos/eléctricos/lógicos para cargas de pago obligatorias (CP-01, CP-04, CP-09, CP-10, CP-14) sin comprometer la estabilidad. | RGEN-28 |

## 4. Reparto de propiedades por rol

| Rol | Ámbito |
|---|---|
| IS | Propiedades de nivel sistema: masa, autonomía, modos |
| Simulación | Propulsión y movilidad: potencia, par, velocidad, pendiente |
| Taller | Chasis e interfaces: dimensiones, pesos, puntos de interfaz (RGEN-28) |
| Software | Comunicaciones y control: alcance BLOS (RCOM-02), latencia, software (RSW) |

## 5. Tabla de propiedades

Cada propiedad lleva nombre, tipo, valor, unidad y el ID del requisito que la justifica. Sin requisito que la justifique, la propiedad no entra en el modelo.

Tabla de trabajo completa en [`propiedades.csv`](propiedades.csv):

| bloque | propiedad | tipo | valor | unidad | id_requisito |
|---|---|---|---|---|---|
| UGV | masa_orden_mision | double | 9000 | kg | RLT1-08 |
| | | | | | |
| | | | | | |

## 6. Observaciones

- Bloques con menos de 2 propiedades tipadas:

- Propiedades sin requisito que las justifique (pendientes de completar o descartar):

- Discrepancias detectadas entre el modelo base y el Anexo I:

## 7. Entregables

| Entregable | Formato |
|---|---|
| `SistemaUGV.slx` con el BDD de primer y segundo nivel | `modelos/sysml/SistemaUGV.slx` |
| Diagrama BDD exportado | `evidencias/` |
| Tabla de propiedades | `propiedades.csv` |
| Este informe | Este documento |

## Anexo — Checklist

| # | Verificación | OK |
|---|---|---|
| 1 | El modelo tiene los 5 bloques de nivel 1 con los nombres exactos de la sección 2 | ☐ |
| 2 | El bloque `UGV` tiene los 5 bloques internos con los nombres exactos de la sección 3 | ☐ |
| 3 | Cada propiedad tiene tipo, valor, unidad y un ID de requisito en su descripción | ☐ |
| 4 | La jerarquía verificada en el Model Browser coincide con las secciones 2 y 3 | ☐ |
| 5 | El modelo abre correctamente en otro equipo antes de dar la semana por cerrada | ☐ |
