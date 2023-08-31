#Área y Perímetro de una Circunferencia
import math

radio = float(input("Ingrese el valor del radio: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

print(f"Área: {area}")
print(f"Perímetro: {perimetro}")
