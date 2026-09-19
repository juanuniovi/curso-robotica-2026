<!-- EJEMPLO — copia este archivo, renómbralo a comprension_[tus-iniciales].md
     (ej. comprension_jgp.md) y bórralo cuando lo subas. Una entrega por alumno. -->

# Ficha de comprensión — Semana 1

**Alumno:** César Bobes Álvarez · **Rol:** IS / Software

## Parte A — Conceptos

**¿Qué es la ingeniería de sistemas y por qué modelar en vez de documentar?**

La ingeniería de sistemas es una disciplina integral que gestiona proyectos complejos durante todo su ciclo de vida, centrándose en el diseño, integración y trazabilidad de las interfaces y dependencias entre múltiples subsistemas. 
Modelar (MBSE) frente a documentar permite mantener una "fuente única de verdad". Con la documentación tradicional, los cambios provocan inconsistencias entre documentos aislados. Al usar modelos, cualquier cambio se actualiza de forma centralizada y se propaga automáticamente, facilitando la detección de errores en etapas tempranas, habilitando la simulación continua y mejorando la comunicación entre todos los roles.

**Ciclo en V — dibújalo y marca hasta dónde llega este curso (rama descendente, sin Implementación)**

```text
Concepto y Necesidad (Semana 1)                            Validación (Semana 14)
  \                                                       /
   CONOPS y Casos de Uso (Semana 2)            Verificación y Cierre (S13-14)
     \                                                 /
      Requisitos del Sistema (S3-4)          Plan de Integración y Pruebas (S11-12)
        \                                           /
         Estudio de Conceptos (S5-6)              /
           \                                    /
            Arquitectura SysML (S7-10)        /
              \                             /
               Implementación (Fuera del alcance del curso)
```

**BDD y IBD, en una frase cada uno**

- **BDD (Block Definition Diagram):** Diagrama estructural que define la jerarquía del sistema, mostrando los bloques que lo componen y sus propiedades o partes.
- **IBD (Internal Block Diagram):** Diagrama que muestra la estructura interna de un bloque en particular, ilustrando cómo se conectan sus partes internas mediante flujos, puertos e interfaces.

## Parte B — El encargo

**¿Qué pide el Cliente, para qué y qué queda fuera? (3 frases)**

El cliente solicita el desarrollo de un Sistema UGV pesado de tracción de ruedas, que incluye un vehículo modular y autónomo, un UAV de apoyo y un Puesto de Mando Portable. El objetivo es utilizarlo en misiones civiles y de emergencias (incendios, logística, rescate) para sustituir a personas en tareas peligrosas, estando concebido como un robot desde el inicio y no como un vehículo tripulado adaptado. Queda fuera del alcance de este curso el diseño detallado e implementación física, las cargas de pago opcionales, y el diseño del UGV de cadenas.

**Los 4 modos de operación, una frase cada uno**

1. **APAGADO:** El UGV está sin actividad; la arquitectura, el software y las comunicaciones se encuentran sin funcionamiento.
2. **FUERA DE LÍNEA (*offline*):** Estado preparatorio para comprobar el funcionamiento de sistemas, planificar misiones en el puesto de mando o realizar mantenimiento.
3. **TELEOPERADO:** Un operador tiene el control remoto directo sobre la dirección, propulsión, frenado y cargas útiles del UGV.
4. **AUTÓNOMO:** El vehículo ejecuta tareas previamente planeadas (como navegación por waypoints o regreso automático) tomando sus propias decisiones de ruta y evasión de obstáculos, siempre bajo supervisión humana.

**Propósito del vehículo y sus 3 misiones principales, con las cifras que las condicionan**

El propósito principal es ofrecer una plataforma robótica pesada, todoterreno y modular (tara entre 3.500 y 7.000 kg, potencia ≥ 140 kW) que permita, mediante el intercambio de módulos funcionales y cargas útiles, realizar misiones de alta movilidad sin comprometer la velocidad ni la robustez.

