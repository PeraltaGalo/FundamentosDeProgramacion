# Ejercicio 13
fecha = input("Ingrese una fecha en formato dd/mm/aaaa: ")
dia = int(fecha[:2])
mes = int(fecha[3:5])
anio = int(fecha[6:])

dia_siguiente = dia + 1
mes_siguiente = mes
anio_siguiente = anio

if dia_siguiente > 30:  # Considerando meses de 30 días
    dia_siguiente = 1
    mes_siguiente += 1
    if mes_siguiente > 12:
        mes_siguiente = 1
        anio_siguiente += 1

print("Fecha siguiente:", f"{dia_siguiente:02d}/{mes_siguiente:02d}/{anio_siguiente:04d}")
