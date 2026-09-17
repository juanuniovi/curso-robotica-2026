import os, json

# ── Datos de cada fase ──────────────────────────────────────────────────────
# 7 fases, una por cada documento técnico de la oferta (Doc.01-07) más el
# cierre (Doc.08 + oferta final) — ver docs/metodologia-mbse.md, sección
# "Documentos de la oferta técnica". No hay calendario fijo: cada fase se
# publica cuando de verdad se llega a ella.
#
# estado: "publicado" (hay página real, contenido cerrado) ·
# "por-definir" (todavía no se ha escrito el contenido — no genera página)
fases = [
  {
    "id": "01-analisis-necesidad", "n": "1", "color": "#2d6a3f",
    "estado": "publicado", "doc": "Doc.01",
    "nombre_es": "Análisis de la Necesidad", "nombre_en": "Needs Analysis",
    "verbo_es": "Situar", "verbo_en": "Frame",
    "objetivo_es": "Entender qué es la ingeniería de sistemas basada en modelos (MBSE) y el ciclo en V, manejar el vocabulario SysML mínimo (bloque, propiedad, puerto, interfaz, BDD vs IBD, trazabilidad), y deducir del pliego — como quien hace ingeniería inversa de un encargo que no se negoció en persona — qué necesidad y qué problema motivan el Sistema UGV, y quiénes son sus stakeholders. Sin herramientas. Mismo trabajo para los cuatro roles.",
    "objetivo_en": "Understand model-based systems engineering (MBSE) and the V-model, handle the minimum SysML vocabulary (block, property, port, interface, BDD vs IBD, traceability), and reverse-engineer from the contract — as you would a brief you never negotiated in person — the need and problem behind the UGV System, and who its stakeholders are. No tools. Same work for all four roles.",
    "tareas_es": [
      "Lectura previa (autónomo): el primer «Introducción a la ingeniería de sistemas y al MBSE» (~15 min) y después el Anexo I anonimizado con este guion: §1 qué es y qué NO es el Sistema UGV · §1.5 los 4 modos de operación · §2 las 3 fases · §3.1 leer todos los RGEN · §3.2 leer todos los RLT1 · lectura rápida §3.4–3.9 · §3.11 RDOC-13 (la arquitectura se entrega en SysML)",
      "Ficha de comprensión — Parte A (conceptos): con tus palabras, qué es la ingeniería de sistemas y por qué modelar en vez de documentar · dibuja el ciclo en V y marca hasta dónde llega este curso (rama descendente, sin Implementación) · define BDD y IBD en una frase cada uno",
      "Ficha — Parte B: en 3 frases, qué pide el Cliente, para qué y qué queda fuera · 3 términos del glosario que no conocías (con su significado) y 1 pregunta que le harías al Cliente",
      "En equipo: rellenar el Análisis de la Necesidad (analisis_necesidad_UGV.md) — necesidad, problema, alcance y tabla de stakeholders",
      "Sesión en grupo (modera el rol IS): construir en pizarra el diagrama de contexto del Sistema UGV — caja central + actores: Puesto de Mando, UAV de apoyo, otros UxV, terreno y ambiente, cargas de pago, vehículos tripulados a los que acompaña, obstáculos",
    ],
    "tareas_en": [
      "Pre-reading (self-study): the «Introduction to systems engineering and MBSE» primer (~15 min), then Annex I with this checklist: §1 what the UGV System is and is NOT · §1.5 the 4 operating modes · §2 the 3 phases · §3.1 read every RGEN · §3.2 read every RLT1 · quick read of §3.4–3.9 · §3.11 RDOC-13 (architecture delivered in SysML)",
      "Comprehension sheet — Part A (concepts): in your own words, what systems engineering is and why model instead of document · sketch the V-model and mark how far this course goes (descending branch only, no Implementation) · define BDD and IBD in one sentence each",
      "Sheet — Part B: in 3 sentences, what the Client asks for, what for and what is out of scope · 3 glossary terms you did not know (with their meaning) and 1 question you would ask the Client",
      "As a team: fill in the Needs Analysis (analisis_necesidad_UGV.md) — need, problem, scope and stakeholder table",
      "Group session (IS role moderates): build the UGV System context diagram on the board — central box + actors: Command Post, support UAV, other UxV, terrain and environment, payloads, manned vehicles it accompanies, obstacles",
    ],
    "entregables_es": [
      "INDIVIDUAL — Ficha de comprensión (Partes A y B), 1 por alumno: copiar fases/01-analisis-necesidad/comprension/comprension_EJEMPLO.md → comprension_[inicial].md",
      "EQUIPO — Análisis de la Necesidad (Doc.01): fases/01-analisis-necesidad/analisis_necesidad_UGV.md",
      "EQUIPO — Diagrama de contexto del Sistema UGV (foto o PDF): fases/01-analisis-necesidad/diagrama-contexto/",
      "1 Pull Request a master con 1 commit por alumno para su ficha de comprensión, y commits del rol IS para el documento y el diagrama",
    ],
    "entregables_en": [
      "INDIVIDUAL — Comprehension sheet (Parts A and B), 1 per student: copy fases/01-analisis-necesidad/comprension/comprension_EJEMPLO.md → comprension_[initial].md",
      "TEAM — Needs Analysis (Doc.01): fases/01-analisis-necesidad/analisis_necesidad_UGV.md",
      "TEAM — UGV System context diagram (photo or PDF): fases/01-analisis-necesidad/diagrama-contexto/",
      "1 Pull Request to master with 1 commit per student for their comprehension sheet, and commits from the IS role for the document and the diagram",
    ],
    "materiales": [
      {"tipo":"md","nombre":"Introducción a la ingeniería de sistemas y al MBSE","archivo":"../../recursos/intro-ingenieria-sistemas.html"},
      {"tipo":"md","nombre":"Anexo I — Requisitos funcionales","archivo":"../../recursos/anexo-I_anonimizado.html"},
      {"tipo":"pdf","nombre":"curso_ROBOT TERRESTRE_Contrato", "archivo":"../../recursos/curso_ROBOT_TERRESTRE_Contrato.pdf"},
      {"tipo":"pdf","nombre":"curso_ROBOT TERRESTRE_Anexo I", "archivo":"../../recursos/curso_ROBOT_TERRESTRE_Anexo_I.pdf"},
      {"tipo":"pptx","nombre":"Introducción a la Ingeniería de Sistemas (transparencias)", "archivo":"Introduccion_Ingenieria_Sistemas.pptx"},
      {"tipo":"md","nombre":"Análisis de la Necesidad — entregable de equipo, a rellenar", "archivo":"analisis_necesidad_UGV.md"},
      {"tipo":"md","nombre":"Ficha de comprensión — ejemplo/plantilla individual", "archivo":"comprension/comprension_EJEMPLO.md"},
      {"tipo":"enlace","nombre":"Metodología del curso (Sols, Fig. 3.5)","archivo":"../../docs/metodologia-mbse.md"},
    ]
  },
  {
    "id": "02-conops", "n": "2", "color": "#0e7c86",
    "estado": "publicado", "doc": "Doc.02",
    "nombre_es": "CONOPS — Concepto de Operaciones", "nombre_en": "CONOPS — Concept of Operations",
    "verbo_es": "Describir", "verbo_en": "Describe",
    "objetivo_es": "Formalizar cómo se usa el Sistema UGV en la práctica: sus modos de operación, sus misiones típicas y un escenario operacional de referencia. El CONOPS traduce la necesidad de la Fase 1 en un uso concreto, y es lo que la Fase 3 tiene que satisfacer con requisitos verificables.",
    "objetivo_en": "Formalise how the UGV System is used in practice: its operating modes, typical missions and a reference operational scenario. The CONOPS translates the Phase 1 need into concrete use, and is what Phase 3 has to satisfy with verifiable requirements.",
    "tareas_es": [
      "Repasar en el Anexo I: §1.5 (definición de términos), §3.4 (modos de operación) y §3.5 (ejecución de misiones)",
      "Reparto por rol: cada rol redacta la descripción de 1 modo de operación (de los 4) con sus propias palabras, y qué Equipo de Control lo activa",
      "En equipo: describir las 3 misiones principales del UGV con las cifras que las condicionan (velocidad, potencia, autonomía, carga), citando el ID de requisito de cada cifra",
      "En equipo: dibujar o describir el ciclo de vida de una misión (Planeamiento → Ejecución → Finalización, ROPE-07) señalando el modo de operación de cada etapa",
      "En equipo: elegir una familia de misión de ROPE-09 y redactar un escenario operacional de referencia (5-8 líneas), incluyendo qué pasa si se pierde el enlace de comunicaciones (RCOM-03)",
    ],
    "tareas_en": [
      "Review in Annex I: §1.5 (definition of terms), §3.4 (operating modes) and §3.5 (mission execution)",
      "Split by role: each role writes up the description of 1 operating mode (of the 4) in their own words, and which Control Equipment activates it",
      "As a team: describe the UGV's 3 main missions with the figures that drive them (speed, power, endurance, payload), citing the requirement ID for each figure",
      "As a team: sketch or describe a mission's life cycle (Planning → Execution → Closeout, ROPE-07) marking the operating mode of each stage",
      "As a team: pick one ROPE-09 mission family and write a reference operational scenario (5-8 lines), including what happens if the communications link is lost (RCOM-03)",
    ],
    "entregables_es": [
      "EQUIPO — CONOPS (Doc.02: modos, misiones, ciclo de vida, escenario): fases/02-conops/conops_UGV.md",
      "1 Pull Request a master; commits por rol en la sección de modos de operación",
    ],
    "entregables_en": [
      "TEAM — CONOPS (Doc.02: modes, missions, life cycle, scenario): fases/02-conops/conops_UGV.md",
      "1 Pull Request to master; per-role commits on the operating modes section",
    ],
    "materiales": [
      {"tipo":"md","nombre":"Anexo I — Requisitos funcionales","archivo":"../../recursos/anexo-I_anonimizado.html"},
      {"tipo":"md","nombre":"CONOPS — entregable de equipo, a rellenar","archivo":"conops_UGV.md"},
    ]
  },
  {
    "id": "03-requisitos-partes-interesadas", "n": "3", "color": "#1a4f8a",
    "estado": "publicado", "doc": "Doc.03",
    "nombre_es": "Requisitos de las Partes Interesadas (StRD)", "nombre_en": "Stakeholder Requirements (StRD)",
    "verbo_es": "Formalizar", "verbo_en": "Formalise",
    "objetivo_es": "Traducir la necesidad (Fase 1) y el CONOPS (Fase 2) en requisitos SHALL verificables, clasificados por subsistema y por verificabilidad mediante simulación. Es la base de trazabilidad de todo lo que sigue: nada entra en el Estudio de Conceptos ni en la arquitectura sin un requisito que lo justifique.",
    "objetivo_en": "Translate the need (Phase 1) and the CONOPS (Phase 2) into verifiable SHALL requirements, classified by subsystem and by simulation-verifiability. This is the traceability foundation for everything that follows: nothing enters the Concept Study or the architecture without a requirement that justifies it.",
    "tareas_es": [
      "Leer la sección 3 completa del Anexo I (requisitos técnicos), con el guion ya seguido en la Fase 1",
      "Ficha de comprensión (si no se hizo en la Fase 1): elegir 8 requisitos (ID RGEN/RLT) verificables por simulación e indicar qué magnitud medirías en cada uno; y 2 requisitos NO verificables por simulación, justificando por qué",
      "En equipo: rellenar el StRD (ficha_requisitos_UGV.md) — matriz SHALL, clasificación por verificabilidad, el posible medio de evidencia de cada requisito verificable (qué se simularía o mediría, sin ejecutarlo todavía) y observaciones/interdependencias",
      "Sesión: el rol IS consolida 15 requisitos ancla del equipo (extraídos del StRD) en recursos/requisitos_ancla.csv y reparte provisionalmente qué familia de requisitos mirará cada rol en la Fase 4",
    ],
    "tareas_en": [
      "Read the full section 3 of Annex I (technical requirements), following the checklist already used in Phase 1",
      "Comprehension sheet (if not done in Phase 1): pick 8 requirements (RGEN/RLT ID) verifiable by simulation and state which quantity you would measure for each; and 2 requirements NOT verifiable by simulation, with justification",
      "As a team: fill in the StRD (ficha_requisitos_UGV.md) — SHALL matrix, verifiability classification, the possible evidence means for each verifiable requirement (what you would simulate or measure, without running it yet) and observations/interdependencies",
      "Session: the IS role consolidates 15 anchor requirements (drawn from the StRD) into recursos/requisitos_ancla.csv and provisionally splits which requirement family each role will look at in Phase 4",
    ],
    "entregables_es": [
      "EQUIPO — StRD (Doc.03: matriz SHALL + observaciones): fases/03-requisitos-partes-interesadas/ficha_requisitos_UGV.md",
      "EQUIPO — 15 requisitos ancla consolidados: recursos/requisitos_ancla.csv",
      "1 Pull Request a master con commits del rol IS para el informe y el CSV",
    ],
    "entregables_en": [
      "TEAM — StRD (Doc.03: SHALL matrix + observations): fases/03-requisitos-partes-interesadas/ficha_requisitos_UGV.md",
      "TEAM — 15 consolidated anchor requirements: recursos/requisitos_ancla.csv",
      "1 Pull Request to master with IS-role commits for the report and the CSV",
    ],
    "materiales": [
      {"tipo":"md","nombre":"Anexo I — Requisitos funcionales","archivo":"../../recursos/anexo-I_anonimizado.html"},
      {"tipo":"md","nombre":"StRD — entregable de equipo, a rellenar","archivo":"ficha_requisitos_UGV.md"},
      {"tipo":"csv","nombre":"requisitos_ancla.csv — plantilla (cabecera + 1 fila de ejemplo)", "archivo":"../../recursos/requisitos_ancla.csv"},
    ]
  },
  {
    "id": "04-estudio-conceptos", "n": "4", "color": "#6b3fa0",
    "estado": "publicado", "doc": "Doc.04",
    "nombre_es": "Estudio de Conceptos y Selección", "nombre_en": "Concept Study & Selection",
    "verbo_es": "Comparar", "verbo_en": "Compare",
    "objetivo_es": "Antes de modelar en SysML, identificar concepciones alternativas de la solución y seleccionar una de forma justificada y trazable a los requisitos (RLT1-02: configuración 4×4, 6×6 u 8×8), mediante una matriz de decisión ponderada (AoA). Sin este paso, la arquitectura de la Fase 5 sería una elección arbitraria.",
    "objetivo_en": "Before modelling in SysML, identify alternative design concepts and select one in a justified, requirement-traceable way (RLT1-02: 4×4, 6×6 or 8×8 configuration), using a weighted decision matrix (AoA). Without this step, the Phase 5 architecture would be an arbitrary choice.",
    "tareas_es": [
      "Leer RLT1-02 y las propiedades de movilidad relacionadas (RLT1-03 a RLT1-09) en el StRD de la Fase 3",
      "Describir las 3 alternativas de configuración (4×4, 6×6, 8×8): implicaciones en tren de rodaje, suspensión (S3) y puntos de interfaz de cargas de pago (RGEN-28)",
      "Definir entre 4 y 6 criterios de decisión, cada uno trazado a un requisito, con pesos que sumen 100% — y para cada criterio, qué posible medio de evidencia (simulación, cálculo analítico, croquis) respaldaría la puntuación",
      "Puntuar cada alternativa en cada criterio (escala 1-5), apoyándote en el medio de evidencia identificado, y calcular la puntuación ponderada total — matriz AoA",
      "Seleccionar la configuración con mayor puntuación y redactar la justificación, incluyendo qué implica para las propiedades del bloque MovilidadTrenRodaje en la Fase 5",
    ],
    "tareas_en": [
      "Read RLT1-02 and the related mobility properties (RLT1-03 to RLT1-09) in the Phase 3 StRD",
      "Describe the 3 configuration alternatives (4×4, 6×6, 8×8): implications for running gear, suspension (S3) and payload interface points (RGEN-28)",
      "Define 4 to 6 decision criteria, each traced to a requirement, with weights summing to 100% — and for each criterion, what possible evidence means (simulation, analytical calculation, sketch) would back the score",
      "Score each alternative on each criterion (1-5 scale), backed by the identified evidence means, and compute the total weighted score — AoA matrix",
      "Select the highest-scoring configuration and write the justification, including what it implies for the MovilidadTrenRodaje block's properties in Phase 5",
    ],
    "entregables_es": [
      "EQUIPO — Estudio de Conceptos y Selección (Doc.04: alternativas, criterios, matriz AoA, decisión): fases/04-estudio-conceptos/estudio_conceptos_UGV.md",
      "1 Pull Request a master",
    ],
    "entregables_en": [
      "TEAM — Concept Study & Selection (Doc.04: alternatives, criteria, AoA matrix, decision): fases/04-estudio-conceptos/estudio_conceptos_UGV.md",
      "1 Pull Request to master",
    ],
    "materiales": [
      {"tipo":"md","nombre":"Estudio de Conceptos — entregable de equipo, a rellenar","archivo":"estudio_conceptos_UGV.md"},
    ]
  },
  {
    "id": "05-arquitectura", "n": "5", "color": "#b8860b",
    "estado": "publicado", "doc": "Doc.05 + Doc.06",
    "nombre_es": "Arquitectura SysML: BDD e IBD de primer nivel", "nombre_en": "SysML Architecture: top-level BDD and IBD",
    "verbo_es": "Construir", "verbo_en": "Build",
    "objetivo_es": "Traducir los requisitos de partes interesadas en requisitos de sistema y construir el BDD (bloques, propiedades) y el IBD (interfaces, conexiones) de primer nivel del Sistema UGV que pide el RDOC-13, sobre la configuración seleccionada en la Fase 4, con cada elemento trazado al requisito que lo justifica. Cerrar con una baseline v1.0 de la arquitectura — la columna vertebral técnica de la oferta.",
    "objetivo_en": "Translate stakeholder requirements into system requirements and build the top-level BDD (blocks, properties) and IBD (interfaces, connections) of the UGV System required by RDOC-13, on top of the Phase 4 configuration, with every element traced to the requirement that justifies it. Close with an architecture baseline v1.0 — the technical backbone of the proposal.",
    "tareas_es": [
      "Copiar el modelo base: base/modelos/sistema.yaml → modelos/sysml/sistema.yaml (una sola vez). Ya trae los bloques de primer nivel y el desglose interno del UGV — tu trabajo es rellenar las propiedades",
      "Revisar que están los bloques de primer nivel (RDOC-13.c.1): UGV, Puesto de Mando Portable, Dispositivo de Telemando Portable, Subsistema de Comunicaciones, UAV de apoyo; y el desglose del UGV: Propulsión y energía, Movilidad y tren de rodaje, Percepción y navegación, Control y computación, Puntos de interfaz. Añadir lo que falte",
      "Reparto por rol (según la Fase 3): IS → propiedades de nivel sistema (masa, autonomía, modos) · Simulación → propulsión y movilidad (potencia, par, velocidad, pendiente — según la configuración elegida en la Fase 4) · Taller → chasis e interfaces (dimensiones, pesos, RGEN-28) · Software → comunicaciones y control (alcance BLOS RCOM-02, latencia, RSW)",
      "Cada propiedad, dentro del bloque en sistema.yaml: nombre, tipo, valor, unidad y el requisito que la justifica (p. ej. UGV.masa_orden_mision = 9000 kg, requisito RLT1-08). Sin requisito que la justifique, la propiedad no entra",
      "En INFORME.md, sección «Posibilidades de evidencia»: para las propiedades críticas de propulsión y movilidad, anotar qué simulación o ensayo de banco podría demostrar que el valor es alcanzable — sin ejecutarlo todavía",
      "Regenerar la vista: python3 render_arquitectura.py modelos/sysml/sistema.yaml -o modelos/sysml/ARQUITECTURA.md — revisar que no reporta problemas de trazabilidad, y que el BDD coincide con lo esperado",
      "Sobre el BDD ya construido, en la sección interfaces de sistema.yaml, rellenar que_transporta, tipo_unidades y requisito de cada una: EnergiaElectrica, ParMecanico, SenalControl, FlujoVideo, DatosNavegacion, EnlaceComunicaciones",
      "En la sección conexiones, añadir una entrada {origen, destino, interfaz} por cada conexión entre bloques de primer nivel y con el exterior (operador, terreno y ambiente, cargas de pago), según el diagrama de contexto de la Fase 1",
      "Añadir también las conexiones internas del bloque UGV entre sus subsistemas (Propulsión y energía → Movilidad; Percepción y navegación → Control; Control → Comunicaciones…)",
      "Reparto por rol (interfaces): IS → interfaces de sistema y con el exterior · Simulación → EnergiaElectrica y ParMecanico (RGEN-11, RLT1-04/09) · Taller → interfaces mecánicas de los Puntos de Interfaz (RGEN-28) · Software → FlujoVideo, DatosNavegacion, EnlaceComunicaciones (RGEN-22, RNAV-01, RCOM-01/02, RSW-07)",
      "Regenerar la vista de nuevo, revisar el IBD y que no queden interfaces sin requisito. Cerrar la fase con un tag de git: git tag -a baseline-v1.0 -m \"Arquitectura v1.0 — BDD+IBD nivel 1\" && git push origin baseline-v1.0",
    ],
    "tareas_en": [
      "Copy the base model: base/modelos/sistema.yaml → modelos/sysml/sistema.yaml (once only). It already has the top-level blocks and the UGV breakdown — your job is to fill in the properties",
      "Check that the top-level blocks are there (RDOC-13.c.1): UGV, Portable Command Post, Portable Remote-Control Device, Communications Subsystem, support UAV; and the UGV breakdown: Propulsion & energy, Mobility & running gear, Perception & navigation, Control & computing, Interface points. Add whatever is missing",
      "Split by role (from Phase 3): IS → system-level properties (mass, endurance, modes) · Simulation → propulsion & mobility (power, torque, speed, gradient — per the Phase 4 configuration) · Workshop → chassis & interfaces (dimensions, weights, RGEN-28) · Software → communications & control (BLOS range RCOM-02, latency, RSW)",
      "Each property, inside its block in sistema.yaml: name, type, value, unit and the requirement that justifies it (e.g. UGV.mission_mass = 9000 kg, requirement RLT1-08). A property with no justifying requirement does not go in",
      "In INFORME.md, «Possible evidence» section: for the critical propulsion and mobility properties, note what simulation or bench test could demonstrate the value is achievable — without running it yet",
      "Regenerate the view: python3 render_arquitectura.py modelos/sysml/sistema.yaml -o modelos/sysml/ARQUITECTURA.md — check it reports no traceability problems, and that the BDD matches what's expected",
      "On top of the finished BDD: in the interfaces section of sistema.yaml, fill in que_transporta, tipo_unidades and requisito for each one: EnergiaElectrica, ParMecanico, SenalControl, FlujoVideo, DatosNavegacion, EnlaceComunicaciones",
      "In the conexiones section, add one {origen, destino, interfaz} entry per connection between top-level blocks and with the exterior (operator, terrain and environment, payloads), following the Phase 1 context diagram",
      "Also add the internal connections of the UGV block between its subsystems (Propulsion & energy → Mobility; Perception & navigation → Control; Control → Communications…)",
      "Split by role (interfaces): IS → system and external interfaces · Simulation → EnergiaElectrica and ParMecanico (RGEN-11, RLT1-04/09) · Workshop → mechanical interfaces of the interface points (RGEN-28) · Software → FlujoVideo, DatosNavegacion, EnlaceComunicaciones (RGEN-22, RNAV-01, RCOM-01/02, RSW-07)",
      "Regenerate the view again, check the IBD and that no interface is left without a requirement. Close the phase with a git tag: git tag -a baseline-v1.0 -m \"Architecture v1.0 — level-1 BDD+IBD\" && git push origin baseline-v1.0",
    ],
    "entregables_es": [
      "EQUIPO — sistema.yaml completo (BDD + IBD: bloques, propiedades, interfaces, conexiones): modelos/sysml/sistema.yaml",
      "EQUIPO — ARQUITECTURA.md regenerado (BDD + IBD, tablas de propiedades e interfaces): modelos/sysml/ARQUITECTURA.md",
      "EQUIPO — Informe de Arquitectura (reparto por rol, observaciones, checklist): modelos/sysml/INFORME.md",
      "Tag de git baseline-v1.0 sobre el commit que cierra la fase",
      "1 Pull Request a master; 1 commit por rol: feat([rol]): arquitectura BDD+IBD nivel 1",
    ],
    "entregables_en": [
      "TEAM — Full sistema.yaml (BDD + IBD: blocks, properties, interfaces, connections): modelos/sysml/sistema.yaml",
      "TEAM — Regenerated ARQUITECTURA.md (BDD + IBD, property and interface tables): modelos/sysml/ARQUITECTURA.md",
      "TEAM — Architecture Report (role split, observations, checklist): modelos/sysml/INFORME.md",
      "Git tag baseline-v1.0 on the commit that closes the phase",
      "1 Pull Request to master; 1 commit per role: feat([role]): top-level BDD+IBD architecture",
    ],
    "materiales": [
      {"tipo":"pptx","nombre":"Arquitectura del Sistema: BDD e IBD (transparencias)","archivo":"Arquitectura_BDD_IBD.pptx"},
      {"tipo":"código","nombre":"Script de render — render_arquitectura.py","archivo":"../../render_arquitectura.py"},
      {"tipo":"código","nombre":"Modelo base — sistema.yaml","archivo":"../../base/modelos/sistema.yaml"},
      {"tipo":"md","nombre":"Anexo I — Requisitos funcionales","archivo":"../../recursos/anexo-I_anonimizado.html"},
      {"tipo":"md","nombre":"Informe de Arquitectura — entregable de equipo, a rellenar","archivo":"../../modelos/sysml/INFORME.md"},
    ]
  },
  {
    "id": "06-plan-verificacion-integracion", "n": "6", "color": "#b85c1a",
    "estado": "por-definir", "doc": "Doc.07",
    "nombre_es": "Plan de Verificación e Integración", "nombre_en": "Verification & Integration Plan",
    "verbo_es": "Planificar", "verbo_en": "Plan",
    "objetivo_es": "Consolidar en un único documento (Doc.07) la matriz de trazabilidad requisito↔método de verificación (definido en la Fase 5 al traducir requisitos de sistema) y el esquema de integración entre subsistemas y roles — sin ejecutar ninguna verificación ni integración real.",
    "objetivo_en": "Consolidate in a single document (Doc.07) the requirement↔verification-method traceability matrix (defined in Phase 5 when translating system requirements) and the integration scheme between subsystems and roles — without actually running any verification or integration.",
    "tareas_es": [], "tareas_en": [],
    "entregables_es": [], "entregables_en": [],
    "materiales": []
  },
  {
    "id": "07-optimizacion-cierre", "n": "7", "color": "#c8382a",
    "estado": "por-definir", "doc": "Doc.08 + Oferta final",
    "nombre_es": "Optimización y cierre", "nombre_en": "Optimisation & close-out",
    "verbo_es": "Cerrar", "verbo_en": "Close",
    "objetivo_es": "Consolidar el documento de oferta técnica que cierra el curso: síntesis de los Doc.01-07, más el plan de gestión (Doc.08: EDT/WBS, cronograma y presupuesto, transversal desde la Fase 1). Es un documento exigente en sí mismo, con su propia estructura y criterios.",
    "objetivo_en": "Consolidate the technical proposal document that closes the course: a synthesis of Doc.01-07, plus the management plan (Doc.08: WBS, schedule and budget, running in parallel since Phase 1). That document is demanding in its own right, with its own structure and criteria.",
    "tareas_es": [], "tareas_en": [],
    "entregables_es": [], "entregables_en": [],
    "materiales": []
  },
]

