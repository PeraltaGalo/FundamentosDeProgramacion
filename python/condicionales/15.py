monto = float(input("Ingrese el monto: "))
if monto > 1000:
    descuento = monto * 0.1
else:
    descuento = monto * 0.02
monto_con_descuento = monto - descuento
print("Monto con descuento:", monto_con_descuento)