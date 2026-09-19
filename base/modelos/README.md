# Modelo base — `sistema.yaml`

Esqueleto **muy básico** del modelo de arquitectura del Sistema UGV, para no empezar la
Fase 5 — Arquitectura desde una hoja en blanco. Es un archivo de datos (YAML), no un archivo de una
herramienta gráfica — se visualiza generando `ARQUITECTURA.md` con `render_arquitectura.py`.

## Qué trae

- Los **bloques de primer nivel**: `UGV`, `PuestoMandoPortable`,
  `DispositivoTelemandoPortable`, `SubsistemaComunicaciones`, `UAVApoyo`.
- El **desglose interno del bloque `UGV`** en 5 subsistemas: `PropulsionEnergia`,
  `MovilidadTrenRodaje`, `PercepcionNavegacion`, `ControlComputacion`,
  `PuntosInterfazCargas`.
- Un **diccionario de interfaces** con 6 interfaces **vacías** (solo el nombre):
  `EnergiaElectrica`, `ParMecanico`, `SenalControl`, `FlujoVideo`, `DatosNavegacion`,
  `EnlaceComunicaciones`.
- Una **descripción por bloque** con las cifras clave y su ID de requisito, como
  ejemplo de la *regla de oro* (todo número lleva su requisito).

## Qué NO trae (es vuestro trabajo)

| Falta | Se hace en |
|---|---|
| Propiedades de valor formales (tipo + valor + unidad) | **Fase 5 — BDD** |
| Interfaces caracterizadas y conexiones (el IBD) | **Fase 5 — IBD** |

## Cómo usarlo

1. Copia `sistema.yaml` a [`modelos/sysml/`](../../modelos/sysml/).
2. Trabaja siempre sobre esa copia, no sobre el original de `base/`.
3. Genera la vista con `python3 render_arquitectura.py modelos/sysml/sistema.yaml -o modelos/sysml/ARQUITECTURA.md`.

Ver [`modelos/sysml/README.md`](../../modelos/sysml/) para el flujo completo.

---

*Un generador MATLAB anterior (`crear_SistemaUGV.m`) queda en esta carpeta sin usar,
como referencia — el flujo activo es el de este documento.*
