<!-- Ficha de comprensión individual - Fase 1 -->

# Ficha de comprensión — Semana 1

**Alumno:** José Escobedo Vázquez · **Rol:** Taller y Simulación

## Parte A — Conceptos

**¿Qué es la ingeniería de sistemas y por qué modelar en vez de documentar?**

La ingeniería de sistemas es una disciplina metodológica e interdisciplinar concebida para abordar el ciclo de vida completo de sistemas complejos (como un UGV pesado), coordinando y engranando múltiples áreas de conocimiento técnico (mecánica estructural, cinemática y dinámica de chasis, electrónica de potencia, software embarcado, sensores y control). Su objetivo esencial es actuar como nexo integrador: traduce las necesidades operacionales y misiones del cliente en requisitos de ingeniería cuantitativos y no ambiguos, asigna dichos requisitos a los subsistemas correspondientes, garantiza interfaces físicas y funcionales unificadas, y define con rigor el plan de verificación antes de fabricar una sola pieza.

El enfoque tradicional ("document-based") gestiona el proyecto mediante colecciones dispersas de documentos estáticos (listas en Excel, memorias en Word, esquemas en PowerPoint y planos CAD aislados). Este enfoque presenta una fragilidad crítica: ante cualquier cambio técnico o rediseño de un subsistema, los documentos pierden coherencia rápidamente, proliferan versiones obsoletas y se invierten ingentes horas de trabajo en reuniones meramente para reconciliar datos. En contraposición, el enfoque basado en modelos (**MBSE**, *Model-Based Systems Engineering*) establece un modelo digital unificado como **fuente única de verdad** (*Single Source of Truth*). En él, los requisitos, componentes arquitectónicos, parámetros físicos, interfaces mecánicas/eléctricas y casos de prueba están vinculados matemáticamente. Cualquier modificación se realiza en un único elemento y se propaga automáticamente por toda la arquitectura, lo que permite detectar colisiones o inconsistencias en etapas tempranas de diseño conceptual, facilita la ejecución de simulaciones multifísicas continuas y garantiza la trazabilidad rigurosa desde la necesidad hasta la verificación.

**Ciclo en V — dibújalo y marca hasta dónde llega este curso (rama descendente, sin Implementación)**

```text
Necesidad, Problema y Stakeholders (Fase 1 - Doc.01)                     Validación pre-operacional en campo [FUERA]
  \                                                                                      /
   CONOPS y Modos de Operación (Fase 2 - Doc.02)                      Verificación de prototipo físico [FUERA]
     \                                                                                /
      Requisitos del Sistema (Fase 3 - Doc.03/05)                    Integración física en banco/taller [FUERA]
        \                                                                          /
         Estudio de Conceptos / Trade-off (Fase 4 - Doc.04)        Fabricación y montaje de componentes [FUERA]
           \                                                             /
            Arquitectura SysML: BDD / IBD (Fase 5 - Doc.06)             /
              \                                                       /
               Plan de Verificación e Integración (Fase 6 - Doc.07)
                 \
                  X === [LÍMITE DEL CURSO: Entrega de la Oferta Técnica Competitiva]
                   \
                    Implementación y Fabricación a Escala Real [FUERA DE ALCANCE]
```

*Acotación del alcance:* El alcance de este trabajo se circunscribe rigurosamente a la **rama descendente (izquierda)** del ciclo en V de Sols / OOSEM (desde el análisis de la necesidad y formulación de requisitos hasta la arquitectura lógica/física y la definición del plan de verificación e integración). Nuestro cometido como licitadores es redactar y entregar la **oferta técnica**, no ejecutar el contrato de producción física. Por tanto, las fases de la rama ascendente (fabricación del prototipo a escala real, integración de subsistemas en taller y validación operacional en campo) quedan expresamente fuera del alcance. No obstante, desde los roles de Taller y Simulación, la solvencia de la oferta se respalda de forma cuantitativa mediante **modelos de simulación física por computador** y ensayos experimentales en un banco de pruebas a escala reducida en laboratorio.

**BDD y IBD, en una frase cada uno**

- **BDD (Block Definition Diagram):** Diagrama estructural de SysML que modela la composición jerárquica del sistema mediante bloques, definiendo sus tipos, atributos físicos, relaciones de descomposición y generalización.
- **IBD (Internal Block Diagram):** Diagrama de SysML que describe el interior de un bloque determinado, mostrando la conectividad interna entre sus partes a través de puertos, flujos e interfaces normalizadas (mecánicas, eléctricas o de datos).

## Parte B — El encargo

