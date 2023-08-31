calif1 = float(input("Ingrese la primera calificación: "))
calif2 = float(input("Ingrese la segunda calificación: "))
calif3 = float(input("Ingrese la tercera calificación: "))
calif4 = float(input("Ingrese la cuarta calificación: "))
promedio = (calif1 + calif2 + calif3 + calif4) / 4
print("Promedio:", promedio)
if promedio >= 4:
    print("Aprobado")
else:
    print("No aprobado")