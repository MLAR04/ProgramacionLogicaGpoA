import json
import random
import os


class AgenteQLearning:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.1, archivo="qtable.json"):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.archivo = archivo
        self.q_table = self.cargar_qtable()

    def cargar_qtable(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                return json.load(f)
        return {}

    def guardar_qtable(self):
        with open(self.archivo, "w") as f:
            json.dump(self.q_table, f)

    def obtener_estado(self, tablero):
        return str(tablero)

    def elegir_accion(self, estado, acciones_validas):
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(acciones_validas)

        valores = [self.q_table.get(estado, {}).get(str(a), 0) for a in acciones_validas]
        max_valor = max(valores)
        return acciones_validas[valores.index(max_valor)]

    def actualizar_q(self, estado, accion, recompensa, siguiente_estado, acciones_validas):
        estado = str(estado)
        accion = str(accion)

        if estado not in self.q_table:
            self.q_table[estado] = {}

        valor_actual = self.q_table[estado].get(accion, 0)

        max_futuro = 0
        if siguiente_estado in self.q_table:
            max_futuro = max(self.q_table[siguiente_estado].values(), default=0)

        nuevo_valor = valor_actual + self.alpha * (recompensa + self.gamma * max_futuro - valor_actual)
        self.q_table[estado][accion] = nuevo_valor