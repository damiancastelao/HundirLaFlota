class Nave:
    def __init__(self, nombre, tipo,vida):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida
        self.hundido = False
        self.TOCADO = 1
        self.HUNDIDO = 2

    def recibir_disparo(self):
        self.vida -= 1
        if self.vida <= 0:
            self.hundido = True
            print(f"{self.nombre} hundido")
            return self.HUNDIDO
        else:
            print(f"{self.nombre} tocado. Vida restante: {self.vida}")
            return self.TOCADO