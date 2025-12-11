
def sofia():
    print("Mi nombre es Sofia")

import juli
import gabriel
import sandra

def menu(vidas):
    while True:
        print("1. JUGAR")
        print("2. INSTRUCCIONES")
        print("3. SALIR")

        opcion = input("opcion: ")
        nivel_elegido = None
        inicial = None
        if opcion == "1":
            print("JUEGO (tenes", vidas, "vidas)")
            inicial = gabriel.pedir_nombre()
            print( inicial )
            nivel_elegido = sandra.niveles()
        elif opcion == "2":
            print("INSTRUCCIONES:")
            juli.instrucciones()
        elif opcion == "3":
            print("Salir")
            nivel_elegido = None
            inicial = "Salir"
            return nivel_elegido, inicial
        else:
            print("Opcion invalida.")
            menu(vidas)
        return nivel_elegido, inicial


def ganaste():
    print("FELICITACIONES,GANASTE")


if __name__ == "__main__":
    sofia()

