
##Variables string o cadena de texto##
""" maria
cristina
gomez, comentarios que no van en la misma linea """
jugador = 'Messi' # variable de tipo string o de cade a de texto,va entre comillas de texto, el igual nos guarda el valor de la variable, si hay dos == nos compara
saludo = "hola"
##Variable numerica de tipo entero##
numero = 10 # si yo al numero lo coloco entre comillas me lo guarda como texto

#Variable numerica de tipo flotante o float##
numero2 = 0.10

##variable booleana##
variavble_boleana = True
variavble_boleana2 = False

print(jugador)
print("Hola" + jugador)
print(saludo)
print(numero2)

saludos = ("hola" , "como estas")
print(saludos)


""" EJERCICIOS:
Crear un programa que almacene tu nombre, edad, 
y ciudad en variables y luego imprima un mensaje con estos datos """

# variables nombre, edad y ciudad
nombre = "Cristina"  
edad = 46
ciudad = "Godoy Cruz"

# Imprimir  mensaje con los datos
print(f"Hola, mi nombre es {nombre}, tengo {edad} años y vivo en {ciudad}.")

print ("Hola soy", nombre, "tengo", edad, "años y soy de la ciudad de", ciudad)

mensaje = "Hola, mi nombre es %s, tengo %d años, vivo en %s." % (nombre, edad, ciudad)
print(mensaje)

"""EJERCICIO 2
Escribe palabras como harías un programa que le pida al usuario su nombre, 
edad y luego le muestre un mensaje
con esos datos. RECORDAR: noes un código si no que escrito, 
es decir, solamente enunciado en texto."""

# Pedir el nombre al usuario
nombre = input("¿Cuál es tu nombre? ")

# Pedir la edad al usuario y convertirla en un número entero
edad = input("¿Cuántos años tienes? ")

# Mostrar el mensaje con los datos ingresados
print(f"Hola, {nombre}. Tienes {edad} años, bienvenida a la primer clase de python.")



#Otra forma de hacerlo 
nombre = input("¿Cuál es tu nombre? ")