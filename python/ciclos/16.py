secuencia = input("Ingrese una secuencia de caracteres (termina en #): ")

for caracter in secuencia:
    if caracter.isdigit():
        print(caracter)
