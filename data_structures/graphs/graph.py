from data_structures.graphs.node import Node

class Graph:
    def __init__(self, nodes=None):
        if nodes is None:
            nodes = list()
        self.nodes = nodes

    def add_new_node(self):
        """
        Add a new node to the graph
        Returns
        -------

        """
        last_id = 0 if not self.nodes else self.nodes[-1].id_no + 1
        node = Node(last_id)
        self.nodes.append(node)

    def add_node(self, no):
        self.nodes.append(no)

    def get_node_by_id(self, id_no) -> Node | None:
        for no in self.nodes:
            if no.id_no == id_no:
                return no
        return None

    def remove_node(self, no):
        self.nodes.remove(no)

