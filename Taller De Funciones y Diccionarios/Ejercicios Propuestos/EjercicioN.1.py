# Definimos una función llamada 'activity' que toma dos parámetros, x e y.
def activity(x, y):
    # Calculamos el resultado de la operación x*2 + y*2
    resultado = x * 2 + y * 2 
    # Imprimimos un mensaje con el resultado
    print(f"El resultado de la operación de {x} x 2 + {y} x 2 es: {resultado}")

# Pedimos al usuario que ingrese el valor de X
x_valor = int(input("Inserte el valor de X: "))
# Pedimos al usuario que ingrese el valor de Y
y_valor = int(input("Inserte el valor de Y: "))

# Llamamos a la función 'activity' con los valores ingresados por el usuario
activity(x_valor, y_valor)
