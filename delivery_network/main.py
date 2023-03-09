from graph import Graph, graph_from_file, graph_from_file_route
from time import perf_counter
from random import randrange, seed, choice

for n in range (1,10) : #on va chercher le temps total qu'il faut pour trouver un chemin entre toutes les paires de sommets dans les 10 fichiers route
    data_path = "input/"
    file_name = "routes."+str(n)+".in"
    g = graph_from_file_route(data_path + file_name)
    time=0
    list=[l for l in g.graph.keys()]
    nb_tests = 8
    for i in range(nb_tests) : #on lance le compteur pour des sommets choisis au hasard dans le graphe
        a=choice(list)
        b=choice(list)
        time_begin=perf_counter()

        g.get_path_with_power(a, b, 10)

        time_stop=perf_counter()
        time+=time_stop-time_begin
    
    print("Pour calculer un trajet de", file_name, "il s'est écoulé en moyenne : ", time/nb_tests, "secondes.")
    
    tot_time_sec = (time/nb_tests)*((g.nb_nodes*(g.nb_nodes-1))/2) #à partir du temps moyen obtenu, on calcule le temps qu'il faudrait pour trouver tous les chemins possibles dans le graphe (il y en a n(n-1)/2 avec n = nb de noeuds)
    tot_time_h = tot_time_sec / 3600
    print("Pour calculer l'ensemble des trajets de", file_name, "il faudra : ", tot_time_sec, "secondes, soit", tot_time_h,"heures.")
