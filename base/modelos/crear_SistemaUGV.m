function crear_SistemaUGV()
%CREAR_SISTEMAUGV  Esqueleto MUY BÁSICO del modelo de arquitectura del Sistema UGV.
%
%   Ejecuta este script en MATLAB R2023b o posterior con System Composer:
%       >> crear_SistemaUGV
%   Genera SistemaUGV.slx en la carpeta actual.
%
%   Sirve para NO empezar la Semana 2 desde una hoja en blanco.
%
%   Qué incluye (a propósito, poco):
%     - Jerarquía de bloques de primer nivel del Sistema UGV
%     - Desglose interno del bloque UGV en 5 subsistemas
%     - Diccionario con 6 interfaces VACÍAS (solo el nombre)
%     - Una descripción por bloque con cifras clave y su ID de requisito
%
%   Qué NO incluye (es el trabajo de las Semanas 2 y 3):
%     - Propiedades de valor formales (tipo + valor + unidad)  -> Semana 2
%     - Puertos, asignación de interfaces y conexiones (el IBD) -> Semana 3
%     - Trazabilidad formal con Requirements Toolbox
%
%   Referencia: Anexo I anonimizado, RDOC-13 (Vista de Sistemas y Subsistemas).

modelName = "SistemaUGV";

% -- Empezar limpio -------------------------------------------------------
if exist(modelName + ".slx", "file")
    error("Ya existe %s.slx en esta carpeta. Bórralo o cámbiate de carpeta antes de regenerar.", modelName);
end
try, close_system(modelName, 0); catch, end  %#ok<CTCH>

model = systemcomposer.createModel(modelName);
arch  = model.Architecture;

% -- Nivel 1: componentes del Sistema UGV -------------------------------
n1 = ["UGV" ...
      "PuestoMandoPortable" ...
      "DispositivoTelemandoPortable" ...
      "SubsistemaComunicaciones" ...
      "UAVApoyo"];
c1 = addComponent(arch, n1);

desc1 = [ ...
 "Vehiculo terrestre no tripulado de traccion de ruedas. " + ...
   "masa en orden de mision <= 9000 kg [RLT1-08]; " + ...
   "autonomia >= 8 h o 400 km [RGEN-14]; autonomia electrica >= 2 h o 100 km [RGEN-15]." ...
 "Puesto de Mando Portable: puesto de operacion + comunicaciones + alimentacion. " + ...
   "3 interfaces independientes (conduccion, mision, carga util) [RPdO-06]." ...
 "Dispositivo de Telemando Portable tipo tablet con joystick para teleoperacion cercana [ROPE-03]." ...
 "Subsistema de Comunicaciones: 3 modulos (5G, radio, satelite) [RCOM-01]; alcance BLOS >= 20 km [RCOM-02]." ...
 "UAV de apoyo para teleoperacion y consciencia situacional; modos TELEOPERADO y CAUTIVO VIRTUAL [ROPE-04]." ];

for k = 1:numel(c1)
    try, c1(k).Description = desc1(k); catch, end  %#ok<CTCH>
end

% -- Nivel 2: dentro del bloque UGV -----------------------------------------
ugvArch = c1(1).Architecture;
n2 = ["PropulsionEnergia" ...
      "MovilidadTrenRodaje" ...
      "PercepcionNavegacion" ...
      "ControlComputacion" ...
      "PuntosInterfazCargas"];
c2 = addComponent(ugvArch, n2);

desc2 = [ ...
 "Propulsion hibrida: motor electrico + combustion (biocombustible 100%) + baterias " + ...
   "[RGEN-11..13]. Potencia total >= 140 kW [RLT1-09]." ...
 "Tren de ruedas 4x4/6x6/8x8 con traccion independiente por rueda [RLT1-04] y " + ...
   "suspension neumatica regulable [RLT1-05]. v_carretera >= 75 km/h, pendiente frontal >= 60% [RLT1-03]." ...
 "Deteccion de obstaculos (LiDAR/radar/vision) con modo SIGILOSO [RGEN-09]; " + ...
   "navegacion alternativa al GNSS, >= 3 tecnologias, >= 5 km sin senal [RNAV-01]." ...
 "Computacion embarcada y control drive-by-wire. Frenado automatico anticolision [RGEN-17]. " + ...
   "Modos TELEOPERADO / AUTONOMO / FUERA DE LINEA [ROPE-01]." ...
 "Puntos de Interfaz mecanicos/electricos/logicos para cargas de pago obligatorias " + ...
   "(CP-01, CP-04, CP-09, CP-10, CP-14) sin comprometer la estabilidad [RGEN-28]." ];

for k = 1:numel(c2)
    try, c2(k).Description = desc2(k); catch, end  %#ok<CTCH>
end

% -- Diccionario de interfaces (VACIAS, se rellenan en la Semana 3) ------
ifNames = ["EnergiaElectrica" "ParMecanico" "SenalControl" ...
           "FlujoVideo" "DatosNavegacion" "EnlaceComunicaciones"];
for nm = ifNames
    try, addInterface(model.InterfaceDictionary, nm); catch, end  %#ok<CTCH>
end

% -- Colocar los bloques de forma legible -------------------------------
try, Simulink.BlockDiagram.arrangeSystem(modelName); catch, end          %#ok<CTCH>
try, Simulink.BlockDiagram.arrangeSystem(modelName + "/UGV"); catch, end  %#ok<CTCH>

% -- Guardar -----------------------------------------------------------
save(model);
try, close_system(modelName, 0); catch, end  %#ok<CTCH>

fprintf("OK: %s.slx creado en %s\n", modelName, pwd);
end
