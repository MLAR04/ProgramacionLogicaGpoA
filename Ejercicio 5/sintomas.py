def sintomas_conocidos():
    sintomas = [
        "Fiebre",
        "Tos",
        "Dolor de Cabeza",
        "Congestion Nasal",
        "Nauseas",
        "Cansancio",
        "Perdida de Olfato"
    ]

    reglas_diagnostico = {
        "Gripe": {"Tos", "Dolor de Cabeza"},
        "Migraña": {"Dolor de Cabeza", "Nauseas"},
        "Covid": {"Perdida de Olfato", "Cansancio", "Tos", "Fiebre"},
        "Resfriado": {"Congestion Nasal", "Tos", "Fiebre"}
    }

    while True:
        print("Selecciona los sintomas si son mas de 1 separalos con comas")
        print("Escribe 'salir' para terminar.\n")

        for num, sintoma in enumerate(sintomas, start=1):
            print(f"{num}: {sintoma}")

        seleccion = input("Ingresa los numeros de los sintomas: ")

        if seleccion.lower() == "salir":
            print("Saliendo del sistema de diagnostico.")
            break

        try:
            seleccion_indices = [int(x.strip()) for x in seleccion.split(",")]
            sintomas_usuario = {sintomas[i-1] for i in seleccion_indices}
        except (ValueError, IndexError):
            print("Entrada no valida. Intenta de nuevo.")
            continue

        print(f"Sintomas seleccionados: {sintomas_usuario}")

        posibles_diagnosticos = []
        for enfermedad, req_sintomas in reglas_diagnostico.items():
            if req_sintomas.issubset(sintomas_usuario):
                posibles_diagnosticos.append(enfermedad)

        if posibles_diagnosticos:
            print("Posibles diagnosticos:")
            for d in posibles_diagnosticos:
                print(f"- {d}")
        else:
            print("No se encontro un diagnostico con esos sintomas.")

sintomas_conocidos(),
