def gabriel():
	print("mi nombre es gabriel")

if __name__ == "__main__":
	gabriel()
	

def pedir_nombre():
    jugador = input("ingrese su nombre  : ")
    letra_inicial = jugador[0]
    return letra_inicial


def perdiste(vidas):
    if vidas == 0 :
        print("se te acabaron las vidas ")

        return True
    return False 

