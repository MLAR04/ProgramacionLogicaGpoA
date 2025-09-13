from functools import reduce
import tkinter as tk
from tkinter import ttk

#Escribe una función suma(a,b) que solo dependa de sus parámetros.
def addition(a,b):
    return a + b

#Implementa una función recursiva factorial(n) que calcule el factorial.
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

#Escribe una función recursiva que calcule el n-ésimo número de Fibonacci.
def fibonacci(n):
    if n > 1:
        return fibonacci(n - 1) + fibonacci(n -2)
    return n

#Dada la lista [1,2,3,4,5,6,7,8,9,10]:
list_nums = [1,2,3,4,5,6,7,8,9,10]

#Genera una nueva lista con los cuadrados de cada número usando map.
def squares(numbers):
    return list(map(lambda n: n**2,numbers))

#Filtra los números pares usando filter
def pairs(numbers):
    return list(filter(lambda n: n % 2 == 0,numbers))

#Usa reduce para calcular:
#La suma de [1..10]
def total(numbers):
    return reduce(lambda x, y: x+y, numbers)

#El producto [1..5]
def product(numbers):
    return reduce(lambda x,y: x*y,numbers[:5])

#Funciones de ayuda para la ventana
def show_addition():
    a = int(addition_a_entry.get())
    b = int(addition_b_entry.get())
    r = addition(a,b)
    result_addition.config(text=f"El resultado es: {r}")

def show_factorial():
    n = int(factorial_entry.get())
    if n < 1:
        result_factorial.config(text='Ingresa un numero positivo')
    else:
        r = factorial(n)
        result_factorial.config(text=f"El resultado es: {r}")

def show_fibonacci():
    n = int(fibonacci_entry.get())
    if n < 1:
        result_fibonacci.config(text='Ingresa un numero positivo')
    else:
        r = fibonacci(n)
        result_fibonacci.config(text=f"El resultado es: {r}")

def show_map():
    r = squares(list_nums)
    result_map.config(text=f'{r}')

def show_pairs():
    r = pairs(list_nums)
    result_filter.config(text=f'{r}')

def show_ruduce():
    r1 = total(list_nums)
    r2 = product(list_nums)
    result_reduce.config(text=f'La suma es: {r1}, y el producto es: {r2}')

#Ventana 
window = tk.Tk()
window.title('Programación Funcional en Python')
window.geometry("1000x700")

label_addition = ttk.Label(window,text='Ingresa tus numeros a sumar')

label_addition.grid(row=0,column=0)

addition_a_entry = ttk.Entry(window,width=30)
addition_b_entry = ttk.Entry(window,width=30)
result_addition = ttk.Label(window)
addition_button = ttk.Button(window,text='Sumar numeros',command= show_addition)

addition_a_entry.grid(row=1,column=0)
addition_b_entry.grid(row=2,column=0)
addition_button.grid(row=3,column=0)
result_addition.grid(row=4,column=0)

label_factorial = ttk.Label(window,text='Ingresa un numero para conocer su factorial')
factorial_entry = ttk.Entry(window,width=30)
factorial_button = ttk.Button(window,text='Secuencia',command=show_factorial)
result_factorial = ttk.Label(window)

label_factorial.grid(row=6,column=0)
factorial_entry.grid(row=7,column=0)
factorial_button.grid(row=8,column=0)
result_factorial.grid(row=9,column=0)

label_fibonacci = ttk.Label(window,text='Ingresa un numero para calculer el número de Fibonacci')
fibonacci_entry = ttk.Entry(window,width=30)
fibonacci_button = ttk.Button(window,text='fibonacci',command=show_fibonacci)
result_fibonacci = ttk.Label(window)

label_fibonacci.grid(row=11,column=0)
fibonacci_entry.grid(row=12,column=0)
fibonacci_button.grid(row=13,column=0)
result_fibonacci.grid(row=14,column=0)

label_map = ttk.Label(window,text='Genera una nueva lista con los cuadrados de cada número usando map y la lista [1,2,3,4,5,6,7,8,9,10]')
map_button = ttk.Button(window,text='Generar cuadrados',command=show_map)
result_map = ttk.Label(window)

label_map.grid(row=15,column=0)
map_button.grid(row=16,column=0)
result_map.grid(row=17,column=0)

label_filter = ttk.Label(window,text='Filtra los números pares usando filter')
filter_map = ttk.Button(window,text='Filtrar',command=show_pairs)
result_filter = ttk.Label(window)

label_filter.grid(row=19,column=0)
filter_map.grid(row=20,column=0)
result_filter.grid(row=21,column=0)

label_reduce = ttk.Label(window,text='Usar reduce para calcular')
reduce_button = ttk.Button(window,text='Reducir',command=show_ruduce)
result_reduce = ttk.Label(window)

label_reduce.grid(row=23,column=0)
reduce_button.grid(row=24,column=0)
result_reduce.grid(row=25,column=0)

window.mainloop()