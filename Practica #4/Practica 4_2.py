# Practica 4_2 - Funciones y Tablas de Verdad - Jesus Martinez Carmona 22760568


def puede_votar(edad: int, tiene_credencial: bool, en_lista_nominal: bool) -> bool:
    return (edad > 18) and tiene_credencial and en_lista_nominal

def tabla_verdad_votar():
    combos = [(a,c,l) for a in [False, True] for c in [False, True] for l in [False, True]]
    print("A(edad>18)\tC(cred)\tL(lista)\tV(puede_votar)")
    for a, c, l in combos:
        v = a and c and l
        print(f"{a}\t\t{c}\t{l}\t\t{v}")

print(puede_votar(19, True, True))  
print(puede_votar(18, True, True))   
tabla_verdad_votar()
