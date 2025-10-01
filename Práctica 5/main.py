""""
Programación Lógica
Práctica 5 - Diagnostico de Enfermedades Comunes
Este programa utiliza la librería Flet para crear una interfaz gráfica que permite a los usuarios seleccionar síntomas y diagnosticar posibles enfermedades comunes basadas en esos síntomas.
"""
import flet as ft
from datos import enfermedades

def main(page: ft.Page):
    page.title = "Práctica 5 - Diagnostico de Enfermedades Comunes"
    page.theme_mode = "dark"
    page.padding = 20
    page.bgcolor = "#000000"
    
    #UI
    header = ft.Row(
        controls=[ft.Text("Diagnostico de Enfermedades Comunes", size=24, weight="bold", color="#FFFFFF")],
        alignment="spaceBetween"
    )
    page.add(header, ft.Text("Selecciona tus síntomas:", size=20, weight="bold"))
    sintomas = set()
    for lista in enfermedades["sintomas"].values():
        sintomas.update(lista)
    sintomas = list(sintomas)
    sintomas.sort()
    checks = []
    for sintoma in sintomas:
        chk = ft.Checkbox(label=sintoma)
        checks.append(chk)
        def on_change(e):
            if e.control.value:
                sintomas_seleccionados.append(e.control.label)
            else:
                sintomas_seleccionados.remove(e.control.label)
        chk.on_change = on_change
        page.add(chk)
    sintomas_seleccionados = [] 
    resultado = ft.Text("", size=16, weight="bold")

    def diagnosticar(e):
        posibles_enfermedades = []
        for enfermedad, lista_sintomas in enfermedades["sintomas"].items():
            if all(sintoma in sintomas_seleccionados for sintoma in lista_sintomas):
                posibles_enfermedades.append(enfermedad)
        if posibles_enfermedades:
            resultado.value = "Podrías tener: " + ", ".join(posibles_enfermedades)
        else:
            resultado.value = "No se pudo determinar una enfermedad con los síntomas seleccionados."
        page.update()
    btn_diagnosticar = ft.ElevatedButton("Diagnosticar", on_click=diagnosticar)
    page.add(btn_diagnosticar)
    page.add(resultado)

    page.add(chk)


ft.app(target=main)