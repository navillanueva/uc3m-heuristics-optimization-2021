import sys

# Lectura de parametros, la misma que en la parte 1
# el numero de pilas que hay en la bodega del barco


def pilas():
    pilas = 0
    f = open(sys.argv[1])
    first = f.readline()
    for letter in first:
        if(letter != " " and letter != "\n"):
            pilas += 1
    f.close
    return pilas

# lectura del mapa y lo guardamos en una matriz


def mapear(pilas):
    mapa = []
    col = []
    x = 0
    f = open(sys.argv[1])
    lines = f.readlines()
    for i in range(0, pilas):
        for j in lines:
            col.append(j.rstrip('\n').split(' ')[x])
        mapa.append(col)
        col = []
        x += 1
    x = 0
    f.close()
    return mapa

# Guardamos los contenedores en la lista del puerto inicial


def PortZero():
    portzero = []
    f = open(sys.argv[2])
    for line in f:
        if(line[1] == 'S' and line[1] == 'R'):
            portzero.append(line[0])
    f.close
    return portzero

# matriz dinámica de los contenedores que están en el barco
# num columnas = 3 (id, pila, profundiad)
# num filas = tamaño de la matriz mapa.txt


def contBarco():
    contbarco = [][]
    f = open(sys.argv[1])

# declarar el estado y su constructor


class estado:
    def __init__(self, puerto0[], puerto1[], puerto2][], pos_barco, cont_barc[][]):
        self.puerto0[] = PortZero
        self.cajas_puerto1 = puerto1[]
        self.cajas_puerto2 = puerto2[]
        self.pos_barco= por_barco
        self.cont_barc[][] = contBarco()

# accion de cargar, nos devuelve el coste

def cargar():

    return 10 + prof

# accion de descargar, nos devuelve el coste

def descargar():

    return 15 + 2 * prof

# accion de navegar, nos devuelve el coste

def navegar():

    return 3500
