import random
import config

from Genetic.solution_validation import is_valid, calculate_solution_cost
from Genetic.solution_generation import find_valid_solution
from Genetic.crossing import crossing2
from Genetic.mutations import (
    fuel_mutation,
    new_neighbour_mutation,
    skip_neighbour_mutation,
)


def generate_initial_population(graph, number, start_station, finish_station):
    population = []
    for i in range(number):
        population.append(
            find_valid_solution(graph.graph, start_station, finish_station)
        )
    return population


def genetic_algorithm(graph, start_station, end_station):

    population = generate_initial_population(graph, config.start_population_size, start_station, end_station)
    for i in range(config.number_of_epochs):
        population.sort(
            key=lambda item: calculate_solution_cost(
                graph.graph, item[0], item[1]
            )
        )
        population = population[:100]
        graph.show_path(population[0][0])
        print(population[0][1])

        print("-------------")
        for item in population[:10]:
            print(calculate_solution_cost(graph.graph, item[0], item[1]))

        new_population = []
        for j in range(config.number_of_crossing):
            parents = random.choices(population, k=2)
            children = crossing2(
                graph, parents[0][0], parents[1][0], parents[0][1], parents[1][1]
            )
            if children[0] is None:
                continue
            new_population.append(children)
        for j in range(config.number_of_fuel_mutation):
            parents = random.choice(population)
            path, refuel = fuel_mutation(parents[0], parents[1])
            if path is None:
                continue
            if is_valid(graph.graph, path, refuel):
                new_population.append((path, refuel))
        for j in range(config.number_of_add_neighbour_mutation):
            parents = random.choice(population)
            path, refuel = new_neighbour_mutation(graph, parents[0], parents[1])
            if path is None:
                continue
            if is_valid(graph.graph, path, refuel):
                new_population.append((path, refuel))
        for j in range(config.number_of_skip_neighbour_mutation):
            parents = random.choice(population)
            path, refuel = skip_neighbour_mutation(graph, parents[0], parents[1])
            if path is None:
                continue
            if is_valid(graph.graph, path, refuel):
                new_population.append((path, refuel))
        population = new_population
    population.sort(
        key=lambda item: calculate_solution_cost(graph.graph, item[0], item[1])
    )


    population.sort(
        key=lambda item: calculate_solution_cost(graph.graph, item[0], item[1])
    )
    return population[0]
