"""Operadores matematicos
suma: +
resta: -
multiplicacion *
division /
division entera //
modulo o resto %
potencia **
"""
#Ejemplo 
numeroa = 7504
numerob = 12
print(numeroa % numerob)
5

#EJERCICIO 1

#Crea un programa que le pida dos números al usuario y muestre su suma, resta, multiplicacion y division. 


# Pedir dos números al usuario
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

# Mostrar los resultados 
print(f"Suma: {numero1} + {numero2} = {numero1 + numero2}")
print(f"Resta: {numero1} - {numero2} = {numero1 - numero2}")
print(f"Multiplicación: {numero1} × {numero2} = {numero1 * numero2}")
print(f"Division: {numero1} / {numero2} = {numero1 / numero2}")

#Otra forma de hacerlo mas facil

print("El resultado de la suma es: ", numero1 + numero2)
print("El resultado de la resta es: ", numero1 - numero2)
print("El resultado de la multiplicación es: ", numero1 * numero2)
print("El resultado de la divisió es: ", numero1 / numero2)


"""Operadores relacionales
igual a ==  ejemplo a == b
Diferebtes de       a !=
Mayo que            a > b
Menor que            a < b
Mayor e igual que    a >= b
"""
#Ejemplo
nro1 = 15
nro2 = 25
print (nro1 > nro2)

"""Ejercicio
#Escribe un programa que:
1. Solicite al usuario dos numeros.
2. Realice las operaciones matematicas basicas: suma, resta, mult, division. 
3. Compare los dos numeros utilizando operadores relacionales.
Muestre los resultados en pantalla.
"""
# Pedir dos números al usuario
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

#Operaciones 
suma = num1 + num2
resta = num1 - num2
multiplicación = num1 * num2
división = num1 / num2

#Comparo
print ("El resultado es: ", num1 > num2)

#Resultados
print("El resultado de la suma es: ", num1 + num2)
print("El resultado de la resta es: ", num1 - num2)
print("El resultado de la multiplicación es: ", num1 * num2)
print("El resultado de la divisió es: ", num1 / num2)
