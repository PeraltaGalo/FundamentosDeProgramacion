precio_inicial = float(input("Ingrese el precio del producto al inicio del año: "))
precio_transcurrido = float(input("Ingrese el precio del producto transcurrido un tiempo: "))
porcentaje_aumento = ((precio_transcurrido - precio_inicial) / precio_inicial) * 100
print("Porcentaje de aumento:", porcentaje_aumento, "%")