TOTAL_FASES = len(fases)

# ── Iconos por tipo de material ──────────────────────────────────────────────
ICONOS = {
  "docx":   ("📄", "#1a4f8a", "#e8f0fb"),
  "pdf":    ("📕", "#c8382a", "#fdecea"),
  "xlsx":   ("📊", "#2d6a3f", "#e8f5ec"),
  "slx":    ("⚙️",  "#6b3fa0", "#f3edfb"),
  "código": ("💻", "#333333", "#f2f2f2"),
  "enlace": ("🔗", "#0077aa", "#e6f4ff"),
  "zip":    ("📦", "#8a6b00", "#fdf8e1"),
  "md":     ("📘", "#1a4f8a", "#e8f0fb"),
  "pptx":   ("📽️", "#b8860b", "#f6efd8"),
  "csv":    ("📊", "#2d6a3f", "#e8f5ec"),
}

# ── Plantilla HTML de cada fase ───────────────────────────────────────────────
def gen_html(s):
  color = s["color"]

  def lista(items_es, items_en):
    li_es = "".join(f'<li class="lang-es">{x}</li>' for x in items_es)
    li_en = "".join(f'<li class="lang-en">{x}</li>' for x in items_en)
    return f'<ul class="item-list">{li_es}{li_en}</ul>'

  def materiales_html():
    if not s["materiales"]:
      return '''
      <div class="no-materiales">
        <span class="lang-es">Los materiales se publicarán antes de empezar esta fase.</span>
        <span class="lang-en">Materials will be published before this phase starts.</span>
      </div>'''
    cards = ""
    for m in s["materiales"]:
      ico, col, bg = ICONOS.get(m["tipo"], ("📄","#333","#f2f2f2"))
      # md/enlace/html se abren en el navegador; el resto se descargan
      abrir = m["tipo"] in ("md", "enlace", "html")
      attrs = 'target="_blank" rel="noopener"' if abrir else 'download'
      flecha = "↗" if abrir else "↓"
      cards += f'''
      <a class="mat-card" href="{m['archivo']}" {attrs}>
        <span class="mat-icon" style="background:{bg};color:{col}">{ico}</span>
        <div class="mat-info">
          <span class="mat-nombre">{m['nombre']}</span>
          <span class="mat-tipo" style="color:{col}">{m['tipo'].upper()}</span>
        </div>
        <span class="mat-dl" style="color:{col}">{flecha}</span>
      </a>'''
    return cards

  return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Fase {s["n"]} · Robótica-MBSE</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@300;400&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{
  --ink:#0d1117;--ink-soft:#3d4451;--ink-muted:#6e7787;
  --paper:#f6f4ef;--paper-warm:#ede9e0;
  --accent:{color};
  --border:rgba(13,17,23,.10);
  --font-d:'Syne',sans-serif;--font-b:'DM Sans',sans-serif;--font-m:'DM Mono',monospace;
}}
body{{font-family:var(--font-b);background:var(--paper);color:var(--ink);line-height:1.6;font-size:16px}}
.lang-en{{display:none}}
body.en .lang-es{{display:none}}
body.en .lang-en{{display:block}}
body.en .lang-en-inline{{display:inline}}
body.en .lang-es-inline{{display:none}}
.lang-en-inline{{display:none}}
.lang-es-inline{{display:inline}}
/* listas bilingües: ganan en especificidad a .item-list li / .entregable-list li */
.item-list li.lang-en,.entregable-list li.lang-en{{display:none}}
body.en .item-list li.lang-es,body.en .entregable-list li.lang-es{{display:none}}
body.en .item-list li.lang-en,body.en .entregable-list li.lang-en{{display:flex}}

