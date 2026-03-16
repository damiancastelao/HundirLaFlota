# Clase que representa una nave en el juego
class Nave:
    def __init__(self, nombre, tipo, vida):
        """
        Constructor de la clase Nave.
        
        Args:
            nombre (str): Nombre de la nave (string)
            tipo (str): Nombre del barco (submarino, fragata, portaaviones)
            vida (int): Tamaño de la nave (número de casillas que ocupa)
        """
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida

    def recibir_disparo(self):
        """
        Procesa el impacto de un disparo en la nave.
        Reduce la vida de la nave y devuelve el estado (Tocado/Hundido).
        
        Returns:
            str: Estado de la nave tras el disparo ("Tocado", "Hundido", etc.)
        """
        return ""