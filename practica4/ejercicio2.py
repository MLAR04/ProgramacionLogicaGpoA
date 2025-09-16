def evaluar_voto(mayor18, tiene_credencial, en_lista):
    R1 = mayor18          
    R2 = tiene_credencial 
    R3 = en_lista         
    PuedeVotar = R1 and R2 and R3  
    return R1, R2, R3, PuedeVotar

casos = [
    (True, True, True),
    (True, True, False),
    (True, False, True),
    (True, False, False),
    (False, True, True),
    (False, True, False),
    (False, False, True),
    (False, False, False)
]

print("R1 (Mayor 18) | R2 (Credencial) | R3 (Lista) | Puede votar")
for caso in casos:
    R1, R2, R3, PV = evaluar_voto(*caso)
    R1v, R2v, R3v, PVv = ('V' if x else 'F' for x in [R1, R2, R3, PV])
    print(f"      {R1v}       |       {R2v}       |     {R3v}     |     {PVv}")
