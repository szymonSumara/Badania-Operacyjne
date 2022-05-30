import random

tank_capacity = 600


def DFS(graph, start, finish):
    path = []
    visited = set()

    def _DFS(graph, actual, finish, path, visited):
        visited.add(actual)
        path.append(actual)

        if actual == finish:
            return True

        neighbors = list(graph[actual])
        while len(neighbors) != 0:

            next_vertex = neighbors[random.randint(0, len(neighbors) - 1)]
            if next_vertex not in visited:
                if _DFS(graph, next_vertex, finish, path, visited):
                    return True
            else:
                neighbors.remove(next_vertex)

        path.remove(actual)
        return False

    _DFS(graph, start, finish, path, visited)
    return path


def get_random_refuel(graph, path):
    values = []
    for _ in path[1:]:
        if random.randint(0, 1) == 1 or len(values) == 0:
            values.append(random.randint(0, tank_capacity))
        else:
            values.append(0)
    return values


def get_valid_random_refuel(graph, path):
    values = []
    actual_fuel_level = 0

    for i in range(len(path[1:])):
        while True:
            next_path_cost = graph[path[i]][path[i + 1]]["weight"][1]
            next_refuel = None

            if random.randint(0, 1) == 1 or len(values) == 0:
                next_refuel = random.randint(0, tank_capacity)
            else:
                next_refuel = 0

            if (
                actual_fuel_level + next_refuel - next_path_cost > 0
                and actual_fuel_level + next_refuel - next_path_cost < tank_capacity
            ):
                values.append(next_refuel)
                actual_fuel_level -= next_path_cost
                actual_fuel_level += next_refuel
                break
    return values


def find_valid_solution(G, start, end):
    path = DFS(G, start, end)
    values = get_valid_random_refuel(G, path)
    return path, values