/* topbar */
.topbar{{position:sticky;top:0;z-index:100;display:flex;align-items:center;justify-content:space-between;padding:0 2rem;height:52px;background:var(--ink);border-bottom:2px solid var(--accent)}}
.topbar-logo{{font-family:var(--font-d);font-size:1rem;font-weight:700;color:var(--paper);text-decoration:none;letter-spacing:.08em}}
.topbar-logo span{{color:var(--accent)}}
.topbar-right{{display:flex;align-items:center;gap:1rem}}
.back-link{{font-family:var(--font-m);font-size:.72rem;color:rgba(246,244,239,.6);text-decoration:none;letter-spacing:.05em;transition:color .2s}}
.back-link:hover{{color:var(--paper)}}
.lang-btn{{font-family:var(--font-m);font-size:.72rem;background:none;border:1px solid rgba(246,244,239,.3);color:rgba(246,244,239,.65);padding:.25rem .7rem;border-radius:4px;cursor:pointer;transition:all .2s;letter-spacing:.1em}}
.lang-btn:hover{{border-color:var(--paper);color:var(--paper)}}

/* hero */
.hero{{background:var(--ink);padding:3.5rem 2rem 3rem;position:relative;overflow:hidden}}
.hero::after{{content:'';position:absolute;bottom:0;left:0;right:0;height:4px;background:var(--accent)}}
.hero-inner{{max-width:900px;margin:0 auto}}
.hero-tags{{display:flex;gap:.6rem;flex-wrap:wrap;margin-bottom:1.2rem}}
.tag{{font-family:var(--font-m);font-size:.65rem;letter-spacing:.12em;text-transform:uppercase;padding:.25rem .7rem;border-radius:3px;border:1px solid rgba(246,244,239,.15);color:rgba(246,244,239,.55)}}
.tag-accent{{background:rgba(255,255,255,.07);border-color:var(--accent);color:var(--accent)}}
.hero-n{{font-family:var(--font-d);font-size:clamp(3rem,8vw,5.5rem);font-weight:800;line-height:1;color:rgba(246,244,239,.08);position:absolute;right:2rem;top:2rem;pointer-events:none;user-select:none}}
.hero-titulo{{font-family:var(--font-d);font-size:clamp(1.6rem,3vw,2.4rem);font-weight:800;color:var(--paper);line-height:1.1;margin-bottom:.8rem}}
.hero-titulo em{{font-style:normal;color:var(--accent)}}
.hero-meta{{display:flex;gap:1.5rem;flex-wrap:wrap;margin-top:1.2rem}}
.meta-item{{display:flex;align-items:center;gap:.4rem;font-family:var(--font-m);font-size:.72rem;color:rgba(246,244,239,.45)}}
.meta-item strong{{color:rgba(246,244,239,.75);font-weight:400}}

