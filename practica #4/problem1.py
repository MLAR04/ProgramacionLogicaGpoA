""" Juan Antonio Román Castro Práctica 4  
    Un número es múltiplo de 6 si es divisible entre 2 y entre 3."""

def problema(x):
    if x%2 == 0 and x%3 == 0:
        return "Es múltiplo de 6"
    return "No es múltiplo de 6"

if __name__ == "__main__":
    try:
        print(problema(int(input("Introduce un número para analizarlo:\n"))))
    except:
        print("Solo se aceptan números enteros")