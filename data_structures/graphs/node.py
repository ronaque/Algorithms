class Node:
    def __init__(self, id_node):
        self.adjascents = []
        self.id_node = id_node

    def add_adjascent(self, adjascente):
        self.adjascents.append(adjascente)

    def remove_adjascent(self, adjascente):
        self.adjascents.remove(adjascente)

