
from tablero import Tablero

class Juego:
    def __init__(self):
        self.tablero = Tablero()

        self.lanzar_ataque(1, 0)
        self.lanzar_ataque(1, 0)
        self.lanzar_ataque(1, 1)
        self.lanzar_ataque(1, 2)
        self.lanzar_ataque(2, 1)
        self.lanzar_ataque(1, 4)

    def mostrar_resultado(self, resultado):
        if resultado == 0:
            print("Agua")
        elif resultado == 1:
            print("Tocado")
        elif resultado == 2:
            print("Hundido")

    def lanzar_ataque(self, x, y):
        print(f"Ataque a {x},{y}")

        casilla = self.tablero.casillero[x][y]

        resultado = casilla.recibir_disparo()

        if resultado is not None:
            self.mostrar_resultado(resultado)

juego = Juego()

