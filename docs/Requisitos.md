# Pliego de Prescripciones Técnicas — Sistema UGV (Anexo I)

Este documento recoge la especificación completa de los requisitos funcionales, técnicos y de ejecución del proyecto UGV dual (civil-militar) conforme al pliego del **Anexo I (CPP 01/2026 AB)** del Centro para el Desarrollo Tecnológico y la Innovación (CDTI) y el Ministerio de Defensa (MINISDEF/DIGEID).

---

## 1. Matriz General de Requisitos del Sistema UGV

### Checklist de cumplimiento por requisito

#### Requisitos generales (RGEN)
- [ ] **RGEN-01** — Plataforma / Mando y Control
- [ ] **RGEN-02** — Arquitectura / Modularidad
- [ ] **RGEN-03** — Estructura / Chasis
- [ ] **RGEN-04** — Concepción Vehicular
- [ ] **RGEN-05** — Interoperabilidad / UxV
- [ ] **RGEN-06** — Resistencia Ambiental
- [ ] **RGEN-07** — Mantenibilidad / Fabricación
- [ ] **RGEN-08** — Mantenimiento 1er Escalón
- [ ] **RGEN-09** — Percepción / Seguridad
- [ ] **RGEN-10** — Capacidad de Tiro / Remolque
- [ ] **RGEN-11** — Propulsión / Planta Motriz
- [ ] **RGEN-12** — Gestión Energética / Baterías
- [ ] **RGEN-13** — Modo Puramente Eléctrico
- [ ] **RGEN-14** — Autonomía Global
- [ ] **RGEN-15** — Autonomía Eléctrica
- [ ] **RGEN-16** — Remolcado Pasivo
- [ ] **RGEN-17** — Seguridad Activa / Frenado
- [ ] **RGEN-18** — Híbrido Enchufable (PHEV)
- [ ] **RGEN-19** — Exportación de Energía
- [ ] **RGEN-20** — Iluminación Periférica
- [ ] **RGEN-21** — Protección Óptica Faros
- [ ] **RGEN-22** — Consciencia Situacional
- [ ] **RGEN-23** — Anclajes de Recuperación
- [ ] **RGEN-24** — Transporte Aéreo
- [ ] **RGEN-25** — Transporte Terrestre
- [ ] **RGEN-26** — Cabestrante y Eslingas
- [ ] **RGEN-27** — Distribución en Lotes
- [ ] **RGEN-28** — Acceso a Puntos de Interfaz
- [ ] **RGEN-29** — Estabilidad con Cargas

#### Requisitos Lote 1 (RLT1)
- [ ] **RLT1-01** — Tren de Rodaje Lote 1
- [ ] **RLT1-02** — Configuración Tracción
- [ ] **RLT1-03** — Prestaciones Cinemáticas
- [ ] **RLT1-04** — Accionamiento Ruedas
- [ ] **RLT1-05** — Sistema de Suspensión
- [ ] **RLT1-06** — Masa en Vacío
- [ ] **RLT1-07** — Capacidad de Carga Útil
- [ ] **RLT1-08** — Peso Máximo de Misión
- [ ] **RLT1-09** — Potencia de Propulsión
- [ ] **RLT1-10** — Capacidad de Vadeo
- [ ] **RLT1-11** — Protección Balística
- [ ] **RLT1-12** — Interfaz Frontal (Punto 1)
- [ ] **RLT1-13** — Interfaz Superior (Puntos 2 y 3)
- [ ] **RLT1-14** — Interfaz Trasera (Punto 4)

#### Requisitos Lote 2 (RLT2)
- [ ] **RLT2-01** — Tren de Rodaje Cadenas
- [ ] **RLT2-02** — Prestaciones Cadenas
- [ ] **RLT2-03** — Modos de Trabajo Dual
- [ ] **RLT2-04** — Masa en Vacío
- [ ] **RLT2-05** — Capacidad de Carga Útil
- [ ] **RLT2-06** — Peso Máximo de Misión
- [ ] **RLT2-07** — Potencia Motriz e Hidráulica
- [ ] **RLT2-08** — Capacidad de Vadeo
- [ ] **RLT2-09** — Anchura en Transporte
- [ ] **RLT2-10** — Protección FOPS Nivel II
- [ ] **RLT2-11** — Iluminación Periférica 360°
- [ ] **RLT2-12** — Rejillas Protectoras Faros
- [ ] **RLT2-13** — Cajones de Herramientas
- [ ] **RLT2-14** — Extintores de Incendios
- [ ] **RLT2-15** — Protección Térmica Ignífuga
- [ ] **RLT2-16** — Especificación de Fundas
- [ ] **RLT2-17** — Desacoplamiento Orugas
- [ ] **RLT2-18** — Interfaz Frontal (Puntos 1 y 2)
- [ ] **RLT2-19** — Interfaz Superior (Puntos 3 y 4)
- [ ] **RLT2-20** — Interfaz Trasera (Puntos 5 y 6)

#### Requisitos operativos (ROPE)
- [ ] **ROPE-01** — Modos Operativos Principales
- [ ] **ROPE-02** — Control en Modo Teleoperado
- [ ] **ROPE-03** — Estaciones de Teleoperación
- [ ] **ROPE-04** — Modos de Apoyo del UAV
- [ ] **ROPE-05** — Submodos de Navegación Autónoma
- [ ] **ROPE-06** — Detección y Evasión Obstáculos
- [ ] **ROPE-07** — Ciclo de Vida de Misiones
- [ ] **ROPE-08** — Requisitos Mínimos de Misión
- [ ] **ROPE-09** — Catálogo de Misiones a Validar
- [ ] **ROPE-10** — Conmutación de Modos sin Retardo

#### Requisitos del Puesto de Operación (RPdO)
- [ ] **RPdO-01** — Movilidad del Puesto de Operación
- [ ] **RPdO-02** — Precarga Cartográfica CIS
- [ ] **RPdO-03** — Consciencia Situacional Avanzada
- [ ] **RPdO-04** — Ergonomía de Interfaces HMI
- [ ] **RPdO-05** — Maletas Rugerizadas
- [ ] **RPdO-06** — Tres Interfaces Independientes
- [ ] **RPdO-07** — Conmutación de Señales de Vídeo
- [ ] **RPdO-08** — Interfaz Inmersivo Háptico / AR

#### Requisitos de navegación (RNAV)
- [ ] **RNAV-01** — Navegación en GNSS Denegado

#### Requisitos de comunicaciones (RCOM)
- [ ] **RCOM-01** — Módulos de Comunicaciones
- [ ] **RCOM-02** — Alcance BLOS ≥ 20 km
- [ ] **RCOM-03** — Aseguramiento de Comunicaciones
- [ ] **RCOM-04** — Autorecuperación de Enlace
- [ ] **RCOM-05** — Carrete de Fibra Óptica

#### Requisitos de software (RSW)
- [ ] **RSW-01** — Arquitectura SW Modular
- [ ] **RSW-02** — Documentación SW en SysML / UML
- [ ] **RSW-03** — Especificación de Interfaces I/O
- [ ] **RSW-04** — Entregables Software Íntegros
- [ ] **RSW-05** — Registro de Dependencias Software
- [ ] **RSW-06** — Escudos Institucionales en GUI
- [ ] **RSW-07** — Formato de Vídeo y Metadatos KLV
- [ ] **RSW-08** — Retransmisión RTSP/RTP Multicast

#### Requisitos de pruebas y validación (RPVyA)
- [ ] **RPVyA-01** — Cobertura Matricial de Ensayos
- [ ] **RPVyA-02** — Cesión de Licencias para Ensayos
- [ ] **RPVyA-03** — Rotulación con Emblemas
- [ ] **RPVyA-04** — Pruebas de Verificación (Fase II)
- [ ] **RPVyA-05** — Supervisión de Verificación
- [ ] **RPVyA-06** — Instalaciones de Verificación
- [ ] **RPVyA-07** — Pruebas de Validación (Fase III)
- [ ] **RPVyA-08** — Cursos de Formación a Dotaciones
- [ ] **RPVyA-09** — Campaña de Validación Semanal

