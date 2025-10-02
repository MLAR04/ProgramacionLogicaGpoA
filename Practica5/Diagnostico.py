
def diagnosticar(sintomas):
    enfermedades = {
        "Gripe": {"tos", "dolor de cabeza"},
        "Covid": {"perdida de olfato", "cansancio", "tos", "fiebre"},
        "Migraña": {"nauseas", "dolor de cabeza"},
        "Resfriado": {"congestion nasal", "tos", "fiebre"}
    }

    diagnosticos = []

    for enfermedad, req_sintomas in enfermedades.items():
        if req_sintomas.issubset(sintomas):
            diagnosticos.append(enfermedad)

    return diagnosticos




# Programa principal
print("=== Sistema Experto de Diagnóstico de Enfermedades Comunes ===")
print("Escribe tus síntomas separados por coma (Sintomas disponibles: tos, dolor de cabeza, cansancio, perdida de olfato, fiebre, nauseas, congestion nasal)")
entrada = input("Ingresa todos tus síntomas: ").lower()

# Convertir en conjunto de síntomas
sintomas_usuario = {s.strip() for s in entrada.split(",")}


# Obtener diagnóstico
resultado = diagnosticar(sintomas_usuario)

if resultado:
    print("\nPosibles diagnósticos:")
    for enf in resultado:
        print(f"- {enf}")
else:
    print("\nNo se encontró una enfermedad exacta con esos síntomas.")
