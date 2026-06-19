#06 realiza la función que reciba un entero y retorne True si es par o False si es impar.
# colocamos el número de la función que se va a realizar
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
# se realiza prueba de la función
numero = int(input("Ingrese un número entero: "))
# se usa la condicional if.
if es_par(numero):
    print(f"El numero es par")# 
else:
    print(f"El numero es impar") # se imprime False si el número es impar