#### Requisitos documentales (RDOC)
- [ ] **RDOC-01** — Formato Dual PDF y Editable
- [ ] **RDOC-02** — Convención de Nomenclatura
- [ ] **RDOC-03** — Entregas Parciales en Soporte USB
- [ ] **RDOC-04** — Entrega Digital Final
- [ ] **RDOC-05** — Plan de Gestión del Proyecto
- [ ] **RDOC-06** — Mantenimiento Vivo del Plan
- [ ] **RDOC-07** — Plan de Gestión de Configuración
- [ ] **RDOC-08** — Plan de Gestión de Riesgos
- [ ] **RDOC-09** — Plan de Pruebas
- [ ] **RDOC-10** — Protocolo de Pruebas
- [ ] **RDOC-11** — Resultados de Pruebas
- [ ] **RDOC-12** — Informe de Pruebas Incremental
- [ ] **RDOC-13** — Arquitectura General en SysML
- [ ] **RDOC-14** — Diseño Hardware Jerárquico
- [ ] **RDOC-15** — Estructura del Diseño Hardware
- [ ] **RDOC-16** — Ficha de Hardware Programable
- [ ] **RDOC-17** — Diseño Software en SysML / UML
- [ ] **RDOC-18** — Estrategia de Propiedad Intelectual

Tabla comprensiva con la totalidad de los requisitos técnicos del pliego clasificados por su identificador oficial, subsistema, lote de aplicación, tipología (Obligatorio u Opcional) y descripción cuantitativa y cualitativa detallada.

