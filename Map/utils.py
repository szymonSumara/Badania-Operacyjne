import math
import random
import config

from Map.petrolStation import PetrolStation
from Map.road import Road
from Map.graph import Graph

def distance_between(petrol_station1, petrol_station2):
    return math.sqrt(
        (petrol_station1.x - petrol_station2.x) ** 2
        + (petrol_station1.y - petrol_station2.y) ** 2
    )


def get_random_petrol_station(map_size, petrol_prizes):
    x = random.randint(0, map_size)
    y = random.randint(0, map_size)
    cost = random.randint(petrol_prizes[0], petrol_prizes[1])
    return PetrolStation(x, y, cost)

def get_first_and_last_station(petrol_stations):
    petrol = PetrolStation(0,0,0)
    sorted_stations= sorted(petrol_stations,key= lambda c: distance_between(petrol,c))
    return sorted_stations[0],sorted_stations[-1]


def get_first_and_last_station(petrol_stations):
    petrol = PetrolStation(0, 0, 0)
    sorted_stations = sorted(petrol_stations, key=lambda c: distance_between(petrol, c))
    print(sorted_stations)
    return sorted_stations[0], sorted_stations[-1]


def calculate_fuel_and_time_costs_off_road(distance):
    return (
        distance * (100 + random.randint(-30, 30)) // 100,
        distance * (100 + random.randint(-30, 30)) // 100,
    )


def generate_petrol_stations(
    petrol_stations_number=100, map_size=1000, petrol_prices=(1, 10)
):
    petrol_stations = []
    for i in range(petrol_stations_number):
        while True:
            new_petrol_station = get_random_petrol_station(map_size, petrol_prices)
            distance_is_ok = True
            for petrol_station in petrol_stations:
                if distance_between(petrol_station, new_petrol_station) < 70:
                    distance_is_ok = False
                    break
            if not distance_is_ok:
                continue
            petrol_stations.append(new_petrol_station)
            break
    return petrol_stations


def add_roads(petrol_stations):
    roads = []
    for i in range(len(petrol_stations) - 1):
        petrol_station = petrol_stations[i]
        roads_number = random.randint(1, 3)
        petrol_stations_copy = petrol_stations[:]
        petrol_stations_copy.remove(petrol_station)
        while roads_number > 0:
            nearest_neighbour = min(
                petrol_stations_copy, key=lambda c: distance_between(petrol_station, c)
            )
            time_cost, fuel_cost = calculate_fuel_and_time_costs_off_road(
                distance_between(petrol_station, nearest_neighbour)
            )
            road = Road(petrol_station, nearest_neighbour, time_cost, fuel_cost)
            if road in roads:
                petrol_stations_copy.remove(nearest_neighbour)
            else:
                roads.append(
                    Road(petrol_station, nearest_neighbour, time_cost, fuel_cost)
                )
                roads_number -= 1

    return roads


def create_random_map():
    petrol_stations = generate_petrol_stations(
        petrol_stations_number=config.petrol_stations_number,
        petrol_prices=config.petrol_prices,
        map_size=config.map_size,
    )
    roads = add_roads(petrol_stations)
    graph = Graph()
    graph.add_nodes(petrol_stations)
    graph.add_edges(roads)
    graph.show()
    return graph
