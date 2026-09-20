# Diagrama de Contexto — Sistema UGV (Lote 1)

El siguiente diagrama SysML / UML simplificado representa el sistema de interés como una "caja central" y sus interacciones con los actores externos identificados en la fase de análisis de la necesidad y stakeholders.

```mermaid
flowchart LR
    %% Actores Externos
    Cliente["Cliente (CDTI / MINISDEF)"]
    Operador["Operador del UGV"]
    UAV["UAV de Apoyo"]
    Mantenimiento["Personal Mantenimiento"]
    Entorno["Entorno Operativo"]
    Satelites["Sistemas GNSS/SATCOM"]

    %% Sistema Central
    SistemaUGV(("SISTEMA UGV\n(Lote 1 - Ruedas)"))

    %% Interacciones
    Cliente <-->|"Requisitos / Demostradores"| SistemaUGV
    Operador <-->|"Comandos / Vídeo y Telemetría"| SistemaUGV
    UAV <-->|"Vídeo aéreo / Base Nodriza"| SistemaUGV
    Mantenimiento <-->|"Reparaciones / Alertas de estado"| SistemaUGV
    Entorno <-->|"Perturbaciones / Acción Física"| SistemaUGV
    Satelites -->|"Señales de Posicionamiento"| SistemaUGV
```

> **Nota:** Este diagrama se ha elaborado en base a los stakeholders definidos en el `Doc.01` (Análisis de la Necesidad) y a los requisitos generales de percepción, comunicaciones y operación (`RGEN-01`, `ROPE-01`, `RCOM-01`).
