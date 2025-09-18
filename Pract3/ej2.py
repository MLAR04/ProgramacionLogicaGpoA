#Gabriel Lopez 22760564
# Práctica #3 - Ejercicio 2
# Implementa una función recursiva factorial(n) que calcule el factorial.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)  

if __name__ == "__main__":
    print("Factorial de 5:", factorial(5))
