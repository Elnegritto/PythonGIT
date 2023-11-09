equipos = {}

# Función para agregar un equipo
def agregarEquipo(id, dispositivos, ambiente):
  equipos[id] = {"dispositivos": dispositivos, "ambiente": ambiente}

# Función para agregar novedades  
def agregarNovedad(id, fecha, descripcion):
  if id in equipos:
    if "novedades" not in equipos[id]:
      equipos[id]["novedades"] = []
    equipos[id]["novedades"].append({"fecha": fecha, "descripción": descripcion})
  else:
    print("No existe equipo con ese id")
      
# Función para mostrar un equipo
def mostrarEquipo(id):
  if id in equipos:
    print(f"Equipo {id}")
    print(f"Dispositivos: {equipos[id]['dispositivos']}")
    print(f"Ambiente: {equipos[id]['ambiente']}")
    if "novedades" in equipos[id]:
      print("Novedades:")
      for novedad in equipos[id]["novedades"]:
        print(f"- {novedad['fecha']} {novedad['descripción']}")
  else:
    print("Equipo no encontrado")

# Función para mostrar novedades de un equipo  
def mostrarNovedad(id):
  if "novedades" in equipos[id]:
    for novedad in equipos[id]["novedades"]:
      print(f"- {novedad['fecha']} {novedad['descripción']}")
  else:
    print("El equipo no tiene novedades")
      
# Función para mostrar todos los equipos
def reporteDeEquipos():
  print("LISTA DE LOS EQUIPOS:")
  for id, equipo in equipos.items():
    print(f"Equipo {id}")
    print(f"Dispositivos: {equipo['dispositivos']}")
    print(f"Ambiente: {equipo['ambiente']}")
    if "novedades" in equipo:
      print("Novedades:")
      for novedad in equipo["novedades"]:
        print(f"- {novedad['fecha']} {novedad['descripción']}")
    print("\n")

# Función para eliminar un equipo
def eliminarEquipo(id):
  if id in equipos: 
    del equipos[id]
    print("Equipo eliminado")
  else:
    print("No existe un equipo con ese ID")

# Función para modificar un equipo
def modificarEquipo(id, nuevos_dispositivos, nuevo_ambiente):
  if id in equipos:
    equipos[id]["dispositivos"] = nuevos_dispositivos 
    equipos[id]["ambiente"] = nuevo_ambiente
    print("Equipo modificado")
  else:
    print("No existe un equipo con ese ID")

# Ejemplo de uso:

print("BIENVENIDO AL SISTEMA DE EQUIPOS DEL SENA")

# Bucle para mostrar el menú al usuario
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
  
  opcion = input("Ingrese una opción: ")
  
  if opcion == "1":
    # Solicitar datos para agregar equipo
    id = input("Ingrese ID del equipo: ")
    dispositivos = input("Ingrese nombre de los dispositivos separados por coma: ").split(",")
    ambiente = input("Inserte el ambiente: ")
    agregarEquipo(id, dispositivos,ambiente)
  
  elif opcion == "2":
     # Solicitar datos para agregar novedad
    id = input("Ingrese ID del equipo: ")
    fecha = input("Ingrese fecha: ")
    descripcion = input("Ingrese descripción de la novedad: ")
    agregarNovedad(id, fecha, descripcion)

  elif opcion == "3":
    # Solicitar ID y mostrar equipo
    id = int(input("Ingrese ID del equipo: "))
    mostrarEquipo(id)

  elif opcion == "4":
    # Mostrar todos los equipos
    reporteDeEquipos()
  
  elif opcion == "5": 
  # Eliminar equipo
   id = input("Ingrese el ID del equipo a eliminar: ")
   eliminarEquipo(id)

  elif opcion == "6":
  # Modificar equipo
   id = input("Ingrese el ID del equipo a modificar: ")
   dispositivos = input("Ingrese los nuevos dispositivos: ").split(",")
   ambiente = input("Ingrese el nuevo ambiente: ")
   modificarEquipo(id, dispositivos, ambiente)
   
  elif opcion == "7":
    # Salir del programa
    print("Saliendo del programa...")
    break
  
  else:
    print("Opción inválida")