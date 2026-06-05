# Ingeniería de Sistemas con MBSE y Simscape
### Systems Engineering with MBSE and Simscape

> **4º Grado en Ingeniería Electrónica · 14 semanas · GitHub Pages: [ver web →](https://[usuario].github.io/ugv-course/)**

Proyecto vertebrador: **CPP 01/2026 AB** — UGV pesado autónomo para misiones de seguridad y defensa (CDTI / Ministerio de Defensa de España, 11.9M€)

---

## Estructura del repositorio / Repository structure

```
ugv-course/
├── index.html              ← Página web del curso (GitHub Pages)
├── semanas/                ← Enunciados semanales en PDF/DOCX
│   ├── semana-01/          ← Extracción de requisitos
│   ├── semana-1b/          ← Introducción SysML / System Composer
│   ├── semana-02/          ← IBD + interfaces + trazabilidad
│   └── ...
├── modelos/
│   ├── sysml/              ← Modelos System Composer (.slx)
│   └── simscape/           ← Modelos Simscape base del profesor
├── recursos/               ← Pliego CDTI, referencias, plantillas
├── evaluacion/             ← Rúbricas y criterios de evaluación
└── docs/                   ← Guía docente y documentación del curso
```

## Herramientas / Tools

| Herramienta | Versión mínima | Uso |
|---|---|---|
| MATLAB | R2023b | Entorno principal |
| System Composer | incluido | Modelado SysML |
| Simscape | incluido | Simulación física |
| Simulink Test | incluido | Verificación de requisitos |

## Equipos / Teams

| Equipo | Subsistema | Dominio Simscape |
|---|---|---|
| A | Propulsión | Electrical + Driveline |
| B | Energía | Electrical (Battery) |
| C | Suspensión | Multibody |
| D | Control y Autonomía | Stateflow |
| E | Sensores y Comunicaciones | Signals |

## Licencia / License

Material docente de uso educativo. Los modelos Simscape son adaptaciones de repositorios oficiales de MathWorks (licencia abierta).
