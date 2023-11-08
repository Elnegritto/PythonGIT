#Funciones anónimas «lambda»

# Definimos una función lambda llamada 'operadorand' que toma dos parámetros 'x' e 'y' y realiza la operación de bits AND
operadorand = lambda x, y: x & y

# Utilizamos dos bucles anidados para recorrer todas las combinaciones de i y j (0 y 1) y aplicamos la función 'operadorand'
for i in range(2):
    for j in range(2):
        # Imprimimos el resultado de la operación AND entre i y j
        print(f"{i} & {j} = {operadorand(i, j)}")



