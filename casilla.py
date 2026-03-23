class Casilla:
    def __init_(self):
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

        return self.nave.recibir_disparo()