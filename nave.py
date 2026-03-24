class Nave:
    def __init__(self, nombre, tipo, vida):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida

    def recibir_disparo(self):
        self.vida -= 1
        print(f"[LOG] Vidas restantes de {self.nombre}: {self.vida}")
        if self.vida > 0:
            return 1
        else:
            print(f"[LOG] Nave hundida")
            return 2