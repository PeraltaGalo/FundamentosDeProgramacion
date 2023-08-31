def es_apto(edad, titulo):
    if edad >= 18:
        if titulo == "administrativo":
            return 18 <= edad <= 55
        elif titulo == "transportista":
            return 18 <= edad <= 55
        elif titulo == "operario":
            return 18 <= edad <= 50
        elif titulo == "guardia":
            return 18 <= edad <= 45
    return False

empleados = {
    "administrativo": 0,
    "transportista": 0,
    "operario": 0,
    "guardia": 0
}

while True:
    titulo = input("Ingrese el título del CV (o 'terminar' para finalizar): ")
    if titulo == "terminar":
        break
    edad = int(input("Ingrese la edad del candidato: "))
    if es_apto(edad, titulo):
        empleados[titulo] += 1
        nombre = input("Ingrese el nombre del candidato: ")
        apellidos = input("Ingrese los apellidos del candidato: ")
        direccion = input("Ingrese la dirección del candidato: ")
        dni = input("Ingrese el número de DNI del candidato: ")
        print(f"{nombre} {apellidos} ha sido seleccionado como {titulo}.")
    else:
        print(f"{titulo} no apto debido a la edad.")
        
print("Resultados de la selección:")
for titulo, cantidad in empleados.items():
    print(f"Cantidad de {titulo}s seleccionados:", cantidad)
