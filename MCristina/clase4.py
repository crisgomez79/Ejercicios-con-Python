"""def #Se usa para crear una función y darle un nombre.
    #Permite organizar el código y evitar repeticiones."""

def saludar():
    print("¡Hola! Bienvenido a Python.")

# Llamamos a la función
saludar()




#FUNCIONES 
#Es un bloque de codigo organizado   
#seintasis_ def saludar() :
    #print("hola a todos")





    #EJERCICIOS
    #Crea una función que imprima "python, es genial" y llamala 3 veces

def imprimir_mensaje():
    print("python, es genial")

# Llamar a la función tres veces
imprimir_mensaje()
imprimir_mensaje()
imprimir_mensaje()

 #Como harias esto para automatizarlo
def imprimir_mensaje():
    print("python, es genial")

# Usamos un bucle para llamar a la función 3 veces
for _ in range(3):
    print("PYTHON, ES GENIAL")

"""Funciones con argunmentos, estos son datos que reciben las funciones para realizar operaciones
Sintaxis:"""

def saludar(nombre):
    print("hola, ", nombre)
    
saludar("Luciano")

#EJERCICIO
#CREAR UNA FUNCION DE PRESENTACION QUE DIGA TU NOMBRE, EDAD Y LO QUE ESTUDIAS/TRABAJAS.
##REALIZAR UNA FUNCION QUE SUME DOS NUMEROS Y MUESTRE EL RESULTADO.
###DEFINIR UNA FUNCION QUE RECIBA UNA EDAD Y DIGA SI LA PERSONA ES MAYOR  O MENOR DE EDAD.
####CON LA FUNCION DEL PUNTO ANTERIOR, REALIZAR EL CÓDIGO PARA QUE IMPRIMA EL NUMERO Y DIGA SI ES PARA O IMPAR.
#####CREAR UNA FUNCION QUE IMPRIMA LA TABLA DE MULTIPLICAR DEL NUMERO INGRESADO 



#Resultados:

def presentacion():
    nombre = "Cristina"  # Aquí pones tu nombre
    edad = 46        # Aquí pones tu edad
    estudio = "Python para principiantes"  # O lo que estudias o trabajas
    trabajo = "Ministerio de Seguridad"

    print(f"Hola, mi nombre es {nombre}. Tengo {edad} años y actualmente soy {estudio}.")



# Llamamos a la función para que imprima 
presentacion()


##Resultado 

def sumar_dos_numeros(num1, num2):
    resultado = num1 + num2
    print(f"La suma de {num1} y {num2} es: {resultado}")

# Llamamos a la función y le pasamos dos números
sumar_dos_numeros(5, 7)



###Resultado 
def verificar_mayoria_edad(edad):
    if edad >= 18:
        print(f"La persona con {edad} años es mayor de edad.")
    else:
        print(f"La persona con {edad} años es menor de edad.")

# Llamamos a la función con diferentes edades para probar
verificar_mayoria_edad(17)
verificar_mayoria_edad(20)



####Resultado
def verificar_mayoria_edad(edad):
    if edad >= 18:
        print(f"La persona con {edad} años es mayor de edad.")
    else:
        print(f"La persona con {edad} años es menor de edad.")
    
    # Verificar si la edad es par o impar
    if edad % 2 == 0:
        print(f"El número {edad} es par.")
    else:
        print(f"El número {edad} es impar.")

# Llamamos a la función con diferentes valores para probar
verificar_mayoria_edad(17)
verificar_mayoria_edad(20)
verificar_mayoria_edad(25)
verificar_mayoria_edad(30)

##otra forma de realizarlo 
def mayor_menor (edad):
    if edad >= 18 and edad % 2 == 0:
        print(f"La persona   con {edad} años es mayor de edad y es numero par.")
    elif edad >= 18 and edad % 2 == 1:
        print(f"La persona  con {edad} años es mayor de edad y es numero impar.")
    elif edad >= 18 and edad % 2 == 0:
        print(f"La persona  con {edad} años es mayor de edad y es numero impar.")


#####Resultado
def tabla_de_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):  # Iteramos del 1 al 10
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

#Otra forma de ralizarlo 


# Llamamos a la función con un número de ejemplo
tabla_de_multiplicar(5)  # Puedes cambiar el número para ver otra tabla

"""Funciones con return"""

def sumar_print(a,b):
    print(f"El resultado de la suma con print es: {a+b}")

    resultado = sumar_print(5,3)
    print(f"El resultado es: {resultado}")
    
def sumar_return(a,b):
    return f"El resultado return es: {a+b}"

resulatdo1 = sumar_return(10,5)
print(resulatdo1)

"""Ejercicio

#Escribe una funcion que reciba cuatro numeros y devuelva el mayor.
##Crea una funcion que reciba el precio de un producto y el porcentaje de descuento, y devuelva el precio final.}
###Escribe una funcion que reciba un mes y un dia del mes, y devuelva auántos días fatan para que termine el año."""

#Primero

def mayor_de_cuatro(num1, num2, num3, num4):
    return max(num1, num2, num3, num4)

# Llamamos a la función con cuatro números
print(mayor_de_cuatro(10, 25, 8, 40))  # Salida: 40



#Segundo
def calcular_precio_final(precio, descuento):
    return precio - (precio  * (descuento / 100))

print(calcular_precio_final(20000,35))

# Llamamos a la función con un precio y un porcentaje de descuento
precio_con_descuento = calcular_precio_final(1000, 20)  # Ejemplo: Producto de $1000 con 20% de descuento
print(f"El precio final con descuento es: ${precio_con_descuento:.2f}")

#Tercero


import datetime

def dias_para_fin_de_anio(mes, dia):
    # Obtener la fecha actual (año actual, mes y día proporcionados)
    fecha_actual = datetime.date(datetime.date.today().year, mes, dia)
    
    # Obtener la fecha del último día del año (31 de diciembre del mismo año)
    fin_de_anio = datetime.date(datetime.date.today().year, 12, 31)
    
    # Calcular la diferencia en días entre las dos fechas
    dias_restantes = (fin_de_anio - fecha_actual).days
    
    return dias_restantes

# Ejemplo de uso
mes = 2  # Febrero
dia = 20  # Día 20
print(f"Faltan {dias_para_fin_de_anio(mes, dia)} días para que termine el año.")

#Otra forma de hacerlo
from datetime import date

def dias_hasta_fin_de_ano(mes, dia):
    # Obtenemos el año actual
    anio = date.today().year
    # Creamos la fecha a partir del mes y día indicados
    fecha_actual = date(anio, mes, dia)
    # Definimos la fecha del 31 de diciembre del mismo año
    fin_de_ano = date(anio, 12, 31)
    # Calculamos la diferencia en días
    dias_faltantes = (fin_de_ano - fecha_actual).days
    return dias_faltantes

if __name__ == "__main__":
    # Ejemplo de uso:
    mes = 2
    dia = 20
    print(f"Faltan {dias_hasta_fin_de_ano(mes, dia)} días para terminar el año.")

