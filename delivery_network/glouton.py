from graph import graph_from_file_route, graph_from_file, Graph, add_utility

#algo glouton : pas très optimal, mais bonne approximation
#https://nsi4noobs.fr/IMG/pdf/f5_1nsi_algos_gloutons.pdf

#On commence par calculer le ration utilité/puissance pour chaque sommet
"""
Pb : ou rajouter l'utilité
pour l'instant elle est sur le graph, mais ca va etre compliqué de triller pour avoir les ratios maximaux (grande complexité)
essayer de le faire sur self.edges ? qui contient [min_power, node1, node2] comme le graph est non orientée.
il on veut ajouter la puissance associée dans cette liste de liste, mais il faut trouver le bon indice pour l'ajouter au bon endroit.

A FAIRE : que faire si on a deux utilités différentes ? et regler le pb dans le dico (avec la dernière arrete)

A CHANGER : appeler get path with power sans contrainte de puissance pour trouver le graph optimisé (déjà fait ?)
[node1, node2, min_power, utility]

TD 30 mars :
1- Trouver le camion qui coute le moins cher pour réaliser un trajet (ATTENTION : pas besoin de voir le profit, juste l'utilité)
2- Faire le glouton avec ces données

"""

#Trouver le camion meilleur rapport "qualité-prix" pour chaque trajat
#Il s'agit de trouver le camion qui coute le moins cher qui est capable d'effectuer le trajet

class Camion:
    def __init__(self, cam=[]):
        self.cam = cam #puissance, que l'on suppose suffisante pour identifier un camion
        self.dico = dict([(n, []) for n in cam]) #puissance et cout dans cet ordre

    def add_camion(self, filename) :
        """Completer le dictionnaire avec le fichier

        Args:
            filename (str): nom du fichier trucks
        """
        with open(filename, "r") as file:
            n = int(file.readline())
            for i in range(n):
                a = list(map(int, file.readline().split()))
                self.dico[a[0]]=a[1]


cam=Camion()
print(cam.dico)

cam.add_camion("input/trucks.1.in")
print(cam.dico)


"""
dico=g.graph

for edge in dico.keys() :
    for j in range(len(dico[edge])) :
        dico[edge][j].append(dico[edge][j][3]/dico[edge][j][1])

sorted_dico= dict(sorted(dico.items(), key=lambda item:item[1][4]))
print(sorted_dico)
"""
#g=add_utility(1)
