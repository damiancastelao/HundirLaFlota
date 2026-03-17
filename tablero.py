from nave import Nave


class Tablero:
    def __init__(self, tamanho=10):
        # self.tamanho = tamanho

        self.AGUA = 0
        self.TOCADO = 1
        self.HUNDIDO = 2
        # Creamos una nave de ejemplo
        por1 = Nave("Destructor", "portaaviones", 5)
        fra1 = Nave("Bismarck", "fragata", 3)
        fra2 = Nave("Prince of Wales", "fragata", 3)
        fra3 = Nave("Graf Spee", "fragata", 3)

        sub1 = Nave("U-47", "submarino", 1)
        sub2 = Nave("U-96", "submarino", 1)
        sub3 = Nave("U-505", "submarino", 1)
        sub4 = Nave("U-534", "submarino", 1)

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

    def comprobar_impacto(self, x, y):
        print("Estoy comprobando el impacto")
        nave = self.casillero[x][y]
        if nave is None:
            return self.AGUA
        else:
            return nave.recibir_disparo()

