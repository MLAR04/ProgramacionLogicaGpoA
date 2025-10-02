import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# =====================
# Base de conocimiento
# =====================
enfermedades = {
    "gripe": {
        "sintomas": ["tos", "dolor_cabeza"],
        "fuente": "Organización Mundial de la Salud. (2021). Guía sobre infecciones respiratorias. OMS."
    },
    "covid": {
        "sintomas": ["fiebre", "tos", "cansancio", "perdida_olfato"],
        "fuente": "Centers for Disease Control and Prevention. (2021). Symptoms of COVID-19. CDC."
    },
    "migraña": {
        "sintomas": ["dolor_cabeza", "nauseas"],
        "fuente": "International Headache Society. (2018). The International Classification of Headache Disorders (3rd ed.)."
    },
    "resfriado": {
        "sintomas": ["fiebre", "tos", "congestion_nasal"],
        "fuente": "Organización Mundial de la Salud. (2021). Resfriado común. OMS."
    }
}

# =============
# Motor lógico
# =============
def normalizar(texto):
    return texto.lower().strip().replace(" ", "_")

def diagnosticar(sintomas_usuario):
    sintomas_usuario = set(normalizar(s) for s in sintomas_usuario)
    mejor = None
    max_coincidencias = 0

    for enfermedad, datos in enfermedades.items():
        coincidencias = [s for s in datos["sintomas"] if s in sintomas_usuario]
        if len(coincidencias) > max_coincidencias:
            mejor = (enfermedad, coincidencias, datos["fuente"])
            max_coincidencias = len(coincidencias)

    return mejor

# =====================
# Funciones de interfaz
# =====================
def mostrar_diagnostico():
    entrada = entrada_sintomas.get("1.0", tk.END).split(",")
    sintomas_usuario = [s for s in entrada if s.strip()]

    if not sintomas_usuario:
        messagebox.showwarning("Aviso", "Escribe al menos un síntoma 🤒")
        return

    resultado = diagnosticar(sintomas_usuario)

    texto_resultado.config(state=tk.NORMAL)
    texto_resultado.delete("1.0", tk.END)

    if resultado:
        enf, coinc, fuente = resultado
        texto_resultado.insert(tk.END, f"• Posible enfermedad: {enf.capitalize()}\n")
        texto_resultado.insert(tk.END, f"  Coincidencias de síntomas: {', '.join(coinc)}\n")
        texto_resultado.insert(tk.END, f"  Fuente (APA): {fuente}\n")
    else:
        texto_resultado.insert(tk.END, "No se encontró coincidencia suficiente. Consulta a un médico.")

    texto_resultado.config(state=tk.DISABLED)

def resetear():
    entrada_sintomas.delete("1.0", tk.END)
    texto_resultado.config(state=tk.NORMAL)
    texto_resultado.delete("1.0", tk.END)
    texto_resultado.config(state=tk.DISABLED)

# =================
# Interfaz gráfica
# =================
ventana = tk.Tk()
ventana.title("🧠 Diagnóstico basado en síntomas según el Dr. Chuy")
ventana.geometry("750x600")
ventana.config(bg="#f0f8ff")

# Imagen decorativa
try:
    img = Image.open("salud.png")
    img = img.resize((250, 250), Image.Resampling.LANCZOS)
    foto = ImageTk.PhotoImage(img)
    etiqueta_imagen = tk.Label(ventana, image=foto, bg="#f0f8ff")
    etiqueta_imagen.pack(pady=10)
except:
    etiqueta_imagen = tk.Label(ventana, text="(Agrega salud.png en la carpeta)", font=("Comic Sans MS", 10), bg="#f0f8ff", fg="red")
    etiqueta_imagen.pack(pady=10)

# Título
titulo = tk.Label(ventana, text="¿Qué enfermedad podrías tener?", font=("Comic Sans MS", 18, "bold"), bg="#f0f8ff", fg="#2e8b57")
titulo.pack(pady=5)

# Instrucciones
instrucciones = tk.Label(ventana, text="Escribe tus síntomas separados por coma (ej: fiebre, tos, dolor de cabeza):", font=("Comic Sans MS", 12), bg="#f0f8ff", fg="#333")
instrucciones.pack(pady=5)

# Entrada de síntomas
entrada_sintomas = tk.Text(ventana, height=3, width=70, font=("Arial", 12))
entrada_sintomas.pack(pady=10)

# Botones
frame_botones = tk.Frame(ventana, bg="#f0f8ff")
frame_botones.pack(pady=10)

boton_diagnostico = tk.Button(frame_botones, text="Diagnosticar 🩺", command=mostrar_diagnostico, font=("Comic Sans MS", 14, "bold"), bg="#58d68d", fg="white")
boton_diagnostico.grid(row=0, column=0, padx=10)

boton_reset = tk.Button(frame_botones, text="Resetear 🔄", command=resetear, font=("Comic Sans MS", 14, "bold"), bg="#f1948a", fg="white")
boton_reset.grid(row=0, column=1, padx=10)

# Resultados
etiqueta_resultado = tk.Label(ventana, text="📋 Diagnóstico:", font=("Comic Sans MS", 14, "bold"), bg="#f0f8ff", fg="#884ea0")
etiqueta_resultado.pack(pady=5)

texto_resultado = tk.Text(ventana, height=12, width=80, font=("Arial", 12), bg="#fef9e7", wrap="word")
texto_resultado.pack(pady=10)
texto_resultado.config(state=tk.DISABLED)

# Iniciar ventana
ventana.mainloop()