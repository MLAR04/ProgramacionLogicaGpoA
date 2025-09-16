#Una persona puede votar si tiene más de 18 años, tiene credencial de elector y 
#está en la lista nominal

edad = input("Tienes 18 años o mas? (S/N) ").upper()
credencial = input("Tienes credencial de elector? (S/N) ").upper()
lista_nominal = input("Estas en la lista nominal (S/N) ").upper()

def puede_votar(x, y, z):
    return (x == "S") and (y == "S") and (z == "S")

print(puede_votar(edad, credencial, lista_nominal))