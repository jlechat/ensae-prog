from ortools.linear_solver import pywraplp
from graph import graph_from_file, graph_from_file_route

#Création des données
data = {}
data['weights'] = []
data['values'] = []


assert len(data['weights']) == len(data['values'])
data['num_items'] = len(data['weights'])
data['all_items'] = range(data['num_items'])

data['bin_capacities'] = [100, 100, 100, 100, 100]
data['num_bins'] = len(data['bin_capacities'])
data['all_bins'] = range(data['num_bins'])


#création du solveur
solver = pywraplp.Solver.CreateSolver('SCIP')
if solver is None:
    print('SCIP solver unavailable.')
    return

# x[i, b] = 1 if item i is packed in bin b.
x = {}
for i in data['all_items']:
    for b in data['all_bins']:
        x[i, b] = solver.BoolVar(f'x_{i}_{b}')

# Each item is assigned to at most one bin.
for i in data['all_items']:
    solver.Add(sum(x[i, b] for b in data['all_bins']) <= 1)

# The amount packed in each bin cannot exceed its capacity (ie la puissance du camion doit être supérieure ou égale à la puissance du trajet).
for b in data['all_bins']:
    solver.Add(
        sum(x[i, b] * data['weights'][i]
            for i in data['all_items']) >= data['bin_capacities'][b])

# Total amount of costs cannot exceed budget / weights cannot exceed 

# Maximize total value (ie utility) of packed items.
objective = solver.Objective()
for i in data['all_items']:
    for b in data['all_bins']:
        objective.SetCoefficient(x[i, b], data['values'][i])
objective.SetMaximization()

#Appel du solutionneur
status = solver.Solve()

#Affichage des résultats
if status == pywraplp.Solver.OPTIMAL:
    print(f'Total packed value: {objective.Value()}')
    total_weight = 0
    for b in data['all_bins']:
        print(f'Bin {b}')
        bin_weight = 0
        bin_value = 0
        for i in data['all_items']:
            if x[i, b].solution_value() > 0:
                print(
                    f"Item {i} weight: {data['weights'][i]} value: {data['values'][i]}"
                )
                bin_weight += data['weights'][i]
                bin_value += data['values'][i]
        print(f'Packed bin weight: {bin_weight}')
        print(f'Packed bin value: {bin_value}\n')
        total_weight += bin_weight
    print(f'Total packed weight: {total_weight}')
else:
    print('The problem does not have an optimal solution.')