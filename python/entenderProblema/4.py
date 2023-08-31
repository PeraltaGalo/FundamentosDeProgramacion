#Sueldo con Descuentos
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
valor_hora = float(input("Ingrese el valor de las horas: "))
sueldo_bruto = horas_trabajadas * valor_hora
descuento = sueldo_bruto * 0.20
sueldo_neto = sueldo_bruto - descuento

print(f"Sueldo a cobrar: {sueldo_neto}")
