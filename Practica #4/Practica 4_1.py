# Practica 4_1 - Funciones y Tablas de Verdad - Jesus Martinez Carmona 22760568

def es_multiplo_de_6(n: int) -> bool:
    return (n % 2 == 0) and (n % 3 == 0)

def tabla_verdad_multiplo6():
    combos = [(d2, d3) for d2 in [False, True] for d3 in [False, True]]
    print("D2\tD3\tMultiplo6")
    for d2, d3 in combos:

        m = d2 and d3
        print(f"{d2}\t{d3}\t{m}")


print(es_multiplo_de_6(18))
print(es_multiplo_de_6(10))
tabla_verdad_multiplo6()
