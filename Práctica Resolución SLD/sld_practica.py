# Práctica de SLD: Plato del Buen Comer - Jesús Martínez 22760568

# Definiciones de la Base de Conocimiento

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

# Motor de Inferencia

# Función de unificación
def unificar(patron, hecho, sustituciones):

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
    nuevo_objetivo = []
    for termino in objetivo:
        t = termino
        while isinstance(t, str) and t.startswith("?") and t in sustituciones:
            t = sustituciones[t]
        nuevo_objetivo.append(t)
    return nuevo_objetivo

# Motor de resolución SLD
def sld(programa, query):
    pila = [([query], {}, [])] 
    contador_soluciones = 0 

    while pila:
        objetivos, sustituciones, ruta = pila.pop()
        
        if not objetivos:
            g1 = sustituciones.get("?G1")
            g2 = sustituciones.get("?G2")
            g3 = sustituciones.get("?G3")
            print(f"🔍 Probando combinación: {g1} {g2} {g3}")
            
            if g1 and g2 and g3 and len(set([g1, g2, g3])) < 3:
                continue

            contador_soluciones += 1
            print(f"\n✅ Derivación #{contador_soluciones}: {sustituciones}") 
            print("🧭 Ruta de derivación:")
            for paso in ruta:
                print(f"→ {paso} {{...}}") 
            
            return sustituciones 

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
                
                pila.append((nuevos_objetivos, nueva_sust, nueva_ruta))

    print("❌ No se pudo derivar el objetivo.")
    return None

# Ejecución
if __name__ == "__main__":
    programa = base_de_conocimiento()
    print("📚 Base de conocimiento cargada con", len(programa), "cláusulas.")

    print("\n🔎 Consulta: ¿comida1 es saludable?")
    resultado1 = sld(programa, ["saludable", "comida1"])

    print("\n🔎 Consulta: ¿comida2 es saludable?")
    resultado2 = sld(programa, ["saludable", "comida2"])