""" Juan Antonio Roman Castro Práctica 3 
    Serie de Fibonacci                   """

def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

if __name__ == "__main__":
    try:
        print("Programa para calcular la sucesión de Fibonacci")
        print(fibo(abs(int(input("Introduce la cantidad de veces para calcular (cualquier número se tomará como positivo):\n")))))
    except:
        print("Introduce caracteres numéricos enteros")