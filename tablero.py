# Clase que representa el tablero del juego
from nave import Nave


class Tablero:

    def __init__(self, tamano=10):
        """
        Constructor de la clase Tablero.
        Inicializa una matriz de casillas vacía (sin naves).
        Las naves se colocan posteriormente usando el método colocar_nave().

        Args:
            tamano (int): Dimensión del tablero (por defecto 10x10)
        """
        self.AGUA = 0
        self.TOCADO = 1
        self.HUNDIDO = 2

        # Definir las naves por separado (4 submarinos, 3 fragatas, 1 portaaviones)
        # Estos objetos se definen una sola vez.
        por1 = Nave("Enterprise", "portaaviones", 5)

        fra1 = Nave("Bismarck", "fragata", 3)
        fra2 = Nave("Prince of Wales", "fragata", 3)
        fra3 = Nave("Graf Spee", "fragata", 3)

        sub1 = Nave("U-47", "submarino", 1)
        sub2 = Nave("U-96", "submarino", 1)
        sub3 = Nave("U-505", "submarino", 1)
        sub4 = Nave("U-534", "submarino", 1)

        # Aquí se podrían colocar las naves en el tablero usando el método colocar_nave()
        # pero por ahora vamos a definir directamente en el array de 10x10 (casillero) las posiciones de las naves para simplificar la implementación inicial.

        self.casillero = [
            [None, None, None, None, None, None, None, None, None, None],
            [None, por1, por1, por1, por1, por1, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, fra1, None, None, None, None, None, None],
            [None, None, None, fra1, None, None, sub1, None, None, None],
            [None, None, None, fra1, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, fra2, fra2, fra2, None, None, sub3, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, fra3, fra3, fra3, None, sub4, None, None, None, sub2]
        ]

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
        print(f"[LOG] estoy en tablero comprobando impacto ({x}, {y})")
        print(f"[LOG] casillero[{x}][{y}] = {self.casillero[x][y]}")
        if self.casillero[x][y] is None:
            print("[LOG] Agua")
        else:
            print(f"[LOG] {self.casillero[x][y].nombre} Tocado")
        return self.AGUA
