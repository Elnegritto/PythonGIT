#Funciones con Parámetros

# Definimos una función llamada 'raiz' que calcula la raíz cuadrada de un valor
def raiz(value):
    return value ** (1/2)

# Imprimimos la raíz cuadrada de 4
print(f'La raíz cuadrada es: {raiz(4)}')

# Definimos una función llamada 'validarsiexiste' que imprime si un objeto es verdadero o falso
def validarsiexiste(obj):
    if obj:
        print(f"{obj} es True")
    else:
        print(f"{obj} es False")

# Llamamos a la función 'validarsiexiste' con el valor 1
validarsiexiste(1)
