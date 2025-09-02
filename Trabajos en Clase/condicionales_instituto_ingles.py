#El usuario ingresa la fecha
fecha= input("Ingrese la fecha actual en formato 'día, DD/MM': ")

fecha = fecha.split(", ")
dia_sem:str= fecha[0]
fecha_numerica= fecha[1].strip().split("/")

dd:int = int(fecha_numerica[0])
mm:int = int(fecha_numerica[1])

#Lista de dias validos
dias_validos:list[str] = ["lunes", "martes", "miercoles", "jueves","viernes"]

#Validacion de fecha
if dia_sem not in dias_validos:
    print("Error: dia inválido")
elif dd < 1 or dd > 31:
    print("Error: número de dia inválido")
elif mm < 1 or mm > 12:
    print("Error: número de mes invalido")
else:
    print(f"Fecha válida: {dia_sem}, {dd}/{mm}")

#Según el dia
if dia_sem in ["lunes", "martes", "miercoles", "miércoles"]:
    print("Nivel con exámenes")
    examenes:str= input("¿Se tomaron exámenes en la fecha? (s/n)").lower()
    if examenes =="s":
        aprobados:int = int(input("Cuantos alumnos aprobaron?: "))
        desaprobados:int= int(input("Cuantos alumnos desaprobaron?: "))
        total:int = aprobados + desaprobados
        if total > 0:
            porcentaje:float=(aprobados/total)*100
            print(f"El porcentaje de alumnos aprobados: {porcentaje:.2f}%")

elif dia_sem == "jueves":
    print("Dia de practica hablada")
    asistencia:float=float(input("Ingrese el porcentaje de asistencia: "))
    if asistencia > 50:
        print("Asistió la mayoria")
    else:
        print("No asistió la mayoria")

elif dia_sem == "viernes":
    print("Dia de Inglés para viajeros")
    if dd == 1 and mm in [1, 7]:
        print("Comienzo de un nuevo ciclo")
        alumnos:int = int(input("Cantidad de alumnos: "))
        arancel:float = float(input("Arancel por alumno ($): "))
        ingreso_total:float = alumnos * arancel
        print (f"Ingreso total: ${ingreso_total:.2f}")