from nave import Nave

class Tablero:
    def __init__(self):
        self.AGUA = 0
        self.TOCADO = 1
        self.HUNDIDO = 2
        pass

    def colocar_nave(self, nave, x, y, orientacion):
        pass

    def comprobar_impacto(self, x ,y):
        print("(LOG) estoy en tablero comprobando el impacto")
        return self.TOCADO