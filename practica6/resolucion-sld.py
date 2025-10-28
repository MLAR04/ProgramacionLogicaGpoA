def unify(x, y, subs=None):
    subs = subs or {}
    if x == y: return subs
    if isinstance(x, str) and x[0].isupper():
        return unify(subs.get(x, y), y, {**subs, x: y}) if x not in subs else unify(subs[x], y, subs)
    if isinstance(y, str) and y[0].isupper(): return unify(y, x, subs)
    if isinstance(x, tuple) and isinstance(y, tuple) and len(x) == len(y):
        for a, b in zip(x, y):
            subs = unify(a, b, subs)
            if subs is None: return None
        return subs
    return None


def sld_resolution(goal, kb, subs=None):
    subs = subs or {}
    for head, args, body in kb:
        new_subs = unify((head, args), goal, subs.copy())
        if not new_subs: continue
        if not body: yield new_subs
        else:
            curr = new_subs
            for pred, arg in body:
                new_goal = (pred, tuple(curr.get(a, a) for a in arg))
                res = list(sld_resolution(new_goal, kb, curr))
                if not res: break
                curr = res[0]
            else: yield curr


def main():
    print("\nBienvenido al sistema del Plato del Buen Comer")

    grupos = {
        "frutas": ["sandia","platano","uvas","papaya","mango","durazno","manzana","fresas","guayaba"],
        "verduras": ["tomate","lechuga","nopal","calabaza","apio","zanahoria","chile"],
        "leguminosas": ["frijol","garbanzo","lenteja","haba","alubia"],
        "cereales": ["maiz","trigo","arroz","avena"],
        "productos_de_origen_animal": ["pollo","pescado","huevo","queso","leche","carne"]
    }

    for g, lista in grupos.items():
        print(f"\n{g.capitalize()} disponibles:\n" + ", ".join(lista))

    comidos = [c.strip() for c in input(
        "\nEscribe los alimentos que comiste (ej: manzana, arroz, pollo): "
    ).lower().split(",") if c.strip()]

    kb = [("healthy", ("persona",), [("eat", ("persona","frutas")),
                                     ("eat", ("persona","verduras")),
                                     ("eat", ("persona","cereales"))])]

    for grupo, alimentos in grupos.items():
        if any(a in comidos for a in alimentos):
            kb.append(("eat", ("persona", grupo), []))

    solutions = list(sld_resolution(("healthy", ("persona",)), kb))
    
    print("\n--------------------------------------")
    if solutions:
        print("Tu alimentacion fue saludable hoy.")
    else:
        faltan = [g for g in ["frutas","verduras","cereales"] if not any(a in comidos for a in grupos[g])]
        print("Te falto comer: " + ", ".join(faltan) + "." if faltan else
              "Comiste algunos grupos, pero no todos los esenciales.")
    print("--------------------------------------")


if __name__ == "__main__":
    main()

