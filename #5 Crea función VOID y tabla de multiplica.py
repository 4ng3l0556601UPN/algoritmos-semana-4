#Crea función VOID y tabla de multiplicar 1 al 10

def tabla(num):
    # El bucle genera multiplicaciones del 1 al 10
    for i in range(1, 11):
        #Muestra la multiplicación directamente en pantalla
        print(f"{num} x {i} = {num * i}") #indica que f-strings se realizarà la multiplica con el multiplicador actual del bucle {i}

num_user = int(input("Ingrese un número para ver su tabla de multiplicar: "))

# Llamamos a la función utilizando tus variables especificadas
tabla(num_user)


