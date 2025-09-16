'''
Predicado: Una computadora puede conectarse a internet si tiene wifi activado o cable ethernet conectado y además el módem funciona
'''
def internet(w,e,m):
    if w or e and m:
        print("\nBienvenido al internet")
    else:
        print("\nError 404 :(")

if __name__ == "__main__":
    wifi = int(input("¿Tiene el wifi activado? (1 para sí, 0 para no): "))
    ethernet = int(input("¿Tiene el cable ethernet conectado? (1 para sí, 0 para no): "))
    modem = int(input("¿El módem está activo? (1 para sí, 0 para no): "))

    internet(wifi,ethernet,modem)
