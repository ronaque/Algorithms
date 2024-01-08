from tkinter import *
from tkinter.messagebox import showinfo

from data_structures.graphs.graph import Graph


def tkinter_update_nodes_frame(frame_nodes: Frame, graph: Graph):
    for widget in frame_nodes.winfo_children():
        widget.destroy()

    for idx, node in enumerate(graph.nodes):
        label = Label(frame_nodes, text=f"Node {node.id_node}")
        aux_column = idx % 4
        aux_row = idx // 4
        label.grid(row=aux_row, column=aux_column, padx=2, pady=2)


def tkinter_update_edges_frame(frame_edges: Frame, graph: Graph):
    for widget in frame_edges.winfo_children():
        widget.destroy()

    for idx, edge in enumerate(graph.edges):
        label = Label(frame_edges, text=f"({edge[0].id_node}, {edge[1].id_node})")
        aux_column = idx % 4
        aux_row = idx // 4
        label.grid(row=aux_row, column=aux_column, padx=2, pady=2)


def tkinter_add_node(graph: Graph, frame_nodes: Frame):
    graph.add_new_node()
    tkinter_update_nodes_frame(frame_nodes, graph)


def tkinter_remove_node(graph: Graph, frame_nodes: Frame):
    graph.remove_node(graph.nodes[-1])
    tkinter_update_nodes_frame(frame_nodes, graph)


def tkinter_add_edge(graph: Graph, frame_edges: Frame, text_node1: Text, text_node2: Text):
    id_node1 = int(text_node1.get(1.0, END))
    id_node2 = int(text_node2.get(1.0, END))

    if graph.get_node_by_id(id_node1) is None or graph.get_node_by_id(id_node2) is None:
        showinfo("Error", "One of the nodes doesn't exist")
        return
    if graph.check_edge_exist(id_node1, id_node2):
        showinfo("Error", "This edge already exists")
        return

    graph.add_edge(id_node1, id_node2)
    tkinter_update_edges_frame(frame_edges, graph)


def tkinter_remove_edge(graph: Graph, frame_edges: Frame, text_node1: Text, text_node2: Text):
    id_node1 = int(text_node1.get(1.0, END))
    id_node2 = int(text_node2.get(1.0, END))

    if graph.get_node_by_id(id_node1) is None or graph.get_node_by_id(id_node2) is None:
        showinfo("Error", "One of the nodes doesn't exist")
        return
    if not graph.check_edge_exist(id_node1, id_node2):
        showinfo("Error", "This edge doesn't exist")
        return

    graph.remove_edge(id_node1, id_node2)
    tkinter_update_edges_frame(frame_edges, graph)


def create_graph_with_tkinter():
    interface = Tk()
    interface.geometry("500x500")
    interface.title("Graph Creator")

    graph = Graph()

    frame_nodes = Frame(interface)
    frame_nodes.pack(pady=10)

    frame_buttons = Frame(interface)
    frame_buttons.pack(pady=10)

    button_add_node = Button(frame_buttons, text="Add Node", command=lambda: tkinter_add_node(graph, frame_nodes))
    button_add_node.grid(row=0, column=0, padx=10, pady=10)

    button_remove_node = Button(frame_buttons, text="Remove Node",
                                command=lambda: tkinter_remove_node(graph, frame_nodes))
    button_remove_node.grid(row=0, column=2, padx=10, pady=10)

    button_add_edge = Button(frame_buttons, text="Add Edge",
                             command=lambda: tkinter_add_edge(graph, frame_edges, text_node1, text_node2))
    button_add_edge.grid(row=2, column=0, padx=10, pady=10)

    button_remove_edge = Button(frame_buttons, text="Remove Edge",
                                command=lambda: tkinter_remove_edge(graph, frame_edges, text_node1, text_node2))
    button_remove_edge.grid(row=2, column=2, padx=10, pady=10)

    text_node1 = Text(frame_buttons, height=1, width=8)
    text_node1.insert(1.0, "")
    text_node1.grid(row=1, column=0, padx=10, pady=(50, 10))

    text_node2 = Text(frame_buttons, height=1, width=8)
    text_node2.insert(1.0, "")
    text_node2.grid(row=1, column=2, padx=10, pady=(50, 10))

    exit_button = Button(frame_buttons, text="Finish", command=interface.destroy)
    exit_button.grid(row=3, column=1, columnspan=1, padx=20, pady=20)

    frame_edges = Frame(interface)
    frame_edges.pack(pady=10)

    interface.mainloop()

    return graph
