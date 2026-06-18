def convertir_nota(nota):
    #if es SI la nota es entre 18 y 20, devuelve "AD" 
    if 18 <= nota <= 20:
        #Devuelve "nota"
        return "AD"
    #if es SI la nota es entre 15 y 17, devuelve "A"
    elif 15 <= nota <= 17: # Se ejecuta solo si la condición anterior fue falsa.
        return "A"
    #if es SI la nota es entre 12 y 14, devuelve "B"
    elif 12 <= nota <= 14:
        return "B"
    #if es SI la nota es 11, devuelve "C"
    elif nota == 11:
        return "C"
    #if es SI la nota es entre 0 y 10, devuelve "Desaprobado"
    # si no, eentonces si.
    elif 0 <= nota <= 10:
        return "Desaprobado"
    else: # en cualquier otro caso colocamos una nota invalida mayor a 20 o menor a 0.
        return "Nota inválida"

# Prueba de la función
# Solicita al usuario que ingrese una nota del 0 al 20
nota = int(input("Ingrese una nota del 0 al 20: "))
# Imprime la calificación correspondiente a la nota ingresada
print("Calificación:", convertir_nota(nota))