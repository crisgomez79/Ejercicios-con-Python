"""Hacer una calculadora básica
Operaciones disponibles: +, -, *, /
tengo que elegir una operación:
ejemplo: +
ingresar el primer número: 50
ingresar el segundo número: 10
Resultado: 60.0
"""
# Calculadora básica en Python

# Mostrar las operaciones disponibles
print("Operaciones disponibles: +, -, *, /")

# Pedir al usuario que elija una operación
operacion = input("Elige una operación: ")

# Pedir al usuario que ingrese dos números
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Realizar la operación según la elección del usuario
if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    if num2 != 0:  # Evitar la división por cero
        resultado = num1 / num2
    else:

        resultado = "Error: No se puede dividir por cero"
else:
    resultado = "Operación no válida"

# Mostrar el resultado
print("Resultado:", resultado)


###Otra forma de hacerlo### 
# Calculadora básica con match-case

# Mostrar las operaciones disponibles
print("Operaciones disponibles: +, -, *, /")
operacion = input("Elige una operación por favor: ")

# Solicitar al usuario los dos números
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Utilizar match-case para realizar la operación
match operacion:
    case "+":
        resultado = num1 + num2
    case "-":
        resultado = num1 - num2
    case "*":
        resultado = num1 * num2
    case "/":
        if num2 != 0:  # Verificar que no se divida por cero
            resultado = num1 / num2
        else:
            resultado = "Error: No se puede dividir por cero"
    case _:
        resultado = "Operación no válida"

# Mostrar el resultado de la operación
print("Resultado:", resultado)