| ID Pliego | Subsistema / Área | Ámbito / Lote | Tipo | Descripción y Parámetros Técnicos | Propuesta de Solución / Ideas del Equipo |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **RGEN-01** | Plataforma / Mando y Control | Común (Lote 1 y 2) | **Obligatorio** | Diseño, desarrollo e instalación de plataforma terrestre no tripulada con gobierno autónomo y capacidad de supervisión y control remoto desde Puesto de Mando Portable (PMP). | |
| **RGEN-02** | Arquitectura / Modularidad | Común (Lote 1 y 2) | **Obligatorio** | Alta modularidad y adaptabilidad de uso dual (civil y militar), facilitando la reconfiguración rápida de módulos funcionales intercambiables sobre la plataforma. | |
| **RGEN-03** | Estructura / Chasis | Común (Lote 1 y 2) | **Obligatorio** | Barcaza principal común: un único bastidor servirá para todas las configuraciones de cada lote mediante acoplamiento/desacoplamiento simple de módulos, accesorios e implementos. | |
| **RGEN-04** | Concepción Vehicular | Común (Lote 1 y 2) | **Obligatorio** | Concepción nativa como robot autónomo no tripulado desde el diseño inicial, prescindiendo del espacio, peso y blindaje de habitáculo para tripulación. Se excluyen explícitamente vehículos tripulados robotizados. | |
| **RGEN-05** | Interoperabilidad / UxV | Común (Lote 1 y 2) | **Obligatorio** | Arquitectura abierta para integrar nuevos módulos funcionales, cargas de pago e implementos, así como vincular e interoperar con otros sistemas no tripulados (UxV) en misiones conjuntas. | |
| **RGEN-06** | Resistencia Ambiental | Común (Lote 1 y 2) | **Obligatorio** | Resistencia de la plataforma, subsistemas y componentes a agentes ambientales severos: temperaturas extremas, lluvia, humedad, corrosión y radiación solar. | |
| **RGEN-07** | Mantenibilidad / Fabricación | Común (Lote 1 y 2) | **Obligatorio** | Proceso de fabricación lo más simple y económico posible para abaratar costes de reparación, mantenimiento o reemplazo si sufre daños o destrucción en combate/misión. | |
| **RGEN-08** | Mantenimiento 1er Escalón | Común (Lote 1 y 2) | **Opcional** (OG-01) | Minimizar la variedad de herramientas requeridas para operaciones y reparaciones de Primer Escalón de todo el Sistema UGV. | |
| **RGEN-09** | Percepción / Seguridad | Común (Lote 1 y 2) | **Obligatorio** | Sistema de detección de obstáculos estáticos y dinámicos basado en tecnologías radiantes (LiDAR, radar...) y no radiantes (visión artificial...). Capacidad de alternar entre Modo SIGILOSO (solo no radiantes) y Modo NORMAL (ambas), operable desde cualquier Equipo de Control y en cualquier modo de operación. | |
| **RGEN-10** | Capacidad de Tiro / Remolque | Común (Lote 1 y 2) | **Obligatorio** | Capacidad para arrastrar e incorporar un remolque trasero de masa ≥ 3.000 kg. Gancho o enganche conforme a dimensiones normalizadas STANAG 4101 (deseable escamotable). | |
| **RGEN-11** | Propulsión / Planta Motriz | Común (Lote 1 y 2) | **Obligatorio** | Tren de propulsión híbrida compuesto por pack de baterías, motor eléctrico y motor de combustión interna capaz de funcionar con biocombustible al 100%. | |
| **RGEN-12** | Gestión Energética / Baterías | Común (Lote 1 y 2) | **Obligatorio** | Baterías recargables en marcha por el motor de combustión interna y por recuperación de energía en fases de deceleración y frenada (frenada regenerativa). | |
| **RGEN-13** | Modo Puramente Eléctrico | Común (Lote 1 y 2) | **Obligatorio** | Modo de marcha 100% eléctrico silencioso (solo motor eléctrico y baterías, prescindiendo del motor térmico) para operar de forma sigilosa con firma térmica y acústica reducida. | |
| **RGEN-14** | Autonomía Global | Común (Lote 1 y 2) | **Obligatorio** | Autonomía total combinada de la plataforma de al menos 8 horas de funcionamiento continuo o 400 km de desplazamiento como mínimo. | |
| **RGEN-15** | Autonomía Eléctrica | Común (Lote 1 y 2) | **Obligatorio** | Autonomía en modo puramente eléctrico de al menos 2 horas de funcionamiento continuo o 100 km de recorrido como mínimo. | |
| **RGEN-16** | Remolcado Pasivo | Común (Lote 1 y 2) | **Obligatorio** | Capacidad del UGV de ser remolcado pasivamente por otros vehículos de la unidad a una velocidad máxima de al menos 65 km/h. | |
| **RGEN-17** | Seguridad Activa / Frenado | Común (Lote 1 y 2) | **Obligatorio** | Frenado automático progresivo ante riesgo inminente de colisión. Función inhabilitable manualmente por el operador para impedir bloqueos inducidos por señuelos enemigos. | |
| **RGEN-18** | Híbrido Enchufable (PHEV) | Común (Lote 1 y 2) | **Opcional** (OG-02) | Movilidad híbrida enchufable: recarga de baterías mediante motor térmico, frenada regenerativa y conexión física a tomas de recarga eléctrica externas. | |
| **RGEN-19** | Exportación de Energía | Común (Lote 1 y 2) | **Opcional** (OG-03) | Capacidad de exportación de energía eléctrica desde el tren motriz hacia sistemas o redes externas a la plataforma con una potencia mínima de 120 kW. | |
| **RGEN-20** | Iluminación Periférica | Común (Lote 1 y 2) | **Obligatorio** | Sistema de iluminación exterior con cobertura periférica de 360°, orientable, graduable y gobernable a distancia por el operador. | |
| **RGEN-21** | Protección Óptica Faros | Común (Lote 1 y 2) | **Obligatorio** | Rejillas de protección en grupos ópticos para soportar impactos de ramas y retener piedras de al menos 3 cm de diámetro sin degradar la emisión lumínica. | |
| **RGEN-22** | Consciencia Situacional | Común (Lote 1 y 2) | **Obligatorio** | Conjunto de captadores de imagen y sensores protegidos: visualización directa de implementos y rodaje, cámaras laterales independientes, visión de profundidad 360° y cámara térmica para identificación de puntos calientes. | |
| **RGEN-23** | Anclajes de Recuperación | Común (Lote 1 y 2) | **Obligatorio** | Puntos de anclaje específicos para rescate o auto-rescate por tracción mediante eslingas y perrillos. | |
| **RGEN-24** | Transporte Aéreo | Común (Lote 1 y 2) | **Obligatorio** | Puntos de amarre y estiba aptos para aerotransporte como carga en aeronaves de ala fija (dimensionamiento según factores de carga del STANAG 3400 ed. 2010, apartado 2.a). | |
| **RGEN-25** | Transporte Terrestre | Común (Lote 1 y 2) | **Obligatorio** | Puntos de amarre y estiba aptos para transporte seguro por vía terrestre como carga sobre plataforma/góndola conforme a la norma UNE-EN 12195. | |
| **RGEN-26** | Cabestrante y Eslingas | Común (Lote 1 y 2) | **Obligatorio** | Cabestrante de gran capacidad y/o tracción por eslingas con protocolos de seguridad para operación en terrenos difíciles, recuperación de vehículos atrapados y auto-recuperación. | |
| **RGEN-27** | Distribución en Lotes | Común (Lote 1 y 2) | **Obligatorio** | Selección de desarrollo bajo Lote 1 (ruedas) o Lote 2 (cadenas). Opcionalmente se permite participar en el desarrollo de ambos lotes de forma independiente. | |
| **RGEN-28** | Acceso a Puntos de Interfaz | Común (Lote 1 y 2) | **Obligatorio** | Disponibilidad de Puntos de Interfaz accesibles (mecánicos, eléctricos y lógicos) para integrar cargas útiles. Desarrollo y entrega obligatoria de las cargas OBLIGATORIAS y opcional para las OPCIONALES. | |
| **RGEN-29** | Estabilidad con Cargas | Común (Lote 1 y 2) | **Obligatorio** | Diseño de los Puntos de Interfaz que garantiza la estabilidad física y dinámica del UGV tanto con cargas útiles instaladas como sin ninguna carga acoplada. | |
| **RLT1-01** | Tren de Rodaje Lote 1 | Lote 1 (Ruedas) | **Obligatorio** | Tren de tracción basado exclusivamente en ruedas para maximizar velocidades en terrenos llanos y consolidados. | |
| **RLT1-02** | Configuración Tracción | Lote 1 (Ruedas) | **Obligatorio** | Esquema de tracción en ruedas 4x4, 6x6 u 8x8 con altas prestaciones de movilidad en entornos todoterreno (off-road) de dificultad media a alta velocidad. | |
| **RLT1-03** | Prestaciones Cinemáticas | Lote 1 (Ruedas) | **Obligatorio** | Parámetros mínimos de movilidad en carretera y campo a través:<br>a) Velocidad máx. en carretera ≥ 75 km/h.<br>b) Velocidad máx. campo a través ≥ 50 km/h.<br>c) Pendiente frontal máxima superable ≥ 60%.<br>d) Pendiente lateral máxima superable ≥ 30%.<br>e) Escalón vertical franqueable ≥ 30 cm (deseable 40 cm).<br>*(Admite degradación en arena, guijarros, nieve, hielo o barro)*. | |
| **RLT1-04** | Accionamiento Ruedas | Lote 1 (Ruedas) | **Obligatorio** | Implementación de tracción directa e independiente en cada una de las ruedas de la plataforma. | |
| **RLT1-05** | Sistema de Suspensión | Lote 1 (Ruedas) | **Obligatorio** | Suspensión neumática retráctil y regulable en altura de forma independiente en cada brazo de suspensión de cada rueda. | |
| **RLT1-06** | Masa en Vacío (Tara) | Lote 1 (Ruedas) | **Obligatorio** | Tara o peso en vacío del UGV comprendido estrictamente entre 3.500 kg y 7.000 kg. | |
| **RLT1-07** | Capacidad de Carga Útil | Lote 1 (Ruedas) | **Obligatorio** | Capacidad de carga neta transportable (payload) ≥ 2.000 kg. | |
| **RLT1-08** | Peso Máximo de Misión | Lote 1 (Ruedas) | **Obligatorio** | Peso total máximo en orden de combate/misión (GVW) no superior a 9.000 kg en ningún caso. | |
| **RLT1-09** | Potencia de Propulsión | Lote 1 (Ruedas) | **Obligatorio** | Potencia continua total combinada del sistema de propulsión ≥ 140 kW (190 CV). | |
| **RLT1-10** | Capacidad de Vadeo | Lote 1 (Ruedas) | **Obligatorio** | Vadeo en profundidad sin preparación previa ≥ 0,75 m (75 cm) tanto en agua dulce como salada. | |
| **RLT1-11** | Protección Balística | Lote 1 (Ruedas) | **Opcional** (OG-04) | Blindaje modular o desmontable capaz de detener proyectiles de armas de fuego de pequeño calibre comúnmente usadas por combatientes. | |
| **RLT1-12** | Interfaz Frontal (Punto 1) | Lote 1 (Ruedas) | **Obligatorio / Opcional** | Interfaz electromecánico frontal para cargas de vialidad:<br>• **CP-01 Hoja quitanieves** (**Obligatoria**): ancho ≥ 2.250 mm, orientación bilateral hidráulica, acero dureza Brinell ≥ 450.<br>• **CP-02 Fresadora de nieve** (**Opcional**, ILT1-01): ancho trabajo ≥ 2.000 mm, altura corte ≥ 1.000 mm, tiro chimenea orientable ≥ 25 m.<br>• **CP-03 Rodillo antiminas** (**Opcional**, ILT1-02): ancho barrido ≥ 2,2 m (> ancho UGV), vel. > 5 km/h, presión ≥ 300 kg/rueda antipinchazos, seguimiento constante del relieve. | |
| **RLT1-13** | Interfaz Superior (Puntos 2 y 3) | Lote 1 (Ruedas) | **Obligatorio / Opcional** | Interfaces en zona superior:<br>• **Punto de Interfaz 2 (Efectores y sensores tácticos)**:<br>&nbsp;&nbsp;- **CP-04 RWS** (**Obligatoria**): estación de armas remota nacional para autoprotección y paz.<br>&nbsp;&nbsp;- **CP-05 Mástil optrónico ISTAR** (**Opcional**, ILT1-04): mástil retráctil con sensor EO/IR estabilizado.<br>&nbsp;&nbsp;- **CP-06 Brazo robótico NRBQ/EOD** (**Opcional**, ILT1-03): brazo articulado con cámaras para toma de muestras y desactivación.<br>• **Punto de Interfaz 3 (Bahía de Carga)**:<br>&nbsp;&nbsp;- **CP-07 Logística** (**Opcional**, ILT1-06): transporte de pertrechos, materiales y víveres.<br>&nbsp;&nbsp;- **CP-08 MEDEVAC** (**Opcional**, ILT1-05): acople de camillas o células medicalizadas para evacuación.<br>&nbsp;&nbsp;- **CP-09 Recarga dual UAV** (**Obligatoria**): recarga simultánea de 2 UAV (UAV Apoyo + 1 externo).<br>&nbsp;&nbsp;- **CP-10 Recarga inalámbrica UGV nodriza** (**Obligatoria**): puntos de recarga inalámbrica (≥ 2) para UGV ligeros con rampa de acceso autónomo.<br>&nbsp;&nbsp;- **CP-11 Manguera explosiva** (**Opcional**, ILT1-07): contenedor o réplica para brechas minadas.<br>&nbsp;&nbsp;- **CP-12 Tolva esparcidora de sal** (**Opcional**, ILT1-08): volumen tolva ≥ 1,2 m³, proyección 2-6 m, boquilla trasera.<br>&nbsp;&nbsp;- **CP-13 Contenedor NRBQ** (**Opcional**): compartimentado para muestras químicas/biológicas + contenedor blindado radiológico. | |
| **RLT1-14** | Interfaz Trasera (Punto 4) | Lote 1 (Ruedas) | **Obligatorio** | Interfaz mecánico de enganche de tiro:<br>• **CP-14 Sistema de enganche** (**Obligatoria**): arrastre de remolques de hasta 3.000 kg de masa. | |
| **RLT2-01** | Tren de Rodaje Cadenas | Lote 2 (Cadenas) | **Obligatorio** | Tren de rodaje por orugas / cadenas metálicas para máxima flotabilidad, estabilidad y tracción en orografía todoterreno severa y terrenos resbaladizos. | |
| **RLT2-02** | Prestaciones Cadenas | Lote 2 (Cadenas) | **Obligatorio** | Parámetros mínimos de movilidad en carretera y campo a través:<br>a) Velocidad máx. en carretera ≥ 50 km/h.<br>b) Velocidad máx. campo a través ≥ 40 km/h.<br>c) Pendiente máxima frontal superable ≥ 60%.<br>d) Pendiente máxima lateral superable ≥ 30%.<br>e) Escalón vertical franqueable ≥ 40 cm. | |
| **RLT2-03** | Modos de Trabajo Dual | Lote 2 (Cadenas) | **Opcional** (OG-05) | Dos funciones de régimen de trabajo: alta potencia de empuje (velocidad máxima acotada a ≤ 14 km/h) y modo transporte (sin limitación de velocidad máxima). | |
| **RLT2-04** | Masa en Vacío (Tara) | Lote 2 (Cadenas) | **Obligatorio** | Tara o peso en vacío comprendido entre 9.000 kg y 12.000 kg. | |
| **RLT2-05** | Capacidad de Carga Útil | Lote 2 (Cadenas) | **Obligatorio** | Capacidad de carga neta transportable ≥ 4.000 kg. | |
| **RLT2-06** | Peso Máximo de Misión | Lote 2 (Cadenas) | **Obligatorio** | Masa máxima total del UGV en orden de combate/misión ≤ 17.000 kg. | |
| **RLT2-07** | Potencia Motriz e Hidráulica | Lote 2 (Cadenas) | **Obligatorio** | Potencia continua de propulsión ≥ 200 kW (270 CV), picos eléctricos de 250-300 kW, y potencia hidráulica disponible para implementos de al menos 100-120 kW. | |
| **RLT2-08** | Capacidad de Vadeo | Lote 2 (Cadenas) | **Obligatorio** | Vadeo en profundidad sin preparación previa ≥ 1,2 m en aguas dulces o saladas. | |
| **RLT2-09** | Anchura en Transporte | Lote 2 (Cadenas) | **Obligatorio** | Anchura máxima total en configuración de transporte con hoja dozer y ripper montados ≤ 3,0 m. | |
| **RLT2-10** | Protección FOPS Nivel II | Lote 2 (Cadenas) | **Obligatorio** | Estructura protegida integralmente contra impactos y caídas con certificación FOPS Nivel II según norma UNE-EN ISO 3449. Diseño antienredos en vegetación para cámaras, sensores y conexiones. | |
| **RLT2-11** | Iluminación Periférica 360° | Lote 2 (Cadenas) | **Obligatorio** | Sistema de iluminación exterior con cobertura perimetral completa de 360°. | |
| **RLT2-12** | Rejillas Protectoras Faros | Lote 2 (Cadenas) | **Obligatorio** | Rejillas en grupos ópticos para retener piedras de al menos 3 cm de diámetro e impactos de ramas sin deteriorar el haz luminoso. | |
| **RLT2-13** | Cajones de Herramientas | Lote 2 (Cadenas) | **Obligatorio** | Cajones de almacenamiento estancos integrados en la barcaza para herramientas de Primer Escalón y pertrechos de campaña. | |
| **RLT2-14** | Extintores de Incendios | Lote 2 (Cadenas) | **Opcional** (OG-06) | Espacio específico para alojamiento seguro de dos extintores portátiles de 9 kg cada uno (fuego clase ABC). | |
| **RLT2-15** | Protección Térmica Ignífuga | Lote 2 (Cadenas) | **Opcional** (OG-07) | Fundas ignífugas para servicio continuo ≥ 260 °C en cableado eléctrico, conducciones de combustible, refrigerante, frenado y latiguillos hidráulicos externos; protección frente a abrasión en tren de rodaje; aceite hidráulico con temperatura de ignición ≥ 120 °C. | |
| **RLT2-16** | Especificación de Fundas | Lote 2 (Cadenas) | **Opcional** (OG-08) | Fundas de tubo trenzado de fibra de vidrio recubierto de silicona: aptas para rango continuo de -60 °C a 260 °C; resistencia ignífuga de al menos 30 min a 800 °C, 15 min a 1.100 °C y 1 min a 1.500 °C. | |
| **RLT2-17** | Desacoplamiento Orugas | Lote 2 (Cadenas) | **Opcional** (OG-09) | Mecanismo manual para desacoplamiento de componentes motrices de las orugas que garantice giro libre para remolque por arrastre sin necesidad de herramientas. | |
| **RLT2-18** | Interfaz Frontal (Puntos 1 y 2) | Lote 2 (Cadenas) | **Obligatorio / Opcional** | Interfaces frontales:<br>• **Punto de Interfaz 1 (Viales y Movimiento de Tierras)**:<br>&nbsp;&nbsp;- **CP-15 Hoja dozer** (**Obligatoria**): ancho ≥ 3.000 mm, alto ≥ 1.200 mm, regulación hidráulica de elevación, inclinación y ataque; excavación ≥ 450 mm, plegable o regulable en anchura.<br>&nbsp;&nbsp;- **CP-16 Rodillo antiminas** (**Opcional**, ILT2-02): ancho barrido ≥ 2,2 m (> ancho UGV), vel. > 5 km/h, presión ≥ 300 kg/rueda antipinchazos.<br>&nbsp;&nbsp;- **CP-17 Desbrozadora forestal** (**Opcional**, ILT2-01): ancho ≥ 2 m, trituración monte bajo y árboles ≤ 15 cm, rendimiento > 0,4 ha/h (deseable 0,6 ha/h).<br>• **Punto de Interfaz 2 (Carga frontal independiente)**:<br>&nbsp;&nbsp;- **CP-18 Cuchara cargadora** (**Opcional**, ILT2-03): ancho ≥ 2.250 mm, capacidad colmada ≥ 1 m³, montada sobre 2 brazos hidráulicos. | |
| **RLT2-19** | Interfaz Superior (Puntos 3 y 4) | Lote 2 (Cadenas) | **Obligatorio / Opcional** | Interfaces superiores:<br>• **Punto de Interfaz 3 (Extinción de Incendios)**:<br>&nbsp;&nbsp;- **CP-19 Bomba impulsión alta presión** (**Obligatoria**): presión > 20 bar, caudal ≥ 220 L/min; monitor: giro 85° V / 360° H, cono 0-90°, 19-200 L/min, presión 6-9 bar, generación de espuma.<br>• **Punto de Interfaz 4 (Bahía de Carga)**:<br>&nbsp;&nbsp;- **CP-20 Logística** (**Opcional**, ILT2-05): transporte de equipos, pertrechos y víveres.<br>&nbsp;&nbsp;- **CP-21 Manguera explosiva** (**Opcional**, ILT2-06): contenedor o réplica para brechas minadas.<br>&nbsp;&nbsp;- **CP-22 Depósito de agua** (**Obligatoria**): volumen ≥ 2.750 L, tomas Barcelona de 25 mm (salida manguera a pie), 45 mm y 70 mm (llenado).<br>&nbsp;&nbsp;- **CP-23 Tolva volquete** (**Opcional**, ILT2-04): contenedor basculante abierto para tierras y escombros. | |
| **RLT2-20** | Interfaz Trasera (Puntos 5 y 6) | Lote 2 (Cadenas) | **Obligatorio / Opcional** | Interfaces traseros:<br>• **Punto de Interfaz 5 (Escarificación y Freno)**:<br>&nbsp;&nbsp;- **CP-24 Arado / ripper 3 rejones** (**Obligatoria**): penetración ≥ 28 cm, anchura útil 2,5-3 m (> ancho UGV), rompedor de rocas y freno/contrapeso.<br>• **Punto de Interfaz 6 (Excavación Profunda)**:<br>&nbsp;&nbsp;- **CP-25 Brazo retroexcavador** (**Opcional**, ILT2-07): cazo 500-700 mm, volumen ≥ 0,20 m³, alcance horizontal ≥ 5,5 m, profundidad excavación ≥ 4,5 m. | |
| **ROPE-01** | Modos Operativos Principales | Común (Lote 1 y 2) | **Obligatorio** | Implementación obligatoria de tres modos operativos:<br>a) Modo TELEOPERADO.<br>b) Modo AUTÓNOMO.<br>c) Modo FUERA DE LÍNEA (offline) para planeamiento de misiones, transporte, chequeos y mantenimiento. | |
| **ROPE-02** | Control en Modo Teleoperado | Común (Lote 1 y 2) | **Obligatorio** | Control remoto directo de dirección, aceleración, frenado, modos de propulsión, suspensión, iluminación, refrigeración, cámaras perimetrales y cargas útiles integradas. | |
| **ROPE-03** | Estaciones de Teleoperación | Común (Lote 1 y 2) | **Obligatorio** | Teleoperación del UGV indistinta desde Puesto de Operador o Dispositivo de Telemando Portable tipo tablet, apoyándose en vídeo en vivo del UAV de apoyo. | |
| **ROPE-04** | Modos de Apoyo del UAV | Común (Lote 1 y 2) | **Obligatorio** | UAV de Apoyo con dos modos de vuelo: Modo TELEOPERADO (control manual independiente) y Modo CAUTIVO VIRTUAL (seguimiento autónomo permanente del UGV), activables desde controles remotos en cualquier modo de operación. | |
| **ROPE-05** | Submodos de Navegación Autónoma | Común (Lote 1 y 2) | **Obligatorio** | Capacidades de autonomía vehicular integradas:<br>a) Puntos de paso (waypoints predefinidos o en tiempo real).<br>b) Punto de destino autónomo (planificación dinámica, búsqueda de trayectorias, maniobras de escape/retroceso).<br>c) Regreso autónomo al origen o punto anterior ("Vuelta a casa").<br>d) Seguimiento autónomo (Follow-me) de personas u otros vehículos.<br>e) Modo lanzadera (Shuttle) bidireccional continuo entre dos puntos. | |
| **ROPE-06** | Detección y Evasión Obstáculos | Común (Lote 1 y 2) | **Obligatorio** | Capacidad "Detectar y Evadir" obstáculos dinámicos y estáticos en modo autónomo (recalculo de ruta, marcha atrás o desvíos), funcional tanto en Modo NORMAL como en Modo SIGILOSO. | |
| **ROPE-07** | Ciclo de Vida de Misiones | Común (Lote 1 y 2) | **Obligatorio** | Fases estructuradas de misión:<br>a) Planeamiento: offline vía GUI, exportación de archivo de misión y carga en BD del UGV.<br>b) Ejecución: lanzamiento desde Puesto de Operación en modo teleoperado o autónomo conmutables.<br>c) Finalización: retorno a offline, descarga de datos/vídeo a mandos superiores, mantenimiento de 1er escalón y recarga de baterías. | |
| **ROPE-08** | Requisitos Mínimos de Misión | Común (Lote 1 y 2) | **Obligatorio** | Toda misión debe tener predefinidos al menos el modo teleoperado y la rutina de vuelta a casa; no se ejecutará ninguna rutina autónoma no especificada en el plan de misión salvo pausa o cancelación. | |
| **ROPE-09** | Catálogo de Misiones a Validar | Común (Lote 1 y 2) | **Obligatorio** | Ejecución y validación en Fases II y III de perfiles de misión por lote:<br>• **Lote 1**: ISTAR, NRBQ, Mantenimiento de la Paz, Logística, MEDEVAC, Búsqueda y Rescate (SAR), Nodriza, Limpieza de Rutas, Apertura de Brechas, Tormentas Invernales.<br>• **Lote 2**: Extinción de Incendios Forestales, Catástrofes/Emergencias, Ingenieros y Zapadores. | |
| **ROPE-10** | Conmutación de Modos sin Retardo | Común (Lote 1 y 2) | **Obligatorio** | Conmutación ágil, inmediata y sin retardo funcional entre modos durante el desarrollo de la misión. | |
| **RPdO-01** | Movilidad del Puesto de Operación | Común (Lote 1 y 2) | **Obligatorio** | Puesto de Operación móvil y fácilmente embarcable en vehículo tipo shelter o contenedor transportable; permite teleoperación y supervisión de autonomía a distancia. | |
| **RPdO-02** | Precarga Cartográfica CIS | Común (Lote 1 y 2) | **Obligatorio** | Capacidad de precargar mapas del teatro de operaciones en el sistema CIS del UGV como base de soporte a la navegación autónoma. | |
| **RPdO-03** | Consciencia Situacional Avanzada | Común (Lote 1 y 2) | **Obligatorio** | Capacidades sensoriales periféricas:<br>a) Percepción en visibilidad degradada (humo, niebla, lluvia intensa, vegetación, polvo).<br>b) Visión perimetral 360° diurna y nocturna bajo condiciones ambientales extremas. | |
| **RPdO-04** | Ergonomía de Interfaces HMI | Común (Lote 1 y 2) | **Obligatorio** | Presentación estructurada y ergonómica de datos (conducción visual/auditiva/háptica, misión y estado de la plataforma) en cualquier entorno sin fatiga cognitiva para el operador. | |
| **RPdO-05** | Maletas Rugerizadas | Común (Lote 1 y 2) | **Obligatorio** | Puesto de Operación transportable en maletas/baúles de transporte rugerizados de alta resistencia. | |
| **RPdO-06** | Tres Interfaces Independientes | Común (Lote 1 y 2) | **Obligatorio** | Disposición de tres interfaces independientes (conducción, misión y carga útil), operándose los módulos de conducción y misión por un único operador. | |
| **RPdO-07** | Conmutación de Señales de Vídeo | Común (Lote 1 y 2) | **Obligatorio** | Capacidad de selección y visualización libre de los canales de vídeo a requerimiento del operador en tiempo real. | |
| **RPdO-08** | Interfaz Inmersivo Háptico / AR | Común (Lote 1 y 2) | **Opcional** (OG-10) | Interfaz inmersivo con tecnologías hápticas y de Realidad Aumentada (AR) para optimizar el control y la comprensión situacional del vehículo. | |
| **RNAV-01** | Navegación en GNSS Denegado | Común (Lote 1 y 2) | **Obligatorio** | Sistema de navegación alternativo a GNSS con al menos tres tecnologías independientes de satélite (IMU, odometría visual, CRPA, odometría mecánica...):<br>a) Estimación de posición con mínimo error acumulado.<br>b) Mantenimiento de navegación autónoma segura durante un trayecto mínimo de 5 km sin señal satelital o hasta recuperar la cobertura. | |
| **RCOM-01** | Módulos de Comunicaciones | Común (Lote 1 y 2) | **Obligatorio** | Tres módulos de comunicaciones alternativos:<br>a) Enlace 5G para seguridad civil con opción de cifrador COMSEC externo.<br>b) Enlace radio militar con TRANSEC, opción COMSEC, interoperable con redes FAS y resistente a perturbaciones y guerra electrónica.<br>c) Terminal SATCOM civil con servicio garantizado durante proyecto y garantía, sustituible por terminal militar equivalente. | |
| **RCOM-02** | Alcance BLOS ≥ 20 km | Común (Lote 1 y 2) | **Obligatorio** | Rango operativo de enlace más allá de la línea de vista (BLOS) ≥ 20 km entre UGV y Puesto de Mando (teleoperación, telemetría y supervisión de autonomía). | |
| **RCOM-03** | Aseguramiento de Comunicaciones | Común (Lote 1 y 2) | **Obligatorio** | Monitorización de enlace en dos estados: NORMAL y DEGRADADO (por guerra electrónica, interferencias o pérdidas de LOS), con detección y respuesta autónoma. | |
| **RCOM-04** | Autorecuperación de Enlace | Común (Lote 1 y 2) | **Obligatorio** | Mecanismo de recuperación ante enlace DEGRADADO:<br>• En teleoperación: regreso automático sobre sus pasos por la ruta previa hasta restablecer el enlace.<br>• En modo autónomo: continuidad con la misión planificada. | |
| **RCOM-05** | Carrete de Fibra Óptica | Común (Lote 1 y 2) | **Opcional** (OG-11) | Cable de fibra óptica en carrete de al menos 100 m para teleoperar cargas útiles bajo burbuja de inhibición electrónica severa desde puesto móvil. | |
| **RSW-01** | Arquitectura SW Modular | Común (Lote 1 y 2) | **Obligatorio** | Toda la arquitectura de software desarrollada debe ser modular, desacoplada y mantenible. | |
| **RSW-02** | Documentación SW en SysML / UML | Común (Lote 1 y 2) | **Obligatorio** | Explicación formal de arquitectura software mediante diagramas UML y/o SysML y textos descriptivos de módulos embarcados y de estaciones de control. | |
| **RSW-03** | Especificación de Interfaces I/O | Común (Lote 1 y 2) | **Obligatorio** | Documentación detallada de interfaces de entrada/salida (APIs, protocolos, formatos de datos) de todos los módulos software. | |
| **RSW-04** | Entregables Software Íntegros | Común (Lote 1 y 2) | **Obligatorio** | Entrega como producto software de código fuente, scripts de generación/compilación, binarios, librerías online/offline, archivos de configuración, datasets de prueba y licencias necesarias. | Propuesta de Solución / Ideas del Equipo |
| **RSW-05** | Registro de Dependencias Software | Común (Lote 1 y 2) | **Obligatorio** | Inventario exhaustivo de dependencias software: librerías, compiladores, intérpretes y versiones de sistemas operativos empleados. | |
| **RSW-06** | Escudos Institucionales en GUI | Común (Lote 1 y 2) | **Obligatorio** | Toda aplicación con interfaz gráfica GUI debe mostrar los escudos de CDTI y MINISDEF/DIGEID en pantalla de bienvenida durante 2 segundos, y de forma permanente en pantalla principal. | |
| **RSW-07** | Formato de Vídeo y Metadatos KLV | Común (Lote 1 y 2) | **Obligatorio** | Formatos de almacenamiento y visualización de vídeo en contenedor MPEG-TS (MPEG2 o H.264) con metadatos KLV incrustados de orientación y posición de plataforma (cadencia ≥ 0,5 Hz / cada 2 s) según STANAG 4609. | |
| **RSW-08** | Retransmisión RTSP/RTP Multicast | Común (Lote 1 y 2) | **Opcional** | Reenvío de flujos de vídeo en red local en tiempo real mediante protocolos RTSP/RTP multicast hacia aplicaciones o monitores externos. | |
| **RPVyA-01** | Cobertura Matricial de Ensayos | Común (Lote 1 y 2) | **Obligatorio** | Pruebas de V&V articuladas considerando todos los modos operativos (teleoperado, autónomo, offline), modos de detección (normal, sigiloso) y estados de enlace (normal, degradado). | |
| **RPVyA-02** | Cesión de Licencias para Ensayos | Común (Lote 1 y 2) | **Obligatorio** | Disponibilidad de licencias software necesarias a favor de CDTI y MINISDEF/DIGEID para la supervisión y ejecución de las pruebas. | |
| **RPVyA-03** | Rotulación con Emblemas | Común (Lote 1 y 2) | **Obligatorio** | Rotulación en cada subsistema de dos adhesivos o imanes con los emblemas de CDTI y MINISDEF/DIGEID en ambos laterales (tamaño mínimo UNE A3: 297x420 mm o máximo geométrico). | |
| **RPVyA-04** | Pruebas de Verificación (Fase II) | Común (Lote 1 y 2) | **Obligatorio** | Batería obligatoria de pruebas en fábrica al cierre de Fase II:<br>a) Pruebas Unitarias.<br>b) Pruebas de Interfaz.<br>c) Pruebas de Sistema en fábrica.<br>d) Pruebas iniciales de Misión en fábrica. | |
| **RPVyA-05** | Supervisión de Verificación | Común (Lote 1 y 2) | **Obligatorio** | Supervisión y dirección de las pruebas de verificación por parte del Equipo Responsable del Contrato (ERC) conforme al Plan de Pruebas. | |
| **RPVyA-06** | Instalaciones de Verificación | Común (Lote 1 y 2) | **Obligatorio** | Ejecución de las pruebas de verificación en las instalaciones y talleres del contratista. | |
| **RPVyA-07** | Pruebas de Validación (Fase III) | Común (Lote 1 y 2) | **Obligatorio** | Campaña de validación preoperacional ejecutada por Unidades Operativas (Ejército de Tierra y UME) en la península ibérica (Castilla-La Mancha para Lote 1; Castilla y León para Lote 2). | |
| **RPVyA-08** | Cursos de Formación a Dotaciones | Común (Lote 1 y 2) | **Obligatorio** | Apoyo del contratista durante las pruebas de validación impartiendo cursos de formación teórica y práctica a los operadores militares asignados. | |
| **RPVyA-09** | Campaña de Validación Semanal | Común (Lote 1 y 2) | **Obligatorio** | Organización de ensayos en ventanas semanales (mínimo dos semanas no consecutivas), integrando transporte, despliegue, formación, ejecución y recogida. | |
| **RDOC-01** | Formato Dual PDF y Editable | Común (Lote 1 y 2) | **Obligatorio** | Entregables documentales en formato PDF y formatos editables originales (Word con control de cambios), facilitando herramientas y licencias de visualización hasta el fin de la garantía. | Propuesta de Solución / Ideas del Equipo |
| **RDOC-02** | Convención de Nomenclatura | Común (Lote 1 y 2) | **Obligatorio** | Regla de nombrado uniforme: Código de entregable + versión incremental (ej. `E01_7 Plan de Gestión de Proyecto.pdf`). | |
| **RDOC-03** | Entregas Parciales en Soporte USB | Común (Lote 1 y 2) | **Obligatorio** | Entrega de copia electrónica completa en memoria USB o equivalente en cada hito parcial contractual con los visores necesarios. | |
| **RDOC-04** | Entrega Digital Final | Común (Lote 1 y 2) | **Obligatorio** | Entrega consolidada en soporte USB al cierre del contrato con la totalidad de los documentos emitidos en su versión final actualizada (PDF y fuente). | |
| **RDOC-05** | Plan de Gestión del Proyecto | Común (Lote 1 y 2) | **Obligatorio** | Presentación a los 15 días tras firma de contrato: objeto de los trabajos, WBS estructurada con I/O de paquetes y tareas, organigrama y roles, cronograma Gantt apaisado (≥ 3 niveles), referencias a planes de calidad/riesgos/configuración y curva de esfuerzo. | |
| **RDOC-06** | Mantenimiento Vivo del Plan | Común (Lote 1 y 2) | **Obligatorio** | Actualización obligatoria del Plan de Gestión del Proyecto ante cualquier variación en su contenido o programación. | |
| **RDOC-07** | Plan de Gestión de Configuración | Común (Lote 1 y 2) | **Obligatorio** | Procedimientos y reglas de identificación de configuración física y documental, con tabla anexa viva de Línea Base de la Configuración y versiones. | |
| **RDOC-08** | Plan de Gestión de Riesgos | Común (Lote 1 y 2) | **Obligatorio** | Procedimiento de análisis, identificación inicial de riesgos, categorización de impacto y probabilidad (alta/media/baja), y matriz de riesgos inicial y evolutiva. | |
| **RDOC-09** | Plan de Pruebas | Común (Lote 1 y 2) | **Obligatorio** | Contenido mínimo del plan: catálogo de pruebas Fases II y III, matriz de trazabilidad requisitos-pruebas, inventario de medios (HW, SW, datasets, herramientas), perfiles de personal, calendario de semanas no consecutivas, permisos/seguros y riesgos. | |
| **RDOC-10** | Protocolo de Pruebas | Común (Lote 1 y 2) | **Obligatorio** | Ficha por prueba: caracterización de escenario, responsable nominal/rol, pasos de ejecución, criterios cuantitativos de aceptación e indicador de prueba bloqueante. | |
| **RDOC-11** | Resultados de Pruebas | Común (Lote 1 y 2) | **Obligatorio** | Registro cronológico de ejecución, dictamen final y análisis causa-raíz y solución adoptada en pruebas repetidas. | |
| **RDOC-12** | Informe de Pruebas Incremental | Común (Lote 1 y 2) | **Obligatorio** | Documento único e incremental que agrupa y consolida todos los resultados de ensayos a lo largo de las distintas fases. | |
| **RDOC-13** | Arquitectura General en SysML | Común (Lote 1 y 2) | **Obligatorio** | Modelado formal en SysML: Vista General (propósito, capacidades, límites, restricciones), Vista Operacional (modos, ConOps), y Vista de Sistemas/Subsistemas (interfaces, diagramas de despliegue físico y SW, puntos de interfaz). | |
| **RDOC-14** | Diseño Hardware Jerárquico | Común (Lote 1 y 2) | **Obligatorio** | Descomposición estructurada en diagramas jerárquicos (sistema, subsistemas, unidades, módulos, bloques) con designadores de referencia estandarizados (1-2 letras + número identificador). | |
| **RDOC-15** | Estructura del Diseño Hardware | Común (Lote 1 y 2) | **Obligatorio** | Estructura formal del documento HW: especificaciones generales (suministros, rangos operativos), teoría de funcionamiento, descripción física/funcional, conexiones internas/externas, y planos (generales, eléctricos, mecánicos). | |
| **RDOC-16** | Ficha de Hardware Programable | Común (Lote 1 y 2) | **Obligatorio** | Registro de PLCs, IPCs, FPGAs, microprocesadores/controladores: IDE y versión, marca/modelo, versión de firmware, descripción funcional y código cargado. | |
| **RDOC-17** | Diseño Software en SysML / UML | Común (Lote 1 y 2) | **Obligatorio** | Modelado formal del software: diagrama de despliegue general, interfaces lógicas y físicas, diagramas de componentes, diagramas de casos de uso con secuencias y estados, dinámica de interfaces de usuario GUI (pantallas y eventos), y herramientas/dependencias de desarrollo. | |
| **RDOC-18** | Estrategia de Propiedad Intelectual | Común (Lote 1 y 2) | **Obligatorio** | Inventario de derechos preexistentes empleados (Anexo IV), modelo de protección de nuevos activos (patentes/modelos o justificación técnica motivada de no protección) y registro de derechos de autor de software con código fuente y manuales. | |

