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
    for f, c in minas:
        matriz_minas[f][c] = "B"
