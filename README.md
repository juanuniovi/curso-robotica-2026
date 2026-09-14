# Ingeniería Robótica con MBSE
### Robotics Engineering with MBSE

> **4º Grado en Ingeniería Electrónica · 14 semanas · GitHub Pages: [ver web →](https://juanuniovi.github.io/curso-robotica-2026/)**

Proyecto vertebrador: un robot móvil autónomo, definido por un pliego de contratación pública real (contrato de referencia, no identificado en el material del curso).

**Alcance del curso — real vs. banco de pruebas:**
La arquitectura SysML (semanas 1-3) trabaja sobre los 80+ requisitos reales de un contrato de licitación pública, el vehículo completo tal cual se definió en el pliego. La evidencia física de las semanas de ingeniería inversa y calibración no intenta replicar ese vehículo completo — se genera sobre un **robot móvil reducido construido con actuadores de laboratorio**, centrado en **navegación, percepción y autonomía**. Es una verificación honesta a escala reducida, no una réplica física del contrato.

---

## Estructura del repositorio / Repository structure

```
curso-robotica-2026/
├── index.html              ← Página web del curso (GitHub Pages)
├── semanas/                ← Enunciados semanales en PDF/DOCX
│   ├── semana-01/          ← Extracción de requisitos + introducción a SysML
│   ├── semana-02/          ← BDD + propiedades tipadas
│   └── ...
├── modelos/
│   ├── sysml/              ← Modelos de arquitectura SysML (YAML + Mermaid, ver render_arquitectura.py)
│   └── simulacion/         ← Modelos de simulación base del profesor
├── hardware/                ← Banco de pruebas físico: ROS 2, calibración, drivers
├── recursos/                ← Pliego, referencias, plantillas
├── evaluacion/               ← Rúbricas y criterios de evaluación
└── docs/                    ← Guía docente y documentación del curso
```

## Herramientas / Tools

| Herramienta | Versión mínima | Uso |
|---|---|---|
| MATLAB | R2023b | Entorno principal (simulación) |
| Python 3 + PyYAML | — | Modelado de arquitectura (`render_arquitectura.py`) — ver `modelos/sysml/` |
| Simulador físico (por definir) | — | Simulación física |
| Simulink Test | incluido | Verificación de requisitos |
| ROS 2 (Humble/Jazzy) | — | Control del banco de pruebas físico y del UR3 (`Universal_Robots_ROS2_Driver`, MoveIt2) |
| SDK / software de configuración del actuador | — | Configuración y prueba directa de motores |
| Gazebo | — | Simulación software del UR3 / youBot cuando no hay acceso al robot físico |

## Banco de pruebas físico / Physical testbed

Robot móvil reducido sobre un bus de actuadores de laboratorio (dual TTL/RS-485, según el modelo elegido), cada uno con su propio adaptador USB-serie y de alimentación. Sirve como plataforma real de navegación y percepción — no como réplica a escala del vehículo completo del contrato.

## Departamentos / Departments

El curso se organiza como un proceso de contratación simulado: un equipo cliente evalúa a varias empresas licitadoras. Dentro de cada empresa, un interlocutor de Ingeniería de Sistemas coordina tres departamentos técnicos — no por subsistema del vehículo, sino por el tipo de evidencia que producen:

| Departamento | Dominio | Herramientas | Evidencia |
|---|---|---|---|
| Simulación | Simulador físico (eléctrico, transmisión, multicuerpo) | MATLAB, Simulador físico, Simulink Test | Simulación |
| Taller | Banco físico de laboratorio (actuador por determinar) | Software de configuración, SDK | **Física** |
| Software | ROS 2 (driver del actuador, UR3, Gazebo) | ROS 2, MoveIt2, Gazebo | Integración software |

Reparto completo de roles (equipo cliente, interlocutor IS, subperfiles técnicos) y temario semana a semana de cada uno en [`docs/guia-roles-equipos.md`](docs/guia-roles-equipos.md).

## Licencia / License

Material docente de uso educativo. Los modelos de simulación son adaptaciones de repositorios oficiales del fabricante de la herramienta empleada (licencia abierta).