---

## 2. Catálogo Desglosado de Cargas de Pago e Implementos (CP-01 a CP-25)

Relación sistemática de las 25 cargas de pago e implementos modulares especificados en el pliego para los dos lotes:

| Código | Carga de Pago / Implemento | Lote | Interfaz / Ubicación | Carácter | Especificaciones Técnicas Clave | Propuesta de Solución / Ideas del Equipo |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **CP-01** | Hoja quitanieves | Lote 1 (Ruedas) | Zona Frontal (Interfaz 1) | **Obligatoria** | Anchura ≥ 2.250 mm; orientación hidráulica bilateral (izquierda/derecha); acero de dureza Brinell ≥ 450. | |
| **CP-02** | Fresadora de nieve | Lote 1 (Ruedas) | Zona Frontal (Interfaz 1) | **Opcional** (ILT1-01) | Anchura de trabajo ≥ 2.000 mm; altura de nieve ≥ 1.000 mm; chimenea de impulsión orientable con alcance ≥ 25 m. | |
| **CP-03** | Rodillo antiminas | Lote 1 (Ruedas) | Zona Frontal (Interfaz 1) | **Opcional** (ILT1-02) | Anchura de barrido ≥ 2,2 m (> ancho UGV); velocidad de avance > 5 km/h; presión mínima ≥ 300 kg por rueda antipinchazos; contacto permanente asegurado. | |
| **CP-04** | Estación de armas remota (RWS) | Lote 1 (Ruedas) | Zona Superior (Interfaz 2) | **Obligatoria** | Estación de armas remota nacional para misiones de autodefensa y mantenimiento de la paz. | |
| **CP-05** | Mástil optrónico ISTAR | Lote 1 (Ruedas) | Zona Superior (Interfaz 2) | **Opcional** (ILT1-04) | Mástil telescópico retráctil con módulo optrónico EO/IR estabilizado para inteligencia, vigilancia y reconocimiento. | |
| **CP-06** | Brazo robótico articulado NRBQ/EOD | Lote 1 (Ruedas) | Zona Superior (Interfaz 2) | **Opcional** (ILT1-03) | Manipulación y toma de muestras NRBQ y desactivación de explosivos; equipado con cámaras integradas de teleoperación. | |
| **CP-07** | Módulo logístico de transporte | Lote 1 (Ruedas) | Zona Superior (Interfaz 3 Bahía) | **Opcional** (ILT1-06) | Alojamiento y transporte seguro de pertrechos, material y víveres de apoyo a unidades de combatientes. | |
| **CP-08** | Células medicalizadas / camillas MEDEVAC | Lote 1 (Ruedas) | Zona Superior (Interfaz 3 Bahía) | **Opcional** (ILT1-05) | Evacuación de heridos y bajas desde primera línea hasta retaguardia mediante camillas o módulos medicalizados. | |
| **CP-09** | Plataforma de recarga dual de UAV | Lote 1 (Ruedas) | Zona Superior (Interfaz 3 Bahía) | **Obligatoria** | Recarga y apontaje simultáneo para dos aeronaves no tripuladas (el UAV de Apoyo orgánico + 1 UAV externo). | |
| **CP-10** | Módulo nodriza de recarga para UGV ligeros | Lote 1 (Ruedas) | Zona Superior (Interfaz 3 Bahía) | **Obligatoria** | Al menos 2 estaciones de recarga inalámbrica por inducción para UGVs ligeros; diseño con rampa de acceso autónomo de entrada/salida. | |
| **CP-11** | Contenedor de manguera explosiva antiminas | Lote 1 (Ruedas) | Zona Superior (Interfaz 3 Bahía) | **Opcional** (ILT1-07) | Contenedor o réplica fiel para transporte y despliegue de manguera explosiva de apertura de brechas. | |
| **CP-12** | Tolva dispensadora de sal | Lote 1 (Ruedas) | Zona Superior (Interfaz 3 Bahía) | **Opcional** (ILT1-08) | Capacidad de tolva ≥ 1,2 m³; anchura de proyección modulable entre 2 y 6 m; salida dispensadora ubicada en la popa. | |
| **CP-13** | Contenedor compartimentado NRBQ | Lote 1 (Ruedas) | Zona Superior (Interfaz 3 Bahía) | **Opcional** | Almacenamiento segregado de muestras líquidas y sólidas químicas/biológicas + contenedor con blindaje de radiación. | |
| **CP-14** | Sistema de enganche de remolque | Lote 1 (Ruedas) | Zona Trasera (Interfaz 4) | **Obligatoria** | Mecanismo de tiro y enganche para arrastre de remolques de masa hasta 3.000 kg. | |
| **CP-15** | Hoja empujadora "dozer" | Lote 2 (Cadenas) | Zona Frontal (Interfaz 1) | **Obligatoria** | Anchura ≥ 3.000 mm; altura ≥ 1.200 mm; elevación, ángulo e inclinación hidráulica; profundidad excavación ≥ 450 mm; plegable o regulable en anchura. | |
| **CP-16** | Rodillo antiminas | Lote 2 (Cadenas) | Zona Frontal (Interfaz 1) | **Opcional** (ILT2-02) | Anchura de barrido ≥ 2,2 m (> ancho UGV); velocidad de avance > 5 km/h; presión mínima ≥ 300 kg por rueda antipinchazos. | |
| **CP-17** | Desbrozadora forestal | Lote 2 (Cadenas) | Zona Frontal (Interfaz 1) | **Opcional** (ILT2-01) | Anchura de trabajo ≥ 2 m; procesado de monte bajo y arbolado ≤ 15 cm; rendimiento > 0,4 ha/h (deseable 0,6 ha/h). | |
| **CP-18** | Cuchara cargadora | Lote 2 (Cadenas) | Zona Frontal (Interfaz 2) | **Opcional** (ILT2-03) | Anchura ≥ 2.250 mm; capacidad colmada ≥ 1 m³; accionada mediante dos brazos hidráulicos independientes. | |
| **CP-19** | Bomba impulsión agente extintor alta presión | Lote 2 (Cadenas) | Zona Superior (Interfaz 3) | **Obligatoria** | Presión > 20 bar; caudal máx. ≥ 220 L/min; monitor: giro 85° V / 360° H, cono 0-90°, caudal regulable 19-200 L/min, presión 6-9 bar, generación de espuma. | |
| **CP-20** | Módulo logístico de transporte | Lote 2 (Cadenas) | Zona Superior (Interfaz 4 Bahía) | **Opcional** (ILT2-05) | Alojamiento y transporte de víveres, pertrechos y munición pesada. | |
| **CP-21** | Contenedor de manguera explosiva antiminas | Lote 2 (Cadenas) | Zona Superior (Interfaz 4 Bahía) | **Opcional** (ILT2-06) | Contenedor o réplica fiel para transporte y despliegue de manguera explosiva en campos minados. | |
| **CP-22** | Depósito de agua contra incendios | Lote 2 (Cadenas) | Zona Superior (Interfaz 4 Bahía) | **Obligatoria** | Capacidad ≥ 2.750 L; conexiones con bomba CP-19; tomas Barcelona de 25 mm (manguera de personal a pie), 45 mm y 70 mm (llenado). | |
| **CP-23** | Tolva / contenedor volquete abierto | Lote 2 (Cadenas) | Zona Superior (Interfaz 4 Bahía) | **Opcional** (ILT2-04) | Volquete abierto para transporte de tierras y escombros de excavación y desescombro. | |
| **CP-24** | Arado / ripper trasero de 3 rejones | Lote 2 (Cadenas) | Zona Trasera (Interfaz 5) | **Obligatoria** | Profundidad de penetración ≥ 28 cm; anchura de desfonde 2,5 a 3 m (> ancho UGV); escarificador de terreno rocoso y freno/contrapeso en pendiente. | |
| **CP-25** | Brazo retroexcavador con cazo | Lote 2 (Cadenas) | Zona Trasera (Interfaz 6) | **Opcional** (ILT2-07) | Cazo de anchura 500 a 700 mm; capacidad ≥ 0,20 m³; alcance horizontal ≥ 5,5 m; profundidad de excavación ≥ 4,5 m. | |

