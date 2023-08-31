num1 = float(input("Ingrese el primer número: "))
operador = input("Ingrese el operador (*, /, +, -): ")
num2 = float(input("Ingrese el segundo número: "))
if operador == "*":
    resultado = num1 * num2
elif operador == "/":
    resultado = num1 / num2
elif operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
else:
    resultado = "Operador no válido"
print("Resultado:", resultado)