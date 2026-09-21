<!-- EJEMPLO — copia este archivo, renómbralo a comprension_[tus-iniciales].md
     (ej. comprension_jgp.md) y bórralo cuando lo subas. Una entrega por alumno. -->

# Ficha de comprensión — Semana 1

**Alumno:** Pelayo Pache Rodríguez · **Rol:**  IS / Simulación 

## Parte A — Conceptos

**¿Qué es la ingeniería de sistemas y por qué modelar en vez de documentar?**

La ingeniería de sistemas es una disciplina integral y estructurada que aborda el diseño, integración y gestión de sistemas multidisciplinares complejos a lo largo de todo su ciclo de vida. En el desarrollo de una plataforma como un UGV pesado intervienen múltiples especialidades técnicas (mecánica, propulsión, potencia eléctrica, control, computación embarcada, comunicaciones y software); cada especialista domina su campo concreto, pero ninguno abarca la totalidad del sistema. El ingeniero de sistemas actúa como el responsable de la coherencia del conjunto y dueño de las interfaces: traduce las necesidades operacionales del cliente en requisitos técnicos cuantitativos y verificables, reparte dichos requisitos entre los diferentes subsistemas asegurando cómo encajan entre sí, mantiene la trazabilidad estricta (justificando por qué existe cada componente y qué requisito lo motiva) y coordina la verificación final para garantizar que el sistema cumple con la misión encomendada.

Frente al enfoque clásico basado en documentos estáticos aislados (requisitos en Word, interfaces en Excel, arquitectura en PowerPoint y planes de pruebas en PDF), que sufren de desincronización inmediata al menor cambio de diseño y provocan inconsistencias críticas, el enfoque basado en modelos (MBSE, *Model-Based Systems Engineering*) sustituye esa dispersión por una base de datos unificada como **fuente única de verdad**. En el modelo digital, los bloques, puertos, interfaces físicas y lógicas, requisitos normativos y casos de prueba viven interconectados de manera consistente. Cualquier modificación se realiza en un único punto y se propaga automáticamente por toda la arquitectura, permitiendo detectar inconsistencias en fases tempranas de diseño, habilitar la simulación por computador continua y asegurar una comunicación técnica sin fisuras entre todos los departamentos del proyecto.

**Ciclo en V — dibújalo y marca hasta dónde llega este curso (rama descendente, sin Implementación)**

```text
Necesidad, Problema y Stakeholders (Fase 1 - Doc.01)                     Validación pre-operacional (Fase III) [FUERA]
  \                                                                                      /
   CONOPS y Modos de Operación (Fase 2 - Doc.02)                      Verificación de prototipo (Fase II) [FUERA]
     \                                                                                /
      Requisitos de Stakeholders (Fase 3 - Doc.03)                   Integración de subsistemas [FUERA]
        \                                                                          /
         Estudio de Conceptos / Trade-off (Fase 4 - Doc.04)        Pruebas en fábrica [FUERA]
           \                                                             /
            Arquitectura del Sistema BDD/IBD (Fase 5 - Doc.05/06)       /
              \                                                       /
               Plan de Verificación / Gestión (Fases 6 y 7 - Doc.07/08)
                 \
                  X === [LÍMITE DEL ALCANCE: Entrega de Oferta Técnica]
                   \
                    Implementación / Fabricación Física [FUERA DE ALCANCE]
```

*Alcance del curso:* Este curso recorre exclusivamente la **rama descendente (izquierda)** del ciclo en V según la metodología OOSEM (desde el análisis de la necesidad y definición de requisitos hasta la arquitectura SysML preliminar y la planificación de la verificación). El encargo contractual simulado consiste en elaborar una **oferta técnica competitiva para una licitación**, no en ejecutar el contrato adjudicado. Por lo tanto, no se llega a la fase de implementación/fabricación física ni se recorre la rama ascendente (pruebas de subsistemas, integración física, verificación de prototipo ni validación operacional). En su lugar, la solvencia de la oferta se respalda mediante **evidencia de viabilidad** obtenida a partir de modelos de simulación por computador y medidas experimentales en un banco de pruebas físico de laboratorio a escala reducida.

**BDD y IBD, en una frase cada uno**

- **BDD (Block Definition Diagram):** Diagrama estructural de SysML que define qué bloques o componentes conforman el sistema, especificando sus propiedades de valor cuantitativas y sus relaciones jerárquicas de composición y generalización.
- **IBD (Internal Block Diagram):** Diagrama de SysML que describe cómo se conectan internamente las partes de un bloque específico, modelando los flujos de energía, datos, control o esfuerzos mecánicos que circulan a través de sus puertos e interfaces.

