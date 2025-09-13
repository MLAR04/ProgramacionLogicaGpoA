""" Juan Antonio Roman Castro Práctica 3 
    Factoriales                          """

def factos(x):
    if x > 1:
        return x * factos(x-1)
    return 1

if __name__ == "__main__":
    try:
        print("Programa para calcular factoriales")
        print(factos(abs(int(input("Introduce el número al que le deseas calcular el factorial (cualquier número se tomará como positivo):\n")))))
    except:
        print("Introduce caracteres numéricos enteros")