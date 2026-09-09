# Oferta OPT-ROB-01 — Robot terrestre pesado multipropósito

## Anexo I. Requisitos funcionales y condiciones técnicas de ejecución

> **Nota docente.** Este documento es una **adaptación anonimizada y resumida** de un
> pliego de licitación real de I+D. Se han sustituido el organismo contratante, las
> referencias institucionales y el encuadre de defensa por un **Cliente genérico** y un
> marco de **uso civil** (emergencias, logística, obra pública, extinción de incendios,
> vialidad invernal). **Se conservan sin cambios** los identificadores de requisito
> (`RGEN-xx`, `RLT1-xx`, `ROPE-xx`, `RPdO-xx`, `RNAV-xx`, `RCOM-xx`,
> `RSW-xx`, `RPVyA-xx`, `RDOC-xx`), las tres fases del contrato, los cuatro modos de
> operación y **todas las magnitudes numéricas**. Úsalo como si fuera el encargo real de
> tu equipo.

---

## 1. Introducción, objetivo y alcance

### 1.1 Introducción

Los **sistemas terrestres no tripulados** (UGV, *Unmanned Ground Vehicle*) permiten
ejecutar tareas peligrosas o penosas sin exponer a las personas que las realizarían:
intervención en emergencias (búsqueda y rescate, incendios, inundaciones, nevadas),
transporte logístico en terreno difícil, movimiento de tierras, limpieza y despeje de
rutas, y trabajos de ingeniería civil.

Un UGV con **arquitectura modular y abierta** puede adaptarse a muchas tareas cambiando
sus cargas útiles y sus módulos funcionales. Los UGV de mayor tamaño y potencia añaden
capacidad de carga y de movilidad todoterreno, pero las soluciones de gran tamaño están
todavía en fase experimental: se necesita I+D para llevarlas a un TRL alto manteniendo
prestaciones elevadas de movilidad y carga.

### 1.2 Objetivo

Desarrollar un **UGV pesado multipropósito con capacidades autónomas**, de carácter
**modular**, capaz de desempeñar misiones muy diversas que requieren transportar y
manejar cargas de elevado peso y dimensiones, y que pueda configurarse fácilmente para
una misión u otra.

Esto exige:

- una plataforma robótica con dimensiones y robustez suficientes para alojar esas cargas;
- un tren de propulsión con la potencia y tracción necesarias para transportarlas en su
  entorno de operación, con las prestaciones de movilidad que la misión requiera;
- un nivel de protección acorde a la peligrosidad de las misiones;
- una arquitectura abierta y modular que permita reconfigurar la plataforma variando
  cargas útiles y equipos embarcados.

Las prestaciones de movilidad deben permitir además **operar junto a vehículos tripulados**
del mismo tipo, desplazándose por los mismos terrenos sin quedarse rezagado.

Se buscan sistemas **concebidos como UGV desde el origen**, no vehículos tripulados
robotizados: se pretende un diseño compacto que prescinda del espacio, el blindaje y el
coste asociados a llevar tripulación a bordo.

### 1.3 Alcance

El desarrollo de un **Sistema UGV** incluye:

- un **vehículo autónomo pesado multipropósito y multimisión** (el UGV);
- un **UAV de apoyo** que facilite la teleoperación del UGV, el seguimiento de la misión y
  la consciencia situacional;
- un **Puesto de Mando Portable (PMP)** con: puesto de operación para el UGV y los UxV
  asociados; subsistemas auxiliares de comunicaciones y alimentación eléctrica; pérgola,
  mesas y sillas para los operadores;
- un **Dispositivo de Telemando Portable** para la teleoperación cercana (independiente
  del PMP) o lejana (a través del subsistema de comunicaciones del PMP);
- **subsistemas auxiliares**: baúles de transporte, transportines o remolques;
- opcionalmente, vehículos autónomos adicionales (terrestres o aéreos) con sus
  repetidores, para operación remota a larga distancia;
- las **cargas de pago** que se mencionen en los requisitos de cada misión;
- la **documentación técnica** requerida en este pliego;
- las **pruebas de verificación y validación en campo**: ensayos, demostraciones,
  formación de operadores, transporte, puesta en marcha y mantenimiento durante las
  pruebas;
