""" Juan Antonio Roman Castro Práctica 3 
    Sumar 2 números                      """
def sumar(a,b):
    return a+b

if __name__ == "__main__":
    try:
        print("Programa para sumar 2 números")
        print(
            sumar(
                float(input("Introduce el primer número:\n")),
                float(input("Introduce el segundo número:\n"))
                )
            )
    except:
        print("Error: solo se aceptan caracteres numéricos")