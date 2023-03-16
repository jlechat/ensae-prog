from graph import graph_from_file_route, graph_from_file, Graph, add_utility_from_file


g=graph_from_file("input/network.1.in")
print(g)
add_utility_from_file("input/routes.1.in", g)
print(g)
