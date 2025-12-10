import gabriel
import gonzalo
import sofia

def sandra():
    print("Mi nombre es Sandra")

if __name__ == "__main__":
	sandra()

def niveles():
    print("--------NIVELES--------")
    print("ELIGE UNA OPCIÓN: ")
    print("1. PRINCIPIANTE.")
    print("2. INTERMEDIO.")
    print("3. EXPERTO.")
    print("4. PERSONALIZADO.")
    #elige la opción
    opcion= input("")
    while True:
        if opcion in ["1","2","3","4"]:
            return crear_tableros(opcion)
        # Así estaba antes: 
        # crear_tableros(opcion) 
        #    break
        else:
            print("OPCION INCORRECTA, ELIGE DE NUEVO.")
            niveles()

def crear_tableros(nivel):
    tablero1 = []
    tablero2 = []
    lugares_a_descubrir = 0
    if nivel == "1":
        tablero1 = gonzalo.generar_matriz_jugador(5, 5)
        tablero2 = gonzalo.generar_matriz_minas(5, 5, 5)
        lugares_a_descubrir = 5*5 - 5
    elif nivel == "2":
        tablero1 = gonzalo.generar_matriz_jugador(8, 8)
        tablero2 = gonzalo.generar_matriz_minas(8, 8, 10)
        lugares_a_descubrir = 8*8 - 10
    elif nivel == "3":
        tablero1 = gonzalo.generar_matriz_jugador(10, 10)
        tablero2 = gonzalo.generar_matriz_minas(10, 10, 20)
        lugares_a_descubrir = 10*10 - 20
    else:
        while True:
            filas = int(input("ingrese la cantidad de filas: "))
            columnas = int(input("ingrese la cantidad de columnas: "))
            minas = int(input("ingrese la cantidad de minas: "))
            if filas >2 and columnas >2:
                if 2 < minas < (filas*columnas):
                    tablero1 = gonzalo.generar_matriz_jugador(filas, columnas)
                    tablero2 = gonzalo.generar_matriz_minas(filas, columnas, minas)
                    lugares_a_descubrir = filas*columnas - minas
                    break
                else:
                    print("La cantidad de minas ingresada no corresponde a la cantidad de lugares. Ingrese nuevamente.")
            else:
                print("La cantidad de filas y columnas debe ser mayor a 2. Ingrese nuevamente.")
    return tablero1, tablero2, lugares_a_descubrir

def ingresar_coordenadas(tablero_jugador, inicial):
    fila = 0
    columna = 0
    while True:
        print("Ingresa las coordenadas que deseas descubrir:")
        fila = input("Ingresa la fila: ")
        columna = input("Ingresa la columna: ")
        if len(fila) == 0 and len(columna) == 0:
            print("Dato vacio. Ingresar nuevamente la fila y columna")
            fila_number = int(fila)
            columna_number = int(columna)
            if fila_number in range(0, len(tablero_jugador)) and columna_number in range(0, len(tablero_jugador[0])):
                if tablero_jugador[fila_number][columna_number] == inicial:
                    fila_number = -1
                    break
            else:
                print("Datos incorrectos. Ingresar nuevamente la fila y columna")

    return fila_number, columna_number
