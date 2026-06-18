# los primeros N términos de Fibonacci (0,1,1,2,3,5...)
# Función para generar los primeros N términos de Fibonacci
def generar_fibonacci(N):

    # Inicializar los dos primeros términos
    a = 0
    b = 1

    # Crear una lista para almacenar la secuencia
    fibonacci = []

    # Generar los N términos usando un bucle
    for i in range(N):

        # Agregar el término actual a la lista
        fibonacci.append(a)

        # Calcular los siguientes términos
        a, b = b, a + b

    # Devolver la lista de Fibonacci
    return fibonacci


# Función para verificar si un número pertenece a Fibonacci
def pertenece_fibonacci(numero):

    # Inicializar los dos primeros términos
    a = 0
    b = 1

    # Generar términos hasta alcanzar o superar el número
    while a < numero:
        a, b = b, a + b

    # Verificar si el número pertenece a la secuencia
    return a == numero


# Solicitar la cantidad de términos
N = int(input("Ingrese la cantidad de términos de Fibonacci: "))

# Generar la secuencia
serie = generar_fibonacci(N)

# Mostrar la secuencia generada
print("Serie de Fibonacci:")
print(serie)

# Solicitar un número para verificar
numero = int(input("Ingrese un número para verificar: "))

# Verificar si pertenece a Fibonacci
if pertenece_fibonacci(numero):
    print(numero, "sí pertenece a la serie de Fibonacci.")
else:
    print(numero, "no pertenece a la serie de Fibonacci.")
    
#generar_fibonacci(N) → genera los primeros N números de Fibonacci.
# a, b = b, a + b → calcula los siguientes términos de la secuencia.
# pertenece_fibonacci(numero) → genera términos de Fibonacci hasta alcanzar o superar el número