- si procede, mantenimiento de primer escalón y consultoría remota durante la garantía.

El desarrollo se centra en un **UGV de tracción de ruedas** para operaciones de alta
movilidad: mayores velocidades en terrenos relativamente llanos y consolidados,
orientado a operaciones tácticas, transporte y limpieza de rutas. La plataforma debe
cubrir el mayor número posible de cometidos sin perjudicar su eficiencia operativa.

> *Nota docente: el pliego original contemplaba un segundo lote (UGV de cadenas para
> trabajos sobre terreno). En esta versión del curso se trabaja **solo con el UGV de
> ruedas** para acotar el alcance.*

### 1.4 Abreviaturas y siglas (selección)

| Sigla | Significado |
|---|---|
| BLOS | *Beyond Line of Sight* — más allá de la línea de visión |
| CIS | Sistema de interfaz cartográfica |
| EO/IR | Electro-óptico / infrarrojo |
| GNSS | Sistema global de navegación por satélite |
| GUI | Interfaz gráfica de usuario |
| IMU | Unidad de medición inercial |
| ISTAR | Inteligencia, vigilancia, adquisición de objetivos y reconocimiento |
| LIDAR | Detección y medición de distancias mediante imágenes láser |
| PMP | Puesto de Mando Portable |
| SysML / UML | Lenguajes de modelado de sistemas / unificado de modelado |
| TRL | *Technology Readiness Level* — nivel de madurez tecnológica |
| UAV | Vehículo aéreo no tripulado |
| UGV / UGS | Vehículo / sistema terrestre no tripulado |
| UxV | Otros sistemas no tripulados |

### 1.5 Definición de términos

- **Equipos de Control:** subsistemas electrónicos y de computación que gestionan la
  movilidad del UGV y el resto de funcionalidades.
- **Dispositivo de Telemando Portable:** dispositivo tipo *tablet* con *joystick* y
  botones para la teleoperación cercana del UGV (o lejana a través del PMP).
- **Interfaz:** programa informático (o MMI) desde el cual el operador interactúa con los
  subsistemas, el planeamiento, el almacenamiento y demás componentes del UGV.
- **Misión / Tarea:** periodo de operación del vehículo en modo autónomo durante el cual
  sus sensores recogen datos.
- **Modo APAGADO:** el UGV está totalmente apagado; arquitectura, software y
  comunicaciones no funcionan.
- **Modo AUTÓNOMO:** la plataforma ejecuta automáticamente tareas previamente planeadas,
  con parámetros establecidos y sin intervención exterior, según los objetivos deseados.
  Siempre hay un operador monitorizando el progreso.
- **Modo FUERA DE LÍNEA (*offline*):** permite arrancar el UGV para comprobar
  funcionamiento e intercambio de datos, definir misiones y realizar chequeos.
- **Modo TELEOPERADO:** la plataforma se opera de forma remota desde el Puesto de
  Operación.
- **Puesto de Mando:** lugar físico con los equipos y el personal para ejecutar,
  monitorizar y analizar las misiones.
- **Puesto de Operación / Operador:** conjunto de equipos de visualización, mandos,
  computación, alimentación, cableado, comunicaciones y sus maletas de transporte. Suele
  estar en el Puesto de Mando.
- **Sistema UGV:** todo el sistema a desarrollar (UGV + cargas de pago + UxV adicionales +
  Puesto de Mando + ...).
- **Teleoperar:** gobernar el vehículo no tripulado mediante control remoto realizado por
  una persona.

---

## 2. Fases de ejecución

El proyecto consta de **tres fases**; al final de cada una se entregan los
demostradores de la solución, debidamente probados y validados.

| Fase | Duración | Contenido |
|---|---|---|
| **Fase I — Diseño de la solución** | 5 meses desde la firma | Diseño conceptual y preliminar de la solución completa: arquitectura física y lógica global (chasis, propulsión y energía, suspensión y tren de rodaje, carrozado y auxiliares, sensores de percepción y navegación, comunicaciones, computación embarcada, *drive-by-wire*, distribución de potencia, puesto de mando y control). Ingeniería de dimensionamiento y validación de todos los elementos estructurales y funcionales, **apoyándose en técnicas de simulación**. Especificación y selección de componentes; compra de los críticos. |
| **Fase II — Desarrollo y pruebas de verificación del prototipo** | 21 meses desde la certificación de Fase I | Desarrollo del prototipo completo con todas las capacidades. **Hito intermedio** de documentación técnica y su validación. Pruebas: unitarias, de interfaz, de sistema en entorno controlado (fábrica) y pruebas iniciales de misión en fábrica. |
| **Fase III — Validación pre-operacional** | 4 meses desde la certificación de Fase II | Corrección de incidencias de la fase anterior. Pruebas de sistema en entorno real (campo) a modo de regresión, y pruebas de misión en campo con los operadores. |