## Parte B — El encargo

**¿Qué pide el Cliente, para qué y qué queda fuera? (3 frases)**

El Cliente solicita el diseño y desarrollo de un Sistema UGV pesado multipropósito y modular con tren de rodaje de ruedas (Lote 1), que incluye la plataforma robótica autónoma, un UAV de apoyo y un Puesto de Mando Portable (PMP). El objetivo es disponer de una plataforma móvil pesada de alta autonomía para acometer misiones críticas y penosas en ámbitos civiles y de emergencias (vialidad invernal, rescate, extinción de incendios y logística todoterreno), sustituyendo al personal humano en situaciones de riesgo y operando en coordinación directa con vehículos tripulados. Quedan fuera del alcance del curso la fabricación e implementación física del vehículo a tamaño real, la ejecución de las campañas de validación en campo, el desarrollo de las cargas de pago opcionales y el diseño de la variante sobre cadenas (Lote 2).

**Los 4 modos de operación, una frase cada uno**

1. **APAGADO:** Estado en el que el UGV se encuentra totalmente desenergizado, con su arquitectura computacional, software, actuadores y subsistemas de comunicaciones completamente inactivos.
2. **FUERA DE LÍNEA (*offline*):** Modo preparatorio y de soporte en el que se enciende la plataforma para realizar diagnósticos, intercambio de datos, chequeos de mantenimiento de primer escalón o planificar y cargar ficheros de misión desde el Puesto de Mando.
3. **TELEOPERADO:** Modo operacional en el que un operador humano gobierna directa y remotamente en tiempo real la dirección, aceleración, frenado, sensores perimetrales y cargas útiles del UGV desde un Equipo de Control (PMP o telemando portátil tipo tablet).
4. **AUTÓNOMO:** Modo operacional en el que la plataforma ejecuta por sí misma planes de misión preprogramados (navegación por waypoints, punto de destino, follow-me, modo shuttle o vuelta a casa) con capacidad de detección y evasión de obstáculos, siempre bajo la supervisión remota de un operador.

**Propósito del vehículo y sus 3 misiones principales, con las cifras que las condicionan**

El propósito del vehículo es proporcionar una plataforma robótica terrestre pesada y todoterreno, concebida de forma nativa como robot autónomo (prescindiendo de cabina, ergonomía o blindaje para tripulación humana), dotada de una barcaza modular común con propulsión híbrida de potencia continua ≥ 140 kW (RLT1-09) y Puntos de Interfaz estandarizados, capaz de operar tanto en carretera (≥ 75 km/h) como en campo a través (≥ 50 km/h) (RLT1-03) transportando grandes cargas útiles.

1. **Vialidad invernal y despeje de rutas:**
   - Incorporación frontal en el Punto de Interfaz 1 de la hoja quitanieves orientable CP-01 (RLT1-12) con anchura de corte ≥ 2.250 mm y acero antidesgaste de dureza Brinell ≥ 450.
   - Capacidad todoterreno para superar pendientes longitudinales de hasta el 60% (RLT1-03c), pendientes laterales del 30% (RLT1-03d) y franqueo de escalón vertical de al menos 30 cm (RLT1-03e).
   - Movilidad en tramos asfaltados a velocidad máxima en carretera ≥ 75 km/h (RLT1-03a) para permitir una rápida apertura de corredores logísticos.
2. **Plataforma Nodriza para sistemas UxV y operaciones conjuntas:**
   - Bahía de carga superior (Punto de Interfaz 3, RLT1-13) con capacidad para la recarga simultánea de 2 UAV (CP-09) y subsistema de recarga inalámbrica para al menos 2 micro/mini UGV transportables (CP-10) con rampa de acceso y salida autónoma.
   - Autonomía operativa global combinada de al menos 8 horas de funcionamiento continuo o 400 km de recorrido (RGEN-14) para actuar como centro de reabastecimiento móvil avanzado.
   - Alcance de comunicaciones de control y supervisión más allá de la línea de vista (BLOS) de al menos 20 km (RCOM-02).
3. **Transporte logístico pesado y remolcado:**
   - Capacidad neta de transporte de carga útil sobre la barcaza ≥ 2.000 kg (RLT1-07) con una tara en vacío entre 3.500 y 7.000 kg (RLT1-06) y un peso máximo en orden de combate/misión ≤ 9.000 kg (RLT1-08).
   - Capacidad de tracción y arrastre de un remolque trasero de masa ≥ 3.000 kg con enganche normalizado STANAG 4101 (RGEN-10, CP-14, RLT1-14).
   - Capacidad de desplazamiento en modo puramente eléctrico silencioso durante al menos 2 horas o 100 km (RGEN-15) para aproximaciones con mínima firma acústica y térmica.

