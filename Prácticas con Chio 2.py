# Poniendo las comillas al número pasa de float a str.
# Usando la función int se convierte el número en entero.
# No se puede convertir letras a números  usando int.

edad = "39"
edad = int(edad)
tipo_edad = type(edad)
print(tipo_edad)

# Operadores Aritméticos: 
#                        Suma
#                        Resta 
#                        Multiplicación
#                        División
#                        Módulo
#                        Exponente 
#                        División Entera

número1 = 39
número2 = 10

print("Suma", número1 + número2)
print("Resta", número1 - número2)
print("Multiplicar", número1 * número2)
print("Dividir", número1 / número2)
print("Módulo", número1 % número2)
print("Exponente", número1 ** número2)
print("Dividir Entero", número1 // número2) 

# Nueva Función Imput: leé lo que el usuario escribe
# hasta que de un enter y ese texto lo regresa como 
# resultado de la ejecución de la función. Se combina con
# int para trnsformar el rsultado en un entero 


# Ejercicio de URI online judge problems&contests

# 1. Pedimos los datos al usuario de forma clara
# Convertimos a entero (int) lo que el usuario escribe
A = int(input("Introduce el valor para A: "))
B = int(input("Introduce el valor para B: "))

# 2. Realizamos las operaciones matemáticas y las guardamos en variables nuevas
suma = A + B
resta = A - B

# 3. Mostramos los resultados en la pantalla
print("El resultado de la suma (x) es:", suma)
print("El resultado de la resta (x) es:", resta)

# 4. Condiciones (Estructuras de Control o Controladores de flujo)

número = float(input())

if número >= 0 and número <= 25:
    print("Intervalo [0,25]")
elif número <0:
    print("Fuera de intervalo")
elif número <= 50:
    print("Intervalo (25,50]")
elif número <= 75:
    print("Intervalo (50,75]")
elif número <= 100:
    print("Intervalo (75,100]")
else:
    print("Fuera de intervalo")