---

## 3. Requisitos técnicos y características

### 3.1 Requisitos generales

| ID | Requisito (resumen) |
|---|---|
| **RGEN-01** | El contratista diseñará, desarrollará e instalará una plataforma terrestre no tripulada que gobierne su comportamiento y permita su supervisión/control remoto desde el PMP. |
| **RGEN-02** | Alta modularidad: configuración y módulos funcionales fácilmente adaptables e **intercambiables**. |
| **RGEN-03** | Una **barcaza (bastidor) principal** común a toda la gama de configuraciones del vehículo, mediante acoplamiento/desacoplamiento de módulos, accesorios e implementos. |
| **RGEN-04** | El UGV se concibe **como robot desde el origen**; se excluyen plataformas tripuladas robotizadas. |
| **RGEN-05** | La arquitectura permitirá incorporar nuevos módulos, cargas de pago e implementos, y vincular otros UxV para operación conjunta. |
| **RGEN-06** | Resistencia de UGV y subsistemas a agentes ambientales: temperaturas extremas, lluvia, humedad, corrosión, radiación solar. |
| **RGEN-07** | Proceso de fabricación lo más simple y económico posible (reparación/reemplazo poco costoso). |
| **RGEN-08** | *[OPCIONAL]* Minimizar la variedad de herramientas para reparaciones de primer escalón. |
| **RGEN-09** | Sistema de detección de obstáculos estáticos y dinámicos, basado en tecnologías radiantes (LiDAR, radar) y/o no radiantes (visión). El sistema podrá pasar a un **Modo de Detección SIGILOSO** (radiantes desactivadas); siempre estará en modo SIGILOSO o NORMAL, conmutable desde cualquier Equipo de Control y en cualquier modo de operación. |
| **RGEN-10** | Capacidad de arrastrar un **remolque trasero de ≥ 3.000 kg**, con gancho normalizado (deseable escamoteable). |
| **RGEN-11** | **Sistema de propulsión híbrida:** pack de baterías + motor eléctrico + motor de combustión interna apto para **biocombustible 100 %**. |
| **RGEN-12** | Baterías recargables por el motor de combustión y por **energía regenerada en frenadas**. |
| **RGEN-13** | Modo **puramente eléctrico** (sin motor de combustión), para operar con firma térmica y acústica reducida. |
| **RGEN-14** | Autonomía total **≥ 8 h de funcionamiento o ≥ 400 km**. |
| **RGEN-15** | Autonomía en modo puramente eléctrico **≥ 2 h o ≥ 100 km**. |
| **RGEN-16** | Remolcable por otros vehículos a **≥ 65 km/h**. |
| **RGEN-17** | **Frenado automático ante riesgo de colisión**, progresivo siempre que sea posible; deshabilitable manualmente para evitar bloqueos por falsos señuelos. |
| **RGEN-18** | *[OPCIONAL]* Movilidad híbrida **enchufable** (recarga también desde puntos de recarga). |
| **RGEN-19** | *[OPCIONAL]* Exportación de energía a sistemas externos, **≥ 120 kW**. |
| **RGEN-20** | Sistema de iluminación con **cobertura completa 360°**, configurable por el operador. |
| **RGEN-21** | Rejillas de protección en los faros capaces de retener piedras de **≥ 3 cm** sin afectar a la emisión luminosa. |
| **RGEN-22** | Medios de captación de imagen y sensores para consciencia situacional y teleoperación (visualización de implementos y tren de rodaje, imágenes de cada lateral, visión de profundidad 360° y **cámara térmica** para puntos calientes), todos protegidos. |
| **RGEN-23** | Puntos de anclaje para rescate o autorrescate por tracción (perrillos y eslingas). |
| **RGEN-24** | Puntos de amarre y estiba para **aerotransporte** como carga en aeronaves de ala fija, dimensionados para los factores de carga (norma de referencia aplicable). |
| **RGEN-25** | Puntos de amarre y estiba para **transporte terrestre** seguro como carga (norma UNE-EN 12195). |
| **RGEN-26** | Cabestrante de gran capacidad y/o tracción con eslingas, con procedimientos de seguridad para terrenos irregulares y recuperación de vehículos atrapados / autorrecuperación. |
| **RGEN-27** | El UGV se basará en un **tren de tracción de ruedas** para operaciones de alta movilidad. |
| **RGEN-28** | El UGV tendrá **Puntos de Interfaz** accesibles (mecánicos, eléctricos, lógicos o combinados) para integrar cargas de pago. Se definen los Puntos de Interfaz y sus cargas asociadas: el contratista **desarrolla y entrega los OBLIGATORIOS** y, opcionalmente, los OPCIONALES. |
| **RGEN-29** | Los Puntos de Interfaz no comprometerán la **estabilidad** del UGV, con o sin carga de pago montada. |

