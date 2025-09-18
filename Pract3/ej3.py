#Gabriel Lopez 22760564
# Práctica #3 - Ejercicio 3
# Escribe una función recursiva que calcule el n-ésimo número de Fibonacci.

def fibonacci(n):
    if n == 0:  
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    print("Fibonacci de 7:", fibonacci(7))
