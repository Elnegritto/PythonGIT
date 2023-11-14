# Ejemplo de Herencia

# Definición de la clase Vehiculo
class Vehiculo:
    # Método especial __init__ para inicializar los atributos al crear una instancia
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # Método para obtener la información del vehículo
    def obtener_info(self):
        return f'{self.marca} {self.modelo}'

# Definición de la clase Coche que hereda de Vehiculo
class Coche(Vehiculo):
    # Método especial __init__ que inicializa atributos propios y llama al __init__ de la clase base
    def __init__(self, marca, modelo, año):
        # Llamada al __init__ de la clase base para inicializar los atributos comunes
        super().__init__(marca, modelo)
        self.año = año

    # Método para obtener la información del coche, que sobrescribe al método en la clase base
    def obtener_info(self):
        # Utiliza super() para llamar al método de la clase base y luego agrega información específica del coche
        return f'{super().obtener_info()} del año {self.año}'

# Crear un objeto de la clase Coche que hereda de Vehiculo
mi_coche = Coche('Toyota', 'Corolla', 2020)

# Usar el método obtener_info de la clase derivada Coche
print(mi_coche.obtener_info())