/* layout */
.main{{max-width:720px;margin:0 auto;padding:2.5rem 2rem 4rem}}

/* secciones */
.section{{margin-bottom:2.5rem}}
.section-label{{font-family:var(--font-m);font-size:.65rem;letter-spacing:.18em;text-transform:uppercase;color:var(--accent);margin-bottom:.6rem}}
.section-title{{font-family:var(--font-d);font-size:1.15rem;font-weight:700;color:var(--ink);margin-bottom:1rem}}
.objetivo-box{{background:white;border:1px solid var(--border);border-left:4px solid var(--accent);border-radius:0 8px 8px 0;padding:1.2rem 1.4rem;font-size:.95rem;color:var(--ink-soft);line-height:1.7}}
.item-list{{list-style:none;display:flex;flex-direction:column;gap:.5rem}}
.item-list li{{display:flex;align-items:flex-start;gap:.6rem;font-size:.9rem;color:var(--ink-soft);line-height:1.55}}
.item-list li::before{{content:'→';color:var(--accent);font-family:var(--font-m);font-size:.8rem;margin-top:.1rem;flex-shrink:0}}
.entregable-list{{list-style:none;display:flex;flex-direction:column;gap:.5rem}}
.entregable-list li{{display:flex;align-items:flex-start;gap:.6rem;font-size:.9rem;color:var(--ink-soft);background:white;border:1px solid var(--border);border-radius:8px;padding:.7rem 1rem;line-height:1.55}}
.entregable-list li::before{{content:'✓';color:var(--accent);font-family:var(--font-m);font-weight:700;flex-shrink:0}}

