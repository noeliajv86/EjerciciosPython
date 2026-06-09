print("Hola, Noelia.¡Estoy aprendiendo Python!")
print("Prueba de escritura)")
print("Hola") 
nombre = input("¿Cómo te llamas?")
print(("Hola," + nombre))

# Pide la edad y el color favorito

edad = input ("¿Qué edad tenés?") 
color = input ("¿Cuál es tu color favorito?") 
print("Hola tenés" + edad)
print("y tu color favorito es" + color) 

#  *El guardian de la Edad*

edad_texto = input("¿Cuántos años tenés? ")
edad = int(edad_texto)
if edad >= 18:
   print("Eres mayor de edad, puedes entrar.")
else: 
   print("Lo siento, eres menor de edad, no puedes entrar.")

# *Lógica con if y else*

edad = int(input("¿Qué edad tenés?"))
if edad >= 18: 
   print("¡Bienvenido sos mayor de edad!")
else: 
   print("Lo siento, no podés entrar. Sos menor de edad.")

   # Primer Ejercicio de esta nueva ronda *Titulo: El Semáforo de la edad*

edad = int(input("¿Qué edad tenés?"))
if edad <13:
     print("Sos un niño/a.")
elif edad >= 13 and edad < 18:
      print("Sos un/a adolescente.")
elif edad >=18 and edad <=59:
      print("Sos un adulto/a.")
else: 
      print ("sos un adulto/a mayor.")

      #Etapas de la vida

edad = int(input("¿Qué edad tenés?"))
if edad <6:
    print("Sos un infante.")
elif edad >= 10 and edad < 11:
    print("Sos un/a pre-adolescente.")
elif edad >= 7 and edad < 9:
    print("Sos un niño/a")
elif edad >=12 and edad <18:
    print("Sos un/a adolescente.")
else:
    print ("sos un adulto/a.")

    