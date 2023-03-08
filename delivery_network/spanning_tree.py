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
    edges = {}
    X = Graph(nodes)
    for u in G.nodes : #construction d'un dictionnaire ayant pour clés le poids des arêtes [u,v]
        for v in range(len(G.graph[u])) :
            power = G.graph[u][v][1]
            edges[power] = [u,G.graph[u][v][0]]
    s_edges = sorted(edges)
    for power in s_edges :
        u = edges[power][0]
        v = edges[power][1]
        if U.find(u) != U.find(v):
            if u not in X.nodes :
                X.nodes.append(u)
            if v not in X.nodes :
                X.nodes.append(v) #on ajoute les sommets u et v à l'abre couvrant
            print(u,v,power)
            X.add_edge(u,v,power)
            U.union(u,v)
    return X

G = graph_from_file("input/network.00.in")
print(Kruskal(G))
