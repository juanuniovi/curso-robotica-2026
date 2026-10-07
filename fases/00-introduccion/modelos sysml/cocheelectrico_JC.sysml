package Model {
	private import ScalarValues::*;
	requirement def RequisitoMasaMaxima {
		doc /* La masa total del vehículo no debe exceder los 1200 kg */
		attribute masaLimite : Real = 1200.0;
	}
	constraint def RestriccionMasa {
		in masaReal : Real;
		in masaMaxima : Real;
	}
	port def PuertoPotenciaElectrica {
		out attribute voltaje : Real;
		out attribute corriente : Real;
	}
	port def PuertoTraccionMecanica {
		out attribute parMotor : Real;
		out attribute rpm : Real;
	}
	part def Bateria {
		attribute capacidadKWh : Real = 44.0;
		attribute pesoKg : Real = 2500.0;
		port salidaElectrica : ~PuertoPotenciaElectrica;
	}
	part def MotorElectrico {
		attribute potenciaMaxKW : Real = 80.0;
		attribute pesoKg : Real = 60.0;
		port entradaElectrica : PuertoPotenciaElectrica;
		port salidaTraccion : PuertoTraccionMecanica;
	}
	part def Rueda {
		attribute radioMetros : Real = 0.3;
		attribute pesoKg : Real = 20.0;
		port entradaTraccion : ~PuertoTraccionMecanica;
	}
	part def Chasis {
		attribute pesoKg : Real = 500.0;
	}
	part def Vehiculo {
		attribute masaTotalCalculada : Real = bateria.pesoKg + motor.pesoKg + chasis.pesoKg + 80.0;
		part bateria : Bateria;
		part motor : MotorElectrico;
		part ruedasDelanteras : Rueda [2];
		part ruedasTraseras : Rueda [2];
		part chasis : Chasis;
		connect bateria.salidaElectrica to motor.entradaElectrica;
		connect motor.salidaTraccion to ruedasTraseras.entradaTraccion;
		perform action conducir : ConducirVehiculo;
		assert constraint verificacionMasa : RestriccionMasa {
			in masaReal = masaTotalCalculada;
			in masaMaxima = 1200.0;
		}
		exhibit state estados : ModosDeOperacion;
	}
	requirement reqMasa : RequisitoMasaMaxima;
	part miCocheReal : Vehiculo {
		ref view view1 : StandardViewDefinitions::GeneralView {
			expose Model::miCocheReal;
		}
	}
	assert satisfy reqMasa by miCocheReal;
	action def ConducirVehiculo {
		first start then encenderSistema;
		action encenderSistema;
		then acelerar;
		action acelerar;
		then frenar;
		action frenar;
		then apagarSistema;
		action apagarSistema;
		then done;
	}
	state def ModosDeOperacion {
		entry ;
		transition then Apagado;
		state Apagado;
		state Listo;
		state EnMarcha;
		state Frenando;
		transition encender first Apagado then Listo;
		transition pisarAcelerador first Listo then EnMarcha;
		transition pisarFreno first EnMarcha then Frenando;
		transition soltarFreno first Frenando then EnMarcha;
		transition apagar first Listo then Apagado;
		view ModosDeOperacionView;
	}
	view view1 : StandardViewDefinitions::GeneralView {
		expose Model;
	}
	view view2 : StandardViewDefinitions::GeneralView;
}