**¿Qué pide el Cliente, para qué y qué queda fuera? (3 frases)**

El Cliente (CDTI y Ministerio de Defensa) demanda el diseño y propuesta técnica de un Sistema UGV pesado multipropósito sobre ruedas (Lote 1), que comprende la plataforma robótica terrestre no tripulada, un UAV cautivo/apoyo aéreo y un Puesto de Mando Portable. El propósito es disponer de una plataforma no tripulada nativa con elevada autonomía y carga útil para acometer misiones críticas, penosas o peligrosas (como extinción de incendios, logística pesada, apertura de vías y reconocimiento), retirando a los operadores humanos de las zonas de riesgo letal. Quedan expresamente fuera del alcance contractual la fabricación e implementación física del prototipo a escala real, la ejecución de las campañas de validación en campo, el desarrollo de las cargas de pago opcionales de terceros y el diseño de la plataforma sobre cadenas (Lote 2).

**Los 4 modos de operación, una frase cada uno**

1. **APAGADO:** Estado inerte en el que el vehículo se encuentra completamente desenergizado, con la electrónica, software y actuadores fuera de tensión y el sistema de frenado de estacionamiento mecánico bloqueado.
2. **FUERA DE LÍNEA (*offline*):** Modo de preparación estática y soporte en el que se energizan los buses de baja tensión para tareas de diagnosis, mantenimiento preventivo de taller, calibración de sensores o carga/planificación de misiones desde el Puesto de Mando sin actuar la propulsión.
3. **TELEOPERADO:** Modo operacional en el que un operador humano ejerce el control continuo y directo en tiempo real de la dirección, tracción, freno y cargas de pago mediante un telemando portátil o la estación de control.
4. **AUTÓNOMO:** Modo operacional en el que el UGV navega y ejecuta de forma autónoma secuencias de waypoints predefinidas o tareas complejas (retorno a casa, seguimiento *follow-me* o patrulla), detectando y esquivando obstáculos por sí mismo bajo supervisión humana remota.

**Propósito del vehículo y sus 3 misiones principales, con las cifras que las condicionan**

El propósito del vehículo es servir como plataforma robótica terrestre pesada, todoterreno y modular, con tren de rodaje de ruedas (Lote 1), barcaza común estandarizada y grupo propulsor híbrido de potencia continua ≥ 140 kW (RLT1-09), capaz de desplazar hasta 9.000 kg de peso máximo en orden de marcha (RLT1-08) tanto en carretera (≥ 75 km/h) como en campo a través (≥ 50 km/h) (RLT1-03).

1. **Apoyo a la Extinción de Incendios Forestales y Emergencias:**
   - Montaje frontal en el Punto de Interfaz 1 de una hoja empujadora pesada CP-15 (anchura ≥ 3.000 mm, altura ≥ 1.200 mm y capacidad de excavación/desbroce en suelo de profundidad ≥ 450 mm).
   - Integración en la bahía de carga (Punto de Interfaz 3) de un módulo de bombeo de agente extintor CP-19 con monitor de agua orientable (360° horizontal / 85° vertical), caudal ≥ 220 L/min y presión > 20 bar, alimentado por depósito CP-22 de capacidad ≥ 2.750 L.
   - Protección y operatividad para avanzar por terreno agreste superando pendientes longitudinales del 60% (RLT1-03c) y laterales del 30% (RLT1-03d).

2. **Transporte Logístico Pesado y Despliegue en Convoys:**
   - Capacidad neta de transporte de carga útil sobre la barcaza de al menos 2.000 kg (RLT1-07), con una tara comprendida entre 3.500 y 7.000 kg (RLT1-06).
   - Arrastre de remolque pesado trasero de al menos 3.000 kg (RGEN-10, CP-14) mediante enganche bajo norma OTAN STANAG 4101 con suministro de potencia y datos (RLT1-14).
   - Autonomía operacional de al menos 8 horas o 400 km en ciclo híbrido estándar (RGEN-14), con velocidad de crucero en carretera ≥ 75 km/h (RLT1-03a).

3. **Plataforma Nodriza para Sistemas Autónomos no Tripulados (UxV):**
   - Bahía de carga superior (Punto de Interfaz 3) configurada con estación de aterrizaje y recarga rápida simultánea para 2 UAVs de reconocimiento (CP-09).
   - Submódulo de alojamiento y recarga inalámbrica automática para al menos 2 micro/mini UGVs (CP-10) provisto de rampa motorizada para despliegue y recogida sin presencia de personal.
   - Modo de sigilo eléctrico (RGEN-15) con autonomía de al menos 2 horas o 100 km a baja firma acústica y térmica durante el estacionamiento y recarga de los robots subordinados.

