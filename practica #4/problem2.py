""" Juan Antonio Roman Castro Práctica 4  
    Una persona puede votar si tiene más de 18 años y 
    tiene credencial de elector y está en la lista nominal."""

def problema(r1,r2,r3):
    if r1 == "si" and r2 == "si" and r3 == "si":
        return "Puedes votar"
    return "No puedes votar"

if __name__ == "__main__":
    print(
        problema(
            input("¿Tienes más de 18 años? (Si o no)\n").lower().strip(),
            input("¿Tienes credencial de elector? (Si o no)\n").lower().strip(),
            input("¿Estás en la lista nominal? (Si o no)\n").lower().strip()
            )
        )
