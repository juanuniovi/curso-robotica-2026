# Metodología MBSE — Curso UGV (basado en Sols, *Systems Engineering*, Fig. 3.5)

## Contexto

El curso termina en la generación de una **oferta técnica** al cliente (parte
descendente de la V), no en la ejecución del contrato. Por tanto, del ciclo
completo de Ingeniería de Sistemas de Sols solo se usa la mitad izquierda del
diagrama (Cap. 4, 6 y 7). Todo lo que corresponde a Cap. 5 y 8 (ejecución real:
verificación física, producción, integración, despliegue, vida operativa,
soporte, retirada) queda **fuera de alcance** — pertenece a la fase
post-adjudicación, no a la oferta.

## Cadena de fases a cubrir (10 pasos)

| # | Fase (Fig. 3.5) | Capítulo del libro |
|---|---|---|
| 1 | Identification of need or opportunity | — |
| 2 | Problem formulation | 4 |
| 3 | Identification of stakeholders | 4 |
| 4 | Concept of Operations (CONOPS) | 4 |
| 5 | Stakeholder requirements *(+ validación / identificación de stakeholders adicionales si hay huecos)* | 7 |
| 6 | Identification of design concepts | 7 |
| 7 | Selection of preferred design concept | 7 |
| 8 | Translation of stakeholder requirements into system requirements **and verification methods** | 7 |
| 9 | Functional analysis | 6 |
| 10 | System architecture | 6 |

**Nota clave sobre la fase 8:** el libro integra la definición de los
**métodos de verificación** dentro de la fase descendente. Esto significa que
el curso sí debe cubrir "cómo se va a verificar" (plan/método), pero no
"verificar de hecho" (Cap. 5, ejecución) — esa ejecución no forma parte de una
oferta.

## Mapeo a los bloques actuales del curso (5 bloques)

| Bloque del curso | Contenido según la cadena MBSE | Qué NO debe incluir |
|---|---|---|
| **Architecture** | Fases 6–10: identificación y selección de conceptos de diseño, traducción a system requirements, functional analysis, system architecture | — |
| **Reverse Engineering** | Fases 1–3: uso del UGV existente / pliego CPP 01/2026 AB como fuente para descubrir necesidad, problema y stakeholders | — |
| **Verification** | Definición del **plan y métodos de verificación** (parte de la fase 8), trazabilidad de requisitos | Ejecución real de pruebas (Cap. 5) |
| **Integration** | Plan de integración de subsistemas entre los 5 equipos (A–E): esquema de interfaces, estrategia de ensamblaje | Integración física real (Cap. 5) |
| **Optimisation / Close-out** | Consolidación final en el documento de oferta: solución técnica + justificación de trade-offs + WBS + cronograma + presupuesto | Despliegue, vida operativa, soporte, retirada (Cap. 8) |

**Recomendación de nomenclatura:** si el nombre de los bloques "Verification"
e "Integration" puede inducir a los estudiantes a pensar que se ejecuta
verificación/integración real, conviene renombrarlos explícitamente como
*"Plan de Verificación"* y *"Plan de Integración"* en la guía docente.

## Documentos de la oferta técnica (orden de generación)

La cadena de 10 fases se consolida en el siguiente paquete documental. El
orden refleja dependencias reales, no solo secuencia temporal en el curso.

| # | Documento | Fases MBSE que cubre | Depende de |
|---|---|---|---|
| Doc.01 | Análisis de la Necesidad / Problem Statement | Need or opportunity, Problem formulation, Identification of stakeholders | — |
| Doc.02 | CONOPS (Concepto de Operaciones) | Concept of Operations | Doc.01 |
| Doc.03 | Documento de Requisitos de las Partes Interesadas (StRD) | Stakeholder requirements (+ validación) | Doc.02 |
| Doc.04 | Estudio de Conceptos y Selección (Trade-off / AoA) | Identification of design concepts, Selection of preferred design concept | Doc.03 |
| Doc.05 | Documento de Requisitos de Sistema (SyRD) | Translation of stakeholder requirements into system requirements **and verification methods** | Doc.03 + Doc.04 |
| Doc.06 | Arquitectura del Sistema (funcional + física) | Functional analysis, System architecture | Doc.05 |
| Doc.07 | Plan de Verificación e Integración (matriz de trazabilidad, métodos ya definidos en Doc.05, esquema de integración entre equipos) | parte de la fase 8 + planificación | Doc.05 + Doc.06 |
| Doc.08 | Plan de gestión — WBS, cronograma, presupuesto, riesgos (documento **paralelo**, no secuencial en la cadena técnica) | — (transversal) | Puede arrancar en paralelo desde Doc.01 |
| Oferta final | Propuesta Técnica compilada — síntesis de Doc.01–07 + Doc.08 | — | Todos los anteriores |

**Total: 8 documentos técnicos + 1 documento de síntesis (la oferta) = 9.**

**Correspondencia con la evaluación real de CPP 02/2025 SENSOR IR:** la cadena
lógica identificada en la evaluación (Doc.05 → Doc.07 → Doc.08, con Doc.06
como documento de planificación paralelo) sigue el mismo patrón —
documento técnico secuencial + documento de gestión en paralelo, no en la
cadena de dependencia principal. Útil como ejemplo real en clase: los
estudiantes generan el mismo tipo de paquete que se evalúa después en un
proceso de licitación real.

**Matices de puesta en práctica:**

1. Doc.08 (gestión/WBS/cronograma/presupuesto) no depende de la cadena
   técnica — debe arrancar en la Semana 1 en paralelo, no esperar a que
   esté cerrada la arquitectura.
2. La oferta final no es un documento nuevo desde cero: es la
   compilación/síntesis ejecutiva de los 8 anteriores con narrativa de
   propuesta — corresponde al bloque *Optimisation/Close-out*.

## Origen

Fase | Documento generado a partir de una foto del esquema de la Fig. 3.5 del
libro de Sols, *Systems Engineering — Facilitating the Process of Complex
System Design*, analizada y discutida en el proyecto "Ingeniería de Sistemas"
de claude.ai (17/09/2026).
