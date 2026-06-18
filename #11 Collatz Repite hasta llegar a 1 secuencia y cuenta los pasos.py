# conjetura de Collatz: si n es par → n/2; si es impar → 3n+1. Repite hasta llegar a 1. Muestra la secuencia y cuenta los pasos.
# Solicitar al usuario un número entero positivo
n = int(input("Ingrese un número entero positivo: "))

# Validar que el número sea mayor que 0
if n <= 0:
    print("Error: Debe ingresar un número entero positivo.")
else:
    
    # Inicializar el contador de pasos
    pasos = 0

    # Mostrar el número inicial de la secuencia
    print("Secuencia de Collatz:")

    # Repetir hasta que n sea igual a 1
    while n != 1:

        # Mostrar el valor actual de n
        print(n)

        # Verificar si n es par
        if n % 2 == 0:
            # Si es par, dividir entre 2
            n = n // 2
        else:
            # Si es impar, aplicar 3n + 1
            n = 3 * n + 1

        # Incrementar el contador de pasos
        pasos += 1

    # Mostrar el último valor de la secuencia (1)
    print(1)

    # Mostrar la cantidad total de pasos realizados
    print("Cantidad de pasos:", pasos)
    
# n % 2 == 0 → verifica si el número es par.
# Si es par, se divide entre 2.
# Si es impar, se calcula 3 * n + 1.
# El proceso se repite con while hasta que n llegue a 1.
# pasos += 1 cuenta cuántas operaciones se realizaron.
# Finalmente se muestra la secuencia completa y el total de pasos.