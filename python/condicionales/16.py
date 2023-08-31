numero_mes = int(input("Ingrese el número de un mes (1 a 12): "))
if numero_mes == 2:
    dias = 28
elif numero_mes in [4, 6, 9, 11]:
    dias = 30
else:
    dias = 31
print("Número de días:", dias)
