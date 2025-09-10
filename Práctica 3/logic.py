
def suma(a: int, b: int) -> int:
    """Función que solo depende de sus parámetros"""
    return a + b

def factorizar(a: int) -> int:
    """Función que calcula el factorial del número ingresado de forma recursiva"""
    if a < 0:
        raise ValueError("El factorial no está definido para números negativos")
    if a == 0 or a == 1:
        return 1
    return a * factorizar(a - 1)

def fibonacci(a):
    """Función que calcula la sucesión de Fibonacci"""
    if a <= 1:
        return a
    else:
        return fibonacci(a-1) + fibonacci(a-2)