#calcular la circunferencia de un círculo con PI

Pi = 3.1416
def cal_circunferencia(radio):
    circunferencia = 2 * Pi * radio  #circunferencia es local
    return circunferencia

radio_usuario = float(input("Ingrese el radio del círculo: "))

#funcion y retorno
resultado = cal_circunferencia(radio_usuario)

print("Circunferencia del círculo es:", resultado)   