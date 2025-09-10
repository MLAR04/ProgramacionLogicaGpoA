from functools import reduce

# --- Funciones de lógica ---
def suma(a: int, b: int) -> int:
    return a + b

def factorizar(a: int) -> int:
    if a < 0:
        raise ValueError("El factorial no está definido para números negativos")
    if a == 0 or a == 1:
        return 1
    return a * factorizar(a - 1)

def fibonacci(a: int) -> int:
    if a <= 1:
        return a
    return fibonacci(a-1) + fibonacci(a-2)

def cuadrados(lista):
    return [n**2 for n in lista]

def filtrar_pares(lista):
    return list(filter(lambda n: n % 2 == 0, lista))

def suma_total(lista):
    return reduce(lambda x, y: x + y, lista)

def producto_total(lista):
    return reduce(lambda x, y: x * y, lista)
