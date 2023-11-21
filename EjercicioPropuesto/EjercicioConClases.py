# Definición de la clase SistemaEquipos
class SistemaEquipos:
    def __init__(self):
        # Inicialización del diccionario de equipos en el constructor
        self.equipos = {}

    # Método para agregar un equipo al diccionario
    def agregarEquipo(self, id, dispositivos, ambiente):
        self.equipos[id] = {"dispositivos": dispositivos, "ambiente": ambiente}

    # Método para agregar una novedad a un equipo existente
    def agregarNovedad(self, id, fecha, descripcion):
        if id in self.equipos:
            if "novedades" not in self.equipos[id]:
                self.equipos[id]["novedades"] = []
            self.equipos[id]["novedades"].append({"fecha": fecha, "descripción": descripcion})
        else:
            print("No existe equipo con ese id")

    # Método para mostrar la información de un equipo y sus novedades
    def mostrarEquipo(self, id):
        if id in self.equipos:
            print(f"Equipo {id}")
            print(f"Dispositivos: {self.equipos[id]['dispositivos']}")
            print(f"Ambiente: {self.equipos[id]['ambiente']}")
            if "novedades" in self.equipos[id]:
                print("Novedades:")
                for novedad in self.equipos[id]["novedades"]:
                    print(f"- {novedad['fecha']} {novedad['descripción']}")
        else:
            print("Equipo no encontrado")

    # Método para mostrar las novedades de un equipo
    def mostrarNovedad(self, id):
        if "novedades" in self.equipos[id]:
            for novedad in self.equipos[id]["novedades"]:
                print(f"- {novedad['fecha']} {novedad['descripción']}")
        else:
            print("El equipo no tiene novedades")

    # Método para generar un reporte de todos los equipos y sus novedades
    def reporteDeEquipos(self):
        print("LISTA DE LOS EQUIPOS:")
        for id, equipo in self.equipos.items():
            print(f"Equipo {id}")
            print(f"Dispositivos: {equipo['dispositivos']}")
            print(f"Ambiente: {equipo['ambiente']}")
            if "novedades" in equipo:
                print("Novedades:")
                for novedad in equipo["novedades"]:
                    print(f"- {novedad['fecha']} {novedad['descripción']}")
            print("\n")

    # Método para eliminar un equipo del diccionario
    def eliminarEquipo(self, id):
        if id in self.equipos:
            del self.equipos[id]
            print("Equipo eliminado")
        else:
            print("No existe un equipo con ese ID")

    # Método para modificar la información de un equipo
    def modificarEquipo(self, id, nuevos_dispositivos, nuevo_ambiente):
        if id in self.equipos:
            self.equipos[id]["dispositivos"] = nuevos_dispositivos
            self.equipos[id]["ambiente"] = nuevo_ambiente
            print("Equipo modificado")
        else:
            print("No existe un equipo con ese ID")


# Ejemplo de uso:
sistema = SistemaEquipos()

print("BIENVENIDO AL SISTEMA DE EQUIPOS DEL SENA")

while True:
    print("""
    Menú:
    1. Agregar equipo
    2. Agregar novedad 
    3. Mostrar equipo
    4. reporteDeEquipos
    5. Eliminar Equipo
    6. Modificar Equipo
    7. Salir """)

    # Obtener la opción del usuario
    opcion = input("Ingrese una opción: ")

    # Procesar la opción seleccionada
    if opcion == "1":
        # Agregar un nuevo equipo
        id = input("Ingrese ID del equipo: ")
        dispositivos = input("Ingrese nombre de los dispositivos separados por coma: ").split(",")
        ambiente = input("Inserte el ambiente: ")
        sistema.agregarEquipo(id, dispositivos, ambiente)

    elif opcion == "2":
        # Agregar una nueva novedad a un equipo existente
        id = input("Ingrese ID del equipo: ")
        fecha = input("Ingrese fecha: ")
        descripcion = input("Ingrese descripción de la novedad: ")
        sistema.agregarNovedad(id, fecha, descripcion)

    elif opcion == "3":
        # Mostrar la información de un equipo
        id = input("Ingrese ID del equipo: ")
        sistema.mostrarEquipo(id)

    elif opcion == "4":
        # Generar un reporte de todos los equipos
        sistema.reporteDeEquipos()

    elif opcion == "5":
        # Eliminar un equipo
        id = input("Ingrese el ID del equipo a eliminar: ")
        sistema.eliminarEquipo(id)

    elif opcion == "6":
        # Modificar la información de un equipo
        id = input("Ingrese el ID del equipo a modificar: ")
        dispositivos = input("Ingrese los nuevos dispositivos: ").split(",")
        ambiente = input("Ingrese el nuevo ambiente: ")
        sistema.modificarEquipo(id, dispositivos, ambiente)

    elif opcion == "7":
        # Salir del programa
        print("Saliendo del programa...")
        break

    else:
        # Opción inválida
        print("Opción inválida")

