# Clase principal que gestiona el juego
from obsoletos.objetos import Juego
from tablero import Tablero

class Juego:
    def __init__(self):
        """
        Constructor de la clase Juego.
        Inicializa el tablero y las naves del juego.
        """
        self.lanzar_ataque(1,1)
        self.lanzar_ataque(4,0)
        self.lanzar_ataque(7,6)


    def inicializar_naves(self):
        """
        Crea e inicializa todas las naves del juego.
        Coloca las naves en el tablero en posiciones predefinidas.
        """

    
    def mostrar_resultado(self, resultado: int):
        """
        Muestra por pantalla el resultado de un disparo.

        Args:
            resultado (str): Resultado del disparo ("Agua", "Tocado", "Hundido")
        """
        if resultado == 0:
            print("Agua")
        elif resultado == 1:
            print("Tocado")
        elif resultado == 2:
            print("Hundido")

    def lanzar_ataque(self, x, y):
        """
        Ejecuta un disparo en las coordenadas indicadas.
        Si impacta una nave y su vida llega a cero, muestra mensaje de hundimiento.

        Args:
            x (int): Coordenada X del disparo
            y (int): Coordenada Y del disparo
        """
        print(f"Atacando a  {x}, {y} ")
        obj_tablero = Tablero()
        resultado = obj_tablero.comprobar_impacto(x,y)
        self.mostrar_resultado(resultado)


if __name__ == "__main__":
        Juego()

