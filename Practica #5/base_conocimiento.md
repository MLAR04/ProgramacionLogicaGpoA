# 🧠 Sistema Experto de Diagnóstico Médico del Dr. Chuy

Este proyecto es una práctica de programación lógica que simula un sistema experto capaz de diagnosticar enfermedades comunes a partir de síntomas ingresados por el usuario. La interfaz está desarrollada en Python con `tkinter`, y el motor lógico se basa en reglas simples de inferencia.

## 📚 Base de Conocimiento

### 🔒 Leyes Lógicas

Estas reglas representan el conocimiento general sobre el estado de salud:

1. **Si te sientes mal, entonces estás enfermo.**  
   `sentirse_mal → enfermo`

2. **Si estás enfermo, entonces tienes síntomas.**  
   `enfermo → tiene_sintomas`

3. **Si tienes temperatura alta, entonces tienes fiebre.**  
   `temperatura_alta → fiebre`

### 🩺 Enfermedades y sus síntomas

| Enfermedad  | Síntomas asociados |
|-------------|--------------------|
| Gripe       | tos, dolor de cabeza |
| Covid       | fiebre, tos, cansancio, pérdida de olfato |
| Migraña     | dolor de cabeza, náuseas |
| Resfriado   | fiebre, tos, congestión nasal |

### 📖 Fuentes de referencia (formato APA)

- Organización Mundial de la Salud. (2021). *Guía sobre infecciones respiratorias*. OMS.
- Centers for Disease Control and Prevention. (2021). *Symptoms of COVID-19*. CDC.
- International Headache Society. (2018). *The International Classification of Headache Disorders (3rd ed.)*.
- Organización Mundial de la Salud. (2021). *Resfriado común*. OMS.

## 🧪 Lógica de Inferencia

El sistema compara los síntomas ingresados por el usuario con los síntomas conocidos de cada enfermedad. Se selecciona la enfermedad con **mayor número de coincidencias**. Si hay empate, se elige la primera en orden de evaluación.

## 🚀 Cómo ejecutar

1. Asegúrate de tener Python instalado.
2. Coloca el archivo `salud.png` en la misma carpeta que el script.
3. Ejecuta el archivo `.py` desde tu entorno de desarrollo o terminal.