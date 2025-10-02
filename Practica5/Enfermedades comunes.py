
ENFERMEDADES: dict[str, tuple[str, ...]] = {
    "gripe": ("tos", "dolor_de_cabeza"),
    "covid": ("perdida_de_olfato", "cansancio", "tos", "fiebre"),
    "migraña": ("nauseas", "dolor_de_cabeza"),
    "resfriado": ("congestion_nasal", "tos", "fiebre")
}

def aplicar_reglas(sintomas: set[str], temperatura_alta: bool, reglas: list) -> set[str]:
    """
    Función recursiva que aplica reglas al conjunto de síntomas.
    """
    if not reglas:  
        return sintomas

    regla, *resto = reglas

    nuevo_sintomas = regla(sintomas, temperatura_alta)
    return aplicar_reglas(nuevo_sintomas, temperatura_alta, resto)

def regla1(sintomas: set[str], _: bool) -> set[str]:

    if "tos" in sintomas and "dolor_de_cabeza" in sintomas:
        sintomas = sintomas.union(ENFERMEDADES["gripe"])
    return sintomas

def regla2(sintomas: set[str], _: bool) -> set[str]:

    if "nauseas" in sintomas and "dolor_de_cabeza" in sintomas:
        sintomas = sintomas.union(ENFERMEDADES["migraña"])
    return sintomas

def regla3(sintomas: set[str], _: bool) -> set[str]:

    if "perdida_de_olfato" in sintomas:
        sintomas = sintomas.union(ENFERMEDADES["covid"])
    return sintomas

def regla4(sintomas: set[str], _: bool) -> set[str]:

    if "congestion_nasal" in sintomas:
        sintomas = sintomas.union(ENFERMEDADES["resfriado"])
    return sintomas

def regla5(sintomas: set[str], temperatura_alta: bool) -> set[str]:

    if temperatura_alta:
        sintomas = sintomas.union({"fiebre"})
    return sintomas

def diagnosticar(sintomas: set[str], temperatura_alta: bool = False) -> str:
    reglas = [regla1, regla2, regla3, regla4, regla5]

    sintomas_procesados = aplicar_reglas(sintomas, temperatura_alta, reglas)

    for enfermedad, sintomas_necesarios in ENFERMEDADES.items():
        if all(s in sintomas_procesados for s in sintomas_necesarios):
            return f"Posible diagnóstico: {enfermedad.capitalize()}"

    return "No se pudo determinar un diagnóstico con certeza."

print(diagnosticar({"tos", "dolor_de_cabeza"}))  

print(diagnosticar({"nauseas", "dolor_de_cabeza"}))  

print(diagnosticar({"perdida_de_olfato"}))  

print(diagnosticar({"congestion_nasal", "tos"}, temperatura_alta=True))  

