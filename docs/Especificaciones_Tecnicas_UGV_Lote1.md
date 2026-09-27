# Hoja de Especificaciones Técnicas Básicas Requeridas — Sistema UGV (Lote 1 - Ruedas)

**Proyecto:** Sistema Terrestre No Tripulado Heavy UGV (CPP 01/2026 AB)  
**Organismos Licitadores:** Centro para el Desarrollo Tecnológico y la Innovación (CDTI) y Ministerio de Defensa de España (MINISDEF/DIGEID)  
**Configuración Seleccionada:** Lote 1 — Plataforma de Ruedas 8×8 (Direct Drive)  
**Trazabilidad:** Pliego de Prescripciones Técnicas (Anexo I)

---

## 1. Resumen Ejecutivo de Especificaciones Clave

| Parámetro Técnico | Valor Requerido / Especificación | Requisito Pliego |
| :--- | :--- | :--- |
| **Tipo de Vehículo** | Robot UGV pesado todoterreno dual (civil-militar) sin habitáculo | `RGEN-01`, `RGEN-04` |
| **Tren de Rodaje** | 8×8 Tracción directa e independiente por rueda (Direct Drive) | `RLT1-01`, `RLT1-02`, `RLT1-04` |
| **Tara / Masa en Vacío** | 3.500 kg – 7.000 kg (nominal diseño: 4.800 kg) | `RLT1-06` |
| **Capacidad Carga Útil (Payload)** | ≥ 2.000 kg (diseño: 2.500 kg sobre barcaza e interfaces) | `RLT1-07` |
| **Peso Máximo de Misión (GVW)** | ≤ 9.000 kg (máximo orden de combate: 7.300 kg) | `RLT1-08` |
| **Capacidad de Tiro / Remolque** | Arrastre de remolque de masa ≥ 3.000 kg (STANAG 4101) | `RGEN-10`, `RLT1-14` |
| **Velocidad Máxima Carretera** | ≥ 75 km/h en firme asfaltado/consolidado | `RLT1-03.a` |
| **Velocidad Máx. Campo a Través** | ≥ 50 km/h en terreno no preparado (off-road) | `RLT1-03.b` |
| **Dimensiones Envolventes Estiba** | ≤ 2,50 m (Ancho) × 2,20 m (Alto) × 5,20 m (Largo) | `RGEN-24`, `RGEN-25` |
| **Potencia de Propulsión Combinada**| ≥ 140 kW (190 CV) potencia continua total | `RLT1-09` |
| **Planta Motriz** | Híbrida (Motor térmico 100% biocombustible + Motor eléctrico + Baterías) | `RGEN-11`, `RGEN-18` |
| **Autonomía Global Continuada** | ≥ 8 horas continuas o ≥ 400 km de recorrido total | `RGEN-14` |
| **Autonomía 100% Eléctrica / Sigilo**| ≥ 2 horas continuas o ≥ 100 km de recorrido silencioso | `RGEN-13`, `RGEN-15` |
| **Capacidad de Vadeo** | ≥ 0,75 m (75 cm) en agua dulce o salada sin preparación | `RLT1-10` |
| **Franqueamiento de Escalón** | ≥ 30 cm vertical (deseable 40 cm) | `RLT1-03.e` |
| **Pendientes Máximas Superables** | Frontal ≥ 60% (31°) \| Lateral ≥ 30% (17°) | `RLT1-03.c/d` |

---

## 2. Desglose Detallado por Categoría Técnica

### 2.1. Dimensiones, Geometría y Estiba (`RGEN-03`, `RGEN-24`, `RGEN-25`)
* **Longitud total de barcaza (sin cargas):** ~ 5.200 mm
* **Anchura total del vehículo (sin cargas):** ≤ 2.450 mm (compatible con gálibo de transporte por carretera/góndola UNE-EN 12195).
* **Altura total del chasis (suspensión en cota nominal):** ~ 1.850 mm (regulable neumáticamente).
* **Batalla (distancia entre ejes extremos):** ~ 3.200 mm
* **Ancho de vía:** ~ 2.050 mm
* **Altura libre sobre el suelo (Clearance):** 400 mm – 550 mm (regulable mediante suspensión neumática retráctil `RLT1-05`).
* **Transportabilidad:**
  * **Transporte Aéreo:** Puntos de amarre y estiba homologados según STANAG 3400 Ed. 2010 (apartado 2.a).
  * **Transporte Terrestre:** Amarres integrados según norma UNE-EN 12195 para fijación sobre góndola o plataforma militar.

### 2.2. Pesos y Distribución de Masa (`RLT1-06`, `RLT1-07`, `RLT1-08`, `RGEN-10`)
* **Masa en Vacío (Tara):** 4.800 kg (nominal, dentro del rango estricto de 3.500 kg a 7.000 kg).
* **Capacidad de Carga Útil Neta (Payload):** 2.500 kg (superando el mínimo contractual de 2.000 kg).
* **Peso Máximo en Orden de Misión (GVW):** 7.300 kg (límite máximo legal del pliego: 9.000 kg).
* **Capacidad de Tiro / Enganche Trasero:** Arrastre pasivo/activo de remolques de hasta 3.000 kg de masa mediante gancho STANAG 4101 escamotable.

