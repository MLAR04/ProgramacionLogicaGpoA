'''
Instrucciones: Implementar una función recursiva factorial(n) que calcule
el factorial.

Memorándum: Mete excepciones y manejo de errores, es decir, especifica
por todos los medios que quieres un valor entero.
'''
import sys

def factorial(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)
        

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Esto se usa así, mira: python factorial.py <n>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        print(factorial(n))
    except ValueError:
        print("El argumento debe ser un entero válido.")
        
# Autor: E. A. Tavares Medina
