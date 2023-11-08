#Modificando parámetros mutables

# Definimos una función llamada 'lista' que toma dos parámetros: 'arg' y 'result' (con un valor por defecto de una lista vacía)
def lista(arg, result=[]):
    # Añadimos 'arg' a la lista 'result'
    result.append(arg)
    # Imprimimos la lista 'result'
    print(result)

# Llamamos a la función 'lista' con el argumento 'domingo' y una lista vacía como segundo argumento
lista('domingo', [])



