"""LISTAS ES UNA COLECCION ORDENADA Y MODIFICABLE DE ELEMENTOS. SE DEFINE CON: ¨

sINTAXIX: """
# Definir listas correctamente
numeros = [1, 2, 3, 4, 5, 6]
nombres = ["Ana", "Leon", "Tomas"]

# Acceder a elementos
print(numeros[0])  # Imprime el primer número de la lista
print(nombres[-1])  # Imprime el último nombre de la lista

# Modificar un elemento
numeros[2] = 100  # Cambia el tercer elemento (índice 2) por 100

# Eliminar un elemento específico
numeros.remove(4)  # Elimina el número 4 de la lista

# Acceder a elementos de nombres
print(nombres[1])  # Imprime el segundo nombre
nombres.remove("Tomas")  # Elimina "Tomas" de la lista
print(nombres)  # Muestra la lista después de eliminar "Tomas"

# Ordenar la lista de mayor a menor
numeros = [11, 2, 30, 4, 55, 6]
numeros.sort() #menor a may
numeros.sort(reverse=True)  # may a menor
print(numeros)

# Agregar un número a la lista
numeros.append(60)
print(numeros)  # Muestra la lista con el nuevo número agregado


"""Ejercicios
1- Crear una lista con los nombres de 5 amigos e imprime el tercero de la lista
2- Dada la lista de edades de un grupo de personas:
edades =  [25,18,30,22,40,35]

a- Agrega la edad de una nueva persona.
b- Elimina la menor edad de la lista.
c- Ordena la lista de menor a mayor.
d- Imprime la lista resultante.

3-Crea un programa que pida al usuario 5 nombre y los almacene en una lista. Luego, muestre los nombres en orden inverso"""


# Crear una lista con los nombres de 5 amigos
amigos = ["Juan", "Pedro", "María", "Lucía", "Carlos"]

# Imprimir el tercer amigo (índice 2)
print(f"El tercer amigo en la lista es: {amigos[-2]}") # si cuento desde izquierda a dcha lo hago con signo - y si es lo contrario es entero

# Lista de edades
edades = [25, 18, 30, 22, 40, 35]

# a) Agregar una nueva edad
nueva_edad = 100
edades.append(nueva_edad)  # Agregar 100 a la lista

print(nueva_edad)

# b) Eliminar la menor edad
edades.remove(min(edades))
print(edades)

# c) Ordenar la lista de menor a mayor
edades.sort() #menor a may

print(edades)

# d) Imprimir la lista resultante
print(f"Lista de edades actualizada: {edades}")

#3 ejercicio

# Crear una lista vacía para almacenar los nombres
nombres = ["Juan", "Pedro", "María", "Lucía", "Carlos"]

# Mostrar los nombres en orden inverso

nombres.sort(reverse=True)
print(nombres)

