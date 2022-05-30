import config

def is_valid(graph, path, values):
    tank = 0
    for i in range(len(path) - 1):

        tank += values[i]
        tank -= graph[path[i]][path[i + 1]]["weight"][1]
        if tank < 0 or tank > config.tank_capacity:
            return False
    return True


def calculate_solution_cost(graph, path, values):
    fuel_cost = 0
    time_cost = 0
    for i in range(len(path) - 1):
        time_cost += graph[path[i]][path[i + 1]]["weight"][0]
        fuel_cost += (values[i]) * path[i].cost
    return config.a * time_cost + config.b * fuel_cost, fuel_cost, time_cost
