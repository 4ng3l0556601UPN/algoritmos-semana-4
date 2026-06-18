# 08 contador global con función incremente cada vez que sea llamada. Usa la palabra clave 'global'.
# usuario coloca el código aquí
# Crear una variable global llamada contador
contador = 0

# Definir una función que aumente el contador
def incrementar_contador():

    # Indicar que se utilizará la variable global
    global contador
    
    # Incrementar el contador en 1
    contador += 1
    
    # Mostrar el valor actual del contador
    print("Contador:", contador)

# Llamar a la función varias veces
incrementar_contador()
incrementar_contador()
incrementar_contador()
incrementar_contador()
incrementar_contador()
incrementar_contador()