# Ejemplo de Polimorfismo

# Definición de la clase Animal
class Animal:
    # Método hablar que será sobrescrito por las clases derivadas
    def hablar(self):
        pass

# Definición de la clase Perro que hereda de Animal
class Perro(Animal):
    # Sobrescribe el método hablar de la clase base
    def hablar(self):
        return 'Guau!'

# Definición de la clase Gato que hereda de Animal
class Gato(Animal):
    # Sobrescribe el método hablar de la clase base
    def hablar(self):
        return 'Miau!'

# Función que utiliza polimorfismo al llamar al método hablar del objeto proporcionado
def hacer_hablar(animal):
    return animal.hablar()

# Crear objetos de las clases derivadas
mi_perro = Perro()
mi_gato = Gato()

# Llamar a la función con diferentes objetos
print(hacer_hablar(mi_perro))  # Imprime: Guau!
print(hacer_hablar(mi_gato))   # Imprime: Miau!
