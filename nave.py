# Creo la clase Nave
class Nave:
    def __init__(self, nombre, tipo, vida):
        # Añado las variables a la clase
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida

    # Creo el metodo con el que se van a restar vidas por cada impacto
    def recibir_disparo(self):
        self.vida -= 1      # Declaro que la vida se reste 1 punto
        print(f"[LOG] Vidas restantes de {self.nombre}: {self.vida}")
        if self.vida > 0:   # Si la vida es mayor que 0 puntos
            return 1        # Devuelve Tocado
        else:
            print(f"[LOG] Nave hundida")
            return 2        # Devuelve Hundido