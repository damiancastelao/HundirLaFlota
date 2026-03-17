# Naves

## Tipos

- Submarinos: la nave más pequeña, ocupa una posición
- Fragatas: nave mediana de tres posiciones
- Portaviones: la mas larga, cinco posiciones

## Vidas

Las posiciones son las vidas de las naves. Si una nave ocupa tres posiciones en el tablero, tendrá tres vidas.

- Submarions: 1 vida
- Fragatas: 3 vidas
- Portaaviones: 5 vidas

## Estado

Las naves tienen tres posibles estados

- Escondida: todavía no ha sido decubierta
- Tocado: se descubrió alguna posición, pero no toda
- Hundido: se descubrió la posición completa, se le acabaron las vidas

## Propiedades

Las naves tienen las siguientes propiedades:

- nombre: nombre único, por ejemplo "la Pinta"
- tipo: submarino, fragata, portaaviones
- vidas: las casillas que ocupa

## Ejemplo de creación

Si en la partida queremos tener:

- **4 submarinos**
- **3 fragatas**
- **1 portaaviones**

podemos crear estas naves con nombres inspirados en barcos históricos:

```python
# Portaaviones
portaaviones = Nave("Enterprise", "portaaviones", 5)

# Fragatas
fragata_1 = Nave("Bismarck", "fragata", 3)
fragata_2 = Nave("Prince of Wales", "fragata", 3)
fragata_3 = Nave("Graf Spee", "fragata", 3)

# Submarinos
sub_1 = Nave("U-47", "submarino", 1)
sub_2 = Nave("U-96", "submarino", 1)
sub_3 = Nave("U-505", "submarino", 1)
sub_4 = Nave("U-534", "submarino", 1)
```

## Explicación

En este ejemplo:

- `Enterprise` es un portaaviones y tiene **5 vidas**
- `Bismarck`, `Prince of Wales` y `Graf Spee` son fragatas y tienen **3 vidas**
- `U-47`, `U-96`, `U-505` y `U-534` son submarinos y tienen **1 vida**