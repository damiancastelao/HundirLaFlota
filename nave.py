# Clase que representa una nave en el juego
class Nave:
    def __init__(self, nombre, tamano):
        """
        Constructor de la clase Nave.
        
        Args:
            nombre (str): Nombre del barco (Submarino, Buque, Portaaviones)
            tamano (int): Tamaño de la nave (número de casillas que ocupa)
        """
        pass

    def recibir_disparo(self):
        """
        Procesa el impacto de un disparo en la nave.
        Reduce la vida de la nave y devuelve el estado (Tocado/Hundido).
        
        Returns:
            str: Estado de la nave tras el disparo ("Tocado", "Hundido", etc.)
        """
        return ""