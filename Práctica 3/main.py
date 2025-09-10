import flet as ft
import logic
from functools import reduce   # Importar reduce de la librería estándar


def main(page: ft.Page):
    page.title = "Práctica"
    page.theme_mode = "light"
    page.padding = 20
    page.bgcolor = "#FFFFFF"
    page.window_full_screen = True 

    # Variables de entrada
    x = ft.TextField(label="Valor X", width=150)
    y = ft.TextField(label="Valor Y", width=150)
    
    # Lista base
    numbers = [1,2,3,4,5,6,7,8,9,10]

    # TextField para mostrar los resultados
    resultado = ft.TextField(label="Suma", read_only=True, width=200)
    resultado_factorial = ft.TextField(label="Factorial", read_only=True, width=200)  
    resultado_fibonacci = ft.TextField(label="Fibonacci", read_only=True, width=200)  
    resultado_cuadrados = ft.TextField(label="Cuadrados", read_only=True, width=200) 
    resultado_filtrados = ft.TextField(label="Filtrados (pares)", read_only=True, width=200) 
    resultado_sumados = ft.TextField(label="Suma total", read_only=True, width=200)
    resultado_productos = ft.TextField(label="Producto", read_only=True, width=200)


    # Función para calcular suma
    def calcular_suma(e):
        try:
            valor_x = int(x.value)
            valor_y = int(y.value)
            suma = logic.suma(valor_x, valor_y)
            resultado.value = str(suma) 
        except ValueError:
            resultado.value = "Error"
        page.update()
    
    # Función para calcular factorial
    def calcular_factorial(e):
        try:
            valor_x = int(x.value)
            factorizar = logic.factorizar(valor_x)
            resultado_factorial.value = str(factorizar)
        except ValueError:
            resultado_factorial.value = "Error"
        page.update()

    # Función para calcular sucesión fibonacci
    def calcular_fibonacci(e):
        try:
            valor_x = int(x.value)
            fibonicciar = logic.fibonacci(valor_x)
            resultado_fibonacci.value = str(fibonicciar)
        except ValueError:
            resultado_fibonacci.value = "Error"
        page.update()

    # Lista Cuadrados
    def calcular_listas(e):
        try:
            numeros_cuadrados = [n**2 for n in numbers]
            resultado_cuadrados.value = str(numeros_cuadrados)
            return numeros_cuadrados
        except Exception as err:
            resultado_cuadrados.value = f"error: {err}"

    def es_par(numero):
        return numero % 2 == 0

    # Filtrar Números
    def filtrar_numbers(e, lista_cuadrados):
        try:
            pares_numbers_filtro = filter(es_par, lista_cuadrados)
            numeros_pares = list(pares_numbers_filtro)
            resultado_filtrados.value = str(numeros_pares)
        except Exception as err:
            resultado_filtrados.value = f"error: {err}"

    # Reduce Números (suma total)
    def calcular_reduce(e):
        try:
            suma_total = reduce(lambda x, y: x + y, numbers)
            resultado_sumados.value = str(suma_total)
        except Exception as err:
            resultado_sumados.value = f"error: {err}"

    # Producto Números
    def producto(e):
        try:
            numeros = [1, 2, 3, 4, 5]
            producto_total = reduce(lambda x, y: x * y, numeros)
            resultado_productos.value = str(producto_total)
        except Exception as err:
            resultado_productos.value = f"error: {err}"

    # Ejecutar todo
    def calcular_todo(e):
        lista_cuadrados = calcular_listas(e)
        if lista_cuadrados:
            filtrar_numbers(e, lista_cuadrados)
        calcular_reduce(e)
        producto(e)
        page.update()

    # Header
    header = ft.Row(
        controls=[
            ft.Text("Práctica Número 3", size=24, weight="bold", color="#000000"),
        ],
        alignment="spaceBetween"
    )

    # Card del ejercicio 1
    card1 = ft.Container(
        content=ft.Column(
            [
                ft.Text("Ejercicio 1", size=20, weight="bold"),
                ft.Text("Escribe una función suma(a,b) que solo dependa de sus parámetros."),
                x, y, resultado,
                ft.ElevatedButton("Realizar Suma", on_click=calcular_suma)
            ],
            spacing=10,
            horizontal_alignment="center"
        ),
        padding=20,
        border_radius=20,
        bgcolor="white",
        shadow=ft.BoxShadow(blur_radius=15, color=ft.Colors.GREY_300),
        width=300,
        height=350
    )
    
    # Card del ejercicio 2
    card2 = ft.Container(
        content=ft.Column(
            [
                ft.Text("Ejercicio 2", size=20, weight="bold"),
                ft.Text("Implementa una función recursiva factorial(n) que calcule el factorial."),
                x, resultado_factorial,
                ft.ElevatedButton("Factorizar", on_click=calcular_factorial)
            ],
            spacing=10,
            horizontal_alignment="center"
        ),
        padding=20,
        border_radius=20,
        bgcolor="white",
        shadow=ft.BoxShadow(blur_radius=15, color=ft.Colors.GREY_300),
        width=300,
        height=350
    )

    # Card del ejercicio 3
    card3 = ft.Container(
        content=ft.Column(
            [
                ft.Text("Ejercicio 3", size=20, weight="bold"),
                ft.Text("Escribe una función recursiva que calcule el n-ésimo número de Fibonacci."),
                x, resultado_fibonacci,
                ft.ElevatedButton("Fibonacciar", on_click=calcular_fibonacci)
            ],
            spacing=10,
            horizontal_alignment="center"
        ),
        padding=20,
        border_radius=20,
        bgcolor="white",
        shadow=ft.BoxShadow(blur_radius=15, color=ft.Colors.GREY_300),
        width=300,
        height=350
    )

    # Card del ejercicio 4
    card4 = ft.Container(
        content=ft.Column(
            [
                ft.Text("Ejercicio 4", size=20, weight="bold"),
                ft.Text("Dada la lista [1,2,3,4,5,6,7,8,9,10]:", size=16),
                resultado_cuadrados,
                resultado_filtrados,
                resultado_sumados,
                resultado_productos,
                ft.ElevatedButton("Mostrar todo", on_click=calcular_todo)
            ],
            spacing=10,
            horizontal_alignment="center"
        ),
        padding=20,
        border_radius=20,
        bgcolor="white",
        shadow=ft.BoxShadow(blur_radius=15, color=ft.Colors.GREY_300),
        width=300,
        height=400
    )

    # Layout con tarjetas
    content = ft.Row(
        controls=[card1, card2, card3, card4],
        alignment="center",
        spacing=30
    )

    # Agregar todo a la página
    page.add(header, ft.Divider(), content)


#ft.app(target=main)
ft.app(target=main, view=ft.WEB_BROWSER)
