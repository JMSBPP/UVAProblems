 
# Se dice que G es conectado si se puede encontrar un camino en 0 o más pasos
# # entre cualquier par de nodos en G.

# Un subgrafo conectado es máximo si no hay nodos ni aristas en
# el grafo original que podría agregarse al subgrafo dejandolo conectado

# Escriba un programa para determinar el número de subgrafos conectados máximos de un gráfico determinado.
class DisjSet:
    def __init__(self, n):
        # Constructor to create and
        # initialize sets of n items
        self.rank = [1] * n
        self.parent = {i: i for i in range(n)}
        self.size = n

    # Finds set of given item x
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # Do union of two sets represented
    # by x and y.
    def Union(self, x, y):
        xset = self.find(x)
        yset = self.find(y)

        if xset == yset:
            return

        self.size = self.size - 1

        if self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[xset] = yset
            if self.rank[xset] == self.rank[yset]:
                self.rank[yset] += 1


from sys import stdin 
# from icecream import ic

def main():
    test = int(stdin.readline().strip())
    # ic(test)
    stdin.readline()
    
    for _ in range(test):
        largest_node = stdin.readline().strip()
        edges = []

        grafo = {}
        grafo[largest_node] = grafo.get(largest_node, [])
        for i in range(ord(largest_node)-64):
            grafo[chr(ord(largest_node)-i)] = grafo.get(chr(ord(largest_node)-i), [])
        # ic(grafo)
        while True:
            edge = stdin.readline().strip()
            if not edge :
                break
            # ic(edge)
            edges.append(edge)
        # ic(edges)
        for edge in edges:
            if edge[0] in list(grafo.keys()):
                grafo[edge[0]].append(edge[1])
        # ic(grafo)
        

           

        disjuntos = DisjSet(len(grafo))
        disjuntos.parent = {v:v for v in grafo}
        disjuntos.rank = {v:1 for v in grafo}
        E = []
        for vert in list(grafo.keys()):
            for adj in grafo[vert]:
                E.append((vert, adj))

        # ic(E)
        for (u,v) in E:
            
            if disjuntos.find(u) != disjuntos.find(v):
                disjuntos.Union(u,v)
            else:
                disjuntos.rank[u]+=1  #¡Porque?
            # ic(disjuntos.parent)
            # ic(disjuntos.rank)
            # ic(disjuntos.size)
        print(disjuntos.size)
        if _ != test-1:
            print()
    
        

        
  

        




main()