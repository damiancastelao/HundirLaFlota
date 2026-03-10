class Nave:
    def __init__(self, nombre, tamano):
        self.nombre = nombre
        self.vida = tamano
        self.TOCADO = 1
        self.HUNDIDO = 2

    def recibir_disparo(self):
        return self.TOCADO
