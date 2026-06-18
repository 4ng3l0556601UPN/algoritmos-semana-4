#10 una función void que muestre todos los números primos desde 2 hasta N usando bucles anidados.
#
# Definir una función para calcular el factorial
def calcular_factorial(n):

    # Validar que el número no sea negativo
    if n < 0:
        return "Error: El número debe ser no negativo."

    # Inicializar el resultado en 1
    factorial = 1

    # Inicializar un contador
    contador = 1

    # Utilizar un bucle while para multiplicar los números
    while contador <= n:
        factorial = factorial * contador
        contador += 1

    # Devolver el resultado
    return factorial

# Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número entero no negativo: "))

# Mostrar el factorial del número ingresado
print("El factorial es:", calcular_factorial(numero))