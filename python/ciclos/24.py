azules_pares = 0
rojas_impares = 0
otras = 0

while True:
    tarjeta = input("Ingrese una tarjeta (color y número) o 'blanca' para terminar: ")
    if tarjeta == "blanca":
        break
    color, numero = tarjeta.split()
    numero = int(numero)
    
    if color == "azul" and numero % 2 == 0:
        azules_pares += 1
    elif color == "roja" and numero % 2 != 0:
        rojas_impares += 1
    else:
        otras += 1

print("Tarjetas azules pares:", azules_pares)
print("Tarjetas rojas impares:", rojas_impares)
print("Otras tarjetas:", otras)
