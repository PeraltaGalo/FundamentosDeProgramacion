#Número Armstrong
numero = input("Ingrese un número de tres dígitos: ")
suma = int(numero[0]) ** 3 + int(numero[1]) ** 3 + int(numero[2]) ** 3

if suma == int(numero):
    print("Es un número Armstrong.")
else:
    print("No es un número Armstrong.")
