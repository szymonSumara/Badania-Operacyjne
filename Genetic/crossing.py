import random
from Genetic.solution_validation import is_valid


def findCommonElements(path1, path2):
    indexes_of_common_elements = []
    for el in path2:
        if el in path1:
            indexes_of_common_elements.append(True)
        else:
            indexes_of_common_elements.append(False)
    if len(indexes_of_common_elements) == 2:
        return [None, None]
    commonPairs = []
    i = 0
    while i < len(indexes_of_common_elements) - 2:
        if not indexes_of_common_elements[i]:
            i += 1
            continue
        j = i + 1
        while not indexes_of_common_elements[j]:
            j += 1
        if j < len(indexes_of_common_elements):
            if i + 2 <= j:
                commonPairs.append((i, j))
            i = j

    if len(commonPairs) == 0:
        return [None, None]
    i, j = random.choice(commonPairs)
    return [path2[i], path2[j]]


def crossing2(graph, path1, path2, refuels1, refuels2):
    choices = findCommonElements(path1, path2)
    if choices[0] is None:
        return (None, None)
    indexes1 = [path1.index(el) for el in choices]
    indexes1.sort()
    indexes2 = [path2.index(path1[el]) for el in indexes1]
    second_part = []
    second_part_refuels = []
    if indexes2[0] > indexes2[1]:
        second_part = path2[indexes2[1] : indexes2[0] + 1][::-1]
        second_part_refuels = refuels2[indexes2[1] : indexes2[0] + 1][::-1]
    else:
        second_part = path2[indexes2[0] : indexes2[1] + 1]
        second_part_refuels = refuels2[indexes2[0] : indexes2[1] + 1]
    newPath1 = path1[: indexes1[0]] + second_part + path1[indexes1[1] + 1 :]
    newRefules1 = (
        refuels1[: indexes1[0]] + second_part_refuels + refuels1[indexes1[1] + 1 :]
    )
    #     print(calculate_solution_cost(graph.graph,newPath1,newRefules1,a,b))
    if is_valid(graph.graph, newPath1, newRefules1):
        #         print(calculate_solution_cost(graph.graph,newPath1,newRefules1,a,b))
        return (newPath1, newRefules1)

    return (None, None)
