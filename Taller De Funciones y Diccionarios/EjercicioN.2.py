# Definimos una función llamada 'lista' que toma dos parámetros: 'dia' y 'semana' (con un valor por defecto de una lista vacía).
def lista(dia, semana=[]):
    # Añadimos el 'dia' a la lista 'semana'
    semana.append(dia)
    # Imprimimos la lista 'semana'
    print(semana)

# Llamamos a la función 'lista' con un día específico y una lista inicial
lista("Domingo", ["Lunes", "Martes", "Miercoles", "Jueves", "Sabado"])
