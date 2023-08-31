contador = 0

for _ in range(100):
    numero = int(input("Ingrese un número: "))
    
    if numero % 2 == 0:
        contador += 1

print("Cantidad de múltiplos de 2:", contador)
