num = int(input("Ingrese un número de tres dígitos: "))
digitos = [int(d) for d in str(num)]
suma_cubos = sum(digitos[i] ** 3 for i in range(3))
if suma_cubos == num:
    print(num, "es un número Armstrong")
else:
    print(num, "no es un número Armstrong")