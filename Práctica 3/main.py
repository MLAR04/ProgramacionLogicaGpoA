import flet as ft
from logic import suma, factorizar, fibonacci, cuadrados, filtrar_pares, suma_total, producto_total

def main(page: ft.Page):
    page.title = "Práctica"
    page.theme_mode = "light"
    page.padding = 20
    page.bgcolor = "#FFFFFF"


    # Campos de entrada y salida
    x = ft.TextField(label="Valor X", width=150)
    y = ft.TextField(label="Valor Y", width=150)

    resultado_suma = ft.TextField(label="Suma", read_only=True, width=200)
    resultado_factorial = ft.TextField(label="Factorial", read_only=True, width=200)
    resultado_fibonacci = ft.TextField(label="Fibonacci", read_only=True, width=200)
    resultado_cuadrados = ft.TextField(label="Cuadrados", read_only=True, width=200)
    resultado_filtrados = ft.TextField(label="Filtrados (pares)", read_only=True, width=200)
    resultado_sumados = ft.TextField(label="Suma total", read_only=True, width=200)
    resultado_productos = ft.TextField(label="Producto", read_only=True, width=200)

    numbers = [1,2,3,4,5,6,7,8,9,10]

    # Handlers
    def calcular_suma(e):
        try:
            resultado_suma.value = str(suma(int(x.value), int(y.value)))
        except:
            resultado_suma.value = "Error"
        page.update()

    def calcular_factorial(e):
        try:
            resultado_factorial.value = str(factorizar(int(x.value)))
        except:
            resultado_factorial.value = "Error"
        page.update()

    def calcular_fibonacci(e):
        try:
            resultado_fibonacci.value = str(fibonacci(int(x.value)))
        except:
            resultado_fibonacci.value = "Error"
        page.update()

    def calcular_todo(e):
        try:
            resultado_cuadrados.value = str(cuadrados(numbers))
            resultado_filtrados.value = str(filtrar_pares(numbers))
            resultado_sumados.value = str(suma_total(numbers))
            resultado_productos.value = str(producto_total(numbers))
        except:
            resultado_cuadrados.value = "Error"
        page.update()

    # UI
    header = ft.Row(
        controls=[ft.Text("Práctica Número 3", size=24, weight="bold", color="#000000")],
        alignment="spaceBetween"
    )

    card1 = ft.Container(
        content=ft.Column([ft.Text("Ejercicio 1", size=20, weight="bold"),
                           ft.Text("Función suma(a,b)"),
                           x, y, resultado_suma,
                           ft.ElevatedButton("Realizar Suma", on_click=calcular_suma)]),
        padding=20, border_radius=20, bgcolor="white", width=300, height=350
    )

    card2 = ft.Container(
        content=ft.Column([ft.Text("Ejercicio 2", size=20, weight="bold"),
                           ft.Text("Función factorial(n)"),
                           x, resultado_factorial,
                           ft.ElevatedButton("Factorizar", on_click=calcular_factorial)]),
        padding=20, border_radius=20, bgcolor="white", width=300, height=350
    )

    card3 = ft.Container(
        content=ft.Column([ft.Text("Ejercicio 3", size=20, weight="bold"),
                           ft.Text("Función fibonacci(n)"),
                           x, resultado_fibonacci,
                           ft.ElevatedButton("Fibonacciar", on_click=calcular_fibonacci)]),
        padding=20, border_radius=20, bgcolor="white", width=300, height=350
    )

    card4 = ft.Container(
        content=ft.Column([ft.Text("Ejercicio 4", size=20, weight="bold"),
                           ft.Text("Lista [1..10]"),
                           resultado_cuadrados, resultado_filtrados,
                           resultado_sumados, resultado_productos,
                           ft.ElevatedButton("Mostrar todo", on_click=calcular_todo)]),
        padding=20, border_radius=20, bgcolor="white", width=300, height=400
    )

    page.add(header, ft.Divider(), ft.Row([card1, card2, card3, card4], alignment="center", spacing=30))
    page.update()


ft.app(target=main)
