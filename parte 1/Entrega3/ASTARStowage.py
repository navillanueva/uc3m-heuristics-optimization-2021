import sys

#Un contenedor s epuede cargar en un puerto o en el barco


#Necesitamos:

#El mapa

def pilas():
    pilas = 0

    f=open(sys.argv[1])

    first = f.readline()
    for letter in first:
        if(letter!=" " and letter !="\n"):
            pilas +=1

    f.close
    
    return pilas
    

def mapear(pilas):
    mapa = []
    col =[]
    x=0

    f=open(sys.argv[1])
    lines = f.readlines()

    for i in range(0,pilas):
        for j in lines:
            col.append(j.rstrip('\n').split(' ')[x])
        mapa.append(col)
        col = []
        x+=1
    x=0

    f.close()

    return mapa

def getLine(id):
    linea = []

    f=open(sys.argv[2])

    for line in f:
        if(int(line[0]) == id):
            linea = [id,line[2],line[4]]
    
    f.close

    return linea

#Los contenedores del puerto inicial, su tipo y destino

def toIntegerList(StringList):
    
    StringList = [int(i) for i in StringList]
    return StringList

def normalContainers():
    nor =[]

    f=open(sys.argv[2])

    for line in f:
        if(line[2] == 'S'):
            nor.append(line.split()[0])
    
    f.close

    norInt = toIntegerList(nor)

    return norInt

def normalPort():
    portnor = []

    f=open(sys.argv[2])

    for line in f:
        if(line[2] == 'S'):
            portnor.append(line.split()[2])

    f.close

    return portnor

def coolContainers():
    ref =[]

    f=open(sys.argv[2])

    for line in f:
        if(line[2] == 'R'):
            ref.append(line.split()[0])
    
    f.close

    refInt = toIntegerList(ref)

    return refInt


def coolPort():
    portref = []

    f=open(sys.argv[2])

    for line in f:
        if(line[2] == 'R'):
            portref.append(line.split()[2])

    f.close

    return portref


def norDomain(mapa):

    norPlace = []

    x=0
    y=0

    for i in mapa:
        for j in i:
            if(j!='X'):
                norPlace.append((x,y))
            y+=1
        x+=1
        y=0
   
    x=0
    y=0


    return norPlace

def coolDomain(mapa):

    coolPlace = []

    x=0
    y=0

    for i in mapa:
        for j in i:
            if(j=='E'):
                coolPlace.append((x,y))
            y+=1
        x+=1
        y=0
   
    x=0
    y=0


    return coolPlace

#Comporbamos si hay suelo debajo de cada contenedor
def posible(estado,contenedor):
    for i in (range(len(estado[5]))):
        x = estado[5][i][0]
        y = estado[5][i][1]
        y = y+1
        if (mapa[x][y]!="X"):
            #Si no hay suelo, miramos si hay otro contenedor
            for i in dominio:
                if(i == (x,y)):
                    for i in (range(len(estado[5]))):
                        if(i == (x,y)):
                            return False
                    return True
                return False
        else:
            return True
    return False

#Definir el estado inicial con estos dos datos
#El estado inicial es:
#Todos los contenedores en el puerto inicial
#0 contenedores en el puerto 1 y 2
#Barco en posicion 0
#Barco vacío

def letsBegin(todos):
    inicial = []
    inicial.append(todos)
    inicial.append([])
    inicial.append([])
    inicial.append(1)
    inicial.append([])
    dominio = norDomain(mapa)
    inicial.append(dominio)


    return inicial


#Definir la operacion cargar

def upload(estado,contenedor):
    posBarco = estado[3]
    newEstado = estado
    newEstado[posBarco].remove(contenedor)
    newEstado[4].append(getLine(contenedor))
    return newEstado

#Definir la operacion descargar

def download(estado,contenedor):
    posBarco = estado[3]
    newEstado = estado
    newEstado[4].remove(getLine(contenedor))
    newEstado[posBarco].append(contenedor)

    return newEstado


#Definir la operacion navegar

def sail(estado):
    temp1 = list(estado)
    r = []
    if(estado[3]==0 or estado[3]==2):
        temp1[3] = 1
        r.append(temp1)
    else:
        temp1[3] = 0
        r.append(temp1)
        r = noMoreBugs(r,estado)
    return r

def noMoreBugs(r,estado):
    r.append(estado)
    r[1][3] = 2
    return r

        
#Definir una heuristica
#Implementar el algoritmo A* con abierta y cerrada
def finalFantasy(n):
    primer =0
    segun =0

    f=open(sys.argv[2])

    for line in f:
        if (int(line[4]) == 1):
            primer = primer+1
        if (int(line[4]) == 2):
            segun = segun+1

    f.close

    if(len(n[1]) == primer and len(n[2]) == segun):
        return True
    else:
        return False

def expandir(n):
    temp = []
    #cargar y append
    #descargar y append
    #navegar y append
    return temp

def aEstrella(abierta,cerrada,exito):
    while(len(abierta)>0 or exito):
        n = abierta.pop(0)
        if(finalFantasy(n)):
            exito = True
        else:
            eSe = expandir(n)
            cerrada.append(n)
            done = False
            for s in eSe:
                #abierta o cerrada o ninguna
                for a in abierta:
                    if(s==a):
                        #se comprueba
                        done = True
                        break
                if(done == False):
                    for c in cerrada:
                        if(s==a):
                            done = True
                            break
                if(done == False):
                    abierta.append(s)
    if(exito):
        print("con solucion")
    else:
        print("sin solucion")

         
                
                
                    


    

if __name__ == '__main__':

    pile = pilas()
    mapa=mapear(pile)

    nor = normalContainers()
    ref = coolContainers()
    todos= nor + ref
    total = len(todos)

    norport = normalPort()
    refport = coolPort()
    port = norport + refport

    EstadoInicial = letsBegin(todos)
    print(EstadoInicial)

    ady = upload(EstadoInicial,2)
    print(ady)

    ady2 = download(ady,2)
    print(ady2)

    uno=(sail(EstadoInicial))
    print(uno)
  