/* materiales */
.materiales-grid{{display:flex;flex-direction:column;gap:.7rem}}
.mat-card{{display:flex;align-items:center;gap:1rem;background:white;border:1px solid var(--border);border-radius:10px;padding:.9rem 1.1rem;text-decoration:none;color:var(--ink);transition:box-shadow .2s,transform .2s}}
.mat-card:hover{{box-shadow:0 4px 20px rgba(0,0,0,.08);transform:translateY(-1px)}}
.mat-icon{{width:42px;height:42px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:1.3rem;flex-shrink:0}}
.mat-info{{flex:1}}
.mat-nombre{{font-family:var(--font-d);font-size:.9rem;font-weight:600;display:block;margin-bottom:.15rem}}
.mat-tipo{{font-family:var(--font-m);font-size:.65rem;letter-spacing:.1em;text-transform:uppercase}}
.mat-dl{{font-size:1.3rem;font-weight:300;opacity:.5;transition:opacity .2s}}
.mat-card:hover .mat-dl{{opacity:1}}
.no-materiales{{background:var(--paper-warm);border:1px dashed rgba(13,17,23,.2);border-radius:8px;padding:1.5rem;text-align:center;font-size:.88rem;color:var(--ink-muted);font-family:var(--font-m)}}

/* nav fases */
.nav-fases{{display:flex;justify-content:space-between;align-items:center;margin-top:3rem;padding-top:1.5rem;border-top:1px solid var(--border)}}
.nav-btn{{font-family:var(--font-m);font-size:.75rem;color:var(--ink-muted);text-decoration:none;padding:.5rem .9rem;border:1px solid var(--border);border-radius:6px;transition:all .2s;letter-spacing:.04em}}
.nav-btn:hover{{color:var(--ink);border-color:var(--ink)}}
.nav-btn.disabled{{opacity:.3;pointer-events:none}}
</style>
</head>
<body>

