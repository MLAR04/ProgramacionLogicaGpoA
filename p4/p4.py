## P4 - González Navarro Oscar Eduardo

## "Un número es múltiplo de 6 si es divisible entre 2 y 3"

x = 12

def multiplos (x):

    if (x % 3 == 0 and x % 2 == 0 ):
        return print("El número: ",x," Es múltiplo de 6")
    
"Una persona puede votar si tiene más de 18 anios, tiene credencial de elector y está en la lista nominal"

lista_nominal = {
    'juan' : {
        'edad': 19,
        'credencial' : True
    },
    'pedro' : {
        'edad': 16,
        'credencial' : False
    },
    'jesus' : {
        'edad': 20,
        'credencial': False
    }
}

def puede_votar(lista_n):

    for persona in lista_n:

        if (persona in lista_n and
            lista_n[persona]['edad'] >= 18 and
            lista_n[persona]['credencial'] == True):

            print('Puede votar')

"Una computadora puede conectarse a internet si tiene wifi conectado o cable Ethernet conectado y además el módem funciona"

red_casa = {
    'PC1': {
        'Ethernet' : True,
        'Wi-fi' : False
    },
    'PC2' : {
        'Ethernet' : False,
        'Wi-fi': True
    },
    'PC3' : {
        'Ethernet' : False,
        'Wi-fi' : False
    }
}

def tiene_internet(lista_red):

    for pc in lista_red:

        if (pc in lista_red and (
                                lista_red[pc]['Ethernet'] == True
                                or
                                lista_red[pc]['Wi-fi'] == True
                                )
            ) :

            print('Tiene internet')


if __name__ == '__main__':

    multiplos(x)

    puede_votar(lista_nominal)

    tiene_internet(red_casa)