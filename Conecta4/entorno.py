import numpy as np

FILAS = 6
COLUMNAS = 7

class Conecta4:
    def __init__(self):
        self.tablero = np.zeros((FILAS, COLUMNAS), dtype=int)

    def reiniciar(self):
        self.tablero = np.zeros((FILAS, COLUMNAS), dtype=int)

    def acciones_validas(self):
        return [c for c in range(COLUMNAS) if self.tablero[0][c] == 0]

    def jugar(self, columna, jugador):
        for fila in reversed(range(FILAS)):
            if self.tablero[fila][columna] == 0:
                self.tablero[fila][columna] = jugador
                return True
        return False

    def verificar_ganador(self, jugador):
        # Horizontal
        for f in range(FILAS):
            for c in range(COLUMNAS-3):
                if all(self.tablero[f][c+i] == jugador for i in range(4)):
                    return True

        # Vertical
        for f in range(FILAS-3):
            for c in range(COLUMNAS):
                if all(self.tablero[f+i][c] == jugador for i in range(4)):
                    return True

        # Diagonal
        for f in range(FILAS-3):
            for c in range(COLUMNAS-3):
                if all(self.tablero[f+i][c+i] == jugador for i in range(4)):
                    return True

        for f in range(3, FILAS):
            for c in range(COLUMNAS-3):
                if all(self.tablero[f-i][c+i] == jugador for i in range(4)):
                    return True

        return False

    def empate(self):
        return all(self.tablero[0] != 0)