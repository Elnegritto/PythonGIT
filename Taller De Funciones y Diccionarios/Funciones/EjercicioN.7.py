#Modificando parámetros mutables

# Definimos una función llamada 'listalimpia' que toma dos parámetros: 'arg' y 'result' (con un valor por defecto de None)
def listalimpia(arg, result=None):
    # Verificamos si 'result' es None
    if result is None:
        # Si es None, creamos una nueva lista y añadimos 'arg' a ella
        result = [arg]
        # Imprimimos la nueva lista
        print(result)

# Llamamos a la función 'listalimpia' con el argumento 'a'
listalimpia("a")

# Llamamos a la función 'listalimpia' con el argumento 'b'
listalimpia("b")

