#Definir una función 

# Definimos una función llamada 'saludar' que imprime un saludo
def saludar():
    print("saludo")

# Definimos una función llamada 'retornarnumero' que retorna el número 1
def retornarnumero():
    return 1

# Llamamos a la función 'saludar', que imprime el saludo
saludar()

# Llamamos a la función 'retornarnumero', pero no almacenamos ni imprimimos el resultado
retornarnumero()

# Comprobamos si el resultado de la función 'retornarnumero' es igual a 1 e imprimimos un mensaje correspondiente
if retornarnumero() == 1:
    print("Devolvió un uno")
else:
    print("No devolvió un uno")

