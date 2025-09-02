#Calculadora de Propinas de un Restaurante
#El usuario ingresa el monto a pagar
monto = float(input("Ingrese el monto de la cuenta: "))
#calcular propina
propina_10 = monto * 0.10
propina_15 = monto * 0.15
#calcular el total a pagar
total_10 = monto + propina_10
total_15 = monto + propina_15
#mostrar los resultados
print("Propina sugerida (10%):", propina_10)
print("Total a pagar (10%):", total_10)
print("Propina sugerida (15%):", propina_15)
print("Total a pagar (15%):", total_15)

