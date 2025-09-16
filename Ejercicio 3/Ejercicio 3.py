from functools import reduce


# Angel Garcia Romero - Ejercicio 3
# Funcion suma(a-b)
def suma(a, b):
    """Suma de dos numeros"""
    return a + b
# Funcion recursiva factorial(n)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
# Función Fibonacci(n)
def fibonacci(n):
    """Calcula el n numero de Fibonacci"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# Operaciones con listas
# Lista: [1,2,3,4,5,6,7,8,9,10]
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a) Nueva lista con los cuadrados de cada número usando map
cuadrados = list(map(lambda x: x**2, num))
# b) Filtrar los números pares usando filter
par = list(filter(lambda x: x % 2 == 0, num))
# Usamos reduce para calcular:
total_suma = reduce(lambda x, y: x + y, num)
#  El producto del [1 al 6]
total_producto = reduce(lambda x, y: x * y, range(1, 6))


# Resultados
if __name__ == "__main__":
    print("suma(3, 5):", suma(3, 5))
    print("factorial(5):", factorial(5))
    print("fibonacci(7):", fibonacci(7))
    print("Pares:", par)
    print("Cuadrados:", cuadrados)
    print("Suma total 1-10:", total_suma)
    print("Producto total 1-5:", total_producto)
