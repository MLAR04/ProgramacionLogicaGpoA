from functools import reduce
import operator

# Ejercicio 1: Suma 

def suma(a, b):
  return a + b

# Ejercicio 2: Factorial

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

# Ejercicio 3: Fibonacci

def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

# --- Ejercicio 4: map, filter y reduce ---

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cuadrados = list(map(lambda x: x**2, numeros))

pares = list(filter(lambda x: x % 2 == 0, numeros))

suma_total = reduce(operator.add, numeros)

# Producto de [1..5]
producto_parcial = reduce(operator.mul, numeros[:5])

# Resultados

print("Ejercicio 1: Suma")
print(f"Resultado de suma(5, 3): {suma(5, 3)}")
print("Ejercicio 2: Factorial")
print(f"Resultado de factorial(5): {factorial(5)}")

print("Ejercicio 3: Fibonacci")
print(f"El 9º número de Fibonacci es: {fibonacci(9)}")

print("Ejercicio 4: map, filter y reduce")
print(f"Lista original: {numeros}")
print(f"Cuadrados de la lista (con map): {cuadrados}")
print(f"Números pares de la lista (con filter): {pares}")
print(f"Suma de la lista [1..10] (con reduce): {suma_total}")
print(f"Producto de la lista [1..5] (con reduce): {producto_parcial}")