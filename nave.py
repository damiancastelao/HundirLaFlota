class Nave:
    def __init__(self, nombre, tamano):
        self.nombre = nombre
        self.vida = tamano

    def recibir_disparo(self):
        self.vida -= 1
        return "Hundido" if self.vida == 0 else "Tocado"