**8 requisitos (ID RGEN/RLT) que crees verificables con un modelo de simulación — indica qué magnitud medirías en cada uno**

| ID | Magnitud a medir |
|---|---|
| RLT1-03a / RLT1-03b | Velocidad punta longitudinal (km/h) y aceleración media (m/s²) simulando resistencia a la rodadura y aerodinámica en perfiles planos de carretera y campo a través. |
| RLT1-03c | Pendiente máxima superable (%) y par motor resistente en rueda (Nm) en rampa continua con coeficiente de fricción controlado para verificar el límite de tracción. |
| RLT1-03d | Ángulo de vuelco estático y dinámico (grados o %) en pendiente lateral evaluando la elevación del centro de masas con la carga útil máxima instalada (2.000 kg). |
| RLT1-03e | Altura del obstáculo vertical franqueable (cm) evaluando cinemática de la suspensión independiente y fuerzas de contacto neumático-escalón en modelo multicuerpo. |
| RLT1-08 | Masa total acumulada del sistema (kg) mediante balance de densidades y volúmenes de los componentes en la herramienta CAD/física para comprobar que no supere los 9.000 kg. |
| RLT1-09 | Curva de potencia continua combinada entregada (kW) y par motor en eje (Nm) a lo largo del régimen de giro de los motores eléctricos y térmico. |
| RGEN-12 | Tasa de energía recuperada en frenada regenerativa (kWh) y variación del estado de carga de la batería (SoC, %) en ciclos de conducción con frenadas repetidas. |
| RGEN-17 | Distancia de detención longitudinal (metros) y deceleración (m/s²) ante la aparición de un obstáculo imprevisto para validar el algoritmo de frenado automático. |

**2 requisitos que NO se puedan verificar por simulación — justifica por qué**

| ID | Justificación |
|---|---|
| RGEN-06 | La resistencia estructural y operativa frente a agentes ambientales severos (corrosión salina, lluvia intensa, humedad extrema y radiación solar continua) requiere pruebas físicas destructivas y climáticas en cámaras de ensayo normativas (normas MIL-STD o grados IP de estanqueidad), ya que el envejecimiento químico de polímeros, sellos y recubrimientos no puede certificarse mediante modelos matemáticos o de simulación numérica. |
| RGEN-21 | La verificación de las rejillas de protección de faros para retener impactos de ramas y piedras de al menos 3 cm de diámetro sin deformación crítica ni alteración de la emisión fotométrica exige ensayos empíricos de impacto balístico/mecánico con proyectiles calibrados y mediciones de haz lumínico en banco de pruebas de laboratorio físico para su homologación formal. |

**3 términos del glosario que no conocías, con su significado**

1. **KLV (Key-Length-Value):** Estándar de codificación binaria de metadatos empleado en flujos de vídeo digital (RSW-07), donde información telemétrica como coordenadas de posición, orientación, velocidad y rumbo del UGV se transmiten empaquetadas y sincronizadas frame a frame dentro del contenedor de vídeo MPEG-TS.
2. **Cautivo Virtual (*Virtual Tethering*):** Submodo de vuelo coordinado del UAV de apoyo (ROPE-04) en el que la aeronave calcula y mantiene automáticamente una posición relativa, altitud y distancia constantes respecto al UGV en movimiento, simulando estar unida físicamente por un cable invisible para ofrecer consciencia situacional permanente.
3. **Vadeo sin preparación:** Capacidad del vehículo terrestre para penetrar y cruzar cursos de agua dulce o salada de hasta una cota especificada (≥ 0,75 m según RLT1-10) de manera directa e inmediata, sin requerir trabajos previos de estanqueizado manual, instalación de tomas elevadas de aire (snorkels) o cierre de compuertas.

**1 pregunta que le harías al Cliente**

En relación con los requisitos RLT1-12 (Punto de Interfaz 1 frontal para la hoja quitanieves CP-01) y RLT1-03e (superación de obstáculo vertical ≥ 30 cm): ¿debe la plataforma ser capaz de franquear el escalón vertical de 30 cm manteniendo acoplada la hoja quitanieves en su posición elevada de transporte, o la cota de franqueo se evalúa exclusivamente sobre la barcaza básica sin implementos frontales instalados debido a la reducción del ángulo de ataque?
