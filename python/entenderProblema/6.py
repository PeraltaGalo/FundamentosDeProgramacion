#Palíndromo
palabra = input("Ingrese una palabra: ")

if palabra == palabra[::-1]:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")
