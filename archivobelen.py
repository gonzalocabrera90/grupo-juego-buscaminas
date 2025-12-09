import gonzalo  # Para mostrar y despejar
import sandra   # Para ingresar coordenadas
import sofia    # Para ganaste
import gabriel  # Para perdiste
import sandra
import descubrir
import juli
def archivobelen():
	print("mi nombre es belen")

def verificar_posicion(tablero_minas, fila, columna):
    # Verificar si la posición actual es una mina
    if tablero_minas[fila][columna] == "B":
        return True, 0  # Es mina, no importa el número adyacente

    # Si no es mina, contar minas alrededor
    filas_totales = len(tablero_minas)
    columnas_totales = len(tablero_minas[0])
    minas_adyacentes = 0

    # Direcciones posibles alrededor de una celda (8 posiciones)
    direcciones = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)
    ]

    for desplazamiento_fila, desplazamiento_columna in direcciones:
        fila_vecina = fila + desplazamiento_fila
        columna_vecina = columna + desplazamiento_columna

        # Verificar que la posición esté dentro del tablero
        if 0 <= fila_vecina < filas_totales and 0 <= columna_vecina < columnas_totales:
            if tablero_minas[fila_vecina][columna_vecina] == "B":
                minas_adyacentes += 1

    return False, minas_adyacentes

    


def jugar(tablero_jugador, tablero_minas, lugares_a_descubrir, vidas, ):
    descubiertos = 0  # Contador de celdas descubiertas sin minas
    while True:
        # Mostrar tablero
        juli.mostrar(tablero_jugador)
        
        # Pedir coordenadas 
        fila, columna = sandra.ingresar_coordenadas(tablero_jugador)  # Debe validar rango
        
        # Verificar posición
        es_mina, minas_adyacentes = verificar_posicion(tablero_minas, fila, columna)
        

        if es_mina:
            vidas -= 1
            print(f"¡Boom! Perdiste una vida. Vidas restantes: {vidas}")
            if vidas == 0:
                gabriel.perdiste()  
                break
        
        else:
            letra = " "   # Lo que quieras mostrar en celdas descubiertas

            # LLAMADA CORRECTA A DESCUBRIR ✅
            lugares_a_descubrir = descubrir.descubrir(
                tablero_jugador,
                tablero_minas,
                fila,
                columna,
                letra,
                lugares_a_descubrir
            )

            # Verificar victoria
            if lugares_a_descubrir == 0:
                sofia.ganaste()
                break


if __name__ == "__main__":
	archivobelen()