<nav class="topbar">
  <a class="topbar-logo" href="../../index.html"><span>Robótica</span>-MBSE</a>
  <div class="topbar-right">
    <a class="back-link" href="../../index.html#proceso">
      <span class="lang-es-inline">← Todas las fases</span>
      <span class="lang-en-inline">← All phases</span>
    </a>
    <button class="lang-btn" onclick="document.body.classList.toggle('en')">EN / ES</button>
  </div>
</nav>

<div class="hero">
  <div class="hero-n">{s["n"]}</div>
  <div class="hero-inner">
    <div class="hero-tags">
      <span class="tag tag-accent">
        <span class="lang-es-inline">Fase {s["n"]} de {TOTAL_FASES}</span>
        <span class="lang-en-inline">Phase {s["n"]} of {TOTAL_FASES}</span>
      </span>
      <span class="tag">{s["doc"]}</span>
    </div>
    <h1 class="hero-titulo">
      <span class="lang-es">{s["nombre_es"]}</span>
      <span class="lang-en">{s["nombre_en"]}</span>
    </h1>
    <div class="hero-meta">
      <div class="meta-item">
        <span class="lang-es-inline">Verbo clave:</span>
        <span class="lang-en-inline">Key verb:</span>
        <strong>
          <span class="lang-es-inline">{s["verbo_es"]}</span>
          <span class="lang-en-inline">{s["verbo_en"]}</span>
        </strong>
      </div>
    </div>
  </div>
