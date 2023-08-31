n = int(input("Ingrese un número n: "))
serie_suma = 0

for i in range(1, n + 1):
    serie_suma += 1 / i

print("Resultado de la serie h(n):", serie_suma)
