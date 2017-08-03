import numpy as np
import os

def getDistancia(ponto, centroide):
    return np.sqrt(np.sum((ponto - centroide)**2))

def addRotuloCluster(distancia, pontoDados, centroides):
    indiceDoMinimo = min(distancia, key=distancia.get)
    return [indiceDoMinimo, pontoDados, centroides[indiceDoMinimo]]

def computaNovosCentroides(rotuloCluster, centroides):
    return np.array(rotuloCluster + centroides)/2

def iteraKMeans(pontosDados, centroides, nIteracoes):
    rotulo = []
    rotuloCluster = []
    pontosTotal = len(pontosDados)
    k = len(centroides)
    
    for it in range(0, nIteracoes):
        for indicePonto in range(0, pontosTotal):
            distancia = {}
            for indiceCentroide in range(0, k):
                distancia[indiceCentroide] = getDistancia(pontosDados[indicePonto], centroides[indiceCentroide])
            rotulo = addRotuloCluster(distancia, pontosDados[indicePonto], centroides)
            centroides[rotulo[0]] = computaNovosCentroides(rotulo[1], centroides[rotulo[0]])

            if it == (nIteracoes - 1):
                rotuloCluster.append(rotulo)

    return [rotuloCluster, centroides]

def imprimeRotuloDado(result):
    print("Resultado do agrupamento k-Means: \n")
    for it in result[0]:
        print("Ponto: {}".format(it[1]))
        print("ID do Grupo: {} \n".format(it[0]))
    print("Ultima posicao do centroide: \n {}".format(result[1]))

def create_centroides():

    centroides = []
    centroides.append([5.0, 0.0])
    centroides.append([45.0, 70.0])
    centroides.append([50.0, 90.0])
    return np.array(centroides)

nomeArq = os.path.dirname(__file__) + "pontos.csv"
pontosDados = np.genfromtxt(nomeArq, delimiter=",")
centroides = create_centroides()
nIteracoes = 100
    
[rotuloCluster, new_centroides] = iteraKMeans(pontosDados, centroides, nIteracoes)
imprimeRotuloDado([rotuloCluster, new_centroides])
