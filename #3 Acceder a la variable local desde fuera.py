#Acceder a la variable local desde fuera de la función
def calc_area(lado):
    #'area' es una variable LOCAL
    area = lado * lado
    return area 

#Pide datos al usuario
lado_usuario = int(input("Ingrese el lado del cuadrado: "))

#Establece la función y se guarda el retorno
resultado = calc_area(lado_usuario)
print("El área del cuadrado es:", resultado)

print(area) 