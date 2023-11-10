from data_structures.graphs.node import Node
from data_structures.graphs.graph import Graph


def initialize_grafo_nao_direcionado(nos: list, adjascencias: list):
    grafo = Graph(nos)

    for no_1, no_2 in adjascencias:
        grafo.get_node_by_id(no_1).add_adjascent(no_2)
        grafo.get_node_by_id(no_2).add_adjascent(no_1)

    return grafo

def cin_initialize_grafo():
    nos = []
    no = int(input("Digite o número do nó, ou 0 para parar: "))
    while (not isinstance(no, int)) or no > 0:
        nos.append(Node(no))
        no = int(input("Digite o número do nó, ou 0 para parar: "))

    adjascencias = []
    no_1, no_2 = [int(v) for v in input("Digite as adjascencias, ou 0 0 para parar: ").split()]
    while ((not isinstance(no_1, int)) or no_1 > 0) or ((not isinstance(no_2, int)) or no_2 > 0):
        adjascencias.append((no_1, no_2))
        no_1, no_2 = [int(v) for v in input("Digite as adjascencias, ou 0 0 para parar: ").split()]

    grafo = initialize_grafo_nao_direcionado(nos, adjascencias)
    return grafo