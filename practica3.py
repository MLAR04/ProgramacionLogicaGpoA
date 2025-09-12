#importaciones
from functools import reduce

#Escribe una funcion suma(a,b) que solo dependa de sus parametros
def suma(a, b):
    return a + b

#implementa una funcion recursiva factorial(n) que calcule el factorial de un numero n
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Escribe una funcion recursiva que calcule el n-esimo numero de la serie de Fibonacci
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Dada la lista [1,2,3,4,5,6,7,8,9,10], genera una nueva lista con los cuadrados de cada numero usando map, filtra los numeros pares usando filter y usa reduce para calcular: la suma de [1...10] y el producto de [1...5]
# Lista base
numeros = [1,2,3,4,5,6,7,8,9,10]

# map para obtener los cuadrados
cuadrados = list(map(lambda x: x**2, numeros))
print("Cuadrados:", cuadrados)

#usar filter para quedarnos con los pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Números pares:", pares)

#3 usar reduce para la suma de [1...10]
suma_total = reduce(lambda x, y: x + y, numeros)
print("Suma de [1...10]:", suma_total)

#4 usar reduce para el producto de [1...5]
producto = reduce(lambda a, b: a * b, numeros[:5])
print("Producto de 1 a 5:", producto)

if __name__ == "__main__":

    print ("-------------------------------------")
    print ("Resultados de las funciones 1, 2 y 3:")
    print(suma(3, 5))  # Ejemplo de uso
    print(factorial(5))  # Ejemplo de uso
    print(fibonacci(10))  # Ejemplo de uso