
def evaluar_multiplo(numero):
    R2 = numero % 2 == 0      
    R3 = numero % 3 == 0      
    R1 = R2 and R3             
    EsMultiplo = R1            
    return R1, R2, R3, EsMultiplo

numeros = [6, 4, 3, 1]

print(" | R1 (Múltiplo) | R2 (Div 2) | R3 (Div 3) | Es múltiplo")
for n in numeros:
    R1, R2, R3, EsMultiplo = evaluar_multiplo(n)

    R1v, R2v, R3v, EMv = ('V' if R else 'F' for R in [R1, R2, R3, EsMultiplo])
    print(f"  {n}    |     {R1v}       |    {R2v}     |    {R3v}     |     {EMv}")
