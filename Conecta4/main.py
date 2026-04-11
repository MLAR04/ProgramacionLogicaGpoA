from agente import AgenteQLearning
from entorno import Conecta4

def entrenar(episodios):
    agente = AgenteQLearning()
    juego = Conecta4()

    for ep in range(episodios):
        juego.reiniciar()
        estado = str(juego.tablero)

        while True:
            acciones = juego.acciones_validas()
            accion = agente.elegir_accion(estado, acciones)

            juego.jugar(accion, 1)

            siguiente_estado = str(juego.tablero)

            if juego.verificar_ganador(1):
                agente.actualizar_q(estado, accion, 1, siguiente_estado, acciones)
                break
            elif juego.empate():
                agente.actualizar_q(estado, accion, 0, siguiente_estado, acciones)
                break
            else:
                agente.actualizar_q(estado, accion, 0, siguiente_estado, acciones)

            estado = siguiente_estado

        print(f"Episodio {ep+1} terminado")

    agente.guardar_qtable()

if __name__ == "__main__":
    entrenar(1000)