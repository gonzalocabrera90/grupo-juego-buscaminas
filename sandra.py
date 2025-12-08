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
            crear_tableros(opcion)
            break
        else:
            print("OPCION INCORRECTA, ELIGE DE NUEVO.")
            niveles()