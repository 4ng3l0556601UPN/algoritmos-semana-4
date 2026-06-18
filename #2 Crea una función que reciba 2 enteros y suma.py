#Crea una función que reciba 2 enteros y retorne suma

def sumar(num1, num2):

    #retorna la suma de los dos números
    return num1 + num2

#pido los datos al usuario
num1 = int(input("Ingrese el primer número: ")) #input lo devuelve con una cadena por eso se convierte a entero con int()
num2 = int(input("Ingrese el segundo número: "))

#almacena el resultado retornado
resultado = sumar(num1, num2)

# muestra el resultado
print("La suma es:", resultado)

# num1 y num2 dentro de la función son variables locales