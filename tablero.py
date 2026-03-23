from nave import Nave
from casilla import Casilla

class Tablero:
    def __init__(self, tamano=10):
        self.tamano = 10
        self.visitadas = [[False for _ in range(self.tamano)] for _ in range(self.tamano)]
        self.AGUA = 0
        self.TOCADO = 1
        self.HUNDIDO = 2

        por1 = Nave("Enterprise", "portaaviones", 5)

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

    def colocar_nave(self, nave, x, y, orientacion):
        pass

    def comprobar_impacto(self, x, y):
        print(f"[LOG] estoy en tablero comprobando impacto ({x}, {y})")

        if self.visitadas[x][y]:
            print("[LOG] Ya has disparado a esta casilla")
            return None

        self.visitadas[x][y] = True

        casilla = self.casillero[x][y]

        if casilla is None:
            print("[LOG] Agua")
            return self.AGUA
        else:
            resultado = casilla.recibir_disparo()
            if resultado == 2:
                print(f"[LOG] {casilla.nombre} Hundido")
                return self.HUNDIDO
            else:
                print(f"[LOG] {casilla.nombre} Tocado")
                return self.TOCADO