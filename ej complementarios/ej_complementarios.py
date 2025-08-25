# Ejercio 1 Creamos la variable numero1 con un número entero
numero1 = 7
print("numero1:", numero1)
# Ejercio 2 Creamos la variable numero2 con un número decimal
numero2 = 3.5
print("numero2",numero2)
# Ejercio 3 Crear la variable suma y almacenar la suma de "numero1" y "numero2"
suma = numero1 + numero2
print(f"Suma: {numero1} + {numero2} = {suma}")
# Ejercio 4 crear tres variables más sin borrar lo que tienes. 
# Una para resta, otra para multiplicación y otra para división. Imprime estas variables.
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
print(f"Resta: {numero1} - {numero2} = {resta}")
print(f"Multiplicación: {numero1} x {numero2} = {multiplicacion}")
print(f"División: {numero1} / {numero2} = {division}")
# Ejercio 5 Crea una variable llamada "nombre" y asígnale tu nombre como valor.
nombre = "Belén"
print("nombre: ",nombre)
# Ejercio 6 Crea una variable llamada "precio" y asígnale un valor decimal que represente 
# el precio de un artículo ficticio
precio = 12000.70
print("El precio del producto es: $", precio)
#Ejercicio 7 Crea una variable llamada "descuento"y asígnale un valor decimal que represente 
# el descuento aplicado al artículo.
descuento = 0.50
print("El descuento es de ", descuento ," (50%)")
#Ejercicio 8 calcular el precio final aplicando el descuento al precio original y almacena el
# resultado en una variable llamada "precio_final".
precio_final = precio * (1 - descuento)
print("El precio final es de: $",precio_final)
#Ejercicio 9 Crea una variable llamada "cadena". Qué sea un string
cadena = "Hola Profe! Esta variable es de tipo string"
print(cadena)
#Ejercicio 10 Crea una nueva variable llamada "longitud". 
# En ella almacena la longitud en caracteres de la cadena utilizando una de las funciones de python
longitud = len(cadena)
print("Longitud de la cadena: ", longitud, " carácteres")
#Ejercicio 11 Crea otra vez la variable "precio" y dale un valor decimal,y conviértelo en número entero. 
#Lo puedes hacer en la misma variable o en otra, da lo mismo.
precio2 = int(23700.89)
print("El precio convertido a numero entero: ", precio2)
#Ejercicio 12 Crea dos variables, "nombre" y "apellido", concaténalas en una tercer variable "nombre_completo", 
# el nombre y el apellido con un espacio entre medio. Puedes usar la forma de concatenación que quieras.
nombre= "Belén"
apellido= "Calvo"
nombre_completo= nombre + " " + apellido
print("El nombre completo es:", nombre_completo)
#Ejercicio 13 Escribe tu edad en una variable. Increméntala en 5 y luego disminúyela en 10
edad = 31
edad += 5
edad -= 10
print("La edad final es:", edad)
#Ejercicio 14  Crea una variable llamada "altura" que contenga con decimales, tu altura en metros y centímetros. 
# Por ejemplo: 1.83. Multiplícala por 4 y luego divídela en 3
altura = 1.65
altura = (altura * 4) / 3
print("La altura modificada es:", altura)
#Ejercicio 15 Crea una variable que contenga tu nombre completamente en mayúsculas. 
# Después transfórmalo todo en minúsculas con algún método o función de Python.
nombreMayus = "BELÉN"
nombreMinus = nombreMayus.lower()
#Ejercicio 16 Con la variable con el nombre en mayúsculas, aplica un método parecido para que 
# se transforme todo en minúsculas excepto la primera letra
nombrePrimerLetra = nombreMayus.capitalize()
print("Nombre en minúsculas, excepto la primer letra: ", nombrePrimerLetra)

