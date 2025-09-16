""" Juan Antonio Roman Castro Práctica 4  
Una computadora puede conectarse a internet si tiene wifi 
activado o cable de ethernet conectado y además el modem funciona."""

def problema(r1,r2,r3):
    if (r1 == "si" or r2 == "si") and r3 == "si":
        return "La computadora está conectada a internet"
    return "La computadora no está conectada a internet"

if __name__ == "__main__":
    print(
        problema(
            input("¿Tiene el wifi activado? (Si o no)\n").lower().strip(),
            input("¿Tiene el cable ethernet conectado? (Si o no)\n").lower().strip(),
            input("¿El modem funciona? (Si o no)\n").lower().strip()
            )
        )
