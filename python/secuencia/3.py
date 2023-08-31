horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
valor_hora = float(input("Ingrese el valor de las horas trabajadas: "))
sueldo = horas_trabajadas * valor_hora
sueldo_descuentos = sueldo * 0.8
print("Sueldo sin descuentos:", sueldo)
print("Sueldo con descuentos del 20%:", sueldo_descuentos)