</div>

<main class="main">

  <div class="section">
    <p class="section-label"><span class="lang-es-inline">Objetivo</span><span class="lang-en-inline">Objective</span></p>
    <div class="objetivo-box">
      <span class="lang-es">{s["objetivo_es"]}</span>
      <span class="lang-en">{s["objetivo_en"]}</span>
    </div>
  </div>

  <div class="section">
    <p class="section-label"><span class="lang-es-inline">Tareas</span><span class="lang-en-inline">Tasks</span></p>
    {lista(s["tareas_es"], s["tareas_en"])}
  </div>

  <div class="section">
    <p class="section-label"><span class="lang-es-inline">Entregables</span><span class="lang-en-inline">Deliverables</span></p>
    <ul class="entregable-list">
      {"".join(f'<li class="lang-es">{x}</li>' for x in s["entregables_es"])}
      {"".join(f'<li class="lang-en">{x}</li>' for x in s["entregables_en"])}
    </ul>
  </div>

  <div class="section">
    <p class="section-label"><span class="lang-es-inline">Materiales</span><span class="lang-en-inline">Materials</span></p>
    <div class="materiales-grid">
      {materiales_html()}
    </div>
  </div>

  <nav class="nav-fases">
    <a class="nav-btn" href="../../index.html#proceso">
      <span class="lang-es-inline">← Índice</span>
      <span class="lang-en-inline">← Index</span>
    </a>
    <a class="nav-btn" href="../../index.html">
      <span class="lang-es-inline">🏠 Inicio</span>
      <span class="lang-en-inline">🏠 Home</span>
    </a>
  </nav>

</main>
</body>
</html>'''

# ── Generar los index.html ──────────────────────────────────────────────────
# Curso en construcción incremental: solo se publican páginas de fases con
# "estado": "publicado". Las demás quedan como borrador en este archivo, sin
# generar página, hasta que de verdad lleguemos a esa fase.
# Ejecuta:  python3 gen_fases.py                       → regenera todas las fases publicadas
#           python3 gen_fases.py 01-analisis-necesidad  → regenera solo la indicada (si está publicada)
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
FASES_DIR = os.path.join(BASE, "fases")
solo = set(sys.argv[1:])

generadas = 0
for s in fases:
  if solo and s["id"] not in solo:
    continue
  if s.get("estado") != "publicado":
    if solo:
      print(f"⏭ fases/{s['id']}/ — por definir (estado != publicado), no generada")
    continue
  path = os.path.join(FASES_DIR, s["id"], "index.html")
  os.makedirs(os.path.dirname(path), exist_ok=True)
  with open(path, "w", encoding="utf-8") as f:
    f.write(gen_html(s))
  print(f"✓ fases/{s['id']}/index.html")
  generadas += 1

print("Total páginas generadas:", generadas)
