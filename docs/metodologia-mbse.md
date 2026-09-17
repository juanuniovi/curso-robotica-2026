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

## Origen

Fase | Documento generado a partir de una foto del esquema de la Fig. 3.5 del
libro de Sols, *Systems Engineering — Facilitating the Process of Complex
System Design*, analizada y discutida en el proyecto "Ingeniería de Sistemas"
de claude.ai (17/09/2026).
