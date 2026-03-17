from tablero import Tablero


class Juego:
    def __init__(self):
        self.lanzar_ataque(4,2)


    def inicializar_naves(self):
        pass

    def mostrar_resultado(self, resultado):
        if resultado == 0:
            print("Agua")
        elif resultado == 1:
            print("Tocado")
        elif resultado == 2:
            print("HundidO")

    def lanzar_ataque(self, x, y):
        print(f"Atacando {x}, {y}")
        obj_tablero = Tablero()
        resultado = obj_tablero.comprobar_impacto(x, y)
        self.mostrar_resultado(resultado)

if __name__ == '__main__':
    Juego()