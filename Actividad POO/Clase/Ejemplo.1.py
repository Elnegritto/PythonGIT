#EJEMPLO DE UNA CLASE

# Definición de la clase Estudiante
class Estudiante:
    # Atributos de la clase
    codigo = 0
    nombre = ""
    apellido = ""

    # Método para imprimir los datos del estudiante
    def imprimir_Datos(self):
        # Usamos self para referenciar los atributos de la instancia
        print(self.codigo, self.nombre, self.apellido)

# Creación de una instancia de la clase Estudiante llamada adso
adso = Estudiante()

# Asignación de valores a los atributos de la instancia adso
adso.codigo = 1
adso.nombre = 'Sandra'
adso.apellido = 'Cruz'

# Llamada al método imprimir_Datos para imprimir la información del estudiante
adso.imprimir_Datos()