### 3.2 Requisitos del UGV (tracción de ruedas, alta movilidad)

#### 3.2.1 Generales

| ID | Requisito (resumen) |
|---|---|
| **RLT1-01** | Tren de tracción de **ruedas**, para mayores velocidades en terrenos llanos y consolidados. |
| **RLT1-02** | Configuración **4×4, 6×6 u 8×8**, con elevadas capacidades todoterreno de dificultad promedio a alta velocidad. |
| **RLT1-03** | Movilidad en carretera y campo a través de dificultad intermedia: **velocidad en carretera ≥ 75 km/h**; **campo a través ≥ 50 km/h**; **pendiente frontal ≥ 60 %**; **pendiente lateral ≥ 30 %**; **obstáculo vertical ≥ 30 cm** (deseable 40 cm). Se admite degradación en arena, guijarros o superficies resbaladizas. |
| **RLT1-04** | **Tracción directa e independiente en cada rueda.** |
| **RLT1-05** | **Suspensión neumática retráctil y regulable**, independiente en cada brazo de cada rueda. |
| **RLT1-06** | Tara (peso en vacío) entre **3.500 y 7.000 kg**. |
| **RLT1-07** | Capacidad de carga **≥ 2.000 kg**. |
| **RLT1-08** | Peso total en orden de misión **≤ 9.000 kg** en todo caso. |
| **RLT1-09** | Potencia total del sistema de propulsión **≥ 140 kW (≈ 190 CV)**. |
| **RLT1-10** | Vadeo sin preparación **≥ 0,75 m** (agua dulce o salada). |
| **RLT1-11** | *[OPCIONAL]* Protección balística mediante blindaje modular/removible frente a armas de pequeño calibre. |

#### 3.2.2 Puntos de Interfaz

- **RLT1-12 — Zona frontal (Punto de Interfaz 1):** interfaz electromecánico para
  **limpieza de rutas**, con cargas alternativas: hoja quitanieves **(CP-01, OBLIGATORIA)**
  anchura ≥ 2.250 mm, acero Brinell ≥ 450, orientable; fresadora de nieve **(CP-02,
  opcional)** anchura ≥ 2.000 mm, altura ≥ 1.000 mm, proyección ≥ 25 m; rodillo de presión
  sobre el terreno **(CP-03, opcional)** barrido ≥ 2,2 m, > 5 km/h, ≥ 300 kg por rueda.
- **RLT1-13 — Zona superior:**
  - **Punto de Interfaz 2:** sensores y efectores; cargas alternativas: **módulo de
    efectores especiales (CP-04, OBLIGATORIA, no detallado en esta versión docente)**;
    módulo optrónico de adquisición sobre mástil retráctil para ISTAR **(CP-05, opcional)**;
    brazo robótico articulado para manipulación de muestras y objetos **(CP-06, opcional)**,
    con sensores de visión para su teleoperación.
  - **Punto de Interfaz 3:** **bahía de carga** de gran capacidad; elementos alternativos:
    equipos y víveres **(CP-07, opcional)**; camillas o células medicalizadas **(CP-08,
    opcional)**; plataforma de recarga simultánea de dos UAV **(CP-09, OBLIGATORIA)**;
    subsistema con ≥ 2 puntos de **recarga inalámbrica para UGV transportables** con acceso
    de entrada/salida sin acción humana (función Nodriza) **(CP-10, OBLIGATORIA)**;
    contenedor de despliegue de carga lineal **(CP-11, opcional; solo el contenedor o
    réplica)**; tolva dispensadora de sal **(CP-12, opcional)** capacidad ≥ 1,2 m³, ancho de
    proyección 2–6 m, salida trasera; contenedor compartimentado para muestras líquidas y
    sólidas **(CP-13, opcional)**.
