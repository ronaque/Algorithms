from data_structures.graphs.node import Node
from data_structures.graphs.graph import Graph
from data_structures.graphs.util import cin_initialize_grafo

def backtracking_first_cycle(grafo: Graph, input: Node, ciclo: list):
    '''
    Algoritmo para encontrar um único ciclo hamiltoniano em um grafo não direcionado

    Parameters
    ----------
    grafo: Instancia de Graph
    input: Node atual
    ciclo: Nós no ciclo

    Returns
    -------

    '''
    # Se input está em r
    if input in ciclo:
        # Retorne falso
        return False, ciclo
    # Insere input em r
    ciclo.append(input)
    # C recebe os nós adjascents de input
    c = input.adjascents
    # Se o tamanho de r é igual o número de nós em G e r[0] está em c
    if len(ciclo) == len(grafo.nodes):
        if ciclo[0] in c:
            # Retorne verdadeiro
            ciclo.append(ciclo[0])
            return True, ciclo

    # Para cada ci em c
    for ci in c:
        # Recursividade do backtracking
        boolback = backtracking_first_cycle(grafo, ci, ciclo)
        if boolback:
            # Se encontrou um ciclo, retorne verdadeiro e o ciclo
            return True, ciclo
    # Se todos os adjanscentes de input já estão em r, remova input e retorne falso
    ciclo.pop()
    return False, ciclo

def executar_backtracking_unico_ciclo():
    grafo = cin_initialize_grafo()
    boolback = backtracking_first_cycle(grafo, grafo.nodes[0], [])
    if boolback[0]:
        print("Existe ciclo: ", [[no.id_no] for no in boolback[1]])
    else:
        print("Não existe ciclo")
