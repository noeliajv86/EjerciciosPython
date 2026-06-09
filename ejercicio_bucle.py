print("Bienvenido al programa de Par o Impar. Para salir, escribe 'salir'.")

while True:
    número = input("\nIntroduce un número: ")

    if número.lower() == 'salir':
        print("Programa finalizado.")
        break
    try:
        valor = int(número)
        if valor % 2 == 0:
            print("Es PAR.")
        else:
            print("Es IMPAR")
    except ValueError:
        print("Error: Eso no es un número entero. Intenta de nuevo")




        