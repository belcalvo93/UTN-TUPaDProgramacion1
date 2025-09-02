#Juego Piedra, Papel o Tijera
opcion_jugador= ""
opcion_pc=""
ganadas_jugador= 0
ganadas_pc= 0
empates= 0
import random #para las jugadas de la compu
menu = {
    "1": "piedra",
    "2": "papel",
    "3": "tijera",
    "4": "salir"}

while opcion_jugador != "salir":
    #Mostrar el menu
    print("Menú:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("4. Salir")
    #Leer la eleccion del jugador
    eleccion = input("Elige una opcion, ingresando un número (1-4): ")
    
    if eleccion in menu:
        opcion_jugador = menu[eleccion]
    else:
        print("Opción no válida, intenta de nuevo")
        continue #vuelve al inicio del while

    if opcion_jugador == "salir":
        break

    #Jugada de la computadora
    opcion_pc = random.choice(["piedra", "papel", "tijera"])
    print("La computadora eligió", opcion_pc)

    #Comparar jugadas y actualizar contadores
    if opcion_jugador == "piedra" and opcion_pc =="tijera":
        print("Gana el jugador")
        ganadas_jugador += 1    
    elif opcion_jugador == "tijera" and opcion_pc =="piedra":
        print("Gana la computadora")
        ganadas_pc += 1
    elif opcion_jugador == "papel" and opcion_pc =="piedra":
        print("Gana el jugador")
        ganadas_jugador += 1
    elif opcion_jugador == "piedra" and opcion_pc =="papel":
        print("Gana la computadora")
        ganadas_pc += 1
    elif opcion_jugador == "tijera" and opcion_pc =="papel":
        print("Gana el jugador")
        ganadas_jugador += 1
    elif opcion_jugador == "papel" and opcion_pc =="tijera":
        print("Gana la computadora")
        ganadas_pc += 1
    elif opcion_jugador == opcion_pc:
        print("Empate")
        empates += 1
    
#Marcador al finalizar el juego
print("Juego terminado")
print("Marcador: Jugador: ", ganadas_jugador, "| Computadora: ", ganadas_pc)