Hechos = {
    "Vehiculos": {
        "vehiculo_001": {
            "Sintomas": {
                "Motor": ["no_arranca", "humo_azul"],
                "Frenos": ["pedal_esponjoso"],
                "Electrico": ["bateria_cargada"],
                "Llantas": ["aire_perfecto","sin_desgaste"]
            }
        },
        "vehiculo_002": {
            "Sintomas":{
                "Motor" : ["arranca","vapor"],
                "Frenos": ["pedal_esponjoso"],
                "Electrico": ["bateria_cargada"],
                "Llantas": ["aire_bajo","sin_desgaste"]
            }
        }
    }
}

## Hechos Escritos como preposiciones
# 1. El vehículo 001 no arranca.
# 2. El vehículo 001 tiene pedal esponjoso al frenar.
# 3. El vehículo 001 tiene la batería cargada.
# 4. El vehículo 001 tiene las llantas infladas correctamente.
# 5. El vehículo 001 no presenta desgaste en las llantas.
# 6. El vehículo 002 desprende vapor azul al arrancar.
# 7. El vehículo 002 tiene pedal esponjoso al frenar.
# 8. El vehículo 002 tiene la batería cargada.
# 9. El vehículo 002 tiene aire bajo en sus llantas.
# 10. El vehículo 002 no presenta desgaste en las llantas.

## Representación de los hechos de forma que puedan manipularse
# 1. no_arranca("vehiculo_001")
# 2. pedal_esponjoso("vehiculo_001")
# 3. bateria_cargada("vehiculo_001")
# 4. llantas_infladas("vehiculo_001")
# 5. sin_desgaste_llantas("vehiculo_001")
# 6. vapor_azul_arrancar("vehiculo_002")
# 7. pedal_esponjoso("vehiculo_002")
# 8. bateria_cargada("vehiculo_002")
# 9. aire_bajo_llantas("vehiculo_002")
# 10. sin_desgaste_llantas("vehiculo_002")

## Hechos escritos como tuplas

h1 = ("Sintoma","Motor","no_arranca","vehiculo_001") ## ASI SE TIENEN QUE VER LAS TUPLAS

h2 = ("pedal_esponjoso","vehiculo_001")

h3 = ("bateria_cargada","vehiculo_001")

h4 = ("llantas_infladas","vehiculo_001")

h5 = ("sin_desgaste_llantas","vehiculo_001")

h6 = ("vapor_azul_arrancar","vehiculo_002")

h7 = ("pedal_esponjoso","vehiculo_002")

h8 = ("bateria_cargada","vehiculo_002")

h9 = ("aire_bajo_llantas","vehiculo_002")

h10 = ("sin_desgaste_llantas","vehiculo_002")