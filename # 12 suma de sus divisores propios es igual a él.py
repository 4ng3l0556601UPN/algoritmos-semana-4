# Un número es PERFECTO si la suma de sus divisores propios es igual a él. Ej: 6=1+2+3. Busca todos los perfectos hasta N.
#
# Solicitar al usuario un número límite N
N = int(input("Ingrese un número entero positivo: "))

# Validar que N sea positivo
if N <= 0:
    print("Error: Debe ingresar un número entero positivo.")
else:

    # Mostrar mensaje inicial
    print("Números perfectos hasta", N, ":")

    # Recorrer todos los números desde 1 hasta N
    for numero in range(1, N + 1):

        # Inicializar la suma de divisores propios
        suma_divisores = 0

        # Buscar los divisores propios del número
        for divisor in range(1, numero):

            # Verificar si el divisor divide exactamente al número
            if numero % divisor == 0:

                # Sumar el divisor a la suma total
                suma_divisores += divisor

        # Verificar si la suma de divisores es igual al número
        if suma_divisores == numero:

            # Mostrar el número perfecto encontrado
            print(numero)
            
# numero % divisor == 0 → verifica si un número tiene un divisor exacto.
# Los divisores propios son todos los divisores menores que el número.
# Se suman todos los divisores propios.
# Si la suma es igual al número, entonces es un número perfecto.
# El programa revisa todos los números desde 1 hasta N.