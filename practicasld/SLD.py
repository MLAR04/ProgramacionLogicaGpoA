# ------------------------------------------------------------
# Resolución SLD (Selective Linear Definite-Clause Resolution)
# Tema: El Plato del Buen Comer
# Autora: Paola Josseline Acosta López
# ------------------------------------------------------------

# Paso 1: Base de conocimiento
base_de_conocimiento = [
    ("verdura(zanahoria)", True),
    ("verdura(espinaca)", True),
    ("verdura(jitomate)", True),
    ("verdura(pepino)", True),
    ("proteina(pollo)", True),
    ("proteina(pescado)", True),
    ("proteina(huevo)", True),
    ("cereal(arroz)", True),
    ("cereal(avena)", True),
    ("cereal(tortilla)", True),
    ("platillo_sano(X)", "verdura(X)"),
    ("platillo_sano(X)", "proteina(X)"),
    ("platillo_sano(X)", "cereal(X)")
]

# ------------------------------------------------------------
# Paso 2: Unificación
# ------------------------------------------------------------
def unificar(x, y, sustituciones=None):
    if sustituciones is None:
        sustituciones = {}
    if x == y:
        return sustituciones
    if isinstance(x, str) and x.islower() and len(x) == 1:  # variable (X)
        return unificar_variable(x, y, sustituciones)
    if isinstance(y, str) and y.islower() and len(y) == 1:
        return unificar_variable(y, x, sustituciones)
    if "(" in x and "(" in y:
        fx, argsx = x.split("(", 1)
        fy, argsy = y.split("(", 1)
        if fx != fy:
            return None
        argsx = argsx[:-1].split(",")
        argsy = argsy[:-1].split(",")
        for a, b in zip(argsx, argsy):
            sustituciones = unificar(a.strip(), b.strip(), sustituciones)
            if sustituciones is None:
                return None
        return sustituciones
    return None

def unificar_variable(var, val, sustituciones):
    if var in sustituciones:
        return unificar(sustituciones[var], val, sustituciones)
    elif val in sustituciones:
        return unificar(var, sustituciones[val], sustituciones)
    else:
        sustituciones[var] = val
        return sustituciones

# ------------------------------------------------------------
# Paso 3: Resolución SLD
# ------------------------------------------------------------
def resolucion_sld(consulta, base_de_conocimiento):
    print(f"\nConsulta: {consulta}")
    for cabeza, cuerpo in base_de_conocimiento:
        if cuerpo is not True:  # regla
            sustituciones = unificar(cabeza, consulta)
            if sustituciones:
                print(f"Unificando {consulta} con {cabeza} → {sustituciones}")
                nueva_consulta = cuerpo
                for var, val in sustituciones.items():
                    nueva_consulta = nueva_consulta.replace(var, val)
                return resolucion_sld(nueva_consulta, base_de_conocimiento)
        else:  # hecho simple
            if unificar(cabeza, consulta):
                print(f"Hecho encontrado: {cabeza}")
                return True
    return False

# ------------------------------------------------------------
# Programa principal
# ------------------------------------------------------------
if __name__ == "__main__":
    print("=== Sistema de Resolución SLD: El Plato del Buen Comer ===")
    alimento = input("Ingrese un alimento: ").strip().lower()
    consulta = f"platillo_sano({alimento})"
    resultado = resolucion_sld(consulta, base_de_conocimiento)

    print("\nResultado final:")
    if resultado:
        print(f"El alimento '{alimento}' forma parte de un platillo sano.")
    else:
        print(f" El alimento '{alimento}' no pertenece al Plato del Buen Comer.")
