from graph import graph_from_file_route
from spanning_tree import Kruskal, path_spanning_tree
from time import perf_counter
from random import choice

for n in range (1,10) : # on va chercher le temps total qu'il faut pour trouver un chemin entre toutes les paires de sommets dans les 10 fichiers route
    data_path = "input/"
    file_name = "routes."+str(n)+".in"
    G = graph_from_file_route(data_path + file_name)
    S = Kruskal(G)
    time=0
    list=[l for l in S.graph.keys()]
    nb_tests = 8
    for i in range(nb_tests) : # on lance le compteur pour des sommets choisis au hasard dans le graphe
        a=choice(list)
        b=choice(list)
        time_begin=perf_counter()

        path_spanning_tree(S, a, b)

        time_stop=perf_counter()
        time+=time_stop-time_begin
    
    print("Pour calculer un trajet de", file_name, "il s'est écoulé en moyenne : ", time/nb_tests, "secondes.")
    
    tot_time_sec = (time/nb_tests)*S.nb_edges # à partir du temps moyen obtenu, on calcule le temps qu'il faudrait pour trouver tous les chemins possibles dans le graphe
    tot_time_min = tot_time_sec / 60
    print("Pour calculer l'ensemble des trajets de", file_name, "il faudra : ", tot_time_sec, "secondes, soit", tot_time_min,"min.")



"""************ Début des résultats d'exécution **************************
Pour calculer un trajet de routes.1.in il s'est écoulé en moyenne :  7.075053872540593e-06 secondes.
Pour calculer l'ensemble des trajets de routes.1.in il faudra :  0.00013442602357827127 secondes, soit 2.240433726304521e-06 min.

RecursionError: maximum recursion depth exceeded in comparison"""
# la fonction récursive "parcours" boucle trop sur elle-même

# les algorithmes que nous avons implémentés dans le TD2 n'ont donc pas permis de réduire le temps de calcul.