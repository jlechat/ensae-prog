
#******************** Ce fichier nous sert lors de la conception des programmes ********************

from graph import graph_from_file_route, graph_from_file
from spanning_tree import Kruskal, UnionFind
from time import perf_counter


#calcul du temps nécessaire pour exécuter Kruskal

for n in range (1,10) :
    data_path = "input/"
    file_name = "routes."+str(n)+".in"

    time1=0
    time1_begin=perf_counter()
    g = graph_from_file_route(data_path + file_name)
    time1_stop=perf_counter()
    time2 = time1_stop-time1_begin
    time2=0

    time2_begin=perf_counter()

    Kruskal(g)

    time2_stop=perf_counter()
    time2 = time2_stop-time2_begin
    
    print("Pour exécuter graph_from_file_route de", file_name, "il faut : ", time1/60, "minutes.")
    print("Pour construire un arbre couvrant de", file_name, "il faut : ", time2/60, "minutes.")

"""Pour exécuter graph_from_file_route de routes.1.in il faut :  0.0 minutes.
Pour construire un arbre couvrant de routes.1.in il faut :  3.388749125103156e-06 minutes.
Pour exécuter graph_from_file_route de routes.2.in il faut :  0.0 minutes.
Pour construire un arbre couvrant de routes.2.in il faut :  1.2575840330993135 minutes.
Pour exécuter graph_from_file_route de routes.3.in il faut :  0.0 minutes.
Pour construire un arbre couvrant de routes.3.in il faut :  2.0910675054163828 minutes."""