- **RLT1-14 — Zona trasera (Punto de Interfaz 4):** enganche mecánico de remolques de
  hasta 3.000 kg **(CP-14, OBLIGATORIA)**.

### 3.3 Requisitos para el UGV de cadenas — *omitido en esta versión*

*El §3.3 del pliego original (UGV de cadenas para trabajos sobre terreno, requisitos
`RLT2-xx` y cargas `CP-15…CP-25`) queda fuera del alcance de este curso. La numeración de
las secciones siguientes se conserva.*

### 3.4 Modos de operación

| ID | Requisito (resumen) |
|---|---|
| **ROPE-01** | El Sistema UGV funciona con **supervisión de un operador**, directa (teleoperando) o indirecta (supervisión autónoma). Se implementan **tres modos**: TELEOPERADO, AUTÓNOMO y, para movimientos cercanos o preparación, FUERA DE LÍNEA (planificación de misiones en el PMP, transporte, mantenimiento). |
| **ROPE-02** | El modo **TELEOPERADO** permite control directo de dirección, aceleración y frenado, y de otras funciones del vehículo (propulsión, suspensión, luces, refrigeración, cámaras perimetrales) y de las cargas útiles. |
| **ROPE-03** | En TELEOPERADO el operador gobierna desde cualquier Equipo de Control no embarcado (Puesto de Operación y Dispositivo de Telemando Portable), apoyándose en las imágenes del UAV de apoyo. |
| **ROPE-04** | El UAV de apoyo tiene dos modos: **TELEOPERADO** y **CAUTIVO VIRTUAL** (sigue al UGV automáticamente), activables desde los Equipos de Control no embarcados. |
| **ROPE-05** | El modo **AUTÓNOMO** minimiza la interacción humana e incluye, al menos, estos submodos activables/desactivables en cualquier momento: (a) navegación por **puntos de paso** (*waypoints*); (b) navegación por **punto de destino** (el vehículo decide la trayectoria, incluso marcha atrás); (c) **regreso autónomo** a un punto anterior o al origen (vuelta a casa); (d) **seguimiento automático** de personas o vehículos; (e) **lanzadera** (*shuttle*) entre dos puntos. |
| **ROPE-06** | En modo AUTÓNOMO, capacidad de **«Detectar y Evadir»** obstáculos estáticos y dinámicos, en modo de detección NORMAL o SIGILOSO: recalcular trayectorias, marcha atrás, buscar alternativas. |

### 3.5 Requisitos para la ejecución de misiones

| ID | Requisito (resumen) |
|---|---|
| **ROPE-07** | Ciclo de vida de una misión: **(a) Planeamiento** en modo FUERA DE LÍNEA, con la GUI, produce un **fichero de misión** que se almacena en el UGV; **(b) Ejecución** ordenada desde el Puesto de Operación, en TELEOPERADO o AUTÓNOMO, con cambio entre modos; **(c) Finalización**: vuelta a FUERA DE LÍNEA, mantenimiento de primer escalón (limpieza de cámaras, carga de baterías) y transmisión de datos (imágenes/vídeos). |
| **ROPE-08** | Toda misión debe tener definidos, como mínimo, el **modo teleoperado y la vuelta a casa**; no se ejecuta ningún modo autónomo no definido en esa misión salvo cancelación o pausa. |
| **ROPE-09** | Familias de misión previstas (probadas en Fases II y III): ISTAR, materiales peligrosos, logística, evacuación, búsqueda y rescate, Nodriza, limpieza de rutas y apoyo en tormentas invernales. |
| **ROPE-10** | El cambio entre modos durante una misión debe ser **lo más rápido posible**, sin retrasar el desarrollo de la misión. |

