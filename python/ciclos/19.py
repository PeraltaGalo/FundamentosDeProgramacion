contador_negativos = 0

while True:
    numero = int(input("Ingrese un número (0 para terminar): "))
    if numero == 0:
        break
    if numero < 0:
        contador_negativos += 1

print("Cantidad de números negativos:", contador_negativos)

