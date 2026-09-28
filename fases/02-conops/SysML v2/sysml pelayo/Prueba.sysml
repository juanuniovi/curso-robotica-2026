package DeliveryDroneSystem {
    
    // --- 1. DATOS Y TIPOS ---
    item def TelemetriaData;
    attribute def Kilogramos :> ScalarValues::Real;

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
        // ...existing code...
        requirement reqMasa : RequisitoMasaMaxima {
            subject dron : DronEntrega;
            in attribute redefines masaMedida = masaTotal;
        }
// ...existing code...
    }

    // --- 5. REQUISITO DEL SISTEMA ---
    requirement def RequisitoMasaMaxima {
        subject dron : DronEntrega;
        in attribute masaMedida : Kilogramos;
        attribute limiteMax : Kilogramos = 10.0 as Kilogramos;
        
        require constraint { masaMedida <= limiteMax }
    }
}
