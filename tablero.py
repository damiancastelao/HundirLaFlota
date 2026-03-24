
from casilla import *

class Tablero:
    def __init__(self, tamanho=10):

        self.AGUA = 0
        self.TOCADO = 1
        self.HUNDIDO = 2

        por1 = Nave("Manuel", "portaaviones", 5)
        fra1 = Nave("Damián", "fragata", 3)
        fra2 = Nave("Elena", "fragata", 3)
        fra3 = Nave("Noelia", "fragata", 3)

        sub1 = Nave("U-47", "submarino", 1)
        sub2 = Nave("U-96", "submarino", 1)
        sub3 = Nave("U-505", "submarino", 1)
        sub4 = Nave("U-534", "submarino", 1)

        self.casillero = [
            [Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua')],
            [Casilla(por1), Casilla(por1), Casilla(por1), Casilla(por1), Casilla(por1), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua')],
            [Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua')],
            [Casilla(fra1), Casilla(fra1), Casilla(fra1), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua')],
            [Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla(sub1), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua')],
            [Casilla(fra2), Casilla(fra2), Casilla(fra2), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua')],
            [Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua')],
            [Casilla(fra3), Casilla(fra3), Casilla(fra3), Casilla('agua'), Casilla('agua'), Casilla(sub3), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua')],
            [Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua')],
            [Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla(sub4), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla(sub2)]
        ]

