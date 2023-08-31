alumnos_promocionados = int(input("Ingrese la cantidad de alumnos promocionados: "))
alumnos_regularizados = int(input("Ingrese la cantidad de alumnos regularizados: "))
alumnos_desaprobados = int(input("Ingrese la cantidad de alumnos desaprobados: "))
alumnos_libres = int(input("Ingrese la cantidad de alumnos libres: "))
total_alumnos = alumnos_promocionados + alumnos_regularizados + alumnos_desaprobados + alumnos_libres
porcentaje_promocionados = (alumnos_promocionados / total_alumnos) * 100
porcentaje_regularizados = (alumnos_regularizados / total_alumnos) * 100
porcentaje_desaprobados = (alumnos_desaprobados / total_alumnos) * 100
porcentaje_libres = (alumnos_libres / total_alumnos) * 100
print("Porcentaje de alumnos promocionados:", porcentaje_promocionados, "%")
print("Porcentaje de alumnos regularizados:", porcentaje_regularizados, "%")
print("Porcentaje de alumnos desaprobados:", porcentaje_desaprobados, "%")
print("Porcentaje de alumnos libres:", porcentaje_libres, "%")