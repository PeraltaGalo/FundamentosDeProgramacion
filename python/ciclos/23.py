mayores_1000 = 0

while True:
    numero = int(input("Ingrese un número (0 para terminar): "))
    if numero == 0:
        break
    if numero > 1000:
        mayores_1000 += 1

if mayores_1000 < 20:
    factorial = 1
    for i in range(1, mayores_1000 + 1):
        factorial *= i
    print("Cantidad de valores mayores a 1000:", mayores_1000)
    print("Factorial:", factorial)
else:
    print("Cantidad de valores mayores a 1000:", mayores_1000)
