#Agregar datos al diccionario después de creado

calificaciones = {'Juan': 4.5, 'Ana': 3.8}

# Imprime el diccionario antes de la actualización
print("Diccionario antes de la actualización:")
print(calificaciones)

# Actualiza el diccionario con nuevos valores para las claves "Rosa" y "German"
calificaciones.update({"Rosa": 3.7, "German": 4.8})

# Imprime el diccionario después de la actualización
print("\nDiccionario después de la actualización:")
print(calificaciones)
