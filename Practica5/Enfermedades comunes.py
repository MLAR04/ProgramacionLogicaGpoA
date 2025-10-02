import unicodedata

class MotorInferencia:
    def __init__(self):
        self.enfermedades = { "gripe": ["fiebre", "tos", "dolor de cabeza", "congestión nasal", "cansancio"],
            "migraña": ["náuseas", "dolor de cabeza"],
            "covid": ["fiebre", "tos", "dolor de cabeza", "pérdida de olfato", "cansancio"],
            "resfriado": ["congestión nasal", "tos"] }
        
        self.reglas = [
            lambda sintomas: ["fiebre"] if "temperatura alta" in sintomas else [],
            lambda sintomas: ["gripe"] if self.tiene_sintomas(sintomas, ["tos", "dolor de cabeza"]) else [],
            lambda sintomas: ["migraña"] if self.tiene_sintomas(sintomas, ["náuseas", "dolor de cabeza"]) else [],
            lambda sintomas: ["covid"] if "pérdida de olfato" in sintomas else [],
            lambda sintomas: ["resfriado"] if "congestión nasal" in sintomas else []
        ]
    
    def normalizar_texto(self, texto):
        """Normaliza el texto para eliminar tildes y convertir a minúsculas"""
        texto = texto.lower()
        texto = unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode('utf-8')
        return texto
    
    def tiene_sintomas(self, sintomas_paciente, sintomas_requeridos):
        """Verifica si el paciente tiene todos los síntomas requeridos"""
        sintomas_paciente_normalizados = [self.normalizar_texto(s) for s in sintomas_paciente]
        sintomas_requeridos_normalizados = [self.normalizar_texto(s) for s in sintomas_requeridos]
        
        return all(sintoma in sintomas_paciente_normalizados for sintoma in sintomas_requeridos_normalizados)
    
    def diagnosticar(self, sintomas_paciente):
        """Realiza el diagnóstico basado en los síntomas del paciente"""
        diagnostico = []
        
        for regla in self.reglas:
            resultado = regla(sintomas_paciente)
            if resultado:
                diagnostico.extend(resultado)
        
        diagnostico = list(set(diagnostico))
       
        diagnostico_final = []
        for enfermedad in diagnostico:
            if self.tiene_sintomas(sintomas_paciente, self.enfermedades[enfermedad]):
                diagnostico_final.append(enfermedad)
        
        return diagnostico_final

def consultar_diagnostico():
    motor = MotorInferencia()
    
    print("Sistema de Diagnóstico de Enfermedades")
    print("======================================")
    print("Síntomas disponibles: fiebre, tos, dolor de cabeza, congestión nasal, náuseas, cansancio, pérdida de olfato, temperatura alta")
    print("Ingrese los síntomas separados por comas:")
    
    sintomas_input = input().strip()
    sintomas_paciente = [sintoma.strip() for sintoma in sintomas_input.split(",")]
    
    diagnostico = motor.diagnosticar(sintomas_paciente)
    
    if diagnostico:
        print(f"\nDiagnóstico: El paciente podría tener {', '.join(diagnostico)}")
    else:
        print("\nNo se pudo determinar un diagnóstico con los síntomas proporcionados.")

if __name__ == "__main__":
    sintomas_ejemplo = ["fiebre", "tos", "dolor de cabeza", "congestión nasal", "náuseas", "cansancio", "pérdida de olfato"]
    
    motor = MotorInferencia()
    diagnostico = motor.diagnosticar(sintomas_ejemplo)
    
    print(f"Síntomas: {', '.join(sintomas_ejemplo)}")
    print(f"Diagnóstico: {', '.join(diagnostico) if diagnostico else 'No se pudo determinar'}")
    
    print("\n" + "="*50)
    consultar_diagnostico()
