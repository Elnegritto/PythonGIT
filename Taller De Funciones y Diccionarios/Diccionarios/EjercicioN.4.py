# Técnicas de iteración

# Creamos un diccionario llamado 'calificaciones' con un nombre y una nota final
calificaciones = {
    'nombre': 'Kevin', 
    'notafinal': 5.0
}

# Sobrescribimos el diccionario 'calificaciones' con un nuevo conjunto de datos
calificaciones = {
    'Sofia': 5.0, 
    'Ivonne': 5.0,
    'Helber': 4.5,
    'Jose Maria': 2.5
}

# Iteramos sobre el diccionario e imprimimos cada clave y valor
for i, j in calificaciones.items():
    print(i, j)

# Imprimimos las claves del diccionario
print("Técnicas por clave")
for i in calificaciones.keys():
    print(i)

# Imprimimos los valores del diccionario
print("Iterar por valor")
for j in calificaciones.values():
    print(j)

# Creamos dos listas y las combinamos usando la función zip para iterar sobre ellas simultáneamente
nombres = ['Maria', 'Sebastian', 'Ana']
edades = ['18', '25', '30']
for n, e in zip(nombres, edades):
    print('Tu nombre es {0} y tu edad es {1}.'.format(n, e))

# Creamos un nuevo diccionario usando una expresión de diccionario y un bucle for
dicaleatorio = {x: x**2 for x in (2, 4, 6)}
print(dicaleatorio)

# Iteramos en reversa sobre un rango de números e imprimimos cada número
print("Números en reversa")
for i in reversed(range(1, 10, 2)):
    print(i)

# Eliminamos la entrada correspondiente a 'Rosa' del diccionario 'calificaciones'
del(calificaciones['Rosa'])

# Iteramos sobre el diccionario actualizado e imprimimos cada clave y valor
for i, j in calificaciones.items():
    print(i, j)





