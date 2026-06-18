#09 función calcule el factorial  n (n!) usando un bucle while. Valida que n sea no negativo.
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


#def calcular_factorial(n): → crea una función llamada calcular_factorial.
#if n < 0: → verifica que el número no sea negativo.
#factorial = 1 → almacena el resultado de las multiplicaciones.
#contador = 1 → comienza desde 1.
#while contador <= n: → repite mientras el contador sea menor o igual a n.
#factorial = factorial * contador → multiplica el resultado por el contador.
#contador += 1 → aumenta el contador en 1.
#return factorial → devuelve el factorial calculado.

