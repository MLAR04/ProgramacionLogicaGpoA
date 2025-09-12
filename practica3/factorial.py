#Implementa una función recursiva factorial(n) que calcule el factorial.

def factorial(n):
    #Funcion para poder sacar el factorial de un numero n
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(4))