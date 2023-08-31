num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 <= num2 <= num3:
    print("Números en orden creciente:", num1, num2, num3)
elif num1 <= num3 <= num2:
    print("Números en orden creciente:", num1, num3, num2)
elif num2 <= num1 <= num3:
    print("Números en orden creciente:", num2, num1, num3)
elif num2 <= num3 <= num1:
    print("Números en orden creciente:", num2, num3, num1)
elif num3 <= num1 <= num2:
    print("Números en orden creciente:", num3, num1, num2)
else:
    print("Números en orden creciente:", num3, num2, num1)