**8 requisitos (ID RGEN/RLT) que crees verificables con un modelo de simulación — indica qué magnitud medirías en cada uno**

| ID | Magnitud a medir |
|---|---|
| RLT1-03a | Velocidad máxima en recta horizontal (km/h) y aceleración longitudinal (m/s²) en modelo dinámico con resistencia a la rodadura y aerodinámica para verificar los ≥ 75 km/h. |
| RLT1-03c | Pendiente máxima superable (%) y par motor instantáneo en rueda (Nm) en rampa de rozamiento controlado comprobando tracción sin pérdidas de adherencia al 60%. |
| RLT1-03d | Ángulo de inclinación crítica de vuelco estático y dinámico (grados o %) en simulación multicuerpo con centro de masas evaluado a carga útil máxima (2.000 kg). |
| RLT1-03e | Altura de franqueo de escalón vertical (cm) y desplazamiento vertical de la suspensión independiente al impactar y remontar el obstáculo de 30 cm. |
| RLT1-09 | Curva combinada de par motor (Nm) y potencia continua (kW) entregada al tren motriz frente a las demandas de resistencia al avance en pendientes. |
| RGEN-10 | Tensión mecánica en el enganche de remolque (kN) y estabilidad en guiñada (*yaw rate*, rad/s) arrastrando un remolque simulado de 3.000 kg a 65 km/h. |
| RGEN-12 | Energía regenerada en desaceleración (kWh) y curva de recuperación del estado de carga de la batería (SoC, %) en ciclos dinámicos de frenado repetido. |
| RGEN-17 | Distancia de parada en frenada de emergencia (metros) y tiempo de activación del freno neumático/hidráulico (ms) ante obstáculo a velocidad máxima. |

**2 requisitos que NO se puedan verificar por simulación — justifica por qué**

| ID | Justificación |
|---|---|
| RGEN-06 | La resistencia estructural, integridad de materiales y estanqueidad frente a agentes ambientales severos (niebla salina, corrosión galvánica, lluvias torrenciales y radiación solar extrema) exige ensayos empíricos normalizados en cámaras climáticas según norma MIL-STD-810 y pruebas de estanqueidad para certificación de grado IP (IP67). La degradación electroquímica y fatiga de elastómeros a largo plazo no puede ser homologada oficialmente mediante modelos numéricos. |
| RLT1-10 | La capacidad de vadeo sin preparación en agua hasta una cota de 0,75 m requiere verificar la impermeabilidad real de juntas, retenes dinámicos de los cubos de rueda, sellado de pasamuros y la ausencia de flotabilidad imprevista en un foso de pruebas real. Las microfugas por tolerancias de mecanizado, presión hidrostática o choque térmico en componentes calientes (motores/frenos) no pueden validarse exclusivamente por ordenador. |

**3 términos del glosario que no conocías, con su significado**

1. **CANopen / J1939 (Protocolos en bus CAN):** Normas de comunicación industrial y de automoción pesada sobre bus CAN (mencionadas en las interfaces de control y potencia de los Puntos de Interfaz PI), que estandarizan el direccionamiento de nodos, mensajes de diagnóstico y perfiles de dispositivos en sistemas embarcados.
2. **Punto de Interfaz (PI):** Conjunto estandarizado de fijaciones mecánicas, conectores eléctricos de potencia (24V / alta tensión) y puertos de datos mediante los cuales se conectan e intercambian mecánicamente las distintas cargas útiles (CP) sobre la barcaza común del UGV sin alterar el chasis.
3. **Firma Multiespectral:** Emisión global detectable del vehículo en múltiples bandas del espectro electromagnético (firma térmica infrarroja por calor del escape y rozamiento, firma acústica por ruido de rodadura y motor, y sección radar). El pliego exige minimizarla en modo sigiloso (RGEN-09 y RGEN-15).

**1 pregunta que le harías al Cliente**

En relación con el requisito RLT1-14 (interfaz para remolque trasero de 3.000 kg bajo norma OTAN STANAG 4101 con suministro de potencia y datos) y el modo de conducción autónomo (ROPE-02): ¿el Cliente contempla que la marcha atrás o maniobras complejas de evasión en modo autónomo deban ejecutarse con el remolque de 3.000 kg acoplado (lo que requeriría sensorización angular en la lanza del remolque y algoritmos de control de articulación), o se asume que las maniobras complejas de retroceso con remolque se realizarán siempre en modo teleoperado?
