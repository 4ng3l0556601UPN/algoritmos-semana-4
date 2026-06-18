def fibonacci(n):

    serie = [0, 1]

    while len(serie) < n:
        serie.append(serie[-1] + serie[-2])

    return serie

def pertenece(numero):

    lista = fibonacci(30)

    return numero in lista

cantidad = int(input("Cantidad de términos: "))

print(fibonacci(cantidad))

valor = int(input("Número a verificar: "))

if pertenece(valor):
    print("Sí pertenece")
else:
    print("No pertenece")
