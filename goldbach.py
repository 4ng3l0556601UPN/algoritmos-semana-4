def es_primo(n):
    """Verifica si un número es primo."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def goldbach(n):
    """Encuentra todas las parejas de primos que suman n."""
    if n % 2 != 0 or n <= 2:
        return []
    
    pares = []
    for i in range(2, n//2 + 1):
        if es_primo(i) and es_primo(n - i):
            pares.append((i, n - i))
    return pares


def verificar_goldbach_hasta(limite):
    """Verifica la conjetura para todos los pares hasta el límite."""
    print(f"Verificando Goldbach hasta {limite}:\n")
    for num in range(4, limite + 1, 2):
        pares = goldbach(num)
        if pares:
            print(f"{num:2d} = {pares[0][0]} + {pares[0][1]}")
        else:
            print(f"¡FALLÓ para {num}!")
            return
    print(f"\n✅ Conjetura verificada correctamente hasta {limite}")


verificar_goldbach_hasta(150)