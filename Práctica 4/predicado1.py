'''
Predicado: Un número es múltiplo de 6 si es divisible entre 2 y entre 3
'''
import sys

def multiplo(n):
    if n % 2 == 0 and n % 3 == 0:
        print(f"El número {n} es divisible entre 2 y 3")
        return True
    else:
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Esto se usa así, mira: python predicado1.py <n>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        print(multiplo(n))
    except ValueError:
        print("El argumento debe ser un entero válido.")
