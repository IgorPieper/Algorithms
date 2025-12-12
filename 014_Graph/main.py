class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_list = {}

    def add_vertex(self, node):
        if node not in self.adjacent_list:
            self.adjacent_list[node] = []
            self.number_of_nodes += 1

    def add_edge(self, node1, node2):
        if node2 not in self.adjacent_list[node1]:
            self.adjacent_list[node1].append(node2)

        if node1 not in self.adjacent_list[node2]:
            self.adjacent_list[node2].append(node1)

    def show_connections(self):
        for node in self.adjacent_list:
            connections = " ".join(self.adjacent_list[node])
            print(f"{node}-->{connections}")