### 3.6 Requisitos técnicos del Puesto de Operación

| ID | Requisito (resumen) |
|---|---|
| **RPdO-01** | Puesto de Operación **móvil y embarcable** en un vehículo tipo *shelter* o *shelter* transportable; permite teleoperación directa o funciones de navegación autónoma. |
| **RPdO-02** | **Precarga de mapas** de la zona en el sistema CIS del UGV para dar soporte a la navegación autónoma. |
| **RPdO-03** | Sistema de **consciencia situacional**: (a) percepción del entorno en visibilidad reducida (vegetación, humo, niebla, lluvia intensa, polvo); (b) **visión perimetral 360°**, diurna y nocturna, bajo distintas condiciones ambientales. |
| **RPdO-04** | Interfaces con información suficiente para controlar el sistema en cualquier entorno y condición ambiental **sin generar confusión ni estrés** en el operador, aportando información de conducción (visual, auditiva, háptica), de misión y de estado del vehículo. |
| **RPdO-05** | Puesto de Operación **transportable** en maletas/baúles rugerizados. |
| **RPdO-06** | **Tres interfaces independientes** (conducción, misión y control de carga útil); conducción y misión operadas por un mismo individuo. |
| **RPdO-07** | Selección y visualización de las imágenes que el operador estime necesarias. |
| **RPdO-08** | *[OPCIONAL]* Interfaz inmersivo con háptica y realidad aumentada. |

### 3.7 Requisitos técnicos de los sensores de navegación

| ID | Requisito (resumen) |
|---|---|
| **RNAV-01** | Sistema de navegación **alternativo al GNSS** para entornos con espectro electromagnético degradado o denegado, con al menos **tres tecnologías independientes de la cobertura satelital** (p. ej. IMU, odometría visual, CRPA), que permita: (a) determinar la posición del UGV con el mínimo error; (b) continuar la navegación autónoma por la ruta programada durante el mayor tiempo posible o hasta recuperar la señal, con **distancia mínima de 5 km** en este modo. |

### 3.8 Requisitos técnicos de las comunicaciones

| ID | Requisito (resumen) |
|---|---|
| **RCOM-01** | **Tres módulos de comunicaciones alternativos:** (a) módulo **5G** para misiones de seguridad civil, con cifrado opcional; (b) módulo de **radio** con protección de transmisión y cifrado opcional, interoperable con sistemas en dotación y robusto ante perturbaciones; (c) **terminal satélite comercial** sustituible por uno de mayores prestaciones, con contrato de uso durante el proyecto y la garantía. |
| **RCOM-02** | Rango de control **más allá de la línea de visión (BLOS) ≥ 20 km** entre UGV y PMP, tanto para supervisión de misión como para teleoperación. |
| **RCOM-03** | Modo de aseguramiento de las comunicaciones con dos estados, **NORMAL** y **DEGRADADO**; el sistema detecta el cambio (por interferencias o pérdida de línea de visión) y actúa en consecuencia. |
| **RCOM-04** | **Auto-recuperación** del enlace ante pérdida (estado DEGRADADO): en TELEOPERADO, regresión automática del recorrido hasta recuperar señal; en AUTÓNOMO, el vehículo continúa la misión programada. |
| **RCOM-05** | *[OPCIONAL]* Conexión directa por **fibra en carrete de ≥ 100 m**. |

### 3.9 Requisitos relativos al software

| ID | Requisito (resumen) |
|---|---|
| **RSW-01** | Todo el software desarrollado será **modular**. |
| **RSW-02** | La documentación explicará la **arquitectura general** con diagramas **UML y/o SysML** más texto: módulos del vehículo, de los puestos de mando y de cualquier subsistema desarrollado. |
| **RSW-03** | Se documentará el **detalle de las interfaces de entrada/salida** de cada módulo. |
| **RSW-04** | Son entregable SW: todos los **scripts, ficheros de configuración, datos de prueba, binarios y librerías** (online y offline), generados o comprados, y las licencias necesarias. |
| **RSW-05** | Apartado de **dependencias**: librerías, compiladores/intérpretes y sistemas operativos, con sus versiones. |
| **RSW-06** | Los binarios con GUI mostrarán el **logotipo del Cliente** durante 2 s al arrancar y de forma visible en la pantalla principal. |
| **RSW-07** | El vídeo mostrado y almacenado usará contenedor **MPEG-TS** con compresión MPEG-2 o H.264; si se dispone de posición y orientación de la plataforma, se incluirán como **metadatos KLV** (stream adicional) con cadencia ≥ 1 cada 2 s. |
| **RSW-08** | *[OPCIONAL]* Transmisión de vídeo a la red local en tiempo real mediante **RTSP/RTP** en dirección multicast. |

