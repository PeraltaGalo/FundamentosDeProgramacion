for i in range(5):
    valor1 = float(input("Ingrese el primer valor: "))
    valor2 = float(input("Ingrese el segundo valor: "))
    
    print("Valores ingresados:", valor1, valor2)
    
    if valor1 > 0 and valor2 > 0:
        promedio = (valor1 + valor2) / 2
        print("Promedio de valores positivos:", promedio)
