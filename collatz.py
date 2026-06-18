from functools import lru_cache

@lru_cache(maxsize=None)
def collatz_pasos(n: int) -> int:
    """Retorna la cantidad de pasos para llegar a 1."""
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + collatz_pasos(n // 2)
    else:
        return 1 + collatz_pasos(3 * n + 1)


def analizar_collatz(hasta: int = 1000):
    max_pasos = 0
    num_max = 1
    
    print(f"Analizando Collatz del 1 al {hasta}...\n")
    
    for i in range(1, hasta + 1):
        pasos = collatz_pasos(i)
        if pasos > max_pasos:
            max_pasos = pasos
            num_max = i
    
    print(f"Número con más pasos: {num_max} ({max_pasos} pasos)")
    return num_max, max_pasos


analizar_collatz(1000)