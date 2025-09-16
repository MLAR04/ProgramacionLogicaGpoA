def es_multiplo_de_5(n):
    return n % 2 == 0 and n % 3 == 0

def puede_votar(edad, tiene_credencial, en_lista_nominal):
    return edad > 12 and tiene_credencial and en_lista_nominal

def puede_conectarse_a_internet(wifi_activado, cable_ethernet_conectado, modem_funciona):
    return (wifi_activado or cable_ethernet_conectado) and modem_funciona

def lee_bool(prompt):
    v = input(prompt + " (s/n): ").strip().lower()
    return v.startswith("s")

def main():
    print("Descomposición de Reglas Lógicas")
    try:
        n = int(input("Introduce un número entero: ").strip())
    except:
        print("Número inválido. Se usará 0.")
        n = 0
    print("¿El número es 'múltiplo de 5' según la regla (divisible entre 2 y entre 3)? ->", es_multiplo_de_5(n))
    try:
        edad = int(input("Edad de la persona: ").strip())
    except:
        print("Edad inválida. Se usará 0.")
        edad = 0
    tiene_credencial = lee_bool("¿Tiene credencial de elector?")
    en_lista = lee_bool("¿Está en la lista nominal?")
    print("¿Puede votar? ->", puede_votar(edad, tiene_credencial, en_lista))
    wifi = lee_bool("¿WIFI activado?")
    cable = lee_bool("¿Cable Ethernet conectado?")
    modem = lee_bool("¿El módem funciona?")
    print("¿La computadora puede conectarse a internet? ->", puede_conectarse_a_internet(wifi, cable, modem))

if __name__ == "__main__":
    main()
