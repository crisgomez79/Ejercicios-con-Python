"""Realizar un programa que sea el juego del ahorcado, ejemplo:
#Infrese la palabra la cual van adivinar: PYTHON
(¨_¨, ¨_¨, ¨_¨, ¨_¨, ¨_¨, ¨_¨)
#Ingrese una letra: a
#Te quedan 5 vidas 
(¨_¨, ¨_¨, ¨_¨, ¨_¨, ¨_¨, ¨_¨)
Ingrese una letra: p
(¨p", ¨_¨, ¨_¨, ¨_¨, ¨_¨, ¨_¨)
Te quedan 4 vidas
Ingrese una letra: y
(¨p", ¨y, ¨_¨, ¨_¨, ¨_¨, ¨_¨)
 y así suscesivamente hasta completar la palabra PYTHON"""

def juego_ahorcado():
    # Se solicita la palabra a adivinar y se pasa a mayúsculas para evitar problemas de comparación.
    palabra = input("Ingrese la palabra a adivinar: ").strip().upper()
    
    # Se genera una lista con "_" para representar cada letra oculta.
    display = ["_" for _ in palabra]
    
    # Se define el número de vidas igual a la cantidad de letras que nos quedan, es decir cantidad de elementos o de  objeto.
    vidas = len(palabra)
    
    # Conjunto para almacenar las letras ya ingresadas y evitar repeticiones.
    letras_usadas = set() #EJEMPLO 
    """Creación de un set a partir de una lista con elementos duplicados
 ista = [1, 2, 2, 3, 4, 4, 5]
 onjunto = set(lista)
 rint(conjunto)  # Salida: {1, 2, 3, 4, 5}"""

    while vidas > 0 and "_" in display:
        # Se muestra el estado actual de la palabra.
        print("\n" + " ".join(display))
        
        # Se solicita una letra al usuario y se normaliza a mayúsculas.
        letra = input("Ingrese una letra: ").strip().upper()
        
        # Se verifica si la letra ya fue ingresada.
        if letra in letras_usadas:
            print("Ya ingresaste esa letra. Intenta con otra.")
            continue
        letras_usadas.add(letra)
        
        # Si la letra está en la palabra, se actualiza el display en todas sus ocurrencias.
        if letra in palabra:
            for i, char in enumerate(palabra):
                if char == letra:
                    display[i] = letra
        
        # Se descuenta una vida por cada intento, sin importar si la letra es correcta o no.
        vidas -= 1
        print(f"Te quedan {vidas} vidas")
    
    # Al salir del ciclo, se verifica si el usuario completó la palabra.
    if "_" not in display:
        print("\n¡Felicidades, ganaste!")
    else:
        print("\n¡Perdiste! La palabra era:", palabra)

if __name__ == "__main__":
    juego_ahorcado()