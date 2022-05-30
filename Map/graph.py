import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        self.graph = nx.Graph()
        self.pos = None
        self.petrol_stations = []

    def add_nodes(self, petrol_stations):
        for station in petrol_stations:
            self.graph.add_node(station)
        self.pos = {v: (v.x, v.y) for v in petrol_stations}

    def add_edges(self, roads):
        for road in roads:
            self.graph.add_edge(
                road.first_station,
                road.second_station,
                weight=(road.time_cost, road.fuel_cost),
                color="g",
            )

    def show(self):
        fig, ax = plt.subplots()
        nx.draw(self.graph, pos=self.pos, node_size=1000, ax=ax)
        nx.draw_networkx_labels(self.graph, pos=self.pos)  # draw node labels/names
        labels = nx.get_edge_attributes(self.graph, "weight")
        plt.axis("on")
        fig.set_size_inches(18.5, 10.5)
        ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
        plt.show()

    def show_path(self, path):
        g = self.graph.copy()
        pos = {v: (v.x, v.y) for v in self.graph.nodes()}
        color_map = []
        for station in self.graph.nodes():
            if station in path:
                color_map.append("blue")
            else:
                color_map.append("green")

        for i in range(len(path) - 1):
            g[path[i]][path[i + 1]]["color"] = "r"
            # edge_map.append(G[petrol_stations.index(path[i])][petrol_stations.index(path[i+1])]['red'])
        edge_map = []
        for v, u in g.edges():
            edge_map.append(g[v][u]["color"])

        fig, ax = plt.subplots()
        nx.draw(
            g, pos=pos, node_size=1000, node_color=color_map, edge_color=edge_map, ax=ax
        )
        nx.draw_networkx_labels(g, pos=pos)  # draw node labels/names
        labels = nx.get_edge_attributes(g, "weight")
        # nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)
        plt.axis("on")
        fig.set_size_inches(18.5, 10.5)
        ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
        plt.show()
