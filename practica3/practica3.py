
def suma(a, b):
    """Devuelve la suma de dos números."""
    return a + b

def factorial(n):
    """Calcula el factorial de un número n de forma recursiva."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    """Calcula el n-ésimo número de Fibonacci de forma recursiva."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

from functools import reduce

lista = [1,2,3,4,5,6,7,8,9,10]
cuadrados = list(map(lambda x: x**2, lista))
pares = list(filter(lambda x: x % 2 == 0, lista))
suma_total = reduce(lambda x, y: x + y, lista)
producto = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])

if __name__ == "__main__":
    print("Suma(5, 3):", suma(5, 3))
    print("Factorial(5):", factorial(5))
    print("Fibonacci(7):", fibonacci(7))
    print("Cuadrados:", cuadrados)
    print("Pares:", pares)
    print("Suma [1..10]:", suma_total)
    print("Producto [1..5]:", producto)

