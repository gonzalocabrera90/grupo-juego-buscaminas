# no pude hacer el push. subido por compañero.

# funcion para mostrar las instrucciones de juego.
# Use las comillas triples para usar saltos de linea y no tantos print()
def instrucciones():
    print("""
1° Elegir el nivel de juego. Recuerda que puedes seleccionar el número de filas, columnas y minas.
          2° Para jugar ingresa primero la fila y la columna.
          3° Intente esquivar todas la minas para ganar. Tienes 3 errores posibles.
    """)

# funcion para mostra matriz por consola y numeros de ayuda visual para filas y columnas.
# recibe la matriz como parametro. mostrar(tablero1) mostrar(tablero2)
def mostrar(item):

    columnas_matriz = len(item[0]) # obtiene el numero de columnas por la cantidad de elementos de la lista
    print("    ", end=" ") # espacios iniciales para alinear el primer numero con la columna

    # imprime una linea con los numeros para la columna
    for i in range(0, columnas_matriz):
        if i == columnas_matriz - 1: # si es la posicion final hace un salto de linea
            print(f"{i}")
        else: # si no es la posicion final imprime el numero con espacios al final para alinear columnas
            print(f"{i}", end="    ")

    # imprime un numero de fila, un espacio y la fila de la matriz
    for i, line in enumerate(item, start=0):
        print(i, line, sep=" ")