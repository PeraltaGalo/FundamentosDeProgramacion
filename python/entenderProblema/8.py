#Verificar Número en Lista
numeros = [int(input("Ingrese el primer número: ")), int(input("Ingrese el segundo número: ")), int(input("Ingrese el tercer número: "))]
numero_buscar = 3

if numero_buscar in numeros:
    print("El número 3 está en la lista.")
else:
    print("El número 3 no está en la lista.")
