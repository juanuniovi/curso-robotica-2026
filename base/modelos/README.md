# Modelo base — `SistemaUGV.slx`

Esqueleto **muy básico** del modelo de arquitectura System Composer del Sistema UGV,
para no empezar la Semana 2 desde una hoja en blanco.

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
| Propiedades de valor formales (tipo + valor + unidad) | **Semana 2** |
| Puertos, asignación de interfaces y conexiones (el IBD) | **Semana 3** |
| Trazabilidad formal con Requirements Toolbox | Semanas 2–3 |

## Cómo usarlo

1. Copia `SistemaUGV.slx` a la carpeta de tu equipo: `equipos/[equipo]/semana-02/`.
2. Trabaja siempre sobre esa copia, no sobre el original de `base/`.
3. Ábrelo en MATLAB R2023b+ con System Composer (`open_system("SistemaUGV")`).

## Regenerarlo

El `.slx` se genera con el script `crear_SistemaUGV.m` (así queda versionado en texto):

```matlab
cd base/modelos
delete SistemaUGV.slx      % el script se niega a sobrescribir
crear_SistemaUGV
```
