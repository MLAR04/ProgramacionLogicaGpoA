def diagnosticar(sintomas_paciente):
    Enfermedades = {
        "Gripe": {"dolor de cabeza", "tos"},
        "Covid": {"fiebre", "tos", "perdida de olfato", "cansancio"},
        "Migraña": {"nauseas", "dolor de cabeza"},
        "Resfriado": {"fiebre", "tos", "congestion nasal"}
    }

    if not sintomas_paciente:
        return "No se proporcionaron síntomas para el diagnóstico."

    mejor_coincidencia = []
    max_puntuacion = 0

    for enfermedad, sintomas_enfermedad in Enfermedades.items():
        puntuacion_actual = len(sintomas_paciente.intersection(sintomas_enfermedad))

        if puntuacion_actual > max_puntuacion:
            max_puntuacion = puntuacion_actual
            mejor_coincidencia = [enfermedad]
        elif puntuacion_actual == max_puntuacion and puntuacion_actual > 0:
            mejor_coincidencia.append(enfermedad)

    if not mejor_coincidencia:
        return "Sus síntomas no coinciden claramente con una enfermedad específica. Es recomendable consultar a un médico."
    else:
        return f"Diagnóstico probable: {' o '.join(mejor_coincidencia)}."

# Consultas

sintomas1 = {"fiebre", "tos", "perdida de olfato"}
print(f"Síntomas: {sintomas1}\n{diagnosticar(sintomas1)}\n")

sintomas2 = {"dolor de cabeza"}
print(f"Síntomas: {sintomas2}\n{diagnosticar(sintomas2)}\n")

sintomas3 = {"fiebre", "tos"}
print(f"Síntomas: {sintomas3}\n{diagnosticar(sintomas3)}\n")

sintomas4 = {"dolor de estomago", "mareo"}
print(f"Síntomas: {sintomas4}\n{diagnosticar(sintomas4)}\n")

sintomas5 = {"nauseas", "dolor de cabeza"}
print(f"Síntomas: {sintomas5}\n{diagnosticar(sintomas5)}\n")