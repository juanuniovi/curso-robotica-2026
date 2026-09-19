# Análisis de la Necesidad — Sistema UGV

**Equipo:** IS-Antigravity&nbsp;&nbsp;&nbsp; **Integrantes:**  Agente IS

## 1. Alcance

Este documento formaliza el análisis de la necesidad y de las partes interesadas (Doc.01,
según `docs/metodologia-mbse.md`) a partir de las secciones 1 y 2 del Anexo I (CPP 01/2026 AB):
qué problema resuelve el sistema, para quién, y quién tiene interés en él. Es la base de la que
parte el CONOPS (Fase 2) y el Documento de Requisitos de las Partes Interesadas (Fase 3).

*Referencia: Anexo I — Requisitos Funcionales, §1 (Introducción, objetivo y alcance) y §2 (Fases
de ejecución). Las cláusulas administrativas y los anexos II a IX quedan fuera de alcance.*

## 2. Necesidad y problema

**¿Qué necesidad u oportunidad motiva el encargo?**
Los sistemas terrestres no tripulados (UGV) son necesarios para ejecutar tareas peligrosas o penosas (intervención en emergencias, incendios, limpieza de rutas) sin exponer vidas humanas. Sin embargo, existe un vacío tecnológico en soluciones modulares de gran tamaño (pesados) que mantengan altas prestaciones de movilidad y capacidad de carga. Se requiere de I+D para llevar estas plataformas de gran tonelaje a un nivel de madurez tecnológica (TRL) alto aplicable a operaciones reales.

**¿Qué problema concreto debe resolver el Sistema UGV?** 
Diseñar y desarrollar un UGV pesado multipropósito con capacidades autónomas, de carácter modular. Debe poder transportar grandes cargas y reconfigurarse rápidamente para misiones muy diversas mediante módulos funcionales. El problema exige concebir un robot robusto de forma nativa (sin cabina para humanos), con un potente tren de propulsión híbrido y una arquitectura abierta que permita operar con gran movilidad todoterreno e interoperar con otros vehículos tripulados y no tripulados (UxV).

**¿Qué queda explícitamente fuera del alcance del sistema a diseñar?** 
Queda fuera del alcance de nuestra oferta técnica el desarrollo de las cargas de pago opcionales (no obligatorias), la ejecución física real de las pruebas de verificación en fábrica/campo (solo llegaremos a la fase de diseño y planificación, Doc.07), las cláusulas puramente administrativas del contrato y, explícitamente para este proyecto, el diseño del UGV de tracción de cadenas (Lote 2), centrándonos de forma exclusiva en el Lote 1 (tracción de ruedas).

## 3. Identificación de los stakeholders

| Stakeholder | Rol / interés en el sistema | Fuente en el Anexo I |
|---|---|---|
| Cliente (CDTI / MINISDEF) | Contrata el desarrollo; define requisitos, financia el I+D y aprueba los criterios de aceptación. | §1, todo el documento |
| Operador del UGV | Teleopera, supervisa la autonomía y ejecuta las misiones desde el Puesto de Operación. | §1.5, §3.6 |
| UAV de apoyo (y su operador) | Proporciona consciencia situacional aérea y apoyo a la teleoperación y navegación del UGV. | §1.3, §3.4 |
| Unidades operativas en campo | Ejecutan las misiones representativas en la Fase III de validación en entornos pre-operacionales. | §6 |
| Personal de Mantenimiento | Realiza operaciones de primer escalón, preparación logística, transporte y reparación post-misión. | §1.3, §2 |
| Redes de Comunicaciones | Interés en la interoperabilidad (5G, radio militar táctica y enlaces por terminal SATCOM civil/militar). | §3.8 |
| Ciudadanía civil | Beneficiaria indirecta en escenarios duales: emergencias, rescate, extinción de incendios y vialidad. | §1.1, §1.2 |

## 4. Diagrama de contexto

El diagrama de contexto (Sistema UGV como caja central, actores externos y flujos entre ellos)
se ha generado utilizando SysML/Mermaid y se encuentra en [`diagrama-contexto/diagrama-contexto.md`](diagrama-contexto/diagrama-contexto.md).

## 5. Entregables de esta fase

| Entregable | Formato | Dónde |
|---|---|---|
| Este documento (necesidad, problema, stakeholders) | Markdown | esta carpeta |
| Diagrama de contexto | Markdown (Mermaid) | [`diagrama-contexto/`](diagrama-contexto/) |
