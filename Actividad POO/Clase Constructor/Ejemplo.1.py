#EJEMPLO DE CLASE CONSTRUCTOR

# Definición de la clase Estudiante1
class Estudiante1:
    # Método especial __init__ que se llama al crear una nueva instancia
    def __init__(self, codigo, nombre, apellido):
        # Inicialización de los atributos de la instancia con los valores proporcionados
        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellido

    # Método para imprimir la información del estudiante
    def imprimir_Informacion(self):
        print(self.codigo, self.nombre, self.apellido)

# Creación de una instancia de la clase Estudiante1 llamada adso1
adso1 = Estudiante1(2, 'Maria', 'Galindo')

# Llamada al método imprimir_Informacion para mostrar la información del estudiante
adso1.imprimir_Informacion()
