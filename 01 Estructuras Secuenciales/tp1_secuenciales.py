#Ejercicio 1
saludo="Hola mundo!"
print(saludo)

#Ejercicio 2
nombre= input("Escribe tu nombre: ")
print(f"Hola {nombre}!")

#Ejercicio 3
nombre= input("Ingrese su nombre: ")
apellido= input("Ingrese su apellido: ")
edad= input("Ingrese su edad: ")
lugarResidencia= input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años, y vivo en {lugarResidencia} ")

#Ejercicio 4: Radio del circulo, calcular area y perimetro
radio=float(input("Ingresa el radio del circulo: "))
pi=3.14
area=pi*radio**2
perimetro= 2*pi*radio
print(f"El área del circulo es: {area}")
print(f"El perimetro del circulo es: {perimetro}")

#Ejercicio 5
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos/3600
print(f"Equivale a {horas} horas")

#Ejercicio 6
numero = int(input("Ingrese un numero para ver su tabla de multiplicar: "))
for i in range(1,11):
    resultado = numero*i
    print(f"{numero} x {i} = (resultado)")

#Ejercicio 7
num1 = int(input("Ingrese el primer numero (distinto de 0): "))
num2 = int(input("Ingrese el primer numero (distinto de 0): "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1*num2
division = num1/num2

print(f"El resultado de la suma de {num1} y {num2} es: {suma}")
print(f"El resultado de la resta de {num1} y {num2} es: {resta}")
print(f"El resultado de la multiplicaciòn entre {num1} y {num2} es: {multiplicacion}")
print(f"El resultado de la division entre {num1} y {num2} es: {division}")

#Ejercicio 8
peso= float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc= peso / (altura**2)

print(f"su indice de masa corporal es de : {imc}")

#Ejercicio 9
celsius= float(input("Ingrese la temperatura en grados celsius: "))
fahrenheit= (9/6) * celsius + 32 
print(f"{celsius} ºC equivalen a {fahrenheit} ºF")

#Ejercicio 10
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))

promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los tres numeros es: {promedio}")