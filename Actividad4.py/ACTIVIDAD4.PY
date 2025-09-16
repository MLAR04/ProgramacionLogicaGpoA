
# EJERCICIO 1: Múltiplo de 6
# ============================================

def es_multiplo_de_6(x):
    return (x % 2 == 0) and (x % 3 == 0)

print("==== TABLA DE VERDAD: Múltiplo de 6 ====")
print("P (divisible entre 2) | Q (divisible entre 3) | R (múltiplo de 6)")
valores = [(True, True), (True, False), (False, True), (False, False)]
for p, q in valores:
    r = p and q
    print(f"{p:<23} {q:<25} {r}")
print()


# EJERCICIO 2: Puede votar
# ============================================

def puede_votar(edad, tiene_credencial, en_lista):
    return (edad > 18) and tiene_credencial and en_lista

print("==== TABLA DE VERDAD: Puede Votar ====")
print("A (>18 años) | B (credencial) | C (lista nominal) | V (puede votar)")
valores = [(a, b, c) for a in [True, False] for b in [True, False] for c in [True, False]]
for a, b, c in valores:
    v = a and b and c
    print(f"{a:<13} {b:<14} {c:<18} {v}")
print()



# EJERCICIO 3: Conexión a Internet
# ============================================

def conexion_internet(wifi, ethernet, modem):
    return (wifi or ethernet) and modem

print("==== TABLA DE VERDAD: Conexión a Internet ====")
print("W (Wi-Fi) | E (Ethernet) | M (módem) | C (conexión)")
valores = [(w, e, m) for w in [True, False] for e in [True, False] for m in [True, False]]
for w, e, m in valores:
    c = (w or e) and m
    print(f"{w:<10} {e:<12} {m:<9} {c}")
print()



