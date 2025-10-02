# Enfermedades.py

enfermedades = {
    "gripe": {"dolor de cabeza", "tos"},
    "covid": {"perdida de olfato", "cansancio", "tos", "fiebre"},
    "migraña": {"nauseas", "dolor de cabeza"},
    "resfriado": {"congestión nasal", "tos", "fiebre"}
}

def diagnosticar(sintomas_usuario):
    sintomas_usuario = set(sintomas_usuario)

    # Reglas
    for enfermedad, sintomas in enfermedades.items():
        if sintomas_usuario == sintomas:
            return f"Usted tiene {enfermedad}"

    # Si no coincide con ninguna enfermedad registrada
    return "Te vas a morir we"

if __name__ == "__main__":
    print("=== Motor de Inferencia: Diagnóstico de Enfermedades ===")
    print("Enfermedades disponibles:", ", ".join(enfermedades.keys()))
    print("Síntomas posibles:", ", ".join({s for lista in enfermedades.values() for s in lista}))
    print("Ingrese sus síntomas separados por comas:\n")

    entrada = input("Síntomas: ").lower()
    sintomas_usuario = [s.strip() for s in entrada.split(",")]

    resultado = diagnosticar(sintomas_usuario)
    print("\n>>>", resultado)
