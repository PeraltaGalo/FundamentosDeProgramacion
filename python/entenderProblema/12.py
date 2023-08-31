#Porcentaje de Aumento
precio_inicial = float(input("Ingrese el precio inicial: "))
precio_final = float(input("Ingrese el precio final: "))
porcentaje_aumento = ((precio_final - precio_inicial) / precio_inicial) * 100

print(f"Porcentaje de aumento: {porcentaje_aumento}%")
