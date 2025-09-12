#Manejos de listas con funciones map, filter y reduce
from functools import reduce
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Genera una nueva lista con los cuadrados de cada número usando map.
cuadrados = list(map(lambda x: x**2, lista))

#Filtra los números pares usando filter
pares = list(filter(lambda x: x % 2 == 0, lista))

def suma (a, b):
    #Funcion para hacer una suma con a y b
    return a + b
def prouct (a, b):
    #Funcion para hacer una multiplicacion con a y b
    return a * b

#Usa reduce para calcular:
#La suma de [1..10]
#El producto [1..5]
suma = reduce(suma, lista)
prouct = reduce(prouct, lista[0:5])

#Se imprimen los resultados en esta parte
print(cuadrados)
print(pares)
print(suma)
print(prouct)