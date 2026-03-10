# Clase que representa una nave en el juego
class Nave:
    def __init__(self, nombre, tamaño):
        self.nombre = nombre  # Nombre del barco (ej: "Submarino")
        self.vida = tamaño    # Número de impactos que puede recibir antes de hundirse

    def recibir_impacto(self):
        self.vida -= 1  # Se resta un punto de vida por cada impacto
        return self.vida == 0  # Devuelve True si la nave ha sido hundida

# Clase que representa una casilla del tablero
class Casilla:
    def __init__(self):
        self.ocupante = None  # Aquí se guarda un objeto Nave si la casilla está ocupada, o None si está vacía
        self.revelada = False # Indica si la casilla ya ha sido atacada

    def disparar(self):
        self.revelada = True  # Marcamos la casilla como revelada tras el disparo
        if self.ocupante:
            # Si hay una nave, se le aplica el impacto
            return self.ocupante.recibir_impacto()
        return False  # Si no hay nave, no se hunde nada

# Clase principal que gestiona el juego
class Juego:
    def __init__(self):
        # Creamos un tablero de 5x5 compuesto por objetos Casilla
        self.tablero = [[Casilla() for _ in range(5)] for _ in range(5)]
        self.inicializar_naves()  # Colocamos las naves en el tablero

    def inicializar_naves(self):
        # Ejemplo: Colocar un Submarino (de tamaño 1) en la posición (3,1)
        submarino = Nave("Submarino", 1)
        self.tablero[3][1].ocupante = submarino
        # Aquí se podrían colocar más naves de diferentes tamaños y posiciones

    def realizar_disparo(self, x, y):
        casilla = self.tablero[x][y]  # Obtenemos la casilla objetivo
        if casilla.revelada:
            # Si ya se disparó aquí, avisamos al usuario
            print(f"Ya has disparado en ({x}, {y})")
            return

        se_hundio = casilla.disparar()  # Disparamos a la casilla y comprobamos si se hundió una nave

        if casilla.ocupante:
            # Si había una nave, informamos del impacto
            print(f"¡Impacto en un {casilla.ocupante.nombre}!")
            if se_hundio:
                # Si la nave se ha hundido, lo notificamos
                print(f"¡Hundido! Has destruido el {casilla.ocupante.nombre}")
        else:
            # Si no había nave, es agua
            print("Agua.")