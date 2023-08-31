total_pagar = 0
cantidad_articulos = 0

while True:
    precio = float(input("Ingrese el precio del artículo (0 para terminar): "))
    if precio == 0:
        break
    total_pagar += precio
    cantidad_articulos += 1

print("Monto total a pagar:", total_pagar)
print("Cantidad de artículos comprados:", cantidad_articulos)
