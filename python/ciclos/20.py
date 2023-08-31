suma = 0
cantidad = 0

while True:
    numero = int(input("Ingrese un número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero
    cantidad += 1

print("Cantidad de valores introducidos:", cantidad)
print("Suma de los valores:", suma)