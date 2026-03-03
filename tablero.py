# Clase que representa el tablero del juego
class Tablero:
    def __init__(self, tamano=10):
        """
        Constructor de la clase Tablero.
        Inicializa una matriz de casillas vacía (sin naves).
        Las naves se colocan posteriormente usando el método colocar_nave().

        Args:
            tamano (int): Dimensión del tablero (por defecto 10x10)
        """
        pass

    def colocar_nave(self, nave, x, y, orientacion):
        """
        Coloca una nave en el tablero en las coordenadas especificadas.
        Marca las casillas ocupadas por la nave según su tamaño y orientación.

        Args:
            nave (Nave): Objeto nave a colocar
            x (int): Coordenada X inicial (fila)
            y (int): Coordenada Y inicial (columna)
            orientacion (str): Orientación de la nave
                              "H" para horizontal (expande en columnas)
                              "V" para vertical (expande en filas)

        Example:
            tablero.colocar_nave(submarino, 0, 0, "H")  # Coloca horizontalmente desde (0,0)
            tablero.colocar_nave(buque, 5, 3, "V")      # Coloca verticalmente desde (5,3)
        """
        pass
    
    def comprobar_impacto(self, x, y):
        """
        Comprueba si hay una nave en las coordenadas indicadas.
        Si hay nave, llama a su método recibir_disparo().

        Args:
            x (int): Coordenada X del disparo
            y (int): Coordenada Y del disparo

        Returns:
            str: Resultado del disparo ("Agua", "Tocado", "Hundido")
        """
        return ""
