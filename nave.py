class Nave:
    def __init__(self, nombre, tipo, vida):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida

    def recibir_disparo(self):
        self.vida -= 1
        if self.vida > 0:
            return 1
        else:
            return 2