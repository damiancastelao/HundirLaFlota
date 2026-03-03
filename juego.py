from tablero import Tablero
from nave import Nave

class Juego:
    def __init__(self):
        self.tablero = Tablero()

    def inicializar_naves(self):
        n1 = Nave("Acorazado", 4)
        n2 = Nave("Destructor", 3)
        self.tablero.colocar_nave(n1, 0, 0, True)
        self.tablero.colocar_nave(n2, 2, 2, False)

    def lanzar_ataque(self, x, y):
        return self.tablero.comprobar_impacto(x, y)

    def mostrar_resultado(self, resultado):
        estado, nombre = resultado
        if estado == "Hundido":
            print(f"¡Hundido! Has destruido el {nombre}")
        else:
            print(estado)