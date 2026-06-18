def torre_hanoi(n: int, origen: str = "A", aux: str = "B", destino: str = "C", movimientos=None):
    if movimientos is None:
        movimientos = [0]  # Lista mutable como contador
    
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
        movimientos[0] += 1
        return
    
    torre_hanoi(n-1, origen, destino, aux, movimientos)
    print(f"Mover disco {n} de {origen} a {destino}")
    movimientos[0] += 1
    torre_hanoi(n-1, aux, origen, destino, movimientos)


def verificar_hanoi(n: int):
    movimientos = [0]
    print(f"\n--- Torre de Hanói con {n} discos ---\n")
    torre_hanoi(n, movimientos=movimientos)
    esperado = (1 << n) - 1  # 2^n - 1
    print(f"\nTotal movimientos: {movimientos[0]}")
    print(f"Esperado: {esperado} → {'✅ Correcto' if movimientos[0] == esperado else '❌ Error'}")


verificar_hanoi(3)