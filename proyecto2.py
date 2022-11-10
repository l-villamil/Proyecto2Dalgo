import sys


#commit prueba
def funcionPrincipal(listaDiccionario):
    vertices = []
    for palabra in listaDiccionario:
        for letra in palabra: 
            if letra not in vertices:
                vertices.append(letra)
    matriz = [-1]*len(vertices)
    for i in range(0,len(vertices)):
        matriz[0]=[-1]*len(vertices)
    i = 0
    j = 1
    while i < len(listaDiccionario-1):
        palabraI = listaDiccionario[i]
        palabraJ = listaDiccionario[j]
        k = 0
        while k<len(palabraJ):
            if palabraI[k]==palabraI[k]:
                k += 1
            else:
                matriz[palabraI[k][palabraI[k]]]
                k += 1




    hayCiclos = DFS(vertices,ejes)
    if hayCiclos:
        return "ERROR"
    else:
        subgrafos = BFS(ejes)
        salida = ''
        for i in subgrafos:
            salida += ''.join(i)
    return salida



def DFS(vertices,ejes):
    hayCiclo=False
    dictVertices={}
    #se crea un diccionario que almacena el color de cada vertice que representa el tipo de eje
    # blanco= Tree edge
    #gris= back edge
    #negro= cross edge
    #si durante el algoritmo se llega a un vertice gris significa que hay un ciclo
    for vertice in vertices:
        dictVertices[vertice]="blanco"
    c=0
    # se recorre cada verice que sea blanco
    while (c<len(vertices) and not hayCiclo):
        if (dictVertices[vertices[c]]=="blanco"):
            hayCiclo=DFSvisita(vertices,ejes,dictVertices,c)
        c+=1
    return hayCiclo

def DFSvisita(vertices,ejes,dictVertices,indiceVertice):
    vertice1=vertices[indiceVertice]
    #se marca el vertice como gris para representar que ha sido visitado
    dictVertices[vertice1]="gris"
    i=0
    centinela=False
    while (i<len(vertices) and not centinela):
            #se recorren los vertices adjacentes
            #si su color es gris significa que ya fue visitado y por lo tanto hay un ciclo
        if (ejes[indiceVertice][i]>0):
            if (dictVertices[vertices[i]]=="gris"):
                centinela=True
            # si es la primera vez que se vista el ciclo se aplica recursivamente la funcion
            elif (dictVertices[vertices[i]]=="blanco"):
                centinela = DFSvisita(vertices,ejes,dictVertices,i)
        i+=1
    #una vez se recorren todos los vertices adjacentes del vertice padre se marca como negro
    #para representar que ya fue completamente examinado
    dictVertices[vertice1]="negro"
    return centinela

def BFS(graph):
    """
        El algoritmo de BFS (breath-first-search)
        para encontrar componentes conectados
        se realiza una búsqueda de los vertices adjuntos
        a partir de un vertice s.
        Se sabe la distancia que se pueden llegar desde s
        -Los vertices se van coloreando dependiendo del estado de estos:
        Blanco: (Inexplorado)
        Gris: (Descubierto pero no sus vecinos)
        Negro: (vertice completamente descubierto)
    Args:
        graph (_list_): matriz simetrica que representa las conexiones entre los vertices
    """
    n=len(graph)+1  #inicializar distancia vertices
    vertices = {}
    #Inicializar vertices
    for i in range(len(graph)):
        vecinos=[]
        fila= graph[i]
        for j in range(len(fila)):
            if fila[j]==1:
                vecinos.append(j)
        vertices[i]=vertice(i,None,"Blanco",n,vecinos)
    #Se inicializa el vertice de 0 dandole los atributos necesarios
    s=0
    vertices[s]["distance"]=0
    vertices[s]["padre"]=None
    vertices[s]["color"]="Gris"
    i=0 #Representa el indice de un vertice, en este caso si el vertice ya ha sido revisado va a incrementarse hasta encontrar uno que no ha sido revisado
    subgrafos=[]#Representa los subgrafos totales encontrados
    revisados=[]# Representa cada subgrafo dentro del grafo total
    subgrafo=[i] # Representa cada vertice y sus vecinos se va actualizando 
    index_revisados=[i] # son los indices de los vertices que ya han sido revisados.
    while len(subgrafo)>0 and i<len(vertices): 
        index=subgrafo[0]  #Se obtiene el indice del vertice contenido
        subgrafo.pop(0)    # Se remueve de la lista de grafo para poder explorar sus vertices vecinos
        if index not in revisados:
            revisados.append(index) #Si el inidice no ha sido agregado a revisados se actualiza la lista con el inidce del grafo
        v=vertices[index] # vertice actual
        if len(v["vecinos"])>0: # Si sus vecinos son mayores a 0
            vecinos = v["vecinos"] #obtiene los vecinos 
            for j in range(len(vecinos)): #itera en los vecinos del vertice y les cambia el color
                vertice_vecino=vertices[vecinos[j]]
                index_vecino=vertice_vecino["index"]
                if vertice_vecino["color"]=="Blanco":
                    vertice_vecino["color"]="Gris"
                    vertice_vecino["padre"]=index
                    vertice_vecino["distance"]=v["distance"]+1
                    if index_vecino not in subgrafo: #agrega el indice a la lista de subgrafos
                        subgrafo.append(index_vecino)
        v["color"]="Negro" #actualiza el color del vertice por negro
        if index not in index_revisados:
            index_revisados.append(index)   #agrega el index del vertice a los indices revisados para no volver a iterar en estos
        if  len(subgrafo)==0:        #una vez que se acabe la lista de subgrafo actualiza la lista de revisados que equivale a cada subconexion y la agrega al total de subgrafos
            subgrafos.append(revisados)
            revisados=[]
            a=True
            while a:
                if i in index_revisados:
                    i+=1
                else:
                    a=False
            subgrafo=[i]  
    return subgrafos
    
def vertice(index:int,padre:int,color,distance,vecinos):
    vertice={
        "index": index,
        "padre":padre,
        "color": color,
        "distance": distance,
        "vecinos": vecinos
    }
    return vertice

numeroDiccionarios=list(map(int, sys.stdin.readline().split()))
c=0
while c < numeroDiccionarios[0]:
    fila_info=list(map(int, sys.stdin.readline().split()))
    numPaginas=fila_info[0]
    numPalabrasPorPaginas=fila_info[1]
    listaDiccionario=[0]*(numPaginas*numPalabrasPorPaginas)
    for i in range(numPaginas):
        fila = list(map(str,sys.stdin.readline().split()))
        pagina=int(fila[0])
        ubicacionInicial=pagina*numPalabrasPorPaginas
        i=1
        while i <= numPalabrasPorPaginas:
            listaDiccionario[ubicacionInicial-1+i]=fila[i]
            i+=1
    salida = funcionPrincipal(listaDiccionario)
    print(salida)
    c+=1



def ordenPalabra(palabra1,palabra2):
    centinela=False
    while i<len(palabra1) and not centinela:
        if palabra1[i]!=palabra2[2]:
            centinela=True
            registro=i
        else:
            i+=1
            centinela=ordenPalabra(palabra1,palabra2)
    return registro


print(ordenPalabra("hola","holo"))

        
