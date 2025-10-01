import flet as ft

enfermedades = {
    "gripe": ("Dolor de cabeza","Tos"),
    "covid": ("Perdida de olfato","Cansancio","Tos","Fiebre"),
    "migrana" :("Dolor de cabeza","Nauseas"),
    "resfriado":("Congestion nasal","Tos","Fiebre")
}

class MyButton(ft.ElevatedButton):
    def __init__(self, text, data, page, resultado):
        super().__init__()
        self.bgcolor = ft.Colors.ORANGE_300
        self.color = ft.Colors.GREEN_800
        self.text = text
        self.data = data
        self.page = page
        self.resultado = resultado
        self.on_click = self.procesar
    
    def procesar(self,e):
        pedillos = []
        for check in e.control.data:
            if check.value:
                pedillos.append(check.label)
        pedillos = tuple(pedillos)
        diagnostico = comparar(pedillos, list(enfermedades.items()))
        self.resultado.value = diagnostico
        self.page.update()

class Check(ft.Checkbox):
    def __init__(self, text):
        super().__init__()
        self.value = False
        self.label = text

def comparar(losPedillos, posiblesPedotes, i=0):
    if len(losPedillos) == 0:
        return "Selecciona tus síntomas  por favor"
    if i == len(posiblesPedotes):
        return "Ese conjunto de síntomas no le pertenece a ninguna enfermedad en el sistema, te recomiendo ir al médico para un mejor análisis"
    enfermedad, sintomas = posiblesPedotes[i]
    if sorted(losPedillos) == sorted(sintomas):
        return f"Por esos síntomas tienes {enfermedad}"
    return comparar(losPedillos,posiblesPedotes, i+1)
    

def main(page: ft.Page):
    page.window.width = 300
    page.window.height = 600
    page.add(ft.Text(
        "Diagnosticador", 
        color=ft.Colors.BLUE, 
        size=24, 
        font_family="Comic Sans MS", 
        text_align="center")
    )
    lista = set()
    for sintomas in enfermedades.values():
        lista.update(sintomas)
    lista = list(lista)
    lista.sort()
    checklist = []
    for sintoma in lista:
        check = Check(sintoma)
        page.add(check)
        checklist.append(check)
    resultado = ft.Text(
        "", 
        color=ft.Colors.BLUE, 
        size=16, 
        font_family="Comic Sans MS"
    )
    page.add(MyButton(
        text="OK", 
        data=checklist, 
        page=page, 
        resultado=resultado)
    )
    page.add(resultado)

if __name__ == "__main__":
    ft.app(main)
