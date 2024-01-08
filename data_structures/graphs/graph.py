from data_structures.graphs.node import Node


class Graph:
    def __init__(self, nodes=None, edges=None):
        if edges is None:
            edges = []
        if nodes is None:
            nodes = []
        self.nodes = nodes
        self.edges = edges

    def add_new_node(self):
        """
        Add a new node to the graph
        Returns
        -------

        """
        last_id = 0 if not self.nodes else self.nodes[-1].id_node + 1
        node = Node(last_id)
        self.nodes.append(node)

    def remove_node(self, node: Node):
        """
        Remove a node from the graph
        Parameters
        ----------
        node: Node to be removed

        Returns
        -------

        """
        self.nodes.remove(node)

    def get_node_by_id(self, id_node: int) -> Node | None:
        """
        Get a node by its id, if the node don't exist, return None
        Parameters
        ----------
        id_node: Id of the node

        Returns
        -------
        Node | None
        """
        for no in self.nodes:
            if no.id_node == id_node:
                return no
        return None

    def add_edge(self, id_node1: int, id_node2: int):
        """
        Add an edge between two nodes, using their ids
        The nodes Must exist
        Parameters
        ----------
        id_node1: Id of the first node
        id_node2: Id of the second node

        Returns
        -------

        """
        node1 = self.get_node_by_id(id_node1)
        node2 = self.get_node_by_id(id_node2)
        node1.add_adjascent(node2)
        node2.add_adjascent(node1)
        self.edges.append((node1, node2))

    def remove_edge(self, id_node1, id_node2):
        """
        Remove an edge between two nodes, using their ids
        The nodes Must exist
        Parameters
        ----------
        id_node1: Id of the first node
        id_node2: Id of the second node

        Returns
        -------

        """
        node1 = self.get_node_by_id(id_node1)
        node2 = self.get_node_by_id(id_node2)
        node1.remove_adjascent(node2)
        node2.remove_adjascent(node1)
        self.edges.remove((node1, node2))

    def check_edge_exist(self, id_node1, id_node2) -> bool:
        """
        Check if an edge exists between two nodes, using their ids
        Parameters
        ----------
        id_node1: Id of the first node
        id_node2: Id of the second node

        Returns
        -------
        bool
        """
        node1 = self.get_node_by_id(id_node1)
        node2 = self.get_node_by_id(id_node2)
        if (node1, node2) in self.edges or (node2, node1) in self.edges:
            return True
        return False
