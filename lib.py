import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = nx.Graph()

    def generate_graph(self, description):
        if "полный граф" in description:
            n = int(description.split()[-2])
            self.graph = nx.complete_graph(n)
        elif "дерево" in description:
            n = int(description.split()[-2])
            self.graph = nx.balanced_tree(n+1, 1)
        elif "граф с" in description:
            n = int(description.split()[-3])
            self.graph = nx.caveman_graph(n, 3)

    def save_to_file(self, filename):
        nodes = self.graph.nodes()
        edges = self.graph.edges()
        with open(filename, 'w') as f:
            f.write(f"вершины: {list(nodes)}\n")
            f.write(f"ребра: {list(edges)}\n")

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
            nodes = eval(lines[0].split(": ")[1])
            edges = eval(lines[1].split(": ")[1])
            self.graph.add_nodes_from(nodes)
            self.graph.add_edges_from(edges)

    def visualize(self):
        nx.draw(self.graph, with_labels=True)
        plt.show()