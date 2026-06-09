print("Bienvenido al verificador de números pares o impares")
print("Escribe 'salir para terminar el programa.\n")

# 1. Pedimos el primer número ANTES de entrar al bucle.

número = input("Ingresa un nuúmero: ")

# 2. El bucle: Mientras el usuario NO haya escrito "salir".

while número != "salir":

    # Convierto el texto a número para poder calcular
    # (Si el usuario escribió algo que no es número ni "salir" esto da error, pero por ahora
    # asumimos que escribe bien.)
    valor = int(número)

    # Lógica de decisión (lo que ya sabés)
    if valor %2 == 0:
        print(f"El {valor} es PAR")
    else:
        print(f"El {valor} es IMPAR.")

        # IMPORTANTE: pedimos el siguiente número al FINAL del bucle.
        # Si no hacemos esto el bucle se repetiría eternamente con el mismo número.

print("\n---")
número = input("Ingresa otro número (o 'salir' para terminar):")

print("\n¡Programa terminado! Hasta luego.")

print("Bienvenido al verificador de números pares o impares.")
print("Escribe 'salir' para terminar el programa.\n")

# 1. Pedimos el primer número ANTES de entrar al bucle
numero = input("Ingresa un número: ")

# 2. El bucle: Mientras el usuario NO haya escrito "salir"
while numero != "salir":

    # Convierto el texto a número para poder calcular
    # (Si el usuario escribió algo que no es número ni "salir", esto dará error,
    # pero por ahora asumimos que escribe bien)
    valor = int(numero)

    # Lógica de decisión (lo que ya sabés)
    if valor % 2 == 0:
        print(f"El {valor} es PAR.")
    else:
        print(f"El {valor} es IMPAR.")

        # IMPORTANTE: Pedimos el siguiente número al FINAL del bucle
        # Si no hacemos esto, el bucle se repetiría eternamente con el mismo número.
print("\n---")
numero = input("Ingresa otro número (o 'salir' para terminar): ")
print("\n¡Programa terminado! Hasta luego.")

print("Inicio del test")
numero = input("Escribe un número: ")
print(f"Valor capturado: {numero}")
print("Fin del test")

contador = 0
print("Inicio")

while contador < 3:
    print(f"Contador: {contador}")
    # ¡FALTA LA LÍNEA QUE SUMA 1!
    # contador += 1  <-- Esto es lo que falta en tu código original

    print("Fin")

    while True:
    numero = input("\nIntroduce un número: ")  # 1. Pide el número AL INICIO de cada vuelta

    if numero.lower() == 'salir':
        break  # 2. Sale del bucle si es 'salir'

    # 3. El resto del código se ejecuta solo si no es 'salir'
    valor = int(numero)
    # ... (lógica par/impar)

    print("INICIO DEL BUCLE")
contador = 0

while contador < 3:
    print(f"Vuelta numero: {contador}")
    numero = input("Escribe un número: ")

    # Aquí está la clave: actualizamos el contador
    contador = contador + 1

    if numero == 'detener':
        print("¡Detenido por el usuario!")
        break

    print("FIN DEL BUCLE")
    
harina = int(input("Dame la harina en gramos: "))
agua = 28*harina/100
sal = 1.8*harina/100
manteca =10*harina/100

print("Para hacer tortillas con", harina, "gramos de harina necesarios.")
print(agua, "gramos de agua.")
print(sal "gramos de sal")
print(manteca, "gramos de manteca")
