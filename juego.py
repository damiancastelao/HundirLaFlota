# Clase principal que gestiona el juego
class Juego:
    def __init__(self):
        """
        Constructor de la clase Juego.
        Inicializa el tablero y las naves del juego.
        """
        pass

    def inicializar_naves(self):
        """
        Crea e inicializa todas las naves del juego.
        Coloca las naves en el tablero en posiciones predefinidas.
        """
        pass
    
    def mostrar_resultado(self, resultado):
        """
        Muestra por pantalla el resultado de un disparo.

        Args:
            resultado (str): Resultado del disparo ("Agua", "Tocado", "Hundido")
        """
        pass

    def lanzar_ataque(self, x, y):
        """
        Ejecuta un disparo en las coordenadas indicadas.
        Si impacta una nave y su vida llega a cero, muestra mensaje de hundimiento.

        Args:
            x (int): Coordenada X del disparo
            y (int): Coordenada Y del disparo
        """
        pass
