import flet as ft

enfermedades = {
    "sintomas": {
        "gripe": ["dolor de cabeza", "tos"],
        "covid": ["perdida de olfato", "cansancio", "tos", "fiebre"],
        "migraña": ["nauseas", "dolor de cabeza"],
        "resfriado": ["congestión nasal", "tos", "fiebre"]
    }
}

def main(page: ft.Page):
    page.title = "P5 - Diagnóstico de Enfermedades Comunes"
    page.padding = 30
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#63DAD0"
    
    sintomas_seleccionados = []
    resultado_texto = ft.Text("", size=16, weight="bold", color="#FFFFFF", text_align=ft.TextAlign.CENTER)

    todos_sintomas = sorted(list(set().union(*enfermedades["sintomas"].values())))
    
    checkboxes = []
    for sintoma in todos_sintomas:
        def crear_on_change(s):
            def on_change(e):
                if e.control.value:
                    if s not in sintomas_seleccionados:
                        sintomas_seleccionados.append(s)
                else:
                    if s in sintomas_seleccionados:
                        sintomas_seleccionados.remove(s)
            return on_change
        
        chk = ft.Checkbox(
            label=sintoma,
            label_style=ft.TextStyle(color="#02756C", size=14),
            fill_color="#02756C",
            check_color="#FFFFFF"
        )
        chk.on_change = crear_on_change(sintoma)
        checkboxes.append(chk)
    
    mitad = (len(checkboxes) + 1) // 2
    columna1 = checkboxes[:mitad]
    columna2 = checkboxes[mitad:]
    
    def diagnosticar(e):
        posibles_enfermedades = []
        
        for enfermedad, lista_sintomas in enfermedades["sintomas"].items():
            if all(sintoma in sintomas_seleccionados for sintoma in lista_sintomas):
                posibles_enfermedades.append(enfermedad)
                
        if posibles_enfermedades:
            resultado_texto.value = f"Podrías tener: {', '.join(posibles_enfermedades)}"
            resultado_texto.color = "#FFFFFF"
        else:
            resultado_texto.value = "No se pudo determinar una enfermedad con los síntomas seleccionados."
            resultado_texto.color = "#FFEB3B"
        
        page.update()
    
    # Interfaz
    contenido = ft.Container(
        content=ft.Column(
            [
                ft.Container(
                    content=ft.Column([
                        ft.Text("🏥", size=40),
                        ft.Text("Diagnóstico de", size=26, weight="bold", color="#FFFFFF"),
                        ft.Text("Enfermedades Comunes", size=26, weight="bold", color="#FFFFFF"),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    padding=20
                ),
                
                ft.Container(
                    content=ft.Column([
                        ft.Text("Selecciona tus síntomas:", 
                               size=18, weight="bold", color="#FFFFFF"),
                        ft.Container(height=15),
                        ft.Row(
                            [
                                ft.Column(columna1, spacing=10),
                                ft.Column(columna2, spacing=10),
                            ],
                            spacing=40,
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ]),
                    padding=25,
                    bgcolor="#FFFFFF",
                    border_radius=15,
                    width=500
                ),
                
                ft.Container(
                    content=ft.ElevatedButton(
                        "Realizar Diagnóstico", 
                        on_click=diagnosticar,
                        style=ft.ButtonStyle(
                            color="#FFFFFF",
                            bgcolor="#02756C",
                            padding=20,
                        )
                    ),
                    padding=15
                ),
                
                ft.Container(
                    content=resultado_texto,
                    padding=20,
                    width=500,
                    bgcolor="#02756C",
                    border_radius=10,
                )
            ],
            spacing=25,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=20
    )
    
    page.add(contenido)

ft.app(target=main)