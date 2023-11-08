#Parámetros por defecto

# Definimos una función llamada 'compra' que toma la marca, la cantidad y el valor unitario (con un valor por defecto de 2500000) como parámetros
def compra(marca, cantidad, valor=2500000):
    # Creamos y retornamos un diccionario con la información de la compra
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor * cantidad
    )

# Imprimimos la información de la compra utilizando la función 'compra' y proporcionando solo la marca y la cantidad
print(f'Lo comprado fue: {compra("AMD", 3)}')
