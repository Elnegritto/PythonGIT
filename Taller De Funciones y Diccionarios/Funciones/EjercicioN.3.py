#Funciones con Parámetros Posicionales

# Definimos una función llamada 'compra' que toma la marca, la cantidad y el valor unitario como parámetros
def compra(marca, cantidad, valor):
    # Creamos y retornamos un diccionario con la información de la compra
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor * cantidad
    )

# Imprimimos la información de la compra utilizando la función 'compra'
print(f'Lo comprado fue: {compra("AMD", 3, 2500000)}')

