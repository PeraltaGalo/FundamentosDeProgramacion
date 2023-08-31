kilometros = float(input("Ingrese los kilómetros recorridos: "))
tarifa = 20  

if kilometros > 30:
    if kilometros <= 100:
        tarifa += (kilometros - 30) * 1  
    else:
        tarifa += 70  
        tarifa += (kilometros - 100) * 0.5  

print("Total a pagar:", tarifa, "euros")