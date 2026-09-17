import os, json

# ── Datos de cada fase ──────────────────────────────────────────────────────
# Orden real del proceso (no calendario fijo): Ingeniería inversa del encargo →
# Arquitectura → Plan de Verificación → Plan de Integración → Optimización y
# cierre. Ver docs/metodologia-mbse.md (basado en Sols, Fig. 3.5) para el
# mapeo completo a la cadena de 10 pasos del libro.
#
# estado: "publicado" (hay página real, contenido cerrado) ·
# "por-definir" (todavía no se ha escrito el contenido — no genera página)
fases = [
  {
    "id": "01-ingenieria-inversa", "n": "1", "color": "#2d6a3f",
    "estado": "publicado",
    "nombre_es": "Ingeniería inversa: del pliego al encargo",
    "nombre_en": "Reverse engineering: from the contract to the brief",
    "verbo_es": "Situar", "verbo_en": "Frame",
    "objetivo_es": "Entender qué es la ingeniería de sistemas basada en modelos (MBSE) y el ciclo en V, manejar el vocabulario SysML mínimo (bloque, propiedad, puerto, interfaz, BDD vs IBD, trazabilidad), y deducir del pliego — como quien hace ingeniería inversa de un encargo que no se negoció en persona — la necesidad, el problema, los stakeholders y el concepto de operación (ConOps) del Cliente. Sin herramientas. Mismo trabajo para los cuatro roles.",
    "objetivo_en": "Understand model-based systems engineering (MBSE) and the V-model, handle the minimum SysML vocabulary (block, property, port, interface, BDD vs IBD, traceability), and reverse-engineer from the contract — as you would a brief you never negotiated in person — the Client's need, problem, stakeholders and concept of operations (ConOps). No tools. Same work for all four roles.",
    "tareas_es": [
      "Lectura previa (autónomo): el primer «Introducción a la ingeniería de sistemas y al MBSE» (~15 min) y después el Anexo I anonimizado con este guion: §1 qué es y qué NO es el Sistema UGV · §1.5 los 4 modos de operación · §2 las 3 fases · §3.1 leer todos los RGEN · §3.2 leer todos los RLT1 · lectura rápida §3.4–3.9 · §3.11 RDOC-13 (la arquitectura se entrega en SysML)",
      "Ficha de comprensión — Parte A (conceptos): con tus palabras, qué es la ingeniería de sistemas y por qué modelar en vez de documentar · dibuja el ciclo en V y marca hasta dónde llega este curso (rama descendente, sin Implementación) · define BDD y IBD en una frase cada uno",
      "Ficha — Parte B (el encargo): en 3 frases, qué pide el Cliente, para qué y qué queda fuera · los 4 modos de operación en una frase cada uno · el propósito del vehículo y sus 3 misiones principales con las cifras que las condicionan (velocidad, potencia, autonomía, carga)",
      "Ficha — Parte B: elegir 8 requisitos (con su ID RGEN/RLT) que creas verificables con un modelo de simulación e indicar qué magnitud medirías en cada uno; y 2 requisitos que NO se puedan verificar por simulación, justificando por qué",
      "Ficha — Parte B: 3 términos del glosario que no conocías (con su significado) y 1 pregunta que le harías al Cliente",
      "En equipo: rellenar el Informe de Requisitos (ficha_requisitos_UGV.md) — matriz SHALL, clasificación por verificabilidad y observaciones/interdependencias",
      "Sesión en grupo (modera el rol IS): construir en pizarra el diagrama de contexto del Sistema UGV — caja central + actores: Puesto de Mando, UAV de apoyo, otros UxV, terreno y ambiente, cargas de pago, vehículos tripulados a los que acompaña, obstáculos",
      "Sesión: el rol IS consolida 15 requisitos ancla del equipo (extraídos del Informe de Requisitos) en recursos/requisitos_ancla.csv y reparte provisionalmente qué familia de requisitos mirará cada rol en la fase siguiente",
    ],
    "tareas_en": [
      "Pre-reading (self-study): the «Introduction to systems engineering and MBSE» primer (~15 min), then Annex I with this checklist: §1 what the UGV System is and is NOT · §1.5 the 4 operating modes · §2 the 3 phases · §3.1 read every RGEN · §3.2 read every RLT1 · quick read of §3.4–3.9 · §3.11 RDOC-13 (architecture delivered in SysML)",
      "Comprehension sheet — Part A (concepts): in your own words, what systems engineering is and why model instead of document · sketch the V-model and mark how far this course goes (descending branch only, no Implementation) · define BDD and IBD in one sentence each",
      "Sheet — Part B (the brief): in 3 sentences, what the Client asks for, what for and what is out of scope · the 4 operating modes, one sentence each · the vehicle's purpose and its 3 main missions with the figures that drive them (speed, power, endurance, payload)",
      "Sheet — Part B: pick 8 requirements (with their RGEN/RLT ID) you believe are verifiable with a simulation model, stating which quantity you would measure for each; and 2 requirements that CANNOT be verified by simulation, with justification",
      "Sheet — Part B: 3 glossary terms you did not know (with their meaning) and 1 question you would ask the Client",
      "As a team: fill in the Requirements Report (ficha_requisitos_UGV.md) — SHALL matrix, verifiability classification and observations/interdependencies",
      "Group session (IS role moderates): build the UGV System context diagram on the board — central box + actors: Command Post, support UAV, other UxV, terrain and environment, payloads, manned vehicles it accompanies, obstacles",
      "Session: the IS role consolidates 15 anchor requirements (drawn from the Requirements Report) into recursos/requisitos_ancla.csv and provisionally splits which requirement family each role will look at in the next phase",
    ],
    "entregables_es": [
      "INDIVIDUAL — Ficha de comprensión (Partes A y B), 1 por alumno: copiar fases/01-ingenieria-inversa/comprension/comprension_EJEMPLO.md → comprension_[inicial].md",
      "EQUIPO — Informe de Requisitos (matriz + observaciones): fases/01-ingenieria-inversa/ficha_requisitos_UGV.md",
      "EQUIPO — 15 requisitos ancla consolidados: recursos/requisitos_ancla.csv",
      "EQUIPO — Diagrama de contexto del Sistema UGV (foto o PDF): fases/01-ingenieria-inversa/diagrama-contexto/",
      "1 Pull Request a master con 1 commit por alumno para su ficha de comprensión, y commits del rol IS para el informe, el CSV y el diagrama",
    ],
    "entregables_en": [
      "INDIVIDUAL — Comprehension sheet (Parts A and B), 1 per student: copy fases/01-ingenieria-inversa/comprension/comprension_EJEMPLO.md → comprension_[initial].md",
      "TEAM — Requirements Report (matrix + observations): fases/01-ingenieria-inversa/ficha_requisitos_UGV.md",
      "TEAM — 15 consolidated anchor requirements: recursos/requisitos_ancla.csv",
      "TEAM — UGV System context diagram (photo or PDF): fases/01-ingenieria-inversa/diagrama-contexto/",
      "1 Pull Request to master with 1 commit per student for their comprehension sheet, and commits from the IS role for the report, the CSV and the diagram",
    ],
    "materiales": [
      {"tipo":"md","nombre":"Introducción a la ingeniería de sistemas y al MBSE","archivo":"../../recursos/intro-ingenieria-sistemas.html"},
      {"tipo":"md","nombre":"Anexo I — Requisitos funcionales","archivo":"../../recursos/anexo-I_anonimizado.html"},
      {"tipo":"pdf","nombre":"curso_ROBOT TERRESTRE_Contrato", "archivo":"../../recursos/curso_ROBOT_TERRESTRE_Contrato.pdf"},
      {"tipo":"pdf","nombre":"curso_ROBOT TERRESTRE_Anexo I", "archivo":"../../recursos/curso_ROBOT_TERRESTRE_Anexo_I.pdf"},
      {"tipo":"pptx","nombre":"Introducción a la Ingeniería de Sistemas (transparencias)", "archivo":"Introduccion_Ingenieria_Sistemas.pptx"},
      {"tipo":"md","nombre":"Informe de Requisitos — entregable de equipo, a rellenar", "archivo":"ficha_requisitos_UGV.md"},
      {"tipo":"md","nombre":"Ficha de comprensión — ejemplo/plantilla individual", "archivo":"comprension/comprension_EJEMPLO.md"},
      {"tipo":"csv","nombre":"requisitos_ancla.csv — plantilla (cabecera + 1 fila de ejemplo)", "archivo":"../../recursos/requisitos_ancla.csv"},
      {"tipo":"enlace","nombre":"Metodología del curso (Sols, Fig. 3.5)","archivo":"../../docs/metodologia-mbse.md"},
    ]
  },
  {
    "id": "02-arquitectura", "n": "2", "color": "#1a4f8a",
    "estado": "publicado",
    "nombre_es": "Arquitectura SysML: BDD e IBD de primer nivel",
    "nombre_en": "SysML Architecture: top-level BDD and IBD",
    "verbo_es": "Construir", "verbo_en": "Build",
    "objetivo_es": "Construir el BDD (bloques, propiedades) y el IBD (interfaces, conexiones) de primer nivel del Sistema UGV que pide el RDOC-13, con cada elemento trazado al requisito que lo justifica. Cerrar con una baseline v1.0 de la arquitectura — la columna vertebral técnica de la oferta.",
    "objetivo_en": "Build the top-level BDD (blocks, properties) and IBD (interfaces, connections) of the UGV System required by RDOC-13, with every element traced to the requirement that justifies it. Close with an architecture baseline v1.0 — the technical backbone of the proposal.",
    "tareas_es": [
      "Copiar el modelo base: base/modelos/sistema.yaml → modelos/sysml/sistema.yaml (una sola vez). Ya trae los bloques de primer nivel y el desglose interno del UGV — tu trabajo es rellenar las propiedades",
      "Revisar que están los bloques de primer nivel (RDOC-13.c.1): UGV, Puesto de Mando Portable, Dispositivo de Telemando Portable, Subsistema de Comunicaciones, UAV de apoyo; y el desglose del UGV: Propulsión y energía, Movilidad y tren de rodaje, Percepción y navegación, Control y computación, Puntos de interfaz. Añadir lo que falte",
      "Reparto por rol (según la Fase 1): IS → propiedades de nivel sistema (masa, autonomía, modos) · Simulación → propulsión y movilidad (potencia, par, velocidad, pendiente) · Taller → chasis e interfaces (dimensiones, pesos, RGEN-28) · Software → comunicaciones y control (alcance BLOS RCOM-02, latencia, RSW)",
      "Cada propiedad, dentro del bloque en sistema.yaml: nombre, tipo, valor, unidad y el requisito que la justifica (p. ej. UGV.masa_orden_mision = 9000 kg, requisito RLT1-08). Sin requisito que la justifique, la propiedad no entra",
      "Regenerar la vista: python3 render_arquitectura.py modelos/sysml/sistema.yaml -o modelos/sysml/ARQUITECTURA.md — revisar que no reporta problemas de trazabilidad, y que el BDD coincide con lo esperado",
      "Sobre el BDD ya construido: en la sección interfaces de sistema.yaml, rellenar que_transporta, tipo_unidades y requisito de cada una: EnergiaElectrica, ParMecanico, SenalControl, FlujoVideo, DatosNavegacion, EnlaceComunicaciones",
      "En la sección conexiones, añadir una entrada {origen, destino, interfaz} por cada conexión entre bloques de primer nivel y con el exterior (operador, terreno y ambiente, cargas de pago), según el diagrama de contexto de la Fase 1",
      "Añadir también las conexiones internas del bloque UGV entre sus subsistemas (Propulsión y energía → Movilidad; Percepción y navegación → Control; Control → Comunicaciones…)",
      "Reparto por rol (interfaces): IS → interfaces de sistema y con el exterior · Simulación → EnergiaElectrica y ParMecanico (RGEN-11, RLT1-04/09) · Taller → interfaces mecánicas de los Puntos de Interfaz (RGEN-28) · Software → FlujoVideo, DatosNavegacion, EnlaceComunicaciones (RGEN-22, RNAV-01, RCOM-01/02, RSW-07)",
      "Regenerar la vista de nuevo, revisar el IBD y que no queden interfaces sin requisito. Cerrar la fase con un tag de git: git tag -a baseline-v1.0 -m \"Arquitectura v1.0 — BDD+IBD nivel 1\" && git push origin baseline-v1.0",
    ],
    "tareas_en": [
      "Copy the base model: base/modelos/sistema.yaml → modelos/sysml/sistema.yaml (once only). It already has the top-level blocks and the UGV breakdown — your job is to fill in the properties",
      "Check that the top-level blocks are there (RDOC-13.c.1): UGV, Portable Command Post, Portable Remote-Control Device, Communications Subsystem, support UAV; and the UGV breakdown: Propulsion & energy, Mobility & running gear, Perception & navigation, Control & computing, Interface points. Add whatever is missing",
      "Split by role (from Phase 1): IS → system-level properties (mass, endurance, modes) · Simulation → propulsion & mobility (power, torque, speed, gradient) · Workshop → chassis & interfaces (dimensions, weights, RGEN-28) · Software → communications & control (BLOS range RCOM-02, latency, RSW)",
      "Each property, inside its block in sistema.yaml: name, type, value, unit and the requirement that justifies it (e.g. UGV.mission_mass = 9000 kg, requirement RLT1-08). A property with no justifying requirement does not go in",
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
    "id": "03-plan-verificacion", "n": "3", "color": "#b85c1a",
    "estado": "por-definir",
    "nombre_es": "Plan de Verificación",
    "nombre_en": "Verification Plan",
    "verbo_es": "Planificar", "verbo_en": "Plan",
    "objetivo_es": "Para cada requisito marcado como verificable, definir el método de verificación (análisis, inspección, demostración o simulación) y su criterio de aceptación — sin ejecutar ninguna verificación real. Es parte de la arquitectura descendente (Sols, Cap. 7), no de la ejecución (Cap. 5).",
    "objetivo_en": "For each requirement marked as verifiable, define the verification method (analysis, inspection, demonstration or simulation) and its acceptance criterion — without actually running any verification. This belongs to the descending architecture work (Sols, Ch. 7), not to execution (Ch. 5).",
    "tareas_es": [], "tareas_en": [],
    "entregables_es": [], "entregables_en": [],
    "materiales": []
  },
  {
    "id": "04-plan-integracion", "n": "4", "color": "#6b3fa0",
    "estado": "por-definir",
    "nombre_es": "Plan de Integración",
    "nombre_en": "Integration Plan",
    "verbo_es": "Planificar", "verbo_en": "Plan",
    "objetivo_es": "Definir el esquema de integración entre subsistemas y roles: qué interfaces conectan qué bloques, y en qué orden se ensamblarían — sin integrar físicamente nada.",
    "objetivo_en": "Define the integration scheme between subsystems and roles: which interfaces connect which blocks, and in what order they would be assembled — without physically integrating anything.",
    "tareas_es": [], "tareas_en": [],
    "entregables_es": [], "entregables_en": [],
    "materiales": []
  },
  {
    "id": "05-optimizacion-cierre", "n": "5", "color": "#8a6b00",
    "estado": "por-definir",
    "nombre_es": "Optimización y cierre",
    "nombre_en": "Optimisation & close-out",
    "verbo_es": "Cerrar", "verbo_en": "Close",
    "objetivo_es": "Consolidar el documento de oferta técnica que cierra el curso: solución técnica, justificación de trade-offs, EDT/WBS, cronograma y presupuesto. Es un documento exigente en sí mismo, con su propia estructura y criterios.",
    "objetivo_en": "Consolidate the technical proposal document that closes the course: technical solution, trade-off justification, WBS, schedule and budget. That document is demanding in its own right, with its own structure and criteria.",
    "tareas_es": [], "tareas_en": [],
    "entregables_es": [], "entregables_en": [],
    "materiales": []
  },
]

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
        <span class="lang-es-inline">Fase {s["n"]} de 5</span>
        <span class="lang-en-inline">Phase {s["n"]} of 5</span>
      </span>
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
#           python3 gen_fases.py 01-ingenieria-inversa  → regenera solo la indicada (si está publicada)
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
