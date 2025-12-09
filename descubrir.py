def descubrir(vista, test, fila, columna, letra, lugares_a_descubrir):
    if fila == 0:#primera fila
        return filaInicial(vista, test, fila, columna, letra, lugares_a_descubrir)
    elif fila == len(test) - 1:#ultima fila
        return filaFinal(vista, test, fila, columna, letra, lugares_a_descubrir)
    else:#filas del medio
        return filaInterna(vista, test, fila, columna, letra, lugares_a_descubrir)
                
def filaInicial(vista, test, fila, columna, letra, lugares_a_descubrir):
    #posibilidades segun el lugar ingreso el usuario
    conjunto_indice_inicio = [(0, 1), (1, 0), (1, 1)]
    conjunto_indice_medio = [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1)]
    conjunto_indice_final = [(0, -1), (1, 0), (1, -1)]
    if columna == 0:# si el index es el primero
        return setValores(vista, test, fila, columna, conjunto_indice_inicio, letra, lugares_a_descubrir)
    elif columna == len(test) - 1:# si el index es el ultimo
        return setValores(vista, test, fila, columna, conjunto_indice_final, letra, lugares_a_descubrir)
    else:#index del medio
        return setValores(vista, test, fila, columna, conjunto_indice_medio, letra, lugares_a_descubrir)

def filaFinal(vista, test, fila, columna, letra, lugares_a_descubrir):
    #posibilidades segun el lugar ingreso el usuario
    conjunto_indice_inicio = [(0, 1), (-1, 0), (-1, 1)]
    conjunto_indice_medio = [(0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]
    conjunto_indice_final = [(0, -1), (-1, 0), (-1, -1)]
    if columna == 0:# si el index es el primero
        return setValores(vista, test, fila, columna, conjunto_indice_inicio, letra, lugares_a_descubrir)
    elif columna == len(test) - 1:# si el index es el ultimo
        return setValores(vista, test, fila, columna, conjunto_indice_final, letra, lugares_a_descubrir)
    else:#index del medio
        return setValores(vista, test, fila, columna, conjunto_indice_medio, letra, lugares_a_descubrir)

def filaInterna(vista, test, fila, columna, letra, lugares_a_descubrir):
    #posibilidades segun el lugar ingreso el usuario
    conjunto_indice_inicio = [(0, 1), (1, 0), (1, 1), (-1, 0), (-1, 1)]
    conjunto_indice_medio = [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]
    conjunto_indice_final = [(0, -1), (1, 0), (1, -1), (-1, 0), (-1, -1)]
    if columna == 0:# si el index es el primero
        return setValores(vista, test, fila, columna, conjunto_indice_inicio, letra, lugares_a_descubrir)
    elif columna == len(test) - 1:# si el index es el ultimo
        return setValores(vista, test, fila, columna, conjunto_indice_final, letra, lugares_a_descubrir)
    else:#index del medio
        return setValores(vista, test, fila, columna, conjunto_indice_medio, letra, lugares_a_descubrir)

def setValores(vista, test, fila, columna, conjunto, letra, lugares_a_descubrir):
    count = 0
    for a, b in conjunto:
        if test[fila + a][columna + b] == "B":
            vista[fila][columna] = letra
            lugares_a_descubrir -= 1
            break
        else:
            count += 1
    
    if count == len(conjunto):
        if vista[fila][columna] != letra:
            vista[fila][columna] = letra
            lugares_a_descubrir -= 1
        for a, b in conjunto:
            if vista[fila + a][columna + b] != letra:
                vista[fila + a][columna + b] = letra
                lugares_a_descubrir -= 1
    return lugares_a_descubrir