---

## 3. Relación Oficial de Entregables del Proyecto (E01 a E18)

| Código | Entregable | Hitos Contractuales de Entrega | Requisitos Vinculados | Descripción del Contenido | Propuesta de Solución / Ideas del Equipo |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **E01** | Plan de Gestión del Proyecto | Fase I (M4), Fase II HI (M16), Fase II HF (M25), Fase III (M29) | RDOC-05, RDOC-06 | Objeto, WBS con I/O de paquetes, organigrama, roles, curva de esfuerzo y diagrama de Gantt apaisado (≥ 3 niveles). | |
| **E02** | Plan de Gestión de Riesgos | Fase I (M4), Fase II HI (M16), Fase II HF (M25), Fase III (M29) | RDOC-08 | Procedimiento de análisis, tipificación de severidad/probabilidad y matriz de riesgos inicial y evolutiva. | |
| **E03** | Plan de Gestión de la Configuración | Fase I (M4), Fase II HI (M16), Fase II HF (M25), Fase III (M29) | RDOC-07 | Procedimiento de control de configuración física y documental, con tabla anexa viva de Línea Base de entregables. | |
| **E04** | Plan de Pruebas | Fase I (M4), Fase II HI (M16), Fase II HF (M25), Fase III (M29) | RDOC-09 | Catálogo de ensayos Fases II y III, matriz de trazabilidad requisitos-pruebas, recursos, perfiles y ventanas de pruebas. | |
| **E05** | Documento de Protocolo de Pruebas | Fase I (M4), Fase II HI (M16), Fase II HF (M25), Fase III (M29) | RDOC-10 | Fichas paso a paso de cada ensayo: caracterización de escenario, responsable, procedimiento, criterios de éxito e impacto bloqueante. | |
| **E06** | Documento de Resultados de Pruebas | Fase II HI (M16), Fase II HF (M25), Fase III (M29) | RDOC-11, RDOC-12 | Informe acumulativo e incremental: registro de fechas, resultados cuantitativos, causa-raíz y corrección de incidencias. | |
| **E07** | Documento General de Arquitectura del Sistema | Fase I (M4), Fase II HI (M16), Fase II HF (M25), Fase III (M29) | RDOC-13 | Modelado formal en SysML: vistas General, Operacional (ConOps, modos) y de Sistemas/Subsistemas (interfaces y despliegue). | |
| **E08** | Documento de Diseño HW | Fase I (M4), Fase II HI (M16), Fase II HF (M25), Fase III (M29) | RDOC-14, RDOC-15, RDOC-16 | Descomposición jerárquica (≥ 3 niveles), designadores de referencia, teoría de funcionamiento, esquemas y planos mecánicos/eléctricos. | |
| **E09** | Documento de Diseño SW | Fase I (M4), Fase II HI (M16), Fase II HF (M25), Fase III (M29) | RDOC-17 | Modelado UML/SysML: diagramas de despliegue, componentes, casos de uso, secuencias, estados, dinámica de GUI y dependencias. | |
| **E10** | Software | Fase II HI (M16), Fase II HF (M25), Fase III (M29) | RSW-01 a RSW-08 | Código fuente completo, binarios, librerías online/offline, scripts de compilación, datos de prueba, configuración y licencias de uso. | |
| **E11** | Plataforma y UAV de Apoyo (*) | Fase II HI (M16), Fase II HF (M25), Fase III (M29) | RGEN-xx, RLTx-xx, ROPE-04 | Demostrador físico del UGV montado y equipado, más el UAV de apoyo, cables, radios, maletas de transporte y elementos auxiliares. | |
| **E12** | Cargas de Pago (UxV, …) (*) | Fase II HI (M16), Fase II HF (M25), Fase III (M29) | RLT1-12/14, RLT2-18/20 | Conjunto de implementos y cargas de pago obligatorias y opcionales integradas en la plataforma según lote. | |
| **E13** | Puesto de Operación (*) | Fase II HI (M16), Fase II HF (M25), Fase III (M29) | RPdO-01 a RPdO-08 | Estación completa de control con hardware de computación, pantallas, radios, maletas rugerizadas y dispositivos portables. | |
| **E14** | Manual de Instalación | Fase II HI (M16), Fase II HF (M25), Fase III (M29) | RDOC-xx | Instrucciones detalladas de instalación/actualización de SW, parametrización, reseteo a fábrica y puesta en marcha del sistema. | |
| **E15** | Manual de Operación y Mantenimiento | Fase II HI (M16), Fase II HF (M25), Fase III (M29) | RDOC-xx | Guía operativa de misiones y planes de mantenimiento preventivo y correctivo de 1er escalón previos y posteriores a misión. | |
| **E16** | Documentación de Curso de Formación | Fase II HI (M16), Fase II HF (M25), Fase III (M29) | RPVyA-08 | Manuales y material pedagógico teórico-práctico para la habilitación e instrucción de los operadores militares (ET y UME). | |
| **E17** | Estrategia de Propiedad Industrial e Intelectual | Fase II HI (M16), Fase II HF (M25), Fase III (M29) | RDOC-18 | Inventario de derechos previos (Anexo IV), modelo de protección de nuevas invenciones (patentes) y registro de derechos de autor de SW. | |
| **E18** | Vídeo Resumen del Proyecto | Fase II HI (M16), Fase II HF (M25), Fase III (M29) | RDOC-xx | Material audiovisual de síntesis sobre las actividades y resultados alcanzados durante las campañas de experimentación y ensayos. | |

