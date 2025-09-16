def es_multiplo(number):
    if number % 2 == 0 and number % 3 == 0:
        return True
    return False

lista_nominal = ['juan','pedro','juanito']

personas = {'juan':{'edad':18,'credencial':True},
            'pedro':{'edad':16,'credencial':False},
            'garo':{'edad':18,'credencial':False}
            }

def puede_votar(name):
    if name in lista_nominal and personas[name]['edad'] >= 18 and personas[name]['credencial'] == True:
        return True
    return False

def puede_conectarse(wifi,ethernet,modem):
    if wifi or ethernet and modem:
        return True
    return False

print('6 es multiplo de 6:',es_multiplo(6))
print('4 es multiplo de 6:',es_multiplo(4))
print('2 es multiplo de 6:',es_multiplo(2))

print('Juan puede votar: ',puede_votar('juan'))
print('Pedro puede votar: ',puede_votar('pedro'))
print('Garo puede votar: ',puede_votar('Garo'))

print('La computadora de Juan puede contarse a internet: ',puede_conectarse(True,False,True))
print('La computadora de Pedro puede contarse a internet: ',puede_conectarse(False,False,True))
print('La computadora de Pedrito puede contarse a internet: ',puede_conectarse(True,True,True))