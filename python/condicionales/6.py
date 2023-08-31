num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
if num1 % num2 == 0:
    num1, num2 = num2, num1
    print("Números intercambiados:", num1, num2)