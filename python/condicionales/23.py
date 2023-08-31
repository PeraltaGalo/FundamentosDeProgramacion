total_preguntas = int(input("Ingrese la cantidad total de preguntas: "))
respuestas_correctas = int(input("Ingrese la cantidad de respuestas correctas: "))

porcentaje_correctas = (respuestas_correctas / total_preguntas) * 100

if porcentaje_correctas >= 90:
    print("Nivel: Muy Bueno")
elif porcentaje_correctas >= 70:
    print("Nivel: Bueno")
elif porcentaje_correctas >= 50:
    print("Nivel: Regular")
else:
    print("Nivel: Malo")
