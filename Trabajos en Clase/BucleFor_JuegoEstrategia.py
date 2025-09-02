#Juego de estrategia
#correr cada letra del mensaje –considerando la posición de c/u en el alfabeto– una determinada cantidad de lugares
corrimiento=int(input("Ingrese el corrimiento: "))
alfabeto="abcdefghijklmnñopqrstuvwxyz"
jefe= "Jefe del equipo A"
oficiales = ["Oficial 1", "Oficial 2", "Oficial 3", "Oficial 4", "Oficial 5"]

for oficial in oficiales:
    mensaje = input(f"Mensaje para {oficial}:")
    nuevo_mensaje=""

    for letra in mensaje:
        if letra.lower() in alfabeto:
            #buscar posicion manualmente
            posicion=None
            #Buscar la posicion 
            for i in range(len(alfabeto)):
                if alfabeto[i] == letra.lower():
                    posicion = i
                    break

            #Aplicar corrimiento circular
            nueva_posicion= (posicion + corrimiento)% 27
            letra_encriptada = alfabeto [nueva_posicion] 
            # Mantener mayúsculas
            if letra.isupper():
                letra_encriptada = letra_encriptada.upper()

            nuevo_mensaje += letra_encriptada
        else:
            # Dejo igual si no es letra
            nuevo_mensaje += letra

    print("Mensaje encriptado:", nuevo_mensaje)           