from graph import Graph, graph_from_file, graph_from_file_route
from time import perf_counter
from random import randrange, seed, choice
for n in range (1,10) :
    data_path = "input/"
    file_name = "routes."+str(n)+".in"
    g = graph_from_file_route(data_path + file_name)
    time=0
    list=[l for l in g.graph.keys()]
    nb_tests = 8
    for i in range(nb_tests) :
        a=choice(list)
        b=choice(list)
        time_begin=perf_counter()

        g.get_path_with_power(a, b, 10)

        time_stop=perf_counter()
        print("Il s'est écoulé : ", time_stop-time_begin, "secondes.")

        time+=time_stop-time_begin
    tot_time_sec = (time/nb_tests)*((g.nb_nodes*(g.nb_nodes-1))/2)
    tot_time_h = tot_time_sec / 3600
    print("Pour calculer l'ensemble des trajets de", file_name, "il faudra : ", tot_time_sec, "secondes, soit", tot_time_min,"minutes.")