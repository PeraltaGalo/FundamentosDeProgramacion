num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
if num1 % num2 == 0:
    print(num1, "es divisible por", num2)
    if num1 % 2 == 0:
        print(num1, "es un número par.")
    else:
        print(num1, "es un número impar.")