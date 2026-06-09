# Adivina el número:

print("Bienvenido al adivinador de número")
nombre = input("¿Cuál es tu nombre?")
print("Hola," + nombre)
número_secreto = 50
intento = int(input("¿Qué número es? "))
if intento < número_secreto:
        print("Demasiado Bajo")
elif intento > número_secreto:
        print("Demasiado Alto")
else:
        print("¡Correcto!")


 # Validar Contraseña:

print("Registrese")
longitud_deseada = 10
ingreso = input("Coloque contraseña: ")
if len(ingreso) <longitud_deseada:
                print ("Contraseña Demasiado Corta")
elif len(ingreso) >longitud_deseada:
                print("Contraseña Demasiado Larga")
else:
                print("Contraseña Adecuada")