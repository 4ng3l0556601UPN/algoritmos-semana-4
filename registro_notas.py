# Diccionario global compartido
registro = {
    "estudiantes": {},      # nombre -> {"notas": [], "promedio": float}
    "asignaturas": set()
}


def agregar_estudiante(nombre: str):
    if nombre not in registro["estudiantes"]:
        registro["estudiantes"][nombre] = {"notas": [], "promedio": 0.0}


def agregar_nota(nombre: str, asignatura: str, nota: float):
    agregar_estudiante(nombre)
    registro["estudiantes"][nombre]["notas"].append((asignatura, nota))
    registro["asignaturas"].add(asignatura)
    actualizar_promedio(nombre)


def actualizar_promedio(nombre: str):
    notas = registro["estudiantes"][nombre]["notas"]
    if notas:
        promedio = sum(n[1] for n in notas) / len(notas)
        registro["estudiantes"][nombre]["promedio"] = round(promedio, 2)


def mostrar_registro():
    print("\n=== REGISTRO DE NOTAS ===")
    for nombre, datos in registro["estudiantes"].items():
        print(f"\n📌 {nombre} (Promedio: {datos['promedio']})")
        for asig, nota in datos["notas"]:
            print(f"   • {asig}: {nota}")
    print(f"\nAsignaturas: {', '.join(sorted(registro['asignaturas']))}")


# Uso del sistema
agregar_nota("Ana", "Matemáticas", 9.5)
agregar_nota("Ana", "Historia", 8.0)
agregar_nota("Luis", "Matemáticas", 7.0)
agregar_nota("Luis", "Física", 8.5)
agregar_nota("Ana", "Física", 9.0)

mostrar_registro()