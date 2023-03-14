#******************** Ce fichier nous sert lors de la conception des programmes ********************


from graph import Graph, graph_from_file_route, graph_from_file
from spanning_tree import Kruskal, UnionFind
from time import perf_counter

g = graph_from_file_route("input/network.00.in")
print(g.min_power(1,4))

