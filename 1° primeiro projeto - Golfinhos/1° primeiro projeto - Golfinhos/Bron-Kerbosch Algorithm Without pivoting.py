#Cria a lista de adjacencia dos 62 nós baseada nas 159 arestas dadas
def ListaAdjacencia():
    grafo = {}
    #N = input('digite a quantidade de arestas que dara entrada:')
    #for i in range(N):
    
    #Apesar de ter feito para qualquer tamanho de grafo, ja
    #implementei o valor de arestas no for abaixo(159).
    for i in range(159):
        aresta = [int(x) for x in input().split()]
        grafo[aresta[0]] = grafo.get(aresta[0], []) + [aresta[1]]
        grafo[aresta[1]] = grafo.get(aresta[1], []) + [aresta[0]]
    return grafo

#algorithm BronKerbosch1(R, P, X) is
#    if P and X are both empty then:
#        report R as a maximal clique
#    for each vertex v in P do
#        BronKerbosch1(R ⋃ {v}, P ⋂ N(v), X ⋂ N(v))
#        P := P \ {v}
#        X := X ⋃ {v}
#Codigo fonte da função a seguir retirado
#de: https://stackoverflow.com/questions/13904636/implementing-bron-kerbosch-algorithm-in-python
def BronKerbosch1(P, R=None, X=None):
    P = set(P)
    R = set() if R is None else R
    X = set() if X is None else X
    if not P and not X:
        yield sorted(R)
    while P:
        v = P.pop()
        yield from BronKerbosch1(
            P=P.intersection(grafo[v]), R=R.union([v]), X=X.intersection(grafo[v]))
        X.add(v)

#2° parte: Função para mostrar os Cliques Maximais
def ImprimeCliques(cliques):
    print('Cliques Maximais:')

    for i in cliques:
        print(f'({len(i)})nós:{i}')
        
#3° parte descobrir todos os coeficientes de aglomeração dos nós
#e em seguida fazer a media do grafo
def Aglomeração(grafo, cliques):
    #todas os coeficientes de aglomeração dos nós
    Aglomeração_Geral = []
    
    #percorre o grafo
    for i in grafo:
        triangulos = []
        for l in grafo[i]:
            for k in grafo[i]:
                if l != k and [l, k] not in triangulos:
                    for clique in cliques:
                        if i in clique and l in clique and k in clique:
                            #compara o no(i) e 2 vizinhos distintos(l e k) para
                            #conferir se existe triangulo nos cliques
                            triangulos.append([l, k])
                            triangulos.append([k, l])
                            break
        #Equação para descobrir o coeficente de aglomeração do nó (i)
        if len(grafo[i]) > 1:
            #Quantidade de triangulos encontrados/triangulos possiveis(n*(n-1)/2)
            Aglomeração_Geral.append((len(triangulos)/2)/(len(grafo[i])*(len(grafo[i])-1)/2))
        else:
            #caso o nó so tenha uma aresta
            Aglomeração_Geral.append(0.0)
    #soma da aglomeração de cada nó/quantidades de nó do grafo
    return f'\nCoeficiente médio de Aglomeração do Grafo = {sum(Aglomeração_Geral)/len(grafo)}'

#Construir a lista de adjacencia
grafo = ListaAdjacencia()

#Aplicando a funçao BronKerbosch1 para conseguir a lista de cliques maximais
cliques = list(BronKerbosch1(grafo.keys()))

#Imprime todos os cliques encontrados
ImprimeCliques(cliques)

#soma da aglomeração de cada nó/quantidades de nó do grafo
print(Aglomeração(grafo, cliques))