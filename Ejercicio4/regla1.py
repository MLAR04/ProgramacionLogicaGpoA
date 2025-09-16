#Un número es múltiplo de 6 si es divisible entre 2 y entre 3

numero = int(input("Inserta tu numero: "))

def revisar_numero(x):
    if x % 2 == 0 and x % 3 == 0:
        return True
    return False

print(revisar_numero(numero))