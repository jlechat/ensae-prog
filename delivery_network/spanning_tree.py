from graph import Graph, graph_from_file, graph_from_file_route

#Question 12
class UnionFind:
    def __init__ (self, G = Graph()) :
        self.parent = {k : k for k in G.nodes} # le parent va permettre d'associer aux sommets d'un sous-ensemble un unique sommet qui sera leur "père" car on veut construire un arbre
        self.rank = {k : 0 for k in G.nodes}

    def find(self, k) : # on trouve le père d'un sommet au sein d'un sous-arbre
        if self.parent[k] != k :      
            return self.find(self.parent[k])
        else : return k

    def union(self, x, y) : # pour construire l'arbre, on relie deux sous-arbres par leurs pères : l'un devient le père de l'autre
        rx = self.find(x)
        ry = self.find(y)
        if self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else :
            self.parent[rx] = ry
            if self.rank[rx] == self.rank[ry] :
                self.rank[ry] += 1
        return None

 
    
def Kruskal(G) : # prend un graph G en entrée
    U = UnionFind(G)
    nodes = []
    edges = []
    X = Graph(nodes)
    for u in G.nodes : # construction d'une liste contenant toutes les arêtes de G (arête = [power, u, v])
        for v in range(len(G.graph[u])) :
            power = G.graph[u][v][1]
            v = G.graph[u][v][0]
            if [power, v, u] not in edges : # pour ne pas ajouter deux fois chaque arête
                edges.append([power, u, v])
    s_edges = sorted(edges) # on trie les arêtes par ordre de poids
    print(s_edges)
    for edge in s_edges : # pour chaque arête, si les sommets u et v ne sont pas dans le même sous-arbre, on va les relier jusqu'à avoir un arbre unique
        power = edge[0]
        u = edge[1]
        v = edge[2]
        if U.find(u) != U.find(v):
            X.add_edge(u,v,power) # on ajoute l'arête (u,v) à l'arbre couvrant
            U.union(u,v) # on unit les sous-arbres des sommets u et v pour qu'ils aient le même "père"(on crée un arbre, sans cycle)
    return X



#Question 14 : même fonction que la Q3 (j'ai pas d'autre idée)
def path_spanning_tree (S, src, dest) : 
    """ Should return power_min, path """

    nodes_v = {node : False for node in S.nodes}  # dictionnaire qui permet de savoir si l'on est déjà passé par un sommet
    nodes_v [src] = True
    powers = []  # on va garder dans une liste tous les powers plutôt que d'update un power_min, pour les cas où il faudrait repartir en arrière
        
    def parcours(node, path) :
        if node == dest:
            return max(powers), path
        for i in S.graph[node] :
            k=i[0]
            k_power = i[1]
            if not nodes_v[k] :
                nodes_v[k]=True
                powers.append(k_power)
                return parcours(k, path+[k])
            elif i == S.graph[node][-1] and path[-1] != src : # en cas de cul-de-sac, on repart en arrière
                nodes_v[i[0]]=True
                powers.pop()
                path.pop()
                k = path[-1]
                return parcours(k, path)
        return None

    return parcours(src, [src])



G = graph_from_file("input/network.00.in")
S = Kruskal(G)
print(path_spanning_tree(S,1,2))


            






