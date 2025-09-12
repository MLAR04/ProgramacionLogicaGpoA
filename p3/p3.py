import math
from functools import reduce

## Escribe una función suma(a,b) que solo dependa de sus parámetros.

def suma(a,b):
    return a + b

## Implementa una función recursiva factorial(n) que calcule el factorial.

def factorial(n):
    return math.factorial(n)

## Escribe una función recursiva que calcule el n-ésimo número de Fibonacci.

def fibonacci(n):

    if n <= 1:

        return n
    
    return fibonacci(n - 1) + fibonacci(n - 2)


##  Dada la lista [1,2,3,4,5,6,7,8,9,10]:
##  Genera una nueva lista con los cuadrados de cada número usando map.
##  Filtra los números pares usando filter
##  Usa reduce para calcular:
##  La suma de [1..10]
##  El producto [1..5]

def operaciones():

    nums = [1,2,3,4,5,6,7,8,9,10]

    cuadrados = list(map(lambda x: x ** 2, nums))

    pares = list(filter(lambda x: x % 2 == 0, nums))

    suma = reduce(lambda x, y: x + y, nums)

    producto = reduce(lambda x, y: x * y, range(1,6))

    print('Lista original:', nums)

    print('Cuadrados:', cuadrados)

    print('Pares:', pares)

    print('Suma[1..10]:', suma)

    print('Producto[1..5]:', producto)


if __name__ == '__main__':

    print(suma(2,2))

    print(factorial(5))

    for i in range(10):
        print(fibonacci(i), end=" ")

    operaciones()
    
        



    


