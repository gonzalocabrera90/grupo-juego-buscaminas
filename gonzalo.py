import random
def generar_matriz_jugador(filas = 10, columnas = 10):
    matriz_jugador = []
    for i in range(filas):
        matriz_jugador.append([])
        for x in range(columnas):
            matriz_jugador[i].append("-")
    return matriz_jugador


def generar_matriz_minas(filas = 10, columnas = 10, minas = 10):
    matriz_minas = []
    for i in range(filas):
        matriz_minas.append([])
        for x in range(columnas):
            matriz_minas[i].append("-")
    set_minas = set()

    while len(set_minas) < minas:
        item_1 = random.randint(0, filas - 1)
        item_2 = random.randint(0, columnas - 1)
        item = (item_1, item_2)
        set_minas.add(item)
    cargarminas(set_minas, matriz_minas)
    return matriz_minas


def cargarminas(minas, matriz_minas):
    print(minas)
    for f, c in minas:
        matriz_minas[f][c] = "B"

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