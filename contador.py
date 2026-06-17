def crear_contador(inicial: int = 0):
    """Crea un contador independiente usando closure."""
    contador = inicial
    
    def incrementar():
        nonlocal contador
        contador += 1
        return contador
    
    def decrementar():
        nonlocal contador
        contador -= 1
        return contador
    
    def valor_actual():
        return contador
    
    return incrementar, decrementar, valor_actual


# Uso
inc1, dec1, val1 = crear_contador(10)
inc2, dec2, val2 = crear_contador(5)

print(inc1())  # 11
print(inc1())  # 12
print(dec1())  # 11
print(val1())  # 11

print(inc2())  # 6
print(inc2())  # 7
print(val2())  # 7