'''
Instrucciones: Una persona puede votar si tiene más de 18 años, tiene credencial para votar y está en la lista nominal
'''

def voto(e, c, l):
    if e and c and l:
        print("\nEs apto para vota.")
    else:
        print("\nNo es apto para vota.")

if __name__ == "__main__":
    edad = int(input("¿Tiene más de 18 años? (1 para sí, 0 para no): "))
    carnet = int(input("¿Tiene una creencia para votar? (1 para sí, 0 para no): "))
    lista_nominal = int(input("¿Está en la lista nominal? (1 para sí, 0 para no): "))

    voto(edad,carnet,lista_nominal)
