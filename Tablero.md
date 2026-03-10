# Tablero

El tablero es una matriz de dos dimensiones de **10 filas por 10 columnas**.

Cada posición del tablero representa una casilla y puede estar en una de estas situaciones:

- **Vacía**: no hay ninguna nave en esa posición.
- **Ocupada**: hay una nave en esa posición.

## Estructura

El tablero tiene un total de **100 casillas**:

- Filas: del 0 al 9
- Columnas: del 0 al 9

Cada casilla se puede identificar mediante unas coordenadas `(x, y)`:

- `x`: fila
- `y`: columna

Por ejemplo:

- `(0, 0)` es la esquina superior izquierda
- `(9, 9)` es la esquina inferior derecha

## Relación con las naves

En cada posición podrá haber como máximo **una nave o una parte de una nave**.

Las naves ocupan varias posiciones consecutivas del tablero, en horizontal o en vertical.

La propiedad más importante de una nave es su **vida**.

## Vida de una nave

La **vida** de una nave indica cuántas posiciones ocupa en el tablero.

Es decir:

- una nave con `vida = 1` ocupa 1 casilla
- una nave con `vida = 3` ocupa 3 casillas
- una nave con `vida = 5` ocupa 5 casillas

Cada vez que una de sus posiciones recibe un disparo, la nave pierde una vida.

Cuando su vida llega a `0`, la nave queda **hundida**.

## Ejemplo

Si una fragata tiene `vida = 3`, significa que ocupa 3 posiciones del tablero, por ejemplo:

- `(2, 4)`
- `(2, 5)`
- `(2, 6)`

Si recibe un disparo en una de esas posiciones, su vida baja de 3 a 2.
Si recibe impactos en todas sus posiciones, su vida llega a 0 y la nave se hunde.

## Matriz con Naves (Ejemplo)

Para visualizar cómo se verían las naves en el tablero de 10x10, usaremos un ejemplo con la flota definida en **Naves.md**:

- **1 Portaaviones (Enterprise)**: 5 casillas (5 vidas)
- **3 Fragatas (Bismarck, Prince of Wales, Graf Spee)**: 3 casillas cada una (3 vidas)
- **4 Submarinos (U-47, U-96, U-505, U-534)**: 1 casilla cada uno (1 vida)

### Representación en el Tablero

En la siguiente tabla visual, representamos el tablero donde:
- `.` : Agua (casilla vacía)
- `S` : Submarino
- `F` : Fragata
- `P` : Portaaviones

| | 0 | 1      | 2      | 3      | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|--------|--------|--------|---|---|---|---|---|---|
| **0** | . | .      | .      | .      | . | . | . | . | . | . |
| **1** | . | **P**  | **P**  | **P**  | **P** | **P** | . | . | . | . |
| **2** | . | .      | .      | .      | . | . | . | . | . | . |
| **3** | . | .      | .      | **F1** | . | . | . | . | . | . |
| **4** | . | .      | .      | **F1** | . | . | **S1**| . | . | . |
| **5** | . | .      | .      | **F1** | . | . | . | . | . | . |
| **6** | . | .      | .      | .      | . | . | . | . | . | . |
| **7** | . | **F2** | **F2** | **F2** | . | . | **S3**| . | . | . |
| **8** | . | .      | .      | .      | . | . | . | . | . | . |
| **9** | . | **F3** | **F3** | **F3** | . | **S4**| . | . | . | **S2** |

## Definición del Tablero (Código Simplificado)

Para gestionar las naves en el tablero sin usar clases adicionales como `Casilla`, podemos usar una matriz donde cada posición guarde directamente la referencia al objeto `Nave` o `None` si hay agua.

### Inicialización de la Matriz y Flota

```python
# 1. Crear la matriz 10x10 vacía (llena de None)
# Cada posición representa una casilla de agua inicialmente.
# La matriz es una lista que contendrá a su vez otras listas (las filas).
matriz = []

# Recorremos un bucle para crear cada una de las 10 filas (0 a 9)
for fila in range(10):
    # Para cada fila, creamos una lista vacía que contendrá sus columnas
    fila_actual = []

    # Recorremos otro bucle para crear cada columna dentro de la fila actual
    for columna in range(10):
        # Añadimos 'None' a la fila para indicar que la casilla está vacía
        fila_actual.append(None)

    # Una vez terminada la fila con sus 10 columnas, la añadimos a la matriz principal
    matriz.append(fila_actual)

# 2. Definir las naves por separado (4 submarinos, 3 fragatas, 1 portaaviones)
# Estos objetos se definen una sola vez.
portaaviones = Nave("Enterprise", "portaaviones", 5)

fragata_1 = Nave("Bismarck", "fragata", 3)
fragata_2 = Nave("Prince of Wales", "fragata", 3)
fragata_3 = Nave("Graf Spee", "fragata", 3)

sub_1 = Nave("U-47", "submarino", 1)
sub_2 = Nave("U-96", "submarino", 1)
sub_3 = Nave("U-505", "submarino", 1)
sub_4 = Nave("U-534", "submarino", 1)

# 3. Ejemplo de cómo asignar una nave a las coordenadas
# El mismo objeto 'portaaviones' se asigna a varias posiciones.
for col in range(1, 6):
    matriz[1][col] = portaaviones

# 4. Comprobar si hay una nave en una posición
def disparar(x, y):
    nave = matriz[x][y]
    if nave:
        print(f"¡Tocado! Has dado a: {nave.nombre}")
        nave.recibir_disparo()
    else:
        print("Agua")
```

### Ubicación de las naves en el ejemplo:

1.  **Enterprise (Portaaviones)**: `(1,1)` a `(1,5)` (Horizontal).
2.  **Bismarck (Fragata 1)**: `(3,3)`, `(4,3)`, `(5,3)` (Vertical).
3.  **Prince of Wales (Fragata 2)**: `(7,1)`, `(7,2)`, `(7,3)` (Horizontal).
4.  **Graf Spee (Fragata 3)**: `(9,1)`, `(9,2)`, `(9,3)` (Horizontal).
5.  **U-47 (Submarino 1)**: `(4,6)`.
6.  **U-96 (Submarino 2)**: `(9,9)`.
7.  **U-505 (Submarino 3)**: `(7,6)`.
8.  **U-534 (Submarino 4)**: `(9,5)`.