*Nota: (\*) Entregables materiales que deben estar operativos y disponibles físicamente durante la ejecución de las pruebas.*

---

## 4. Criterios de Evaluación y Baremo (Específico Lote 1 y Generales)

**Baremo de puntuación:**
*   **0-9:** Incumplimiento (Muy deficiente)
*   **10-49:** Cumplimiento insuficiente
*   **50-64:** Cumplimiento parcial
*   **65-74:** Cumplimiento adecuado (Grado de ejecución mínimo para puntuar entregables)
*   **75-100:** Cumplimiento excelente

### Valoración de Opcionales de Interfaz Lote 1 ($V_{Int}$)
| Código | Descripción (Lote 1) | Valoración máxima | Propuesta de Solución / Ideas del Equipo |
| :--- | :--- | :--- | :--- |
| **ILT1-01** | Posición Frontal; Interfaz 1: Fresadora | 5 | |
| **ILT1-02** | Posición Frontal; Interfaz 1: Rodillo Antiminas | 20 | |
| **ILT1-03** | Posición Superior; Interfaz 3: Brazo robótico articulado | 20 | |
| **ILT1-04** | Posición Superior; Interfaz 3: Módulo de adquisición optrónico | 20 | |
| **ILT1-05** | Posición Superior; Interfaz 4: Bajas y heridos | 3 | |
| **ILT1-06** | Posición Superior; Interfaz 4: Equipos y materiales | 3 | |
| **ILT1-07** | Posición Superior; Interfaz 4: Manguera explosiva | 3 | |
| **ILT1-08** | Posición Superior; Interfaz 4: Tolva | 3 | |
*Coeficiente = 100 / Suma de máximos (1,2987)*

