from obsoletos.objetos import Juego
from tablero import Tablero

class Juego:
    def __init__(self):
        self.obj_tablero = Tablero()
        self.lanzar_ataque(7, 1)
        self.lanzar_ataque(7, 2)
        self.lanzar_ataque(7, 3)

    def inicializar_naves(self):
        pass

    def mostrar_resultado(self, resultado: int):
        if resultado == 0:
            print("Agua")
        elif resultado == 1:
            print("Tocado")
        elif resultado == 2:
            print("Hundido")

    def lanzar_ataque(self, x, y):
        print(f"Atacando a  {x}, {y} ")
        resultado = self.obj_tablero.comprobar_impacto(x, y)
        self.mostrar_resultado(resultado)


if __name__ == "__main__":
    Juego()