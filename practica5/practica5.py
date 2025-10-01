import tkinter as tk
from tkinter import ttk

sintomas = [
'Fiebre',
'Tos',
'Dolor de cabeza',
'Congestion nasal',
'Nauseas',
'Cansansio',
'Perdida de olfato']

enfermedades = {'gripa':[1,2],'covid':[0,1,2,5],'migraña':[2,4],'resfriado':[1,3,5]}

respuestas = []

def diagnostico(resultados):
    resultados.sort()
    for key,value in enfermedades.items():
        if value == resultados:
            resultado.config(text=f'Estas enfermo de {key}')
            resultado.pack()
            return
    resultado.config(text='No pudimos diagnosticar tu enfermedad')
    resultado.pack()
    return

def agregar_sintoma(sintoma):
    resultado.pack_forget()
    if sintoma in respuestas:
        respuestas.remove(sintoma)
    else:
        respuestas.append(sintoma)

window = tk.Tk()
window.title('Diagnostico de Enfermedades Comunes')
window.geometry("500x500")

texto = ttk.Label(window,text='Marca tus sintomas para recibir un diagnostico')
texto.pack()

for index, valor in enumerate(sintomas):
    var = tk.BooleanVar()
    checkbox = tk.Checkbutton(window,text=valor,variable=var,command=lambda i=index: agregar_sintoma(i))
    checkbox.pack()

diagnostico_button = ttk.Button(window,text='Diagnosticar',command=lambda: diagnostico(respuestas))
diagnostico_button.pack()

resultado = ttk.Label(window)
    
window.mainloop()
