print("Hola Mundo")
print(2 + 4)
nombre = "Juan"
edad = 25
print("Hola", nombre, "tienes", edad, "años")
for i in range(5):
    print("Contando:", i)
    # 1. Creamos una "caja" llamada mensaje y guardamos un texto
mensaje = "¡Hola, futuro programador!"

# 2. Creamos otra "caja" llamada numero y guardamos un número
numero = 42

# 3. Usamos las cajas para mostrar algo
print(mensaje)
print("Mi número favorito es:", numero)
mi_nombre="Noelia"
print("Me llamo",mi_nombre)
# Crear variables
nombre = "Noe"
edad = 39
anio_nacimiento = 1986

# Mostrar información combinada
print("Hola, soy", nombre)
print("Tengo", edad, "años")
print("Nací en el año", anio_nacimiento)

# ¡Un cálculo simple!
print("En 10 años tendré:", edad + 10, "años")
# Mis datos
mi_nombre = "Noe"
mi_edad = 39
mi_anio_nacimiento = 1986

# Calculadora automática
# La computadora puede calcular el año en que tendré 100 años
falta_para_100 = 100 - mi_edad
anio_cumple_100 = mi_anio_nacimiento + falta_para_100

print("Me llamo", mi_nombre)
print("Tengo", mi_edad, "años.")
print("Faltan", falta_para_100, "años para tener 100.")
print("Cumpliré 100 años en el año:", anio_cumple_100)
# La computadora te pregunta
tu_nombre = input("¿Cómo te llamas? ")
tu_edad_texto = input("¿Cuántos años tienes? ")

# Convertimos el texto a número para poder sumar
tu_edad = int(tu_edad_texto)

# Cálculo
futuro = tu_edad + 10

print("Hola", tu_nombre, "¡en 10 años tendrás", futuro, "años!")
print("me llamo Noelia")
print("son las 19:37")
# Pide tu nombre
nombre = input("¿Cómo te llamas? ")

# Pide tu edad
edad_texto = input("¿Cuántos años tienes? ")
edad = int(edad_texto)

# Condición: si tienes 30 años o más
if edad >= 30:
    print("Hola", nombre, "¡eres una adulta experimentada!")
else:
    print("Hola", nombre, "¡eres joven y llena de energía!")

    # Otra condición: si tu año de nacimiento es anterior a 1990
    anio_nacimiento = 2026 - edad
    if anio_nacimiento < 1990:
        print("Naciste antes de 1990, ¡tienes experiencia!")
    else:
        print("Naciste después de 1990, ¡eres de la era moderna!")
    
    edad = int(input("¿Cuántos años tienes? "))

if edad >= 19:
    print("Eres un Adulto.")
else: 
    print("Eres un Adolescente.")

    edad = int(input("¿Cuántos años tienes?"))

if edad >= 13:
    print("Eres imputable")
else:
        print("Eres inimputable")
        # Otra condición: si tu año de nacimiento es anterior a 1990
anio_nacimiento = 2026 - edad
if anio_nacimiento < 1990:
    print("Naciste antes de 1990, ¡tienes experiencia!")
else:
    print("Naciste después de 1990, ¡eres de la era moderna!")