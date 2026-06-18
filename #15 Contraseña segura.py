def validar(password):

    def tiene_mayuscula():
        return any(c.isupper() for c in password)

    def tiene_minuscula():
        return any(c.islower() for c in password)

    def tiene_numero():
        return any(c.isdigit() for c in password)

    return (
        len(password) >= 8
        and tiene_mayuscula()
        and tiene_minuscula()
        and tiene_numero()
    )

clave = input("Ingrese una contraseña: ")

if validar(clave):
    print("Contraseña segura")
else:
    print("Contraseña insegura")
