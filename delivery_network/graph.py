class Graph:
    """
    A class representing graphs as adjacency lists and implementing various algorithms on the graphs. Graphs in the class are not oriented. 
    Attributes: 
    -----------
    nodes: NodeType
        A list of nodes. Nodes can be of any immutable type, e.g., integer, float, or string.
        We will usually use a list of integers 1, ..., n.
    graph: dict
        A dictionnary that contains the adjacency list of each node in the form
        graph[node] = [(neighbor1, p1, d1), (neighbor1, p1, d1), ...]
        where p1 is the minimal power on the edge (node, neighbor1) and d1 is the distance on the edge
    nb_nodes: int
        The number of nodes.
    nb_edges: int
        The number of edges.
    """

    def __init__(self, nodes=[]):
        """
        Initializes the graph with a set of nodes, and no edges. 
        Parameters: 
        -----------
        nodes: list, optional
            A list of nodes. Default is empty.
        """
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
    

    def __str__(self):
        """Prints the graph as a list of neighbors for each node (one per line)"""
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output
    
    def add_edge(self, node1, node2, power_min, dist=1):
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes. 

        Parameters: 
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        power_min: numeric (int or float)
            Minimum power on this edge
        dist: numeric (int or float), optional
            Distance between node1 and node2 on the edge. Default is 1.
        """
        if node1 not in self.nodes  : 
            self.nodes.append(node1)
            self.graph[node1]=[]
            self.nb_nodes+=1
        if node2 not in self.nodes : 
            self.nodes.append(node2)
            self.graph[node2]=[]
            self.nb_nodes+=1
        self.graph[node1]=self.graph[node1]+[[node2, power_min, dist]]
        self.graph[node2]=self.graph[node2]+[[node1, power_min, dist]]
        self.nb_edges+=1


    def get_path_with_power(self, src, dest, power): #complexité en O(V²)
        #Q5 : on implémente un Dijkstra
        import math
        visited = {node : False for node in self.nodes} #dictionnaire qui permet de savoir si le noeud a déjà été visité ou non
        distance = {node : math.inf for node in self.nodes} #on donne +l'infini comme valeur de distance à la source pour tous les points
        visited[src] = True
        distance[src] = 0
        k = src
        path = [src]
        while dest not in path : 
            min_dist = math.inf
            for node in self.graph[k] : # on regarde pour tous les voisins si faire un détour par le voisin améliore la distance du sommet à la source
                new_dist = distance[k] + node[2]
                if not visited[node[0]]:
                    if new_dist < distance[node[0]] and node[1] <= power : # si la nouvelle distance est meilleure et que la puissance nécessaire reste dans nos cordes, on remplace la valeur de la distance actuelle par la nouvelle
                        distance[node[0]] = new_dist
                    if distance[node[0]] < min_dist : # on ne garde que la meilleure des distances trouvées en passant par de nouveaux sommets dans la boucle for
                        min_dist = distance[node[0]]
                        min_node = node[0]
            if min_dist != math.inf : # si min_dist a bougé, c'est qu'il y avait un nouveau sommet intéressant, donc on l'ajoute au chemin
                visited[min_node] = True
                path.append(min_node)
                k = min_node
            else : return None # si min_dist n'a pas bougé, c'est que la source et la destination ne sont pas reliées
        return "path : " + str(path) + ", distance : " + str(distance[dest])

        """ ************** Question 3  #complexité en O(V+E) ***************
        nodes_v={node : False for node in self.nodes} #dictionnaire qui permet de savoir si l'on est déjà passé par un point
        nodes_v[src] = True
        def parcours(node, chemin) :
            if node == dest:
                return chemin
            for i in self.graph[node] :
                k=i[0]
                k_power = i[1]
                if power >= k_power and not nodes_v[k]:
                    nodes_v[k]=True
                    return parcours(k, chemin+[k])
                elif i == self.graph[node][-1] and chemin[-1] != src :
                    nodes_v[i[0]]=True
                    chemin.pop()
                    k = chemin[-1]
                    return parcours(k, chemin)
            return None

        return parcours(src, [src])"""



    def connected_components(self): #complexité en O(V(V+E))
        l=[] #liste vide qui contiendra les listes de composants connectés
        nodes_v={node : False for node in self.nodes} #dictionnaire qui permet de savoir si l'on est déjà passé par un point

        def components(node) :
            comp=[node]
            for i in self.graph[node] :
                k=i[0]
                if not nodes_v[k] :
                    nodes_v[k]=True
                    comp+=components(k)
            return comp
        
        for k in self.nodes :
            if not nodes_v[k] : l.append(components(k))

        return l



    def connected_components_set(self):
        """
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        return set(map(frozenset, self.connected_components()))
    
    def min_power(self, src, dest): #complexité en O(log P + log((b-a)/0.1)), avec P la puissance nécessaire pour parcourir le trajet le + court
        """
        Should return path, min_power. 
        """        
        a = 0
        b = 1
        def dicho(a, b) : # on raisonne par dichotomie pour approcher la puissance minimale nécessaire sur le trajet
            while b-a > 0.1 :
                if self.get_path_with_power(src, dest, (a+b)/2) != None: #si le trajet est faisable, alors on peut diminuer b
                    b = (a+b)/2
                else :                                                   #si le trajet n'est pas faisable, il faut augmenter a
                    a = (a+b)/2
                dicho(a, b)
            return self.get_path_with_power(src, dest, b), b
        
        while self.get_path_with_power(src, dest, b) == None : # on augmente b rapidement pour trouver un majorant de la puissance du trajet
            b = 2*b
        return dicho(a, b)

