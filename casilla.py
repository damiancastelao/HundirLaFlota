from nave import Nave

class Casilla:
    def __init__(self, nave):
        self.nave = nave

        self.disparada = False

    def recibir_disparo(self):
        if self.disparada == True:
            if self.nave != 'agua':
                print(f'Casilla ya disparada con {self.nave.nombre}, de tipo {self.nave.tipo}, con {self.nave.vida} vidas')
            else:
                print('Casilla ya disparada es de agua')
            return None

        if self.nave == 'agua':
            self.disparada = True
            return 0

        if self.disparada == False:
            resultado = self.nave.recibir_disparo()

            self.disparada = True
            return resultado




