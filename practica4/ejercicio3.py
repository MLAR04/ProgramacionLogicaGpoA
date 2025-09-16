
def evaluar_conexion(wifi, cable, modem):
    R1 = wifi             
    R2 = cable            
    R3 = modem            
    PuedeConectarse = R1 or (R2 and R3)  
    return R1, R2, R3, PuedeConectarse

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

print("WiFi | Cable Ethernet | Modem | Puede conectarse")
for caso in casos:
    R1, R2, R3, PC = evaluar_conexion(*caso)
 
    R1v, R2v, R3v, PCv = ('V' if x else 'F' for x in [R1, R2, R3, PC])
    print(f" {R1v}  |       {R2v}       |   {R3v}   |       {PCv}")
