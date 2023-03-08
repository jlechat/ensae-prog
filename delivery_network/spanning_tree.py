from graph import Graph, graph_from_file, graph_from_file_route

class UnionFind:
    def __init__ (self, G = Graph()) :
        self.parent = {k : k for k in G.nodes}
        self.rank = {k : 0 for k in G.nodes}

    def find(self, k) :
        if self.parent[k] != k :      
            return self.find(self.parent[k])
        else : return k

    def union(self, x, y) :
        rx = self.find(x)
        ry = self.find(y)
        if self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else :
            self.parent[rx] = ry
            if self.rank[rx] == self.rank[ry] :
                self.rank[ry] += 1
        return None

 
    
def Kruskal(G) : #prend un graph G en entrée
    U = UnionFind(G)
    nodes = []
    edges = []
    X = Graph(nodes)
    for u in G.nodes : #construction d'une liste contenant toutes les arêtes de G (arête = [power, u, v])
        for v in range(len(G.graph[u])) :
            power = G.graph[u][v][1]
            v = G.graph[u][v][0]
            if [power, v, u] not in edges : #pour ne pas ajouter deux fois chaque arête
                edges.append([power, u, v])
    s_edges = sorted(edges) #on trie les arêtes par ordre de poids
    print(s_edges)
    for edge in s_edges :
        power = edge[0]
        u = edge[1]
        v = edge[2]
        if U.find(u) != U.find(v):
            X.add_edge(u,v,power) #on ajoute l'arête (u,v) à l'arbre couvrant
            U.union(u,v) #on unit les sous-ensembles des sommets u et v pour qu'ils aient le même "père"(on crée un arbre, sans cycle)
    return X

G = graph_from_file("input/network.02.in")
print(Kruskal(G))
