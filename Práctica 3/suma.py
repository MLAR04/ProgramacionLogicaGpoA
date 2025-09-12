'''
Instrucciones: Escribir una función suma(a,b) que solo dependa de sus
parámetros.

Memorándum: Especifica que quieres obtener datos numéricos flotantes
o enteros, de lo contrario lo único que harás es que sumar 2+2 te de 22
como en JS.
'''

import sys

def suma(a, b):
    print(float(a)+float(b))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Esto se usa así, mira: python suma.py <a> <b>")
        sys.exit(1)

    numero1 = sys.argv[1]
    numero2 = sys.argv[2]
    suma(numero1, numero2)

# Autor: E. A. Tavares Medina
