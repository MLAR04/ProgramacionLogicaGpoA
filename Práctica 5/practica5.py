'''
Aquí hay que hacer un programa que pueda diagnosticar las enfermedades
deacuerdo a los síntomas.
'''
import argparse

enfermedades = {
    "gripe": ["dolor de cabeza","tos"],
    "covid": ["perdida de olfato","cansancio","tos","fiebre"],
    "migraña" :["dolor de cabeza","nauseas"],
    "resfriado":["congestion nasal","tos","fiebre"]
}

def diagnosticar(sintomas_usuario):
    mejor_coincidencia = None
    max_coincidencias = 0
    
    for enfermedad, sintomas in enfermedades.items():
        coincidencias = sum(1 for sintoma in sintomas if sintoma in sintomas_usuario)
        if coincidencias > max_coincidencias:
            max_coincidencias = coincidencias
            mejor_coincidencia = enfermedad
        elif coincidencias == max_coincidencias and coincidencias > 0:
            mejor_coincidencia = None 
    
    return mejor_coincidencia if max_coincidencias > 0 else "No se pudo diagnosticar"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Diagnosticar enfermedades basado en síntomas')
    parser.add_argument('sintomas', nargs='+', help='Lista de síntomas separados por espacios')
    
    args = parser.parse_args()
    sintomas_usuario = args.sintomas
    
    resultado = diagnosticar(sintomas_usuario)
    print(f"Síntomas ingresados: {', '.join(sintomas_usuario)}")
    print(f"Diagnóstico: {resultado}")
