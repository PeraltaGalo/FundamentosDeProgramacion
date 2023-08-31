numeros = []

while True:
    numero = int(input("Ingrese un número (0 para terminar): "))
    if numero == 0:
        break
    numeros.append(numero)

rango = max(numeros) - min(numeros)
print("El rango de los valores es:", rango)
