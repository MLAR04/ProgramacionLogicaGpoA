# Práctica de SLD: Plato del Buen Comer - Jesús Martínez 22760568

#Definiciones de Base de Conocimiento

def grupos():
    return [
        (["grupo", "frutas"], []),
        (["grupo", "verduras"], []),
        (["grupo", "cereales"], []),
        (["grupo", "leguminosas"], []),
        (["grupo", "origen_animal"], [])
    ]

def alimentos():
    return [
        (["alimento", "frutas", "manzana"], []),
        (["alimento", "frutas", "sandía"], []),
        (["alimento", "frutas", "plátano"], []),
        (["alimento", "verduras", "tomate"], []),
        (["alimento", "verduras", "lechuga"], []),
        (["alimento", "leguminosas", "frijol"], []),
        (["alimento", "origen_animal", "pollo"], []),
        (["alimento", "origen_animal", "pescado"], []),
        (["alimento", "cereales", "arroz"], []),
        (["alimento", "cereales", "maíz"], [])
    ]

def comidas():
    return [
        # Comida saludable
        (["comida", "comida1"], []),
        (["contiene", "comida1", "frutas"], []),
        (["contiene", "comida1", "verduras"], []),
        (["contiene", "comida1", "cereales"], []),

        # Comida no saludable
        (["comida", "comida2"], []),
        (["contiene", "comida2", "origen_animal"], []),
        (["contiene", "comida2", "cereales"], [])
    ]

def reglas():
    return [
        (["saludable", "?X"], [
            ["comida", "?X"],
            ["contiene", "?X", "?G1"],
            ["grupo", "?G1"],
            ["contiene", "?X", "?G2"],
            ["grupo", "?G2"],
            ["contiene", "?X", "?G3"],
            ["grupo", "?G3"]
        ])
    ]

def base_de_conocimiento():
    return grupos() + alimentos() + comidas() + reglas()


def unificar(patron, hecho, sustituciones):
    """Función de unificación."""
    nueva_sust = sustituciones.copy()
    pila = list(zip(patron, hecho))

    while pila:
        p, h = pila.pop()

        while isinstance(p, str) and p.startswith("?") and p in nueva_sust:
            p = nueva_sust[p]
        while isinstance(h, str) and h.startswith("?") and h in nueva_sust:
            h = nueva_sust[h]

        if p == h:
            continue
        elif isinstance(p, str) and p.startswith("?"):
            nueva_sust[p] = h
        elif isinstance(h, str) and h.startswith("?"):
            nueva_sust[h] = p
        elif isinstance(p, list) and isinstance(h, list) and len(p) == len(h):
            pila.extend(zip(p, h))
        else:
            return None

    return nueva_sust

def sustituir(objetivo, sustituciones):
    """Función de sustitución."""
    nuevo_objetivo = []
    for termino in objetivo:
        t = termino
        while isinstance(t, str) and t.startswith("?") and t in sustituciones:
            t = sustituciones[t]
        nuevo_objetivo.append(t)
    return nuevo_objetivo


def sld_recursivo(programa, query):

    contador_soluciones = 0


    def _solve(objetivos, sustituciones, ruta):

        nonlocal contador_soluciones

        if not objetivos:
            
            g1 = sustituciones.get("?G1")
            g2 = sustituciones.get("?G2")
            g3 = sustituciones.get("?G3")
            print(f"🔍 Probando combinación: {g1} {g2} {g3}")
            
            if g1 and g2 and g3 and len(set([g1, g2, g3])) < 3:
                return

            contador_soluciones += 1
            print(f"\n✅ Derivación #{contador_soluciones}: {sustituciones}")
            print("🧭 Ruta de derivación:")
            for paso in ruta:
                print(f"→ {paso} {{...}}")
            
            yield sustituciones  
            return
        objetivo_original = objetivos[0]
        resto_objetivos = objetivos[1:]
        
        objetivo_a_probar = sustituir(objetivo_original, sustituciones)

        for cabeza_original, cuerpo_original in programa:
            cabeza = cabeza_original[:]
            cuerpo = [c[:] for c in cuerpo_original] 

            nueva_sust = unificar(cabeza, objetivo_a_probar, sustituciones)
            
            if nueva_sust is not None:
                nuevos_objetivos = cuerpo + resto_objetivos
                nueva_ruta = ruta + [objetivo_a_probar]
                
                yield from _solve(nuevos_objetivos, nueva_sust, nueva_ruta)

    print(f"--- Iniciando motor recursivo para: {query} ---")

    soluciones_encontradas = list(_solve([query], {}, [])) 

    if not soluciones_encontradas:
        print("❌ No se pudo derivar el objetivo.")
        return None

    return soluciones_encontradas[0]

if __name__ == "__main__":
    programa = base_de_conocimiento()
    print("📚 Base de conocimiento cargada con", len(programa), "cláusulas.")

    print("\n🔎 Consulta: ¿comida1 es saludable?")
    resultado1 = sld_recursivo(programa, ["saludable", "comida1"])

    print("\n\n🔎 Consulta: ¿comida2 es saludable?")
    resultado2 = sld_recursivo(programa, ["saludable", "comida2"])
