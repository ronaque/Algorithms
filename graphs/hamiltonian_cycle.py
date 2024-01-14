from data_structures.graphs.node import Node
from data_structures.graphs.graph import Graph
from utils.tkinter import create_graph_with_tkinter


def backtracking_first_cycle(graph: Graph, input: Node, cycle: list):
    '''
    Algoritmo para encontrar um único ciclo hamiltoniano em um grafo não direcionado

    Parameters
    ----------
    graph: Instancia de Graph
    input: Node atual
    cycle: Nós no ciclo

    Returns
    -------

    '''
    # If the input is already in the cycle, return false
    if input in cycle:
        return False, cycle

    # Append the input to the cycle
    cycle.append(input)

    # Get the adjascent nodes of the input
    adjascent_nodes = input.adjascents

    # If the cycle size is equal to the number of nodes, check if the first node is adjascent to the last node
    if len(cycle) == len(graph.nodes):
        if cycle[0] in adjascent_nodes:
            # If it is, the cycle is complete, append the first node to the cycle and return true and the cycle
            cycle.append(cycle[0])
            return True, cycle

    # For each adjascent node of the input, call the backtracking recursively
    for adj_node in adjascent_nodes:
        boolback = backtracking_first_cycle(graph, adj_node, cycle)
        if boolback[0]:
            # If a cycle was found, return true and the cycle
            return True, cycle

    # If all adjascent Nodes of input were visited and no cycle was found
    # remove the input from the cycle and return false
    cycle.pop()
    return False, cycle

def get_first_cycle_backtracking():
    graph = create_graph_with_tkinter()
    boolback = backtracking_first_cycle(graph, graph.nodes[0], [])
    if boolback[0]:
        print("Cycle: ", [[node.id_node] for node in boolback[1]])
    else:
        print("The graph don't have a cycle")
