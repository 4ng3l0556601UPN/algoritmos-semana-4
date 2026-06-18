# Python no tiene variables estáticas nativas. Simúlalas usando un atributo de la propia función para generar IDs únicos
# Definir una función para generar IDs únicos
def generar_id():

    # Verificar si la función ya tiene el atributo contador
    if not hasattr(generar_id, "contador"):

        # Inicializar el contador en 0 la primera vez
        generar_id.contador = 0

    # Incrementar el contador en 1
    generar_id.contador += 1

    # Devolver el ID generado
    return generar_id.contador

# Llamar a la función varias veces para generar IDs únicos
print("ID:", generar_id())
print("ID:", generar_id())
print("ID:", generar_id())
print("ID:", generar_id())
print("ID:", generar_id())
# def generar_id(): → crea una función llamada generar_id.
# hasattr(generar_id, "contador") → verifica si la función ya tiene un atributo llamado contador.
# generar_id.contador = 0 → crea el atributo la primera vez que se ejecuta la función.
# generar_id.contador += 1 → incrementa el contador en cada llamada.
# return generar_id.contador → devuelve el ID generado.