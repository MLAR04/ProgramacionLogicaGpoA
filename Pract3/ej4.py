#Gabriel Lopez 22760564
# Práctica #3 - Ejercicio 4
# Dada la lista [1,2,3,4,5,6,7,8,9,10]:

from functools import reduce

numeros = [1,2,3,4,5,6,7,8,9,10]

# a) Cuadrados con map
cuadrados = list(map(lambda x: x**2, numeros))

# b) Números pares con filter
pares = list(filter(lambda x: x % 2 == 0, numeros))

# c) Suma de [1..10]
suma_total = reduce(lambda x, y: x + y, numeros)

# d) Producto de [1..5]
producto = reduce(lambda x, y: x * y, [1,2,3,4,5])

if __name__ == "__main__":
    print("Lista de cuadrados:", cuadrados)
    print("Números pares:", pares)
    print("Suma de [1..10]:", suma_total)
    print("Producto de [1..5]:", producto)
