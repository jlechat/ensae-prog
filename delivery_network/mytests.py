from graph import graph_from_file_route, graph_from_file
from spanning_tree import Kruskal, UnionFind
from time import perf_counter


#calcul du temps nécessaire pour exécuter Kruskal

for n in range (1,10) :
    data_path = "input/"
    file_name = "routes."+str(n)+".in"
    g = graph_from_file_route(data_path + file_name)
    time=0

    time_begin=perf_counter()

    Kruskal(g)

    time_stop=perf_counter()
    time+=time_stop-time_begin
    
    print("Pour construire un arbre couvrant de ", file_name, "il faut : ", time, "secondes.")
