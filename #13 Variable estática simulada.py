def generar_id():

    if not hasattr(generar_id, "contador"):
        generar_id.contador = 0

    generar_id.contador += 1

    return generar_id.contador

print(generar_id())
print(generar_id())
print(generar_id())
