<!-- EJEMPLO — copia este archivo, renómbralo a comprension_[tus-iniciales].md
     (ej. comprension_jgp.md) y bórralo cuando lo subas. Una entrega por alumno. -->

# Ficha de comprensión — Semana 1

**Alumno:** [Eloy Suárez Costales] · **Rol:** [IS / Software]

## Parte A — Conceptos

**¿Qué es la ingeniería de sistemas y por qué modelar en vez de documentar?**

[La ingenieriería de sistemas es una disiciplina, que se basa en como integrar y gestionar sistemas complejos, dentro de un mismo proyecto relacionando y explicando las conexinoes entre los distintos subsistemas, así como, interacciones entre sistemas, dependencias, roles, tareas asignadas... En pocas palabras vendría a ser una visión más alejada del proyecto que permite que todo se conecte. Además la ingeniería de sistemas no concluye en el  término del ciclo de vida, sino que en ello incluye también pensar en mantenimiento y operación final.

El enfoque tradicional que consiste en documentar tiene el gran problema de que al mínimo cambio los documentos (Excels, Words, PowerPoints de architectura...) dejan de estar de acuerdo entre sí y nadie sabe cual es la versión válida, que archivos se deben mantener y cuales no dando lugar a mucho trabajo y reuniones dedicadas a esta documentación. Además, toda esta documentación no permite una facil visión global y de conexion entre los sistemas y roles del proyecto. Sin embargo el modelado MSBE, resuelve este conflicto, sustituyendo todos estos documentos, por una base de datos donde se encuentran bloques, interfaces, requisitos, simulaciones, vertificaciones y dependencias. De esta manera, al mínimo cambio o fallo, se actualiza en un solo lugar y esto se propaga automaticamente. Otra gran ventaja es que detecta inconsistencias y habilita simulaciones y validaciones, algo que con el sistema tradicional sería imposible ya que todos los documentos están aislados.]

**Ciclo en V — dibújalo y sitúa en él las 14 semanas del curso**

[SEMANA 1
    \\\
    SEMANA 2
        \\\
        SEMANAS 3-4           SEMANAS 13-14
            \\\               ///
           SEMANAS 5-6    SEMANAS 11-12
               \\\        ///
               SEMANAS 7-10
               
SEMANA 1: necesidad problema y stakeholders
SEMANA 2: modos de operación y escenario de misión
SEMANAS 3-4: requisitos
SEMANAS 5-6: estudio de conceptos: lote 1 vs lote 2, matriz AoA
SEMANAS 7-10: arquitectura BDD, IBD y trazabilidad (modelo SysML)
SEMANAS 11-12: plan de verificación e integración
SEMANAS 13-14: optimizacion y cierre]



**BDD y IBD, en una frase cada uno**

- BDD: diagrama que muestra que bloques hay en el sistema y como se componen unos dentro de otros
- IBD: diagrama que muestra como se conectan esos bloques por dentro, mediante puertos e interfaces

## Parte B — El encargo

**¿Qué pide el Cliente, para qué y qué queda fuera? (3 frases)**

[El cliente pide crear un UGV pesado multipropósito, modular y de uso civil y militar con un UAV de apoyo y un puesto de mando desde donde se controle. Para cubrir un vacío tencológico real y poder sustitituir a los vehículos tripulados en misiones peligrosas. Se debe concebir como un robot no como un vehículo tripulado, no se exige diseño de detalle ni implementación real y no será necesario desarrollar los UGV y UAV externos qeu se acoplan a la plataforma.]

**Los 4 modos de operación, una frase cada uno**

1. TELEOPERADO: el operario controla directamente el UGV desde los Equipos de Control
2. AUTÓNOMO: Navegación autónoma con el mínimo grado de interacción humana posible
3. FUERA DE LÍNEA: Durante este modo se planificaran misiones, trnasportara el vehículo, se hará mantenimiento...
4. -

**Propósito del vehículo y sus 3 misiones principales, con las cifras que las condicionan**

[El principal propósito es desarrollar un UGV pesado con capacidades autónomas y de uso civil y militar. Debe combinar dimensiones y robustez suficientes, un tren de propulsión con potencia y tracción adecuadas, un nivel de protección proporcional al riesgo de la misión, y una arquitectura abierta y modular.

Misiones principales:

1. ISTAR (Inteligencia, Vigilancia, Adquisición de objetivos y Reconocimiento)
   - CP-05: Requiere el Punto de Interfaz 3 con el Módulo de adquisición óptronico sobre mástil retráctil
   - RGEN-09: debe poder alternar entre modo NORMAL y SIGILOSO, desactivando tecnologías como LiDAR/radar
   - RGEN-14: Autonomía mínima de 8 horas o 400 km en modo híbrido ; 2 horas o 100 km en modo puramente eléctrico 
   - RGEN-15: clave para operar con baja firma térmica y acústica.
   - RGEN-22: cámara térmica que identifique puntos calientes y visión de profundidad en 360°
2. Extinción de incendios
   - CP-15: hoja empujadora con anchura mínima 3.000 mm, altura mínima 1.200 mm, profundidad de excavación ≥450 mm
   - CP-19: bomba de impulsión de agente extintor de alta presión, debe tener: presión >20 bares, caudal ≥220 L/min, monitor orientable 85° vertical / 360° horizontal
   - CP-22: depósito de agua con capacidad ≥2.750 L y con tomas Barcelona de 25 mm de salida y 45/70 mm de llenado
3. Sistema nodriza, MEDEVAC
   - CP-09 y CP-10: Bahía de carga de gran capacidad con plataforma de recarga simultánea de 2 UAV y subsistema con al menos 2 puntos de recarga inalambrica para UGV transpotables
   - Capacidad de arrastre: remolque de hasta 3.000 kg (RGEN-10) y capacidad de carga mínima de 2.000 kg (RLT1-07) o 4.000 kg(RLT2-05)
   - RCOM-02: Comunicaciones BLOS no inferior a 20 km ]

**8 requisitos (ID RGEN/RLT) que crees verificables con un modelo de simulación — indica qué magnitud medirías en cada uno**

| ID | Magnitud a medir |
|---|---|
| | |

**2 requisitos que NO se puedan verificar por simulación — justifica por qué**

| ID | Justificación |
|---|---|
| | |

**3 términos del glosario que no conocías, con su significado**

1.
2.
3.

**1 pregunta que le harías al Cliente**

[pregunta]
