import sofia
import archivobelen
import juli

vidas = 3

data_juegos, letra_nombre = sofia.menu(vidas)
tablero_vista = data_juegos[0]
tablero_minas = data_juegos[1]
lugares_a_descubrir = data_juegos[2]

juli.mostrar(tablero_minas)#borrar

archivobelen.jugar(tablero_vista, tablero_minas, lugares_a_descubrir, vidas, letra_nombre)
