# Guía Rápida: Clases y Objetos en Python

## 1. Concepto de Clase y Objeto
Si queremos construir diversos barcos para un simulador, en lugar de definir cada dato de manera aislada, utilizaremos un plano o estructura base.

- **La Clase (El Plano):** Representa la definición técnica. Establece que todas las naves poseen un nombre y una cantidad de puntos de vida, aunque no constituye una nave real en sí misma.
- **El Objeto (La Instancia):** Es la entidad real construida a partir de la clase. Podemos tener un objeto "Submarino" y un objeto "Portaaviones", ambos creados bajo la misma Clase, pero con datos específicos distintos.

## 2. Anatomía de una Clase en Python
Para crear un objeto, necesitamos definir primero su estructura mediante la palabra clave `class`.

### El método `__init__` (El Constructor)
Es un método especial que se ejecuta automáticamente al instanciar el objeto. Su función es asignar los valores iniciales o atributos.

### El parámetro `self`
Representa una referencia a la instancia específica que estamos procesando. Permite que el objeto acceda a sus propios atributos y métodos. Por ejemplo, `self.nombre` identifica el nombre propio de esa instancia.

```python
class Nave:
    # El "constructor": define los datos necesarios al instanciar
    def __init__(self, nombre, tamano):
        self.nombre = nombre       # Atributo: Nombre de la nave
        self.vida = tamano         # Atributo: Resistencia de la nave
        self.hundido = False       # Atributo: Estado lógico inicial

    # Un "método": Comportamiento definido para el objeto
    def recibir_disparo(self):
        self.vida -= 1
        if self.vida <= 0:
            self.hundido = True
            print(f"¡El {self.nombre} ha sido hundido!")
        else:
            print(f"¡El {self.nombre} ha sido tocado! Vida restante: {self.vida}")
```

## 3. Creación y Uso de Objetos (Instanciación)
Una vez definido el plano, procederemos a la creación de objetos reales de la siguiente manera:

```python
# Creación (instanciación) de dos objetos independientes
submarino = Nave("Submarino", 1)
buque = Nave("Destructor", 2)

# Acceso a los atributos del objeto
print(submarino.nombre) # Salida esperada: Submarino

# Ejecución de los métodos del objeto
buque.recibir_disparo() # Salida esperada: ¡El Destructor ha sido tocado! Vida restante: 1
```

## 4. Utilidad de la Programación Orientada a Objetos
- **Organización:** Nos permite agrupar variables relacionadas en una sola entidad. En lugar de gestionar `nombre_barco1` y `vida_barco1` de forma independiente, el objeto integra toda la información.
- **Abstracción:** Podemos invocar el método `recibir_disparo()` sin necesidad de conocer los detalles internos de la implementación aritmética. El objeto gestiona su propio estado.
- **Reutilización:** La definición de una única clase nos permite generar múltiples instancias de forma eficiente.
- **Escalabilidad:** Si requerimos añadir nuevas propiedades (como "escudos" o "munición"), los cambios se realizan en la clase y se aplican automáticamente a todos los objetos derivados de ella.

---

## Resumen Conceptual
> "Consideremos que una Clase es el molde de una galleta; el Objeto es la galleta resultante. Podemos emplear el mismo molde para producir galletas con diferentes ingredientes, pero todas conservarán la misma estructura fundamental."