### 2.3. Cinemática, Dinámica y Movilidad Todoterreno (`RLT1-03`, `RLT1-10`, `RGEN-16`)
* **Velocidad Máxima en Carretera (asfalto/firme consolidado):** ≥ 75 km/h.
* **Velocidad Máxima Campo a Través (Off-road):** ≥ 50 km/h.
* **Capacidad de Remolcado Pasivo (ser remolcado por otro vehículo):** Hasta 65 km/h.
* **Pendiente Frontal Máxima:** 60% (superación de rampas inclinadas hasta 31°).
* **Pendiente Lateral Máxima:** 30% (estabilidad en peraltes hasta 17° con cargas útiles acopladas `RGEN-29`).
* **Franqueamiento de Escalón Vertical:** ≥ 30 cm (objetivo de diseño: 40 cm).
* **Profundidad de Vadeo sin Preparación Previa:** ≥ 0,75 m (750 mm) tanto en agua dulce como salada.

### 2.4. Propulsión, Planta Motriz y Chasis (`RLT1-04`, `RLT1-05`, `RLT1-09`, `RGEN-11`, `RGEN-12`, `RGEN-18`)
* **Configuración del Tren de Rodaje:** 8 ruedas con tracción total 8×8.
* **Accionamiento de Ruedas:** Tracción independiente en cada rueda mediante motores eléctricos síncronos de imanes permanentes (Direct Drive / In-Wheel).
* **Sistema de Suspensión:** Suspensión neumática independiente por brazo oscilante en cada rueda, retráctil y regulable en altura electrónicamente.
* **Potencia Total Continua de Propulsión:** ≥ 140 kW (190 CV) combinados.
* **Arquitectura de Propulsión Híbrida (PHEV):**
  * Motor térmico diésel acoplado a generador, 100% compatible con biocombustible.
  * Pack de baterías de Ion-Litio de alta densidad energética.
  * Sistema de recarga en marcha por motor térmico y recuperación de energía por frenada regenerativa.

### 2.5. Autonomía y Gestión Energética (`RGEN-13`, `RGEN-14`, `RGEN-15`, `RGEN-19`)
* **Autonomía Combinada Global:** ≥ 8 horas de funcionamiento operativo o ≥ 400 km de alcance continuo.
* **Autonomía Puramente Eléctrica (Modo Sigiloso):** ≥ 2 horas continuas o ≥ 100 km de recorrido con baja firma térmica y acústica.
* **Exportación de Energía Eléctrica (Opcional OG-03):** Capacidad de suministrar hasta 120 kW de potencia eléctrica externa para redes o campamentos.

### 2.6. Navegación, Percepción y Comunicaciones (`RGEN-09`, `ROPE-01..06`, `RNAV-01`, `RCOM-01..04`)
* **Modos de Operación:** TELEOPERADO, AUTÓNOMO (waypoints, follow-me, shuttle, regreso a casa) y FUERA DE LÍNEA.
* **Navegación en Entornos GNSS Denegado (`RNAV-01`):** Triangulación mediante IMU de grado táctico, odometría visual y odometría de rueda (mínimo 5 km de trayecto sin satélite).
* **Sistema de Percepción y Seguridad (`RGEN-09`):** Detección 360° de obstáculos estáticos y dinámicos con sensores LiDAR, Radar y visión electro-óptica/térmica EO/IR (modos NORMAL y SIGILOSO).
* **Alcance de Comunicaciones (`RCOM-02`):** Rango de enlace Beyond Line-of-Sight (BLOS) ≥ 20 km.
* **Subsistema de Redes (`RCOM-01`):** Módulo 5G civil/emergencias, Radio Militar táctica (TRANSEC/COMSEC) y Terminal SATCOM.

---

## 3. Puntos de Interfaz Mecánicos y Cargas Útiles Obligatorias (Lote 1)

El UGV dispone de 4 Puntos de Interfaz estandarizados (`RGEN-02`, `RGEN-28`) para el acople rápido de implementos:

| Punto de Interfaz | Ubicación | Carga Útil Obligatoria Integrada | Especificación Resumida |
| :--- | :--- | :--- | :--- |
| **Punto 1** | Frontal | **`CP-01` Hoja Quitanieves** | Ancho ≥ 2.250 mm, orientación hidráulica bilateral, acero Brinell ≥ 450 |
| **Punto 2** | Superior Frontal | **`CP-04` Estación de Armas Remota (RWS)** | Estación de empleo remoto nacional para autoprotección y patrulla |
| **Punto 3** | Superior Bahía | **`CP-09` Plataforma Recarga Dual UAV** | Apontaje y recarga simultánea para 2 UAVs (UAV apoyo + 1 externo) |
| **Punto 3** | Superior Bahía | **`CP-10` Módulo Nodriza UGV Ligeros** | Al menos 2 estaciones de recarga inductiva inalámbrica con rampa |
| **Punto 4** | Trasero | **`CP-14` Sistema de Enganche Remolque** | Gancho de tiro STANAG 4101 para arrastre de hasta 3.000 kg |
