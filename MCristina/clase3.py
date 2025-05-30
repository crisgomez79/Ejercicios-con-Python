
 
""" BUCLES Y ESTRUCTURAS DE DATOS 
Permiten repetir una accion multiples veces

BUCLES WHILE
Ejemplo:"""

contador = 1
while contador <= 5:
    print(f"numero: {contador}")
    contador += 1 ##TENER CUIDADO EN LA IDENTACION POR QUE SI NO SE HACE INFINITOS NROS, SE PARA CON CONTROL + 2C

#EJERCICIO
#Escribe un programa que pida un numero y cuente desde el 2, hasta ese numero usando while


    # Pedimos al usuario que ingrese un número
numero = int(input("Ingresa un número: "))

# Inicializamos el contador desde 2
contador = 2

# Utilizamos un bucle while para contar hasta el número ingresado
while contador <= numero:
  print(f"numero: {contador}")
  contador += 15


  """ESCRIBE UN PROGRAMA QUE RECORRA UNA FRASE INGRESA POR EL USUARIO Y CUENTE CUANTAS LETRAS TIENE LA FRASE"""

  # Solicita al usuario que ingrese una frase
frase_usuario = input("Ingresa una frase: ")

# Filtra solo las letras (ignora espacios, números y signos de puntuación)
letras_solo = ''.join(caracter for caracter in frase_usuario if caracter.isalpha())

# Cuenta las letras usando len()
cantidad_letras = len(letras_solo)

# Muestra el resultado
print(f"La cantidad de letras en la frase es: {cantidad_letras}")

#Otra forma de hacerlo

while True:  # Bucle infinito hasta que el usuario decida salir
    frase_usuario = input("Ingresa una frase (o escribe 'salir' para terminar): ")
    
    # Si el usuario escribe 'salir', rompemos el bucle
    if frase_usuario.lower() == 'salir':
        print("Programa finalizado.")
        break  # Sale del bucle

    # Filtra solo las letras (ignora espacios, números y signos de puntuación)
    letras_solo = ''.join(caracter for caracter in frase_usuario if caracter.isalpha())

    # Cuenta las letras usando len()
    cantidad_letras = len(letras_solo)

    # Muestra el resultado
    print(f"La cantidad de letras en la frase es: {cantidad_letras}\n")
    
