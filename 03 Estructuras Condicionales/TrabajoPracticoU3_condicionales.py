#Ejercicio 1
edad= int(input("Ingrese su edad: "))
if edad >= 18:
    print("Usted, es mayor de edad")
else:
    print("Usted, es menor de edad")
#Ejercicio 2
nota=float(input("Ingrese su nota:"))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
#Ejercicio 3
numero=int(input("Ingrese un numero par: "))
if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("El numero es impar")
    print("Por favor, ingrese un numero par")
#Ejercicio 4
edad=int(input("Cuál es tu edad? :"))

if edad < 12:
    print(f"Categoria: Niño/a, tiene {edad} años")
elif edad >= 12 and edad < 18:
    print(f"Categoria: Adolescente, tiene {edad} años")
elif edad >= 18 and edad < 30:
    print(f"Categoria: Adulto/a Joven, tiene {edad} años") 
else:
    print(f"Categoria: Adulto/a, tiene {edad} años")  
#Ejercicio 5
contrasena=(input("Ingrese una contraseña: "))
if len(contrasena) >=8 and len(contrasena) <= 14:
    print("Ingresò una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
#Ejercicio 6
import random
from statistics import mode, median, mean

numeros_aleatorios=[random.randint(1, 100)for i in range(50)] #Generar 50 nros aleatorios, entre 1 y 100
media = mean(numeros_aleatorios)
#Media (MEAN) es la suma de todos los valores dividida por la cantidad de valores

mediana= median(numeros_aleatorios)
#Mediana (MEDIAN) es el valor central en un conjunto de datos ordenado, 
#o el promedio de los dos valores centrales si el conjunto tiene un número par de datos. 

moda= mode(numeros_aleatorios)
#Moda (MODE) es el valor que aparece con mayor frecuencia en un conjunto de datos

print("Numeros aleatorios: ", numeros_aleatorios)
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

#comparaciones
if media > mediana > moda:
    print("Distribucion con sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Distribucion con sesgo negativo (a la izquierda)")
elif media == mediana == moda:
    print("Distribución sin sesgo ")
else:
    print("La distribucion no cumple exactamente con los criterios dados")            
#Ejercicio 7
frase_palabra=str(input("Ingrese una frase o palabra: "))
vocales=("AEIOUaeiou")
if frase_palabra.endswith(vocales): #Para revisar si una palabra termina en algo, Python tiene la función .endswith()
    print(f"{frase_palabra}!")
else:
    print(frase_palabra)
#Ejercicio 8
nombre=str(input("Ingrese su nombre: "))
elegir_formato_nombre=int(input("Ingrese 1 si quiere su nombre en mayÚsculas, 2 si lo quiere en minusculas, 3 si lo quiere con la primer letra en mayuscula: "))
if elegir_formato_nombre == 1:
    print(f"Su nombre en MAYÚSCULAS: {nombre.upper()}")
elif elegir_formato_nombre == 2:
    print(f"Su nombre en minusculas {nombre.lower()}")
elif elegir_formato_nombre == 3:
    print(f"Su nombre con la Primer letra Mayuscula {nombre.title()}")        
else:
    print("Opción inválida, por favor ingrese 1, 2 o 3")
#Ejercicio 9
magnitud=float(input("Igrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >=3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >=4 and magnitud < 5:
    print("Moderado (sentido por las personas, pero no causa daño generalmente)")
elif magnitud >=5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras debiles)")
elif magnitud >= 6 and magnitud <7:
    print("Muy fuerte (puede causar daños significativos)")
else: 
    print("Extremo (puede causar daños graves a gran escala)")    
#Ejercicio 10

hemisferio= input("Ingrese su hemisferio (N para norte / S para sur): ").upper()
mes= int(input("Ingrese el mes en numero (1-12): "))
dia= int(input("Ingrese el día del mes: "))

estacion= ""

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes in [1,2]) or (mes == 3 and dia <= 20):
        estacion= "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <= 20):
        estacion= "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia <= 20):
        estacion= "Verano"
    elif (mes == 9 and dia >= 21) or (mes in [10,11]) or (mes == 12 and dia <= 20):
        estacion="Otoño"  
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes in [1,2]) or (mes == 3 and dia <= 20):
        estacion= "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <= 20):
        estacion= "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia <= 20):
        estacion= "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10,11]) or (mes == 12 and dia <= 20):
        estacion="Primavera"
else:
    estacion= "Hemisferio invalido" 

print(f"Usted se encuentra en estacion {estacion}")            