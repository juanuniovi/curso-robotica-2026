import os, json

# ── Datos de cada semana ──────────────────────────────────────────────────────
semanas = [
  {
    "id": "semana-01", "n": "1", "bloque": "I", "color": "#1a4f8a",
    "titulo_es": "Extracción de requisitos del pliego",
    "titulo_en": "Requirements extraction from the contract",
    "verbo_es": "Extraer", "verbo_en": "Extract",
    "tipo": "grupal",
    "duracion_es": "1 sesión de 2h + 2h trabajo autónomo",
    "duracion_en": "1 × 2h session + 2h self-study",
    "objetivo_es": "Leer el Anexo I del pliego CPP 01/2026 AB e identificar, clasificar y formalizar todos los requisitos técnicos numerados en formato SHALL con trazabilidad al texto original.",
    "objetivo_en": "Read Annex I of contract CPP 01/2026 AB and identify, classify and formalise all numbered technical requirements in SHALL format with traceability to the original text.",
    "tareas_es": ["Lectura activa del pliego con código de colores (verde/amarillo/naranja)","Transformación a formato SHALL: [ID] El [sujeto] SHALL [verbo] [condición]","Asignación de cada requisito a su subsistema (S1–S5)","Identificación de requisitos verificables con Simscape","Diagrama de contexto del sistema (caja con flechas)"],
    "tareas_en": ["Active reading of the contract with colour coding (green/yellow/orange)","Transformation to SHALL format: [ID] The [subject] SHALL [verb] [condition]","Assignment of each requirement to its subsystem (S1–S5)","Identification of requirements verifiable with Simscape","System context diagram (box with arrows)"],
    "entregables_es": ["Tabla de requisitos (Excel): ID · Texto SHALL · Subsistema · Fuente § · Simscape","Respuestas escritas a las preguntas de análisis (máx. 1 página)","Diagrama de contexto del sistema (foto o PDF)"],
    "entregables_en": ["Requirements table (Excel): ID · SHALL text · Subsystem · Source § · Simscape","Written answers to analysis questions (max. 1 page)","System context diagram (photo or PDF)"],
    "materiales": [
      {"tipo":"docx","nombre":"Enunciado Semana 1","archivo":"Semana1_Ejercicio_Requisitos_UGV.docx"},
    ]
  },
  {
    "id": "semana-1b", "n": "1·5", "bloque": "I", "color": "#1a4f8a",
    "titulo_es": "Introducción a SysML y System Composer",
    "titulo_en": "Introduction to SysML and System Composer",
    "verbo_es": "Nombrar", "verbo_en": "Name",
    "tipo": "grupal",
    "duracion_es": "1 sesión de laboratorio de 2h",
    "duracion_en": "1 × 2h lab session",
    "objetivo_es": "Abrir MATLAB System Composer por primera vez y construir el BDD de nivel 1 del UGV: cinco bloques de subsistema con propiedades tipadas, valoradas y trazadas al pliego.",
    "objetivo_en": "Open MATLAB System Composer for the first time and build the UGV level-1 BDD: five subsystem blocks with typed, valued properties traced to the contract.",
    "tareas_es": ["Crear el proyecto SistemaUGV en System Composer","Añadir los 5 bloques de subsistema con sus propiedades (potencia, masa, autonomía…)","Verificar la jerarquía en el Model Browser","Añadir la relación de composición","Exportar el modelo como imagen PNG"],
    "tareas_en": ["Create the SistemaUGV project in System Composer","Add the 5 subsystem blocks with their properties (power, mass, autonomy…)","Verify the hierarchy in the Model Browser","Add the composition relationship","Export the model as PNG image"],
    "entregables_es": ["Modelo SysML (.slx) con BDD nivel 1","Capturas del Model Browser anotadas con IDs de requisitos","Pregunta de reflexión: ¿qué propiedad fue más difícil de representar?"],
    "entregables_en": ["SysML model (.slx) with level-1 BDD","Model Browser screenshots annotated with requirement IDs","Reflection question: which property was hardest to represent?"],
    "materiales": [
      {"tipo":"docx","nombre":"Enunciado Semana 1·5","archivo":"Semana1b_Introduccion_SysML_SystemComposer.docx"},
    ]
  },
  {
    "id": "semana-02", "n": "2", "bloque": "I", "color": "#1a4f8a",
    "titulo_es": "IBD, interfaces y trazabilidad",
    "titulo_en": "IBD, interfaces and traceability",
    "verbo_es": "Conectar", "verbo_en": "Connect",
    "tipo": "grupal",
    "duracion_es": "2 sesiones de laboratorio de 2h",
    "duracion_en": "2 × 2h lab sessions",
    "objetivo_es": "Añadir al modelo SysML los puertos tipados de cada bloque, las interfaces que definen qué fluye por cada conexión, e importar y vincular los requisitos desde la tabla Excel al modelo.",
    "objetivo_en": "Add typed ports to each block, define interfaces specifying what flows through each connection, and import and link requirements from the Excel table to the model.",
    "tareas_es": ["Definir las 7 interfaces principales en el Interface Editor","Añadir puertos In/Out a cada bloque con tipo de interfaz asignado","Dibujar las conexiones del IBD","Importar requisitos desde Excel con slreq.import()","Vincular cada requisito al bloque responsable","Generar el esqueleto Simulink con Create Behavior Model"],
    "tareas_en": ["Define the 7 main interfaces in the Interface Editor","Add In/Out ports to each block with assigned interface type","Draw IBD connections","Import requirements from Excel using slreq.import()","Link each requirement to its responsible block","Generate Simulink skeleton with Create Behavior Model"],
    "entregables_es": ["Modelo SysML completo (.slx) + esqueleto Simulink (.slx)","Captura del Requirements Editor con requisitos vinculados","Justificación de interfaces: cada interfaz citando el requisito que la justifica"],
    "entregables_en": ["Complete SysML model (.slx) + Simulink skeleton (.slx)","Requirements Editor screenshot with linked requirements","Interface justification: each interface citing its justifying requirement"],
    "materiales": [
      {"tipo":"docx","nombre":"Enunciado Semana 2","archivo":"Semana2_Arquitectura_SysML_SystemComposer.docx"},
    ]
  },
  {
    "id": "semana-03", "n": "3", "bloque": "I", "color": "#1a4f8a",
    "titulo_es": "Formalización y revisión de arquitectura",
    "titulo_en": "Architecture formalisation and review",
    "verbo_es": "Formalizar", "verbo_en": "Formalise",
    "tipo": "grupal",
    "duracion_es": "1 sesión de laboratorio de 2h",
    "duracion_en": "1 × 2h lab session",
    "objetivo_es": "Completar el BDD de segundo nivel, revisar la coherencia de toda la arquitectura mediante revisión cruzada entre equipos y obtener el visto bueno antes de pasar a simulación.",
    "objetivo_en": "Complete the second-level BDD, review the coherence of the full architecture through cross-team review, and get approval before moving to simulation.",
    "tareas_es": ["Completar los componentes internos del subsistema asignado (BDD nivel 2)","Revisión cruzada: inspeccionar el IBD del equipo adyacente","Comprobar coherencia de interfaces entre equipos","Corregir discrepancias y cerrar el modelo v1.0"],
    "tareas_en": ["Complete internal components of assigned subsystem (BDD level 2)","Cross-review: inspect the IBD of the adjacent team","Check interface coherence between teams","Fix discrepancies and close model v1.0"],
    "entregables_es": ["Modelo SysML v1.0 cerrado y validado","Acta de revisión cruzada: discrepancias encontradas y soluciones adoptadas"],
    "entregables_en": ["Closed and validated SysML model v1.0","Cross-review record: discrepancies found and solutions adopted"],
    "materiales": []
  },
  {
    "id": "semana-04", "n": "4", "bloque": "II", "color": "#2d6a3f",
    "titulo_es": "Caja negra: ejecutar el modelo Simscape",
    "titulo_en": "Black box: run the Simscape model",
    "verbo_es": "Observar", "verbo_en": "Observe",
    "tipo": "individual",
    "duracion_es": "1 sesión de laboratorio de 2h",
    "duracion_en": "1 × 2h lab session",
    "objetivo_es": "Ejecutar el modelo Simscape completo del UGV sin abrir ningún subsistema, observar las salidas y desarrollar intuición sobre el comportamiento del sistema antes de analizarlo.",
    "objetivo_en": "Run the complete UGV Simscape model without opening any subsystem, observe outputs and develop intuition about system behaviour before analysing it.",
    "tareas_es": ["Abrir y ejecutar el modelo base proporcionado por el profesor","Registrar variables de entrada y salida con sus unidades","Modificar 3 parámetros y observar el efecto en las salidas","Formular hipótesis sobre la estructura interna"],
    "tareas_en": ["Open and run the base model provided by the instructor","Record input and output variables with their units","Modify 3 parameters and observe the effect on outputs","Formulate hypotheses about the internal structure"],
    "entregables_es": ["Ficha de observación individual: variables I/O, unidades, efecto de cambios de parámetros, 3 hipótesis sobre la estructura interna"],
    "entregables_en": ["Individual observation form: I/O variables, units, effect of parameter changes, 3 hypotheses about the internal structure"],
    "materiales": []
  },
  {
    "id": "semana-05", "n": "5", "bloque": "II", "color": "#2d6a3f",
    "titulo_es": "Caja gris: abrir el subsistema asignado",
    "titulo_en": "Grey box: open the assigned subsystem",
    "verbo_es": "Descomponer", "verbo_en": "Decompose",
    "tipo": "grupal",
    "duracion_es": "1 sesión de laboratorio de 2h + 2h trabajo autónomo",
    "duracion_en": "1 × 2h lab session + 2h self-study",
    "objetivo_es": "Entrar en el subsistema asignado del modelo Simscape, identificar los bloques que lo componen, trazar el flujo físico y construir el IBD de segundo nivel en System Composer.",
    "objetivo_en": "Enter the assigned subsystem of the Simscape model, identify its blocks, trace the physical flow and build the second-level IBD in System Composer.",
    "tareas_es": ["Abrir el subsistema asignado en Simulink","Identificar los bloques Simscape y sus dominios físicos","Trazar el flujo de energía/señal en papel","Actualizar el modelo SysML con los componentes encontrados","Construir tabla SysML↔Simscape"],
    "tareas_en": ["Open the assigned subsystem in Simulink","Identify Simscape blocks and their physical domains","Trace the energy/signal flow on paper","Update the SysML model with the found components","Build SysML↔Simscape table"],
    "entregables_es": ["Tabla de correspondencia SysML↔Simscape","IBD de segundo nivel actualizado en System Composer"],
    "entregables_en": ["SysML↔Simscape correspondence table","Updated second-level IBD in System Composer"],
    "materiales": []
  },
  {
    "id": "semana-06", "n": "6", "bloque": "II", "color": "#2d6a3f",
    "titulo_es": "Caja blanca: trazabilidad inversa",
    "titulo_en": "White box: reverse traceability",
    "verbo_es": "Trazar", "verbo_en": "Trace",
    "tipo": "grupal",
    "duracion_es": "1 sesión de laboratorio de 2h + 2h trabajo autónomo",
    "duracion_en": "1 × 2h lab session + 2h self-study",
    "objetivo_es": "Identificar los parámetros críticos de cada bloque Simscape y construir la tabla de trazabilidad inversa completa: parámetro → propiedad SysML → requisito SHALL.",
    "objetivo_en": "Identify the critical parameters of each Simscape block and build the complete reverse traceability table: parameter → SysML property → SHALL requirement.",
    "tareas_es": ["Análisis de sensibilidad: modificar cada parámetro ±20% y observar el efecto","Completar la tabla de trazabilidad inversa","Identificar parámetros sin requisito asociado (señal de alerta)"],
    "tareas_en": ["Sensitivity analysis: modify each parameter ±20% and observe the effect","Complete the reverse traceability table","Identify parameters without an associated requirement (warning signal)"],
    "entregables_es": ["Tabla de trazabilidad inversa: parámetro Simscape | propiedad SysML | ID requisito | valor pliego | valor modelo | delta"],
    "entregables_en": ["Reverse traceability table: Simscape parameter | SysML property | requirement ID | contract value | model value | delta"],
    "materiales": []
  },
  {
    "id": "semana-07", "n": "7", "bloque": "III", "color": "#b85c1a",
    "titulo_es": "Calibración: adaptar el modelo al UGV real",
    "titulo_en": "Calibration: adapt the model to the real UGV",
    "verbo_es": "Calibrar", "verbo_en": "Calibrate",
    "tipo": "grupal",
    "duracion_es": "1 sesión de laboratorio de 2h + 3h trabajo autónomo",
    "duracion_en": "1 × 2h lab session + 3h self-study",
    "objetivo_es": "Modificar los parámetros del modelo Simscape para que representen exactamente las especificaciones del pliego y verificar que el comportamiento es físicamente coherente.",
    "objetivo_en": "Modify the Simscape model parameters to exactly represent the contract specifications and verify that the behaviour is physically coherent.",
    "tareas_es": ["Modificar parámetros usando la tabla de trazabilidad inversa como guía","Ejecutar el modelo modificado y verificar coherencia física","Documentar diferencias entre valores originales y valores del pliego"],
    "tareas_en": ["Modify parameters using the reverse traceability table as a guide","Run the modified model and verify physical coherence","Document differences between original values and contract values"],
    "entregables_es": ["Modelo Simscape calibrado v1.0","Tabla de parámetros: valores originales vs. valores del pliego","Gráficas de validación física"],
    "entregables_en": ["Calibrated Simscape model v1.0","Parameter table: original values vs. contract values","Physical validation plots"],
    "materiales": []
  },
  {
    "id": "semana-08", "n": "8", "bloque": "III", "color": "#b85c1a",
    "titulo_es": "Verificación formal de requisitos",
    "titulo_en": "Formal requirements verification",
    "verbo_es": "Demostrar", "verbo_en": "Demonstrate",
    "tipo": "grupal",
    "duracion_es": "2 sesiones de laboratorio de 2h",
    "duracion_en": "2 × 2h lab sessions",
    "objetivo_es": "Diseñar y ejecutar un test de verificación por cada requisito SHALL marcado como verificable con Simscape, con criterio de aceptación cuantitativo derivado del pliego.",
    "objetivo_en": "Design and run a verification test for each SHALL requirement marked as Simscape-verifiable, with a quantitative acceptance criterion derived from the contract.",
    "tareas_es": ["Definir escenario de simulación y criterio de aceptación para cada requisito","Ejecutar cada test y registrar resultado pass/fail","Capturar gráfica de evidencia por test","Documentar requisitos que no pueden verificarse con simulación"],
    "tareas_en": ["Define simulation scenario and acceptance criterion for each requirement","Run each test and record pass/fail result","Capture evidence plot per test","Document requirements that cannot be verified with simulation"],
    "entregables_es": ["Matriz de verificación completa: ID requisito | test | criterio | resultado | gráfica (≥80% de requisitos Sí-Simscape cubiertos)"],
    "entregables_en": ["Complete verification matrix: requirement ID | test | criterion | result | plot (≥80% of Yes-Simscape requirements covered)"],
    "materiales": []
  },
  {
    "id": "semana-09", "n": "9", "bloque": "IV", "color": "#6b3fa0",
    "titulo_es": "Análisis de modos de fallo",
    "titulo_en": "Failure mode analysis",
    "verbo_es": "Degradar", "verbo_en": "Degrade",
    "tipo": "grupal",
    "duracion_es": "1 sesión de laboratorio de 2h + 2h trabajo autónomo",
    "duracion_en": "1 × 2h lab session + 2h self-study",
    "objetivo_es": "Simular fallos en el subsistema asignado y verificar que el sistema activa los modos de seguridad del pliego en modo degradado.",
    "objetivo_en": "Simulate failures in the assigned subsystem and verify that the system activates the contract safety modes in degraded operation.",
    "tareas_es": ["Identificar los 3-5 modos de fallo más críticos del subsistema","Inyectar cada fallo en el modelo Simscape","Verificar activación de modos de seguridad (RGEN-17, ROPE-06)","Registrar comportamiento del sistema ante cada fallo"],
    "tareas_en": ["Identify the 3-5 most critical failure modes of the subsystem","Inject each failure into the Simscape model","Verify activation of safety modes (RGEN-17, ROPE-06)","Record system behaviour for each failure"],
    "entregables_es": ["Tabla FMEA ligera: modo de fallo | efecto | requisito de seguridad | resultado | acción correctora"],
    "entregables_en": ["Lightweight FMEA table: failure mode | effect | safety requirement | result | corrective action"],
    "materiales": []
  },
  {
    "id": "semana-10", "n": "10", "bloque": "IV", "color": "#6b3fa0",
    "titulo_es": "Integración entre subsistemas",
    "titulo_en": "Cross-subsystem integration",
    "verbo_es": "Integrar", "verbo_en": "Integrate",
    "tipo": "grupal",
    "duracion_es": "1 sesión de laboratorio de 2h + 3h trabajo autónomo",
    "duracion_en": "1 × 2h lab session + 3h self-study",
    "objetivo_es": "Conectar el modelo Simscape del subsistema asignado con los modelos de los subsistemas adyacentes y resolver las incompatibilidades de interfaz que aparezcan.",
    "objetivo_en": "Connect the assigned subsystem's Simscape model with adjacent subsystem models and resolve any interface incompatibilities that arise.",
    "tareas_es": ["Conectar el modelo con el subsistema adyacente según el IBD","Identificar y resolver incompatibilidades de tipo, unidad o rango","Verificar al menos 1 requisito de sistema en el modelo integrado","Documentar incompatibilidades detectadas y soluciones adoptadas"],
    "tareas_en": ["Connect the model with the adjacent subsystem following the IBD","Identify and resolve type, unit or range incompatibilities","Verify at least 1 system-level requirement in the integrated model","Document detected incompatibilities and adopted solutions"],
    "entregables_es": ["Modelo integrado (≥2 subsistemas conectados)","Registro de incompatibilidades y soluciones","Verificación de ≥1 requisito de sistema"],
    "entregables_en": ["Integrated model (≥2 subsystems connected)","Incompatibilities and solutions log","Verification of ≥1 system-level requirement"],
    "materiales": []
  },
  {
    "id": "semana-11", "n": "11", "bloque": "V", "color": "#8a6b00",
    "titulo_es": "Optimización de parámetros",
    "titulo_en": "Parameter optimisation",
    "verbo_es": "Optimizar", "verbo_en": "Optimise",
    "tipo": "grupal",
    "duracion_es": "1 sesión de laboratorio de 2h + 3h trabajo autónomo",
    "duracion_en": "1 × 2h lab session + 3h self-study",
    "objetivo_es": "Usar Simulink Design Optimization o análisis de barrido paramétrico para encontrar el punto de operación óptimo del subsistema dentro de las restricciones del pliego.",
    "objetivo_en": "Use Simulink Design Optimization or parametric sweep analysis to find the optimal operating point of the subsystem within the contract constraints.",
    "tareas_es": ["Definir función objetivo y restricciones a partir del pliego","Ejecutar barrido paramétrico o Simulink Design Optimization","Interpretar resultados: ¿el óptimo viola algún requisito? ¿Hay trade-offs?"],
    "tareas_en": ["Define objective function and constraints from the contract","Run parametric sweep or Simulink Design Optimization","Interpret results: does the optimum violate any requirement? Are there trade-offs?"],
    "entregables_es": ["Informe de optimización: parámetro | función objetivo | restricciones | valor óptimo | comparación con pliego | interpretación técnica"],
    "entregables_en": ["Optimisation report: parameter | objective function | constraints | optimum value | comparison with contract | technical interpretation"],
    "materiales": []
  },
  {
    "id": "semana-12", "n": "12", "bloque": "V", "color": "#8a6b00",
    "titulo_es": "Preparación del CDR",
    "titulo_en": "CDR preparation",
    "verbo_es": "Documentar", "verbo_en": "Document",
    "tipo": "grupal",
    "duracion_es": "Trabajo autónomo + tutorías disponibles",
    "duracion_en": "Self-study + available office hours",
    "objetivo_es": "Redactar la memoria técnica del subsistema siguiendo la estructura de RDOC-13 del pliego y preparar la presentación del CDR.",
    "objetivo_en": "Write the subsystem technical report following the RDOC-13 structure from the contract and prepare the CDR presentation.",
    "tareas_es": ["Redactar la memoria técnica: vista general, vista operacional, vista de subsistemas con interfaces, evidencias de verificación","Actualizar el modelo SysML con todos los resultados acumulados","Preparar la presentación CDR (máx. 15 diapositivas)"],
    "tareas_en": ["Write the technical report: general view, operational view, subsystem view with interfaces, verification evidence","Update the SysML model with all accumulated results","Prepare the CDR presentation (max. 15 slides)"],
    "entregables_es": ["Borrador de memoria técnica","Presentación CDR (máx. 15 diapositivas)","Modelo SysML actualizado a versión final"],
    "entregables_en": ["Draft technical report","CDR presentation (max. 15 slides)","SysML model updated to final version"],
    "materiales": []
  },
  {
    "id": "semana-13", "n": "13", "bloque": "V", "color": "#8a6b00",
    "titulo_es": "CDR — Critical Design Review",
    "titulo_en": "CDR — Critical Design Review",
    "verbo_es": "Defender", "verbo_en": "Defend",
    "tipo": "individual",
    "duracion_es": "1 sesión de 2h (15 min presentación + 10 min preguntas por equipo)",
    "duracion_en": "1 × 2h session (15 min presentation + 10 min questions per team)",
    "objetivo_es": "Presentar el diseño del subsistema ante la clase en formato de revisión de diseño real: arquitectura → requisitos verificados → simulación → evidencias.",
    "objetivo_en": "Present the subsystem design before the class in a real design review format: architecture → verified requirements → simulation → evidence.",
    "tareas_es": ["Presentar: arquitectura SysML → requisitos verificados → modelo Simscape → matriz de verificación → análisis de fallos → parámetros optimizados","Responder preguntas técnicas del panel (otros equipos + profesor como representante del CDTI)"],
    "tareas_en": ["Present: SysML architecture → verified requirements → Simscape model → verification matrix → failure analysis → optimised parameters","Answer technical questions from the panel (other teams + instructor as CDTI representative)"],
    "entregables_es": ["Presentación CDR (evaluación en directo)","Versión final de la memoria técnica"],
    "entregables_en": ["CDR presentation (live evaluation)","Final version of technical report"],
    "materiales": []
  },
  {
    "id": "semana-14", "n": "14", "bloque": "V", "color": "#8a6b00",
    "titulo_es": "Cierre y reflexión",
    "titulo_en": "Close-out and reflection",
    "verbo_es": "Reflexionar", "verbo_en": "Reflect",
    "tipo": "grupal",
    "duracion_es": "1 sesión de 2h",
    "duracion_en": "1 × 2h session",
    "objetivo_es": "Debate estructurado sobre los límites de la verificación por simulación, lecciones aprendidas del curso y cierre del hilo pliego → arquitectura → simulación → evidencias.",
    "objetivo_en": "Structured debate on the limits of verification by simulation, course lessons learned and closing the thread contract → architecture → simulation → evidence.",
    "tareas_es": ["Debate: ¿qué requisitos resultaron imposibles de verificar con simulación y por qué?","¿Qué reveló el modelo que el pliego no anticipaba?","¿Qué habrían diseñado diferente?","Presentación de lección aprendida por equipo (5 min)"],
    "tareas_en": ["Debate: which requirements were impossible to verify with simulation and why?","What did the model reveal that the contract did not anticipate?","What would you have designed differently?","One lesson learnt per team (5 min)"],
    "entregables_es": ["Memoria técnica final corregida tras el CDR","Contribución al documento colectivo de lecciones aprendidas del curso"],
    "entregables_en": ["Final technical report corrected after CDR","Contribution to the course collective lessons-learnt document"],
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
}

BLOQUE_LABEL = {
  "I":   {"es": "Bloque I — Arquitectura",          "en": "Block I — Architecture"},
  "II":  {"es": "Bloque II — Ingeniería inversa",   "en": "Block II — Reverse engineering"},
  "III": {"es": "Bloque III — Verificación",        "en": "Block III — Verification"},
  "IV":  {"es": "Bloque IV — Integración",          "en": "Block IV — Integration"},
  "V":   {"es": "Bloque V — Optimización y cierre", "en": "Block V — Optimisation & close-out"},
}

# ── Plantilla HTML de cada semana ────────────────────────────────────────────
def gen_html(s):
  color = s["color"]
  bloque_es = BLOQUE_LABEL[s["bloque"]]["es"]
  bloque_en = BLOQUE_LABEL[s["bloque"]]["en"]

  def lista(items_es, items_en, cls_li=""):
    li_es = "".join(f'<li class="lang-es">{x}</li>' for x in items_es)
    li_en = "".join(f'<li class="lang-en">{x}</li>' for x in items_en)
    return f'<ul class="item-list">{li_es}{li_en}</ul>'

  def materiales_html():
    if not s["materiales"]:
      return '''
      <div class="no-materiales">
        <span class="lang-es">Los materiales se publicarán antes de la sesión.</span>
        <span class="lang-en">Materials will be published before the session.</span>
      </div>'''
    cards = ""
    for m in s["materiales"]:
      ico, col, bg = ICONOS.get(m["tipo"], ("📄","#333","#f2f2f2"))
      cards += f'''
      <a class="mat-card" href="{m['archivo']}" download>
        <span class="mat-icon" style="background:{bg};color:{col}">{ico}</span>
        <div class="mat-info">
          <span class="mat-nombre">{m['nombre']}</span>
          <span class="mat-tipo" style="color:{col}">{m['tipo'].upper()}</span>
        </div>
        <span class="mat-dl" style="color:{col}">↓</span>
      </a>'''
    return cards

  tipo_es = "Entrega grupal" if s["tipo"]=="grupal" else "Entrega individual"
  tipo_en = "Group submission" if s["tipo"]=="grupal" else "Individual submission"

  return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Semana {s["n"]} · IS-UGV</title>
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
.main{{max-width:900px;margin:0 auto;padding:2.5rem 2rem 4rem}}
.grid-2{{display:grid;grid-template-columns:1fr 1fr;gap:1.5rem}}
@media(max-width:700px){{.grid-2{{grid-template-columns:1fr}}}}

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

/* añadir material — instrucción para el profesor */
.add-material-hint{{margin-top:.8rem;background:#fffbea;border:1px dashed #c8a800;border-radius:8px;padding:1rem 1.2rem;font-size:.8rem;color:#6b5500;font-family:var(--font-m);line-height:1.6}}
.add-material-hint code{{background:rgba(0,0,0,.07);padding:.1rem .35rem;border-radius:3px;font-size:.78rem}}

/* nav semanas */
.nav-semanas{{display:flex;justify-content:space-between;align-items:center;margin-top:3rem;padding-top:1.5rem;border-top:1px solid var(--border)}}
.nav-btn{{font-family:var(--font-m);font-size:.75rem;color:var(--ink-muted);text-decoration:none;padding:.5rem .9rem;border:1px solid var(--border);border-radius:6px;transition:all .2s;letter-spacing:.04em}}
.nav-btn:hover{{color:var(--ink);border-color:var(--ink)}}
.nav-btn.disabled{{opacity:.3;pointer-events:none}}
</style>
</head>
<body>

<nav class="topbar">
  <a class="topbar-logo" href="../../index.html"><span>IS</span>-UGV</a>
  <div class="topbar-right">
    <a class="back-link" href="../../index.html#semanas">
      <span class="lang-es-inline">← Todas las semanas</span>
      <span class="lang-en-inline">← All weeks</span>
    </a>
    <button class="lang-btn" onclick="document.body.classList.toggle('en')">EN / ES</button>
  </div>
</nav>

<div class="hero">
  <div class="hero-n">{s["n"]}</div>
  <div class="hero-inner">
    <div class="hero-tags">
      <span class="tag tag-accent">
        <span class="lang-es-inline">{bloque_es}</span>
        <span class="lang-en-inline">{bloque_en}</span>
      </span>
      <span class="tag">
        <span class="lang-es-inline">{tipo_es}</span>
        <span class="lang-en-inline">{tipo_en}</span>
      </span>
      <span class="tag">
        <span class="lang-es-inline">{s["duracion_es"]}</span>
        <span class="lang-en-inline">{s["duracion_en"]}</span>
      </span>
    </div>
    <h1 class="hero-titulo">
      <span class="lang-es">{s["titulo_es"]}</span>
      <span class="lang-en">{s["titulo_en"]}</span>
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
      <div class="meta-item">
        <span class="lang-es-inline">Semana:</span>
        <span class="lang-en-inline">Week:</span>
        <strong>{s["n"]}</strong>
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

  <div class="grid-2">
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
  </div>

  <div class="section">
    <p class="section-label"><span class="lang-es-inline">Materiales</span><span class="lang-en-inline">Materials</span></p>
    <div class="materiales-grid">
      {materiales_html()}
    </div>
    <div class="add-material-hint">
      <span class="lang-es">
        <strong>Profesor:</strong> para añadir un material, copia el archivo en esta carpeta
        (<code>{s["id"]}/</code>) y añade una entrada al array <code>materiales</code>
        en <code>gen_semanas.py</code>, luego regenera con <code>python3 gen_semanas.py</code>.
        Tipos disponibles: <code>docx · pdf · xlsx · slx · código · enlace · zip</code>
      </span>
      <span class="lang-en">
        <strong>Instructor:</strong> to add material, copy the file to this folder
        (<code>{s["id"]}/</code>) and add an entry to the <code>materiales</code> array
        in <code>gen_semanas.py</code>, then regenerate with <code>python3 gen_semanas.py</code>.
        Available types: <code>docx · pdf · xlsx · slx · code · link · zip</code>
      </span>
    </div>
  </div>

  <nav class="nav-semanas">
    <a class="nav-btn" href="../../index.html#semanas">
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

# ── Generar todos los index.html ─────────────────────────────────────────────
base = "/home/claude/ugv-course/semanas"
for s in semanas:
  path = os.path.join(base, s["id"], "index.html")
  with open(path, "w", encoding="utf-8") as f:
    f.write(gen_html(s))
  print(f"✓ {s['id']}/index.html")

# Guardar también el script para que el profesor lo tenga en el repo
import shutil
shutil.copy("/home/claude/gen_semanas.py", "/home/claude/ugv-course/gen_semanas.py")
print("\nScript gen_semanas.py copiado al repositorio.")
print("Total páginas generadas:", len(semanas))
