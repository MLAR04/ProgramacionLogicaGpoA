import tkinter as tk
from entorno import Conecta4
from agente import AgenteQLearning
import time

TAM_CELDA = 80
FILAS = 6
COLUMNAS = 7

class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Conecta 4 con IA")

        self.juego = Conecta4()
        self.agente = AgenteQLearning(epsilon=0)

        # Puntaje
        self.puntaje_jugador = 0
        self.puntaje_ia = 0

        # Frame superior (botones + marcador)
        top_frame = tk.Frame(root)
        top_frame.pack()

        self.label_puntaje = tk.Label(top_frame, text=self.obtener_texto_puntaje(), font=("Arial", 14))
        self.label_puntaje.pack()

        # Botones de columnas
        botones_frame = tk.Frame(root)
        botones_frame.pack()

        for c in range(COLUMNAS):
            btn = tk.Button(botones_frame, text=f"↓ {c}", command=lambda col=c: self.jugar_turno(col))
            btn.grid(row=0, column=c)

        # Botón reiniciar
        tk.Button(root, text="Reiniciar", command=self.reiniciar_juego).pack(pady=5)

        # Canvas tablero
        self.canvas = tk.Canvas(root, width=COLUMNAS*TAM_CELDA, height=FILAS*TAM_CELDA)
        self.canvas.pack()

        self.dibujar_tablero()

    def obtener_texto_puntaje(self):
        return f"Jugador: {self.puntaje_jugador}  |  IA: {self.puntaje_ia}"

    def actualizar_puntaje(self):
        self.label_puntaje.config(text=self.obtener_texto_puntaje())

    def dibujar_tablero(self):
        self.canvas.delete("all")

        for f in range(FILAS):
            for c in range(COLUMNAS):
                x1 = c * TAM_CELDA
                y1 = f * TAM_CELDA
                x2 = x1 + TAM_CELDA
                y2 = y1 + TAM_CELDA

                self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue")

                valor = self.juego.tablero[f][c]

                color = "white"
                if valor == 1:
                    color = "red"
                elif valor == 2:
                    color = "yellow"

                self.canvas.create_oval(
                    x1+10, y1+10, x2-10, y2-10,
                    fill=color
                )

    def animar_caida(self, columna, jugador):
        for fila in range(FILAS):
            if self.juego.tablero[fila][columna] != 0:
                continue

            # Dibujar ficha en caída
            for paso in range(fila+1):
                self.dibujar_tablero()
                x1 = columna * TAM_CELDA
                y1 = paso * TAM_CELDA
                x2 = x1 + TAM_CELDA
                y2 = y1 + TAM_CELDA

                color = "red" if jugador == 1 else "yellow"

                self.canvas.create_oval(
                    x1+10, y1+10, x2-10, y2-10,
                    fill=color
                )
                self.root.update()
                time.sleep(0.05)

        # Colocar definitivamente
        self.juego.jugar(columna, jugador)

    def jugar_turno(self, columna):
        if columna not in self.juego.acciones_validas():
            return

        # Turno jugador
        self.animar_caida(columna, 1)

        if self.juego.verificar_ganador(1):
            self.puntaje_jugador += 1
            self.actualizar_puntaje()
            self.mostrar_mensaje("¡Ganaste!")
            return

        if self.juego.empate():
            self.mostrar_mensaje("Empate")
            return

        # Turno IA
        estado = str(self.juego.tablero)
        acciones = self.juego.acciones_validas()
        accion_ia = self.agente.elegir_accion(estado, acciones)

        self.animar_caida(accion_ia, 2)

        if self.juego.verificar_ganador(2):
            self.puntaje_ia += 1
            self.actualizar_puntaje()
            self.mostrar_mensaje("La IA ganó")
            return

        if self.juego.empate():
            self.mostrar_mensaje("Empate")
            return

    def mostrar_mensaje(self, texto):
        ventana = tk.Toplevel(self.root)
        ventana.title("Resultado")

        tk.Label(ventana, text=texto, font=("Arial", 20)).pack(pady=10)

        tk.Button(ventana, text="Jugar otra vez", command=lambda: [ventana.destroy(), self.reiniciar_juego()]).pack()
        tk.Button(ventana, text="Cerrar", command=ventana.destroy).pack()

    def reiniciar_juego(self):
        self.juego.reiniciar()
        self.dibujar_tablero()


if __name__ == "__main__":
    root = tk.Tk()
    app = Interfaz(root)
    root.mainloop()