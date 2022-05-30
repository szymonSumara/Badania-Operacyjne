import matplotlib.pyplot as plt
import networkx as nx
import pickle

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Map.graph import Graph
from Map.utils import create_random_map, get_first_and_last_station
from Genetic.core import genetic_algorithm



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {name}")  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    petrol_stations_map = create_random_map()
    # nx.write_weighted_edgelist( petrol_stations_map.graph, "graph.txt")
    with open('graph.txt', 'wb') as config_dictionary_file:
        pickle.dump(petrol_stations_map, config_dictionary_file)

    petrol_stations_map = pickle.load(open('graph.txt', 'rb'))
    petrol_stations_map.show()
    start_station, end_station = get_first_and_last_station(petrol_stations_map.graph.nodes)
    genetic_algorithm(petrol_stations_map, start_station, end_station)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
