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
        filas = int(input("ingrese la cantidad de filas: "))
        columnas = int(input("ingrese la cantidad de columnas: "))
        minas = int(input("ingrese la cantidad de minas: "))
        tablero1 = gonzalo.generar_matriz_jugador(filas, columnas)
        tablero2 = gonzalo.generar_matriz_minas(filas, columnas, minas)
        lugares_a_descubrir = filas*columnas - minas
    return tablero1, tablero2, lugares_a_descubrir

def ingresar_coordenadas():
    fila = int(input("Ingresa la fila: "))
    columna = int(input("Ingresa la columna: "))
    return fila, columna
