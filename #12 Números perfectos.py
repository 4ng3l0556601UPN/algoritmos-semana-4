def es_perfecto(numero):

    suma = 0

    for i in range(1, numero):

        if numero % i == 0:
            suma += i

    return suma == numero

limite = int(input("Buscar números perfectos hasta: "))

for numero in range(2, limite + 1):

    if es_perfecto(numero):
        print(numero)