def graph_from_file(filename):
    """
    Reads a text file and returns the graph as an object of the Graph class.

    The file should have the following format: 
        The first line of the file is 'n m'
        The next m lines have 'node1 node2 power_min dist' or 'node1 node2 power_min' (if dist is missing, it will be set to 1 by default)
        The nodes (node1, node2) should be named 1..n
        All values are integers.

    Parameters: 
    -----------
    filename: str
        The name of the file

    Outputs: 
    -----------
    G: Graph
        An object of the class Graph with the graph from file_name.
    """
    with open(filename, "r") as file:
        n, m = map(int, file.readline().split())
        g = Graph(range(1, n+1))
        for _ in range(m):
            edge = list(map(int, file.readline().split()))
            if len(edge) == 3:
                node1, node2, power_min = edge
                g.add_edge(node1, node2, power_min) # will add dist=1 by default
            elif len(edge) == 4:
                node1, node2, power_min, dist = edge
                g.add_edge(node1, node2, power_min, dist)
            else:
                raise Exception("Format incorrect")
    return g

def graph_from_file_route(filename):
    """
    Reads a text file and returns the graph as an object of the Graph class, for files routes.

    The file should have the following format: 
        The first line of the file is 'n' the number of edges
        The next m lines have 'node1 node2 power_min dist' or 'node1 node2 power_min' (if dist is missing, it will be set to 1 by default)
        The nodes (node1, node2) should be named 1..n
        All values are integers.

    Parameters: 
    -----------
    filename: str
        The name of the file

    Outputs: 
    -----------
    G: Graph
        An object of the class Graph with the graph from file_name.
    """
    with open(filename, "r") as file:
        nb_edges = int(file.readline())
        nodes = []
        n = list(range(len(nodes)))
        g = Graph(n)
        for _ in range(nb_edges):
            edge = list(map(int, file.readline().split()))
            if len(edge) == 3:
                node1, node2, power_min = edge
                g.add_edge(node1, node2, power_min) # will add dist=1 by default
            elif len(edge) == 4:
                node1, node2, power_min, dist = edge
                g.add_edge(node1, node2, power_min, dist)
            else:
                raise Exception("Format incorrect")
            if node1 not in nodes :
                nodes.append(node1)
            if node2 not in nodes :
                nodes.append(node2)
    return g






