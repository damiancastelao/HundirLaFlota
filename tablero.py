class Tablero:
    def __init__(self):
        self.AGUA = 0
        self.TOCADO = 1
        self.HUNDIDO = 2

    def colocar_nave(self, nave, fila, columna, horizontal=True):
        pass

    def comprobar_impacto(self, fila, columna):
        print("[LOG] estoy en tablero comprobando impacto")
        return self.AGUA
