# Practica 4_3 - Funciones y Tablas de Verdad - Jesus Martinez Carmona 22760568


def puede_conectarse(wifi_activado: bool, ethernet_conectado: bool, modem_funciona: bool) -> bool:
    return (wifi_activado or ethernet_conectado) and modem_funciona

def tabla_verdad_conexion():
    combos = [(w,e,m) for w in [False, True] for e in [False, True] for m in [False, True]]
    print("W(wifi)\tE(eth)\tM(modem)\tI(conecta)")
    for w,e,m in combos:
        i = (w or e) and m
        print(f"{w}\t{e}\t{m}\t\t{i}")

print(puede_conectarse(True, False, True))  
print(puede_conectarse(False, True, False))  
tabla_verdad_conexion()
