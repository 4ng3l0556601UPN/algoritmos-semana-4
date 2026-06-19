#10 una función void que muestre todos los números primos desde 2 hasta N usando bucles anidados.
# Función que muestra los números primos desde 2 hasta N
def mostrar_primos(N):

    # Mostrar un mensaje inicial
    print("Números primos desde 2 hasta", N, ":")

    # Recorrer los números desde 2 hasta N
    for numero in range(2, N + 1):

        # Variable para determinar si el número es primo
        es_primo = True

        # Buscar divisores desde 2 hasta numero - 1
        for divisor in range(2, numero):

            # Verificar si el número es divisible exactamente
            if numero % divisor == 0:

                # Si tiene un divisor, no es primo
                es_primo = False

                # Salir del bucle interno
                break

        # Si sigue siendo primo, mostrarlo
        if es_primo:
            print(numero)


# Solicitar al usuario un número entero positivo
N = int(input("Ingrese el valor de N: "))

# Validar que N sea mayor o igual a 2
if N < 2:
    print("Debe ingresar un número mayor o igual a 2.")
else:
    # Llamar a la función para mostrar los números primos
    mostrar_primos(N)