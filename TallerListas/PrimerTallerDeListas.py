# Aqui se Crean las listas vacías
aprendices = []
edades = []

# Aqui se Llenan las listas solicitando datos por el teclado
numeroAprendices = int(input("Ingrese el número de aprendices: "))
for _ in range(numeroAprendices):
    nombre = input("Ingrese el nombre del aprendiz: ")
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    aprendices.append(nombre)
    edades.append(edad)

# Aqui se Imprimen las listas
print(f"Lista de aprendices: {aprendices}")
print(f"Lista de edades: {edades}")

# Por aqui se Muestra el aprendiz con la mayor edad o el aprendiz que es mayor de edad en pocas palabras el pensionado del ambiente 
mayorDeEdad = edades.index(max(edades))
print(f"Aprendiz con la mayor edad: {aprendices[mayorDeEdad]}")

# Aqui se Inserta el nombre de nuestra querida instructora en la posición 1
nombreDeLaInstructora = input("Ingrese el nombre de la instructora: ")
aprendices.insert(1, nombreDeLaInstructora)

# En esta parte cuenta cuántos aprendices tienen 18 años o en pocas palabras cuantos estan pensionados en el ambiente
conteo18Edad = edades.count(18)
print(f"Número de aprendices con 18 años: {conteo18Edad}")

# Aqui se Agrega el nombre de otro veneco digo de un aprendiz al final de la lista
nuevoNombreDelAprendiz = input("Ingrese el nombre del nuevo aprendiz o nuevo aprendiz: ")
aprendices.append(nuevoNombreDelAprendiz)

# Aqui se borrar el nombre de nuestra querida instructora de la lista
aprendices.remove(nombreDeLaInstructora)

# Aqui se Indica un dato a buscar en la lista de aprendices
datoABuscar = input("Ingrese un dato a buscar en la lista de aprendices(nombre): ")
if datoABuscar in aprendices:
    print(f"{datoABuscar} está en la lista de aprendices.")
else:
    print(f"{datoABuscar} no está en la lista de aprendices.")

# Puse lo que decia en el documento porque no tuve mas imaginacion para los comentarios XD

# Mostrar los primeros 10 aprendices
print(f"Primeros 10 aprendices: {aprendices[:10]}")

# Mostrar los últimos 10 aprendices
print(f"Últimos 10 aprendices: {aprendices[-10:]}")

# Mostrar del elemento 10 al elemento 20
print(f"Elementos del 10 al 20: {aprendices[10:21]}")
