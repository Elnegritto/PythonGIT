#Accediedo a los elementos de  un diccionario

Diccionario = {'nombre': 'Ejemplo'}

# Imprime el valor asociado a la clave 'nombre'
print(Diccionario['nombre'])

# Imprime el valor asociado a la clave 'nombre' utilizando get(), con un mensaje predeterminado si la clave no existe
print(Diccionario.get('nombre', 'No existe'))