### 3.10 Requisitos de las pruebas

| ID | Requisito (resumen) |
|---|---|
| **RPVyA-01** | Las pruebas de verificación y validación tendrán en cuenta los **modos operativos** (TELEOPERADO, AUTÓNOMO, FUERA DE LÍNEA), los **modos de detección** (NORMAL, SIGILOSO) y los **modos de comunicaciones** (NORMAL, DEGRADADO). |
| **RPVyA-02** | El contratista dispondrá de todas las **licencias software** necesarias, instaladas en sus sistemas; el Cliente tendrá licencia de uso durante las pruebas. |
| **RPVyA-03** | Durante pruebas y demostraciones, el contratista aplicará el **distintivo del Cliente** (≥ tamaño A3) en los laterales de cada sistema/subsistema. |
| **RPVyA-04** | Las **pruebas de verificación** se realizan al final de la Fase II (obligatorias para cerrarla): unitarias, de interfaz, de sistema en entorno controlado (fábrica) y pruebas iniciales de misión en fábrica. |
| **RPVyA-05** | Las pruebas de verificación las supervisa y dirige el **ERC**; el contratista planifica el tiempo en el Plan de Pruebas. |
| **RPVyA-06** | Las pruebas de verificación se realizan en las **instalaciones del contratista**. |
| **RPVyA-07** | Las **pruebas de validación** de la Fase III las llevan a cabo **unidades operativas** designadas por el Cliente, en instalaciones designadas por el Cliente. |
| **RPVyA-08** | El contratista da apoyo durante las pruebas de validación e imparte **formación** a los operadores. |
| **RPVyA-09** | Las pruebas podrán ejecutarse en varios periodos de **una semana**, mínimo **dos semanas no consecutivas**, incluyendo llegada, instalación/montaje, formación, apoyo y recogida. |

### 3.11 Requisitos de la documentación

