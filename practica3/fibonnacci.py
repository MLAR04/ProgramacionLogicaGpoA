#Escribe una función recursiva que calcule el n-ésimo número de Fibonacci.

def fibonacci(i):
    #Funcion de la sucesion de Fibonacci
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i - 1) + fibonacci(i - 2) #Recursividad, llama la funcion en la misma funcion
    
    
print(fibonacci(4))