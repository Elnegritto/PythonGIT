#Funciones anónimas «lambda»

# Definimos una función lambda llamada 'numero_palabras' que toma un parámetro 't'
# La función cuenta el número de palabras en 't' utilizando strip() para eliminar espacios en blanco y split() para dividir por palabras
numero_palabras = lambda t: len(t.strip().split())

# Llamamos a la función lambda con una cadena de prueba y la imprimimos
print(numero_palabras("hola, esto es una prueba con lambda"))
