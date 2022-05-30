import random


def fuel_mutation(path_original, refuels_original):
    refuels = refuels_original[:]
    idx = random.randint(0, len(refuels) - 2)

    val1 = 0
    val2 = 0
    #     if idx == 0:
    #         val1 = refuels[idx] + random.randint(-30,0)
    #         val2 = refuels[idx + 1] + random.randint(0,30)
    #     else:
    val1 = refuels[idx] + random.randint(-30, 30)
    val2 = refuels[idx + 1] + random.randint(-30, 30)
    if val1 < 0:
        refuels[idx] = 0
    else:
        refuels[idx] = val1

    if val2 < 0:
        refuels[idx] = 0
    else:
        refuels[idx] = val2

    return path_original[:], refuels


def new_neighbour_mutation(graph, path_original, refuels_original):
    candidates = []
    path = path_original[:]
    refuels = refuels_original[:]
    for i in range(len(path) - 1):
        neigbours = graph.graph[path[i]]
        next_neighbours = graph.graph[path[i + 1]]
        for el in neigbours:
            if el in next_neighbours:
                if el not in path:
                    candidates.append((i + 1, el))
    if len(candidates) == 0:
        return None, None
    j, n = random.choice(candidates)
    path.insert(j, n)
    refuels.insert(j, random.randint(0, 100))
    return path, refuels


def skip_neighbour_mutation(graph, path_original, refuels_original):
    path = path_original[:]
    refuels = refuels_original[:]
    candidates = []
    for i in range(len(path) - 2):
        neigbours = graph.graph[path[i]]
        for el in neigbours:
            if path[i + 2] == el:
                candidates.append(i)
    if len(candidates) > 0:
        i = random.choice(candidates)
        del path[i + 1]
        del refuels[i + 1]
        return path, refuels
    return None, None
