#Funciones utilizadas para nuestra base de conocimiento
import sys
def te_sientes_mal():
    "Si te sientes mal --> estas enfermo"
    while True:
        x = input("Te sientes mal? Si/No \n").lower()
        if x == 'si':
            print("Estas enfermo")
            break
        elif x == 'no':
            print("Que haces aqui no estas enfremo")
            break
        else:
            print("Ingresa un valor valido Si/No")


def estas_enfermo(x):
    "Si estas enfermo --> tienes sintomas"
    if x == []:
        print("No estas enfermo")
    else:
        print("Estas enfermo")

def fiebre_alta(x):
    "Si tienes temperatura alta --> tienes fiebre"
    temperatura = int(input("Cual es tu temperatura?"))
    if temperatura > 37.5:
        if 'fiebre' in x:
            print("Tienes fiebre alta")
        else:
            x.append('fiebre')
    else:
        print("No tienes fiebre")

def diagnosticar_enfermedad_especifica(enfermo, sintomas_usuario, nombre):
    "Si tienes x sintomas --> tienes enfermedad y"
    if nombre in enfermo:
        sintomas = enfermo[nombre]
        if set(sintomas) == set(sintomas_usuario):
            print(f'Tienes: {nombre}')
            return True
        elif sintomas_usuario == []:
            print("No tienes ningún síntoma chic@")
            sys.exit()
    return False
    


