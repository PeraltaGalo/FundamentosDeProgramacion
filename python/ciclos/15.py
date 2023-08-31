a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))

for multiplicando in range(a, b + 1):
    for multiplicador in range(1, 11):
        resultado = multiplicando * multiplicador
        print(f"{multiplicando} por {multiplicador} es {resultado}", end="\t")
    print()
