#Base de conocimiento (Diagnostico de enfermedades)
from reglas import *
import sys

enfermo = {
    'gripe':['dolor de cabeza', 'tos'],
    'covid': ['perdida de olfato', 'cansancio', 'tos', 'fiebre'],
    'migraña': ['nauseas', 'dolor de cabeza'],
    'resfriado': ['congestion nasal', 'tos', 'fiebre']
}
sintomas_seleccionados = []

a = 'fiebre'
b = 'tos'
c = 'dolor de cabeza'
d = 'congestion nasal'
e = 'nauseas'
f = 'cansancio'
g = 'perdida de olfato'

while True:
    sintomas = input(f'¿Qué síntomas tienes?\n a. {a}\n b. {b}\n c. {c}\n d. {d}\n e. {e}\n f. {f}\n g. {g}\n x. Otros\n s. Salir\n').lower()
    if sintomas == "s":
        break
    elif sintomas == "x":
        print("Si tienes sintomas que no sean los de las opciones no te puedo ayudar")
        sys.exit()
    elif sintomas in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        opciones = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'g': g}
        sintomas_seleccionados.append(opciones[sintomas])
    else:
        print("Ingresa una opcion valida")

print("Regla 1.")
te_sientes_mal()

print("-----------------")
print("Regla 2.")
estas_enfermo(sintomas_seleccionados)

print("-----------------")
#Si la fiebre es mayor a 37.5 se agrega fiebre a sintomas seleccionados
print("Regla 3.")
fiebre_alta(sintomas_seleccionados)

print("-----------------")
print("Regla 4, 5, 6, 7.")
enfermedades = ['gripe', 'covid', 'migraña', 'resfriado']
for enfermedad in enfermedades:
    if diagnosticar_enfermedad_especifica(enfermo, sintomas_seleccionados, enfermedad):
        break
else:
    print("Tienes una enfermedad que no puedo diagnosticar")