1. **Limpieza de rutas:** Condicionada por la necesidad de incorporar el Punto de Interfaz 1 (CP-01) con una hoja quitanieves de acero Brinell ≥ 450 y anchura ≥ 2.250 mm.
2. **Función Nodriza:** Basada en la bahía de carga superior (Punto de Interfaz 3), requiriendo una plataforma para la recarga simultánea de 2 UAV (CP-09) y recarga inalámbrica para 2 UGV (CP-10) sin intervención humana.
3. **Logística y Transporte Pesado:** Condicionada por soportar una carga útil propia de ≥ 2.000 kg (RLT1-07), un peso en orden de misión de hasta 9.000 kg, y la capacidad de arrastrar un remolque trasero de ≥ 3.000 kg (RGEN-10) manteniendo velocidades de ≥ 75 km/h en carretera (RLT1-03).

**8 requisitos (ID RGEN/RLT) que crees verificables con un modelo de simulación — indica qué magnitud medirías en cada uno**

| ID | Magnitud a medir |
|---|---|
| RGEN-14 | Nivel de carga de la batería (State of Charge, %) y horas efectivas de operación en un escenario simulado para verificar las 8 horas. |
| RGEN-16 | Fuerzas en el gancho de remolque (Newtons) y estabilidad longitudinal al alcanzar los 65 km/h simulados. |
| RGEN-17 | Distancia de frenado (metros) y tiempo de respuesta (ms) del sistema automático ante la aparición repentina de un obstáculo. |
| RLT1-03 | Aceleración (m/s²) y velocidad final (km/h) logradas en un entorno de simulación 3D configurado con pendientes frontales del 60% y laterales del 30%. |
| RLT1-08 | Sumatoria automática de las propiedades de masa de los bloques en el modelo SysML (kg) para asegurar que el conjunto es ≤ 9.000 kg. |
| RLT1-09 | Par motor (Nm) y potencia mecánica (kW) entregada a las ruedas en perfiles de alta resistencia al avance. |
| RNAV-01 | Error de posicionamiento estimado (metros de desviación) tras simular la desconexión de los satélites GNSS durante un recorrido de 5 km usando odometría y la IMU. |
| RCOM-02 | Potencia de señal (dBm) y ancho de banda efectivo a una distancia > 20 km simulando atenuación y orografía (BLOS). |

**2 requisitos que NO se puedan verificar por simulación — justifica por qué**

| ID | Justificación |
|---|---|
| RGEN-06 | La resistencia física real a agentes ambientales como la corrosión, la lluvia, la humedad o la radiación solar requiere de la prueba de los materiales y recubrimientos en cámaras climáticas reales para certificar su durabilidad, estanqueidad e IP final. |
| RGEN-24 | Los puntos de amarre para aerotransporte deben certificarse con pruebas de tracción y ensayo destructivo en un entorno de laboratorio para cumplir con las normas de seguridad de carga aeronáutica, algo que un modelo informático puede aproximar pero no certificar oficialmente. |

**3 términos del glosario que no conocías, con su significado**

1. **BLOS (Beyond Line of Sight):** Control remoto o comunicaciones que se efectúan "más allá de la línea de visión", permitiendo operar a grandes distancias mediante repetidores o satélites (≥ 20 km en este proyecto).
2. **CIS:** Sistema de interfaz cartográfica. En este contexto, un software empleado para la gestión y precarga de los mapas usados por la plataforma.
3. **CRPA (Controlled Reception Pattern Antenna):** Una tecnología de antena direccional (mencionada como método antijamming en RNAV-01) usada para poder seguir navegando en ambientes donde el GPS/GNSS esté degradado o denegado.

**1 pregunta que le harías al Cliente**

¿Existe un tiempo máximo estipulado de "tolerancia" desde que se detecta el estado DEGRADADO en las comunicaciones, hasta que el UGV deba forzar obligatoriamente el frenado automático de emergencia si el regreso automático por la ruta (*regresión*) no logra recuperar la señal?
