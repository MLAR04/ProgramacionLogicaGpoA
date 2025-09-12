import tkinter as tk
from tkinter import ttk
from functools import reduce


# Funciones de la práctica

def suma(a, b):
    return a + b

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

lista = [1,2,3,4,5,6,7,8,9,10]


# Funciones auxiliares

def ejecutar_suma():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        resultado_suma.set(f"Suma({a},{b}) = {suma(a,b)}")
    except ValueError:
        resultado_suma.set("⚠️ Ingresa números válidos")

def ejecutar_factorial():
    try:
        n = int(entry_fact.get())
        resultado_fact.set(f"Factorial({n}) = {factorial(n)}")
    except ValueError:
        resultado_fact.set("⚠️ Ingresa un número válido")

def ejecutar_fibonacci():
    try:
        n = int(entry_fib.get())
        resultado_fib.set(f"Fibonacci({n}) = {fibonacci(n)}")
    except ValueError:
        resultado_fib.set("⚠️ Ingresa un número válido")

def ejecutar_map():
    cuadrados = list(map(lambda x: x**2, lista))
    resultado_lista.set(f"Cuadrados: {cuadrados}")

def ejecutar_filter():
    pares = list(filter(lambda x: x % 2 == 0, lista))
    resultado_lista.set(f"Pares: {pares}")

def ejecutar_reduce_suma():
    suma_total = reduce(lambda x, y: x + y, lista)
    resultado_lista.set(f"Suma [1..10] = {suma_total}")

def ejecutar_reduce_producto():
    lista_5 = [1, 2, 3, 4, 5]
    producto = reduce(lambda x, y: x * y, lista_5)
    resultado_lista.set(f"Producto [1..5] = {producto}")

# Interfaz gráfica con estilo

ventana = tk.Tk()
ventana.title("Práctica #3 -22760568- Programación Funcional en Python")
ventana.geometry("700x700")
ventana.configure(bg="#f5f6fa")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Segoe UI", 11), padding=6, relief="flat", background="#0984e3", foreground="white")
style.map("TButton", background=[("active", "#74b9ff")])
style.configure("TLabel", font=("Segoe UI", 11), background="#f5f6fa")
style.configure("Title.TLabel", font=("Segoe UI", 14, "bold"), background="#dfe6e9", padding=8)

# Variables de resultado independientes
resultado_suma = tk.StringVar()
resultado_fact = tk.StringVar()
resultado_fib = tk.StringVar()
resultado_lista = tk.StringVar()

# Título principal
ttk.Label(ventana, text="Práctica #3 -22760568- Programación Funcional", style="Title.TLabel").pack(fill="x", pady=10)

# Frame de suma
frame_suma = ttk.LabelFrame(ventana, text="Suma de dos números")
frame_suma.pack(padx=10, pady=10, fill="x")
ttk.Label(frame_suma, text="Número a:").grid(row=0, column=0, padx=5, pady=5)
entry_a = ttk.Entry(frame_suma)
entry_a.grid(row=0, column=1, padx=5, pady=5)
ttk.Label(frame_suma, text="Número b:").grid(row=1, column=0, padx=5, pady=5)
entry_b = ttk.Entry(frame_suma)
entry_b.grid(row=1, column=1, padx=5, pady=5)
ttk.Button(frame_suma, text="Calcular Suma", command=ejecutar_suma).grid(row=2, column=0, columnspan=2, pady=5)
ttk.Label(frame_suma, textvariable=resultado_suma, font=("Segoe UI", 11), foreground="#2d3436").grid(row=3, column=0, columnspan=2, pady=5)

# Frame factorial
frame_fact = ttk.LabelFrame(ventana, text="Función Recursiva: Factorial")
frame_fact.pack(padx=10, pady=10, fill="x")
ttk.Label(frame_fact, text="Número n:").grid(row=0, column=0, padx=5, pady=5)
entry_fact = ttk.Entry(frame_fact)
entry_fact.grid(row=0, column=1, padx=5, pady=5)
ttk.Button(frame_fact, text="Calcular Factorial", command=ejecutar_factorial).grid(row=1, column=0, columnspan=2, pady=5)
ttk.Label(frame_fact, textvariable=resultado_fact, font=("Segoe UI", 11), foreground="#2d3436").grid(row=2, column=0, columnspan=2, pady=5)

# Frame fibonacci
frame_fib = ttk.LabelFrame(ventana, text="Función Recursiva: Fibonacci")
frame_fib.pack(padx=10, pady=10, fill="x")
ttk.Label(frame_fib, text="Número n:").grid(row=0, column=0, padx=5, pady=5)
entry_fib = ttk.Entry(frame_fib)
entry_fib.grid(row=0, column=1, padx=5, pady=5)
ttk.Button(frame_fib, text="Calcular Fibonacci", command=ejecutar_fibonacci).grid(row=1, column=0, columnspan=2, pady=5)
ttk.Label(frame_fib, textvariable=resultado_fib, font=("Segoe UI", 11), foreground="#2d3436").grid(row=2, column=0, columnspan=2, pady=5)

# Frame operaciones con listas
frame_lista = ttk.LabelFrame(ventana, text="Operaciones con listas")
frame_lista.pack(padx=10, pady=10, fill="x")
ttk.Button(frame_lista, text="Map: cuadrados", command=ejecutar_map).grid(row=0, column=0, padx=5, pady=5)
ttk.Button(frame_lista, text="Filter: pares", command=ejecutar_filter).grid(row=0, column=1, padx=5, pady=5)
ttk.Button(frame_lista, text="Reduce: suma [1..10]", command=ejecutar_reduce_suma).grid(row=1, column=0, padx=5, pady=5)
ttk.Button(frame_lista, text="Reduce: producto [1..5]", command=ejecutar_reduce_producto).grid(row=1, column=1, padx=5, pady=5)
ttk.Label(frame_lista, textvariable=resultado_lista, font=("Segoe UI", 11), foreground="#2d3436").grid(row=2, column=0, columnspan=2, pady=10)

ventana.mainloop()
