from graph import graph_from_file_route, graph_from_file, Graph, add_utility_from_file

g=graph_from_file("input/network.1.in")
add_utility_from_file("input/routes.1.in", g)

#algo glouton : pas très optimal, mais bonne approximation
#https://nsi4noobs.fr/IMG/pdf/f5_1nsi_algos_gloutons.pdf

#On commence par calculer le ration utilité/puissance pour chaque sommet
"""
Pb : ou rajouter l'utilité
pour l'instant elle est sur le graph, mais ca va etre compliqué de triller pour avoir les ratios maximaux (grande complexité)
essayer de le faire sur self.edges ? qui contient [min_power, node1, node2] comme le graph est non orientée.
il on veut ajouter la puissance associée dans cette liste de liste, mais il faut trouver le bon indice pour l'ajouter au bon endroit.

A FAIRE : que faire si on a deux utilités différentes ? et regler le pb dans le dico
"""

"""
dico=g.graph

for edge in dico.keys() :
    for j in range(len(dico[edge])) :
        dico[edge][j].append(dico[edge][j][3]/dico[edge][j][1])

sorted_dico= dict(sorted(dico.items(), key=lambda item:item[1][4]))
print(sorted_dico)
"""
print(g.edges)