### Valoración de Opcionales Generales ($V_{OGen}$) aplicables al Lote 1
*(Se excluyen los códigos OG-05 a OG-09 por ser específicos del Lote 2)*
| Código | Descripción | Valoración máxima | Propuesta de Solución / Ideas del Equipo |
| :--- | :--- | :--- | :--- |
| **OG-01** | RGEN-08: Minimizar variedad de herramientas (1er escalón) | 5 | |
| **OG-02** | RGEN-18: Movilidad híbrida enchufable | 20 | |
| **OG-03** | RGEN-19: Exportar energía (mínimo 120 kW) | 5 | |
| **OG-04** | RLT1-11: Protección balística (Lote 1) | 5 | |
| **OG-10** | RPdO-08: Interfaz inmersivo, tecnologías hápticas/AR | 5 | |
| **OG-11** | RCOM-05: Conexión fibra carrete (100 m) | 20 | |

### Valoración Conjugación de Cargas de Pago ($V_{CCdP}$) aplicables al Lote 1
*(Se excluyen CdP-01, CdP-02 y CdP-03 exclusivos de Lote 2)*
| Código | Descripción Conjugación | Valoración máxima | Propuesta de Solución / Ideas del Equipo |
| :--- | :--- | :--- | :--- |
| **CdP-04** | Maniobra terrestre (1): RWS CP-04 + Módulo nodriza CP-09 + CP-10 | 10 | |
| **CdP-05** | Maniobra terrestre (2): Mástil ISTAR CP-05 + Módulo nodriza CP-09 + CP-10 | 10 | |
| **CdP-06** | Operaciones defensa NRBQ: Brazo robótico CP-06 + Contenedor NRBQ CP-13 | 10 | |
| **CdP-07** | Tormentas invernales severas: Hoja quitanieves CP-01 + Tolva CP-12 | 10 | |
| **CdP-08** | Zapadores (Versión Lote 1): Rodillo antiminas CP-03 + Manguera explosiva CP-11 | 10 | |