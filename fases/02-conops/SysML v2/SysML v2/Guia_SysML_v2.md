# Guía Completa de Inicio Rápido: SysML v2
**Lenguaje de Modelado de Sistemas (Versión 2)**

---

## 📋 Tabla de Contenidos
- [Guía Completa de Inicio Rápido: SysML v2](#guía-completa-de-inicio-rápido-sysml-v2)
  - [📋 Tabla de Contenidos](#-tabla-de-contenidos)
  - [1. Introducción y Filosofía de SysML v2](#1-introducción-y-filosofía-de-sysml-v2)
    - [🌟 ¿Por qué SysML v2?](#-por-qué-sysml-v2)
  - [2. Conceptos Fundamentales: `def` vs Ocurrencia](#2-conceptos-fundamentales-def-vs-ocurrencia)
    - [Ejemplo básico de paquetes y definiciones:](#ejemplo-básico-de-paquetes-y-definiciones)
  - [3. Estructura del Sistema (Partes, Puertos y Conexiones)](#3-estructura-del-sistema-partes-puertos-y-conexiones)
    - [3.1 Partes y Atributos (`part def`, `attribute def`)](#31-partes-y-atributos-part-def-attribute-def)
    - [3.2 Puertos e Interfaces (`port def`, `port`)](#32-puertos-e-interfaces-port-def-port)
    - [3.3 Conexiones y Flujos (`connect`, `flow`)](#33-conexiones-y-flujos-connect-flow)
  - [4. Comportamiento y Dinámica (Acciones y Estados)](#4-comportamiento-y-dinámica-acciones-y-estados)
    - [4.1 Definición de Acciones (`action def`, `action`)](#41-definición-de-acciones-action-def-action)
    - [4.2 Máquinas de Estado (`state def`, `state`)](#42-máquinas-de-estado-state-def-state)
  - [5. Gestión de Requisitos y Restricciones](#5-gestión-de-requisitos-y-restricciones)
  - [6. Caso Práctico Completo: Sistema de Dron de Entrega](#6-caso-práctico-completo-sistema-de-dron-de-entrega)
  - [7. Entorno de Trabajo y Herramientas](#7-entorno-de-trabajo-y-herramientas)
  - [8. Hoja de Referencia Rápida (Cheatsheet)](#8-hoja-de-referencia-rápida-cheatsheet)

---

## 1. Introducción y Filosofía de SysML v2

SysML v2 (Systems Modeling Language v2) es el estándar internacional desarrollado por el **OMG (Object Management Group)** para la **Ingeniería de Sistemas Basada en Modelos (MBSE)**.

### 🌟 ¿Por qué SysML v2?
- **Modelo como Código (*Model-as-Code*):** Introduce una sintaxis textual nativa que permite usar control de versiones (Git), integrarse en pipelines CI/CD y realizar revisiones de código (*pull requests*).
- **Metamodelo Formal (KerML):** Ya no depende de UML como perfil rígido. Posee su propia semántica matemática sólida.
- **Interoperabilidad Vía API REST/OSLC:** Permite la conexión directa con herramientas de CAD, simulación (MATLAB/Simulink), gestión de requisitos (DOORS) y PLM.

---

## 2. Conceptos Fundamentales: `def` vs Ocurrencia

Uno de los pilares de la sintaxis de SysML v2 es la distinción clara entre la **definición** (tipo/plantilla) y la **ocurrencia** (uso/instancia).

| Concepto | Sintaxis en SysML v2 | Descripción |
| :--- | :--- | :--- |
| **Definición** | `... def Nombre { ... }` | Declara un tipo reutilizable (ej. un modelo de motor). |
| **Ocurrencia** | `... nombre : NombreDef;` | Instancia de ese tipo en un contexto específico. |

### Ejemplo básico de paquetes y definiciones:
```sysml
package ConceptosBasicos {
    
    // Definición de un tipo de atributo
    attribute def Masa;

    // Definición de una parte reutilizable
    part def Bateria {
        attribute capacidadTotal : ScalarValues::Real;
    }

    // Sistema que utiliza la batería
    part def Sistema {
        // Ocurrencia: la batería 'bateriaPrincipal' es de tipo 'Bateria'
        part bateriaPrincipal : Bateria;
    }
}
```

---

## 3. Estructura del Sistema (Partes, Puertos y Conexiones)

La estructura define los componentes físicos o lógicos, sus atributos y cómo se interconectan.

### 3.1 Partes y Atributos (`part def`, `attribute def`)
```sysml
package EstructuraComponentes {
    
    attribute def Voltaje;

    part def Sensores {
        attribute numUnidades : ScalarValues::Integer;
    }

    part def SistemaControl {
        attribute voltajeOperacion : Voltaje;
        part sensorObstaculos : Sensores;
    }
}
```

### 3.2 Puertos e Interfaces (`port def`, `port`)
Los puertos definen los puntos de interacción (intercambio de energía, datos o material).

```sysml
package InterfacesYPuertos {
    
    // Definición del tipo de datos/item que fluye
    item def ComandoVuelo;

    // Definición de puertos
    port def PuertoDatosOut {
        out item comando : ComandoVuelo;
    }

    port def PuertoDatosIn {
        in item comando : ComandoVuelo;
    }

    // Uso de puertos en componentes
    part def Controlador {
        port salidaComando : PuertoDatosOut;
    }

    part def Esc {
        port entradaComando : PuertoDatosIn;
    }
}
```

### 3.3 Conexiones y Flujos (`connect`, `flow`)
```sysml
package ConexionesSistema {
    private import InterfacesYPuertos::*;

    part def SubcuerpoDron {
        part ctrl : Controlador;
        part motorEsc : Esc;

        // Conexión entre puertos de subsistemas
        connect ctrl.salidaComando to motorEsc.entradaComando;
    }
}
```

---

## 4. Comportamiento y Dinámica (Acciones y Estados)

SysML v2 permite modelar tanto procesos ordenados (**Acciones**) como comportamiento guiado por eventos (**Estados**).

### 4.1 Definición de Acciones (`action def`, `action`)
```sysml
package ComportamientoAcciones {

    action def Despegar {
        in attribute altitudObjetivo : ScalarValues::Real;
        out attribute alcanzado : ScalarValues::Boolean;
    }

    action def MisionVuelo {
        action paso1 : Despegar;
        action paso2;

        // Secuencia de ejecución
        first paso1 then paso2;
    }
}
```

### 4.2 Máquinas de Estado (`state def`, `state`)
```sysml
package ComportamientoEstados {

    state def EstadosDron {
        entry action prepararSistemas;

        state EnTierra;
        state EnVuelo;
        state Aterrizando;

        transition EnTierra to EnVuelo accept ordenDespegue;
        transition EnVuelo to Aterrizando accept bateriaBaja;
        transition Aterrizando to EnTierra accept toqueSuelo;
    }
}
```

---

## 5. Gestión de Requisitos y Restricciones

Los requisitos en SysML v2 se expresan con condiciones verificables formalmente mediante expresiones lógicas y de cálculo.

```sysml
package RequisitosYRestricciones {

    attribute def PesoKilos;

    requirement def RequisitoMasaMaxima {
        doc /* La masa total del dron no debe exceder los 5.0 kg */
        
        in attribute masaMedida : PesoKilos;
        attribute limiteMasa : PesoKilos = 5.0;

        // Condición lógica de verificación
        require masaMedida <= limiteMasa;
    }

    constraint def ValidacionPotencia {
        in attribute voltaje : ScalarValues::Real;
        in attribute corriente : ScalarValues::Real;
        in attribute potenciaMax : ScalarValues::Real;

        voltaje * corriente <= potenciaMax
    }
}
```

---

## 6. Caso Práctico Completo: Sistema de Dron de Entrega

A continuación se muestra un modelo completo que integra **Estructura, Puertos, Requisitos y Conexiones**:

```sysml
package DeliveryDroneSystem {
    
    // --- 1. DATOS Y TIPOS ---
    item def TelemetriaData;
    attribute def Kilogramos;

    // --- 2. PUERTOS ---
    port def TelemetryPort {
        out item data : TelemetriaData;
    }

    port def PowerPort {
        inout attribute voltaje : ScalarValues::Real;
    }

    // --- 3. COMPONENTES DEL DRON ---
    part def BateriaPacks {
        port pwrOut : PowerPort;
        attribute capacidadAh : ScalarValues::Real;
        attribute masa : Kilogramos;
    }

    part def UnidadGPS {
        port telemOut : TelemetryPort;
        attribute masa : Kilogramos;
    }

    part def ComputadoraVuelo {
        port telemIn : TelemetryPort;
        port pwrIn : PowerPort;
        attribute masa : Kilogramos;
    }

    // --- 4. ENSAMBLE DEL DRON (SISTEMA PRINCIPAL) ---
    part def DronEntrega {
        // Atributos del sistema
        attribute masaTotal : Kilogramos;

        // Subsistemas
        part bateria : BateriaPacks;
        part gps : UnidadGPS;
        part flightComputer : ComputadoraVuelo;

        // Conexiones internas
        connect gps.telemOut to flightComputer.telemIn;
        connect bateria.pwrOut to flightComputer.pwrIn;

        // Requisito integrado en el sistema
        requirement reqMasa : RequisitoMasaMaxima {
            attribute redefines masaMedida = masaTotal;
        }
    }

    // --- 5. REQUISITO DEL SISTEMA ---
    requirement def RequisitoMasaMaxima {
        in attribute masaMedida : Kilogramos;
        attribute limiteMax : Kilogramos = 10.0;
        
        require masaMedida <= limiteMax;
    }
}
```

---

## 7. Entorno de Trabajo y Herramientas

Para escribir y visualizar modelos SysML v2 hoy en día, puedes utilizar las siguientes herramientas:

1. **VS Code + SysML v2 Extension:**
   - Instala la extensión oficial de **SysML v2** en Visual Studio Code para resaltado de sintaxis, autocompletado y validación.
2. **Implementación de Referencia OMG (Pilot Implementation):**
   - Repositorio oficial en GitHub: [Systems-Modeling/SysML-v2-Release](https://github.com/Systems-Modeling/SysML-v2-Release)
   - Incluye entorno en Jupyter Notebook, servidor API REST y plugins para Eclipse.
3. **Plantilla de proyecto recomendable en Git:**
   - `models/`: Archivos `.sysml` del proyecto.
   - `docs/`: Documentación generada.
   - `.gitignore`: Ignorar archivos temporales del entorno.

---

## 8. Hoja de Referencia Rápida (Cheatsheet)

| Elemento SysML v2 | Palabra Clave | Ejemplo de Sintaxis |
| :--- | :--- | :--- |
| **Paquete** | `package` | `package MiSistema { ... }` |
| **Definición de Parte** | `part def` | `part def Motor { ... }` |
| **Instancia de Parte** | `part` | `part motorIzquierdo : Motor;` |
| **Definición de Atributo** | `attribute def` | `attribute def Temperatura;` |
| **Instancia de Atributo** | `attribute` | `attribute tempActual : Temperatura;` |
| **Puerto** | `port def` / `port` | `port def P1;` / `port p : P1;` |
| **Acción / Proceso** | `action def` / `action` | `action def MedirSensor;` |
| **Estado** | `state def` / `state` | `state def EstadoSistema;` |
| **Requisito** | `requirement def` | `requirement def ReqVelocidad;` |
| **Conexión** | `connect ... to ...` | `connect p1 to p2;` |
| **Comentario / Doc** | `doc /* ... */` | `doc /* Descripción del bloque */` |
