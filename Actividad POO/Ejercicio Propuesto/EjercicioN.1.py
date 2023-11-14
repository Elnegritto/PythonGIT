# Ejemplo de clase con atributos y métodos

# Definición de la clase Coche
class Coche:
    # Método especial __init__ para inicializar los atributos al crear una instancia
    def __init__(self, marca, modelo, año):
        # Inicialización de atributos con los valores proporcionados
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.estado = 'Apagado'  # Estado predeterminado al crear un coche

    # Método para encender el coche
    def encender(self):
        self.estado = 'Encendido'
        print(f'{self.marca} {self.modelo} ha sido encendido.')

    # Método para apagar el coche
    def apagar(self):
        self.estado = 'Apagado'
        print(f'{self.marca} {self.modelo} ha sido apagado.')

# Crear una instancia de la clase Coche llamada mi_coche
mi_coche = Coche('Toyota', 'Corolla', 2020)

# Usar métodos y acceder a atributos
print(f'Mi coche es un {mi_coche.marca} {mi_coche.modelo} del año {mi_coche.año}.')
mi_coche.encender()
print(f'Estado del coche: {mi_coche.estado}')
mi_coche.apagar()
print(f'Estado del coche: {mi_coche.estado}')
