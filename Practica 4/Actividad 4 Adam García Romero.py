def es_multiplo_de_6(num):
  
#Verifica si un número es múltiplo de 6.
 
  es_divisible_entre_2 = (num % 2 == 0)
  es_divisible_entre_3 = (num % 3 == 0)
  return es_divisible_entre_2 and es_divisible_entre_3

# Ejecucion
print(f"¿El número 30 es múltiplo de 6?: {es_multiplo_de_6(30)}")
print(f"¿El número 15 es múltiplo de 6?: {es_multiplo_de_6(15)}")
print(f"¿El número 8 es múltiplo de 6?: {es_multiplo_de_6(8)}")

def verificar_votantes(lista_personas):
#Evalúa una lista de personas para determinar quiénes pueden votar.
  votantes_aprobados = []
  for persona in lista_personas:
    if (persona['mayor_de_18'] and
        persona['tiene_credencial'] and
        persona['en_lista_nominal']):
      votantes_aprobados.append(persona['nombre'])
  return votantes_aprobados

# Lista de personas
personas = [
    {'nombre': 'Ana', 'mayor_de_18': True, 'tiene_credencial': True, 'en_lista_nominal': True},
    {'nombre': 'Luis', 'mayor_de_18': True, 'tiene_credencial': False, 'en_lista_nominal': True},
    {'nombre': 'Elena', 'mayor_de_18': False, 'tiene_credencial': True, 'en_lista_nominal': True},
    {'nombre': 'Carlos', 'mayor_de_18': True, 'tiene_credencial': True, 'en_lista_nominal': True},
    {'nombre': 'Sofia', 'mayor_de_18': True, 'tiene_credencial': True, 'en_lista_nominal': False}
]

# Ejecucion
personas_que_pueden_votar = verificar_votantes(personas)
print(f"Lista de personas que pueden votar: {personas_que_pueden_votar}")

def verificar_conexiones(lista_de_equipos):
#Verifica el estado de la conexión a internet de una lista de equipos.
  estado_conexion = {}
  for equipo in lista_de_equipos:
    puede_conectarse = ((equipo['wifi_activado'] or equipo['ethernet_conectado']) and
                        equipo['modem_funciona'])
    estado_conexion[equipo['nombre']] = puede_conectarse
  return estado_conexion

# Lista de computadoras
equipos = [
    {'nombre': 'Laptop-Oficina', 'wifi_activado': True, 'ethernet_conectado': False, 'modem_funciona': True},
    {'nombre': 'PC-Gamer', 'wifi_activado': False, 'ethernet_conectado': True, 'modem_funciona': True},
    {'nombre': 'Servidor', 'wifi_activado': False, 'ethernet_conectado': True, 'modem_funciona': False},
    {'nombre': 'Tablet', 'wifi_activado': True, 'ethernet_conectado': False, 'modem_funciona': False},
    {'nombre': 'PC-Vieja', 'wifi_activado': False, 'ethernet_conectado': False, 'modem_funciona': True}
]

# Ejecución
estatus_final = verificar_conexiones(equipos)
print("Estado de conexión de cada equipo:")
for nombre, conectado in estatus_final.items():
    print(f"- {nombre}: {'Conectado' if conectado else 'Desconectado'}")