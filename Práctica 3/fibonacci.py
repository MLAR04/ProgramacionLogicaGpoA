'''
Instrucciones: Escribir una función recursiva que calcule el n-ésimo
número de fibonacci.

Nota: Este sí me salió a la primera juejue
'''
import sys

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Esto se usa así, mira: python fibonacci.py <n>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        print(fibonacci(n))
    except ValueError:
        print("El argumento debe ser un entero válido")

# Autor: E. A. Tavares Medina
