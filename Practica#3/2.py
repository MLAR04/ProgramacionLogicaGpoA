def factorial(n):

    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial de 8 =", factorial(8))