nombre1 = input("Ingrese el nombre del primer socio: ")
edad1 = int(input("Ingrese la edad del primer socio: "))
direccion1 = input("Ingrese la dirección del primer socio: ")

nombre2 = input("Ingrese el nombre del segundo socio: ")
edad2 = int(input("Ingrese la edad del segundo socio: "))
direccion2 = input("Ingrese la dirección del segundo socio: ")

if edad1 < edad2:
    print("Socio más joven:", nombre1, edad1, direccion1)
else:
    print("Socio más joven:", nombre2, edad2, direccion2)