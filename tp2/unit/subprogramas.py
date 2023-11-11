def cargar(matriz,filas,columnas):
    for i in range(filas):
        for j in range(columnas):
            print(f"posicion: {i} {j}")
            matriz[i][j] = int(input("ingrese numero: "))

def procedimiento(matriz,filas,columnas):
    for j in range(columnas):
        c=0
        for i in range(filas):
            if ((matriz[i][j]) % 2 != 0):
                c += matriz[i][j]
        print(f"IMPAR POR COLUMNA {j+1} es : {c}")