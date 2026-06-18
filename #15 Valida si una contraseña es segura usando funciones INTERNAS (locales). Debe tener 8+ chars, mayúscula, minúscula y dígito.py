#
# Función principal para validar la contraseña
def validar_contrasena(contrasena):

    # Función local para verificar longitud mínima
    def tiene_longitud():
        return len(contrasena) >= 8

    # Función local para verificar si tiene mayúsculas
    def tiene_mayuscula():
        for caracter in contrasena:
            if caracter.isupper():
                return True
        return False

    # Función local para verificar si tiene minúsculas
    def tiene_minuscula():
        for caracter in contrasena:
            if caracter.islower():
                return True
        return False

    # Función local para verificar si tiene dígitos
    def tiene_digito():
        for caracter in contrasena:
            if caracter.isdigit():
                return True
        return False

    # Verificar todas las condiciones
    if (tiene_longitud() and
        tiene_mayuscula() and
        tiene_minuscula() and
        tiene_digito()):
        return True
    else:
        return False


# Solicitar al usuario una contraseña
clave = input("Ingrese una contraseña: ")

# Validar la contraseña
if validar_contrasena(clave):
    print("La contraseña es segura.")
else:
    print("La contraseña NO es segura.")
    print("Debe tener:")
    print("- Al menos 8 caracteres")
    print("- Una letra mayúscula")
    print("- Una letra minúscula")
    print("- Un número")
#validar_contrasena() → es la función principal.
# Dentro de ella se crean funciones locales:
# tiene_longitud() → verifica que tenga 8 o más caracteres.
# tiene_mayuscula() → busca una letra mayúscula.
# tiene_minuscula() → busca una letra minúscula.
# tiene_digito() → busca un número.
# Si todas las funciones devuelven True, la contraseña es segura.
# Si alguna condición falla, la contraseña no es segura.