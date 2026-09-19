# Diagrama de Contexto — Sistema UGV (Lote 1)

El siguiente diagrama SysML / UML simplificado representa el sistema de interés como una "caja central" y sus interacciones con los actores externos identificados en la fase de análisis de la necesidad y stakeholders.

```mermaid
flowchart TD
    %% Estilos de Nodos
    classDef actor fill:#f9f9f9,stroke:#333,stroke-width:2px;
    classDef system fill:#003366,stroke:#fff,stroke-width:3px,color:#fff;

    %% Actores Externos
    Cliente["👨‍💼 Cliente\n(CDTI / MINISDEF)"]:::actor
    Operador["🎮 Operador del UGV"]:::actor
    UAV["🚁 UAV de Apoyo"]:::actor
    Mantenimiento["🔧 Personal de\nMantenimiento"]:::actor
    Entorno["🌲 Entorno Operativo\n(Terreno, Clima, Obstáculos)"]:::actor
    Satelites["🛰️ Sistemas GNSS / SATCOM"]:::actor

    %% Sistema Central
    SistemaUGV(("🤖 SISTEMA UGV\n(Lote 1 - Ruedas)")):::system

    %% Interacciones (Flujos)
    Cliente -- "Establece Requisitos\ny Escenarios" --> SistemaUGV
    SistemaUGV -- "Entrega Demostradores\ny Datos de Validación" --> Cliente

    Operador -- "Comandos de Teleoperación\ny Plan de Misión" --> SistemaUGV
    SistemaUGV -- "Vídeo, Telemetría\ny Estado HMI" --> Operador

    UAV -- "Vídeo aéreo para\nConsciencia Situacional" --> SistemaUGV
    SistemaUGV -- "Plataforma de Recarga\n(Función Nodriza)" --> UAV

    Mantenimiento -- "Tareas de 1er Escalón,\nDespliegue y Recuperación" --> SistemaUGV
    SistemaUGV -- "Alertas y Diagnósticos\nde Estado (Offline)" --> Mantenimiento

    Entorno -- "Perturbaciones Físicas,\nClima y Obstáculos" --> SistemaUGV
    SistemaUGV -- "Acción Física Directa\n(Empuje, Remolque, Extinción)" --> Entorno

    Satelites -- "Señales de Posicionamiento\ny Enlace BLOS" --> SistemaUGV
```

> **Nota:** Este diagrama se ha elaborado en base a los stakeholders definidos en el `Doc.01` (Análisis de la Necesidad) y a los requisitos generales de percepción, comunicaciones y operación (`RGEN-01`, `ROPE-01`, `RCOM-01`).
