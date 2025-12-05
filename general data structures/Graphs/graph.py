

class Node:
    def __init__(self, val):
        self.value = val
        self.edges = []

    def set_value(self, val):
        self.value = val

    def get_value(self):
        return self.value

    def get_edges(self):
        return self.edges

    def __str__(self):
        return "Node with value " + str(self.value)


class Graph:
    def __init__(self):
        self.nodes = []

    def get_nodes(self):
        return self.nodes

    def add_node(self, n):
        if n in self.get_nodes():
            raise ValueError("Node already exists.")
        self.nodes.append(n)

    def add_edge(self, n1:Node, n2:Node):
        if self.edge_exists(n1,n2):
            raise ValueError("Node already exists.")
        n1.edges.append(n2)
        n2.edges.append(n1)

    def __str__(self):
        s = "Graph with the following nodes:"
        for n in self.get_nodes():
            s += "\n\t" + str(n)
        return s

    def edge_exists(self, n1:Node, n2:Node):
        return n2 in n1.get_edges()