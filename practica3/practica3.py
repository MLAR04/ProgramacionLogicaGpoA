# Ejercicio 1: Función suma(a, b)

def suma(a, b):
    """Devuelve la suma de dos números."""
    return a + b

# Ejercicio 2: Factorial recursivo

def factorial(n):
    """Calcula el factorial de un número n de forma recursiva."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Ejercicio 3: Fibonacci recursivo
def fibonacci(n):
    """Calcula el n-ésimo número de Fibonacci de forma recursiva."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Ejercicio 4: Operaciones con listas
from functools import reduce

lista = [1,2,3,4,5,6,7,8,9,10]

# 4a) Lista con los cuadrados de cada número usando map
cuadrados = list(map(lambda x: x**2, lista))

# 4b) Filtrar los números pares usando filter
pares = list(filter(lambda x: x % 2 == 0, lista))

# 4c) Usar reduce
# Suma de [1..10]
suma_total = reduce(lambda x, y: x + y, lista)

# Producto de [1..5]
producto = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])


# Las Pruebas de ejecución

if __name__ == "__main__":
    print("Suma(5, 3):", suma(5, 3))
    print("Factorial(5):", factorial(5))
    print("Fibonacci(7):", fibonacci(7))
    print("Cuadrados:", cuadrados)
    print("Pares:", pares)
    print("Suma [1..10]:", suma_total)
    print("Producto [1..5]:", producto)
