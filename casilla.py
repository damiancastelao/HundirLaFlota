class Casilla:
    def __init__(self):
        self.nave = None
        self.visitada = False

    def disparar(self):
        if self.visitada:
            print("Ya has disparado a esta casilla.")
            return None

        self.visitada = True

        if self.nave is None:
            print("Agua")
            return 0

        else:
            resultado = self.nave.recibir_disparo()
            if resultado == 2:
                print(f"{self.nave.nombre} Hundido")
            else:
                print(f"{self.nave.nombre} Tocado")
            return resultado