#Una computadora puede conectarse a internet si tiene wifi activado o
#cable de Ethernet conectado y además el modem funciona.

R1 = input("Tienes wifi? (S/N) ").upper()
R2 = input("Tienes Ethernet? (S/N) ").upper()
R3 = input("Funciona tu modem? (S/N) ").upper()

def te_puedes_conectar(x, y, z):
    return (x == "S" or y == "S") and z == "S"

print(te_puedes_conectar(R1, R2, R3))
