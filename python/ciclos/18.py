cadena = input("Ingrese una secuencia de caracteres (termina en punto): ")
caracter = input("Ingrese el carácter a contar: ")

contador = 0

for c in cadena:
    if c == caracter:
        contador += 1

print(f"El carácter '{caracter}' aparece {contador} veces.")