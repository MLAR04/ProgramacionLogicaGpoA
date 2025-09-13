'''
Instrucciones: Dada la lista [1,2,3,4,5,6,7,8,9,10]
- [x] Generar una nueva lista con los cuadrados de cada número usando map
- [x] Filtra los números pares usando *filter*
- [x] Usa reduce para calcular:
  - La suma de [1..10]
  - El producto de [1..5]
'''
from functools import reduce

lista = [1,2,3,4,5,6,7,8,9,10]
print(f"Lista original: {lista}")

cuadrados = list(map(lambda x: x**2, lista))
print(f"Lista de los cuadrados de los números de la lista: {cuadrados}")

pares = list(filter(lambda x: x % 2 == 0, lista))
print(f"Lista de los pares de la lista original: {pares}")

def sumar(a, b):
    return a+b

def multiplicar(a, b):
    return a*b

suma = reduce(sumar, lista)
print(f"Suma desde el 1 al 10: {suma}")

producto = reduce(multiplicar, lista[:5])
print(f"Producto desde el 1 al 5: {producto}")

# Autor: E. A. Tavares Medina
