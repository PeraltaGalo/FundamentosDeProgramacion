calif1 = 0
calif2 = 0
calif3 = 0

for _ in range(1000):
    calificacion = int(input("Ingrese la calificación (1, 2 o 3): "))
    
    if calificacion == 1:
        calif1 += 1
    elif calificacion == 2:
        calif2 += 1
    elif calificacion == 3:
        calif3 += 1

print("Cantidad de alumnos con calificación 1:", calif1)
print("Cantidad de alumnos con calificación 2:", calif2)
print("Cantidad de alumnos con calificación 3:", calif3)