| ID | Requisito (resumen) |
|---|---|
| **RDOC-01** | Entregables documentales en **PDF y en el formato fuente** original (se fomenta Word con control de cambios en la fase de armonización). |
| **RDOC-02** | Nombre de fichero = **código identificativo + número de versión** (p. ej. `E01_7 Plan de Gestión de Proyecto.pdf`); versiones incrementales de uno en uno. |
| **RDOC-03** | En cada plazo parcial, copia electrónica (USB o equivalente) con toda la documentación generada en el periodo. |
| **RDOC-04** | Al fin del contrato, copia electrónica con todos los documentos en su última versión, en PDF y fuente. |
| **RDOC-05** | **Plan de Gestión del Proyecto** (a los 15 días de la firma): objeto; descomposición estructurada en paquetes de trabajo, tareas y subtareas con entradas/salidas; organización y roles; programa de trabajos con **diagrama de Gantt** (apaisado, ≥ 3 niveles); referencias a Calidad, Riesgos y Configuración; perfil de esfuerzo. |
| **RDOC-06** | El Plan de Gestión del Proyecto se **actualiza** ante cualquier cambio. |
| **RDOC-07** | **Plan de Gestión de la Configuración**: identificación de elementos de configuración; anexo con la **Línea Base de la Configuración** (versiones de entregables), actualizado a lo largo del proyecto. |
| **RDOC-08** | **Plan de Gestión de Riesgos**: procedimiento; identificación inicial; catalogación de impacto y probabilidad con sus criterios; **matriz de riesgos** inicial y actualizada. |
| **RDOC-09** | **Plan de Pruebas**: descripción de las pruebas de las Fases II y III; **matriz de trazabilidad pruebas ↔ requisitos**; recursos materiales, inmateriales y humanos; responsables por rol; planificación temporal (≥ 2 semanas no consecutivas por fase); permisos y seguros; riesgos del plan. |
| **RDOC-10** | **Protocolo de Pruebas**: por cada prueba — caracterización del escenario (situación inicial/final, condiciones ambientales), responsable, pasos, **criterios de aceptación**, y si su no aceptación es bloqueante y a qué pruebas bloquea. |
| **RDOC-11** | **Resultado de las Pruebas**: por fase — fechas de ejecución (incluidas repeticiones), resultado final, y causa/solución si hubo repeticiones. |
| **RDOC-12** | **Informe de Pruebas**: único e **incremental**, integra toda la información de las pruebas de todas las fases. |
| **RDOC-13** | **Arquitectura General del Sistema** — con **uso extensivo de diagramas SysML**. Debe contener al menos: **(a) Vista General** — propósito del Sistema UGV, descripción de capacidades, **límites del sistema**, suposiciones y restricciones; **(b) Vista Operacional** — modos de operación y conceptos de operación; **(c) Vista de Sistemas y Subsistemas** — primer nivel (UGV, PMP, Dispositivo de Telemando Portable, subsistema de Comunicaciones, auxiliares), **interfaces entre subsistemas y con el exterior** con diagramas de despliegue (incluidos los módulos SW), Puntos de Interfaz de las cargas de pago, y niveles inferiores de los subsistemas más destacados con sus interfaces. |
| **RDOC-14** | **Diseño Hardware** con diagramas jerárquicos; nomenclatura inequívoca y **designadores de referencia** (1–2 letras + número) para todos los elementos en todos los niveles. |
| **RDOC-15** | Orden de la descripción del Diseño Hardware: especificaciones generales (alimentación, rangos de funcionamiento), teoría de funcionamiento, descripción de elementos (física, funcional, interfaces), conexiones internas/externas, planos (generales, eléctricos, mecánicos), anexos (manuales, *datasheets*). |
| **RDOC-16** | Para elementos programables (PLC/PAC/IPC, FPGA, microcontroladores): IDE y versión, componente (marca y modelo), versión de firmware, descripción del programa, programa cargado. |
| **RDOC-17** | **Diseño de Software** — con **uso extensivo de diagramas SysML y/o UML**: estructura general con **diagrama de despliegue** (equipos que ejecutan software: puestos de operación, plataforma, cargas de pago, UAV de apoyo); interfaces entre módulos (lógicas y físicas); estructura de cada componente (diagramas de componentes); **casos de uso** con diagramas de secuencia y, si procede, de estados; dinámica de las GUI (pantallas y transiciones); herramientas de desarrollo y dependencias (lenguajes, *frameworks*, librerías con versiones, IDE/RAD, control de versiones, gestión de fallos). |
| **RDOC-18** | **Estrategia IP**: derechos preexistentes utilizados; identificación de nuevos derechos de propiedad industrial/intelectual asociados a la solución (o justificación motivada de no protección); vías de protección elegidas. |

---

## 4. Calendario de ejecución (resumen)

Diagrama de Gantt previsto para las tres fases, con hitos de **justificación (J)**,
**evaluación y certificación (C)** en cada fase. La Fase II incluye un **hito intermedio**
(J.II.HI / C.II.HI) y un hito final (J.II.HF / C.II.HF).

## 5. Entregables y criterios de verificación de ejecución (resumen)

- Cada fase se cierra con la **entrega** de documentación y su **validación** por el ERC,
  siguiendo los criterios de verificación de la ejecución.
- La evaluación de las ofertas usa **criterios no evaluables mediante fórmulas (80 %)** y
  **evaluables mediante fórmulas (20 %)**, con umbrales mínimos por criterio.
- Entre los criterios técnicos: valoración de la solución, de la conjugación de las cargas
  de pago (VCCdP) y de los **resultados de las pruebas de verificación (VPVerc)**.

## 6. Alcance del servicio — escenario de validación pre-operacional (resumen)

En la Fase III el Cliente proporciona un **escenario pre-operacional** en el que unidades
operativas ejercitan el prototipo en misiones representativas, con el contratista dando
apoyo y formación. El objetivo es comprobar que se alcanzan las prestaciones y los
objetivos del reto en condiciones próximas a las reales (TRL 7).
