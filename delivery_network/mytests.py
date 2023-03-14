from graph import graph_from_file, graph_from_file_route
from spanning_tree import Kruskal
from random import randrange, choice
from time import perf_counter
from spanning_tree import route, Kruskal, path_spanning_tree, UnionFinds

g = graph_from_file_route("input/network.00.in")
kruskal = g.kruskal()
f = open("input/network..00.in", "r")
h = open("input/network.route.x.out", "w")
nb_route = f.readline()
for i in range(int(nb_route) - 1):
    line = f.readline().split()
    src = int(line[0])
    dest = int(line[1])
    h.write(str(path_spanning_tree(g, src, dest)[1]) + "\n")
f.close()
h.close()