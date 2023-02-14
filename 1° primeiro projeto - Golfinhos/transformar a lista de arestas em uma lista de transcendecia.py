grafo = {}
for i in range(159):
    aresta = [int(x) for x in input().split()]
    grafo[aresta[0]] = grafo.get(aresta[0], []) + [aresta[1]]
    grafo[aresta[1]] = grafo.get(aresta[1], []) + [aresta[0]]


for i in sorted(grafo):
    print(grafo[i])