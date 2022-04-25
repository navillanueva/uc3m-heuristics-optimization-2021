import constraint
from constraint import *
import sys

#Con esta funcion obtenemos el número de pilas en la bodega del barco
def pilas():
    pilas = 0

    f=open(sys.argv[1])

    first = f.readline()
    for letter in first:
        if(letter!=" " and letter !="\n"):
            pilas +=1

    f.close
    
    return pilas
    
#Una vez obtenido el número de pilas almacenamos el mapa en una lista y la devolvemos
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

#Guardamos los contenedores en dos listas, dependiendo si es refrigerado o no

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

#Al igual que con los contenedores, almacenamos en una lista el destino de los
#contenedores normales y en otra los refrigerados
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


#Obtenemos las posiciones posibles en la bodega y las almacenmaos en una lista
#y en otra lista solo las posiciones para los contenedores refrigerados
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


#RESTRICCIONES

#Comprobamos si hay un contenedor debajo del contenedor n
def Cdebajo(n, *args):
    for i in (range(len(args))):
        if(n!=i):
            if(args[i][0]==args[n][0]):
                prof = args[n][1] + 1 
                if(args[i][1] == prof):                    
                    return True
    return False

#Comporbamos si hay suelo debajo de cada contenedor
def posible(*args):
    for i in (range(len(args))):
        x = args[i][0]
        y = args[i][1] +1
        if (mapa[x][y]!="X"):
            #Si no hay suelo, miramos si hay otro contenedor
            if(Cdebajo(i,*args) == False):
                return False
    return True

#No puede haber sobre un contenedor que va al puerto 1 uno que va al puerto 2
def orden(args,args2):
    if(args[0] == args2[0]):
        if(args[1] > args2[1]):
            return False
        else:
            return True
    else:
        return True

if __name__ == '__main__':

    #Invocamos las funciones anteriores
    pile = pilas()
    mapa=mapear(pile)

    nordomain = norDomain(mapa)
    refdomain = coolDomain(mapa)

    nor = normalContainers()
    ref = coolContainers()
    todos= nor + ref
    
    norport = normalPort()
    refport = coolPort()
    port = norport + refport

    #Empezamos con la resolución del problema
    problem = constraint.Problem ()
    
    #Unas variables son los contenedores normales y su dominio
    problem.addVariables(nor,nordomain)
    #Las demás son los contenedores refrigerados y sus dominios
    problem.addVariables(ref,refdomain)

    #No se pueden almacenar dos contenedores en la misma posición
    problem.addConstraint(AllDifferentConstraint())

    #Comprobamos que las posiciones no desafían a la gravedad
    problem.addConstraint(posible,todos)
    
    #Si dos contenedores tienen diferente puerto de destino, se comprueba que el
    #de menor puerto no se encuentra debajo del de mayor puerto
    for x in (range(len(todos))):
        for y in (range(len(todos))):
            if(port[x] < port[y]):
                problem.addConstraint(orden,(todos[x], todos[y])) 

   

    s = problem.getSolutions()

    with open(sys.argv[1][0:5]+'-'+sys.argv[2][0:13]+'.output.', 'w') as f:
        print('Número de soluciones:',len(s),file=f)
        for n in (range(len(s))):
            print(s[n],file=f)
 