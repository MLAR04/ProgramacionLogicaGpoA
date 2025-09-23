
# suma
def suma(a, b):
    """Devuelve la suma de dos números"""
    return a + b

print("Suma de 3 + 5:", suma(3, 5))



#funcionn recursiva factorial
def factorial(n):
    """Calcula el factorial de un número n recursivamente"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial de 5:", factorial(5))



#Función recursiva Fibonacci

def fibonacci(n):
    """Devuelve el n-ésimo número de Fibonacci recursivamente"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci de 7:", fibonacci(7))

#Lista del [1..10]

from functools import reduce

numeros = [1,2,3,4,5,6,7,8,9,10]

#lista con cuadrados usando map
cuadrados = list(map(lambda x: x**2, numeros))
print("Cuadrados:", cuadrados)

#Filtrar números pares usando filter
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Números pares:", pares)

# Usar reduce
# Suma de [1..10]
suma_total = reduce(lambda x, y: x + y, numeros)
print("Suma de [1..10]:", suma_total)

#Producto de [1..5]
producto = reduce(lambda x, y: x * y, [1,2,3,4,5])
print("Producto de [1..5]:", producto)

