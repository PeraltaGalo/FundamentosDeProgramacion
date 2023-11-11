#Se tiene una matriz cuadrada cargada con números enteros, determinar y mostrar la suma de los números impares que se encuentran en cada una de sus columnas.
from io import open
from unit.subprogramas import cargar, procedimiento

matriz = [[0, 0], [0, 0]]
filas = len(matriz)
columnas = len(matriz[0])
archivo = "archivo.txt"

with open(archivo, "w") as archivo_actual:
    # Realizar y guardar el primer procedimiento
    cargar(matriz, filas, columnas)
    procedimiento(matriz, filas, columnas)
    archivo_actual.write("\nResultado del Primer Procedimiento:\n")
    for fila in matriz:
        archivo_actual.write(", ".join(map(str, fila)) + "\n")

    # Guardar los elementos impares por columna
    archivo_actual.write("\nElementos Impares por Columna:\n")
    for col in range(columnas):
        elementos_impares = [matriz[fila][col] for fila in range(filas) if matriz[fila][col] % 2 != 0]
        archivo_actual.write(f"Columna {col + 1}: {', '.join(map(str, elementos_impares))}\n")

    # Realizar y guardar el segundo procedimiento
    cargar(matriz, filas, columnas)
    procedimiento(matriz, filas, columnas)
    archivo_actual.write("\nResultado del Segundo Procedimiento:\n")
    for fila in matriz:
        archivo_actual.write(", ".join(map(str, fila)) + "\n")
    # Guardar los elementos impares por columna
    archivo_actual.write("\nElementos Impares por Columna:\n")
    for col in range(columnas):
        elementos_impares = [matriz[fila][col] for fila in range(filas) if matriz[fila][col] % 2 != 0]
        archivo_actual.write(f"Columna {col + 1}: {', '.join(map(str, elementos_impares))}\n")
