from tkinter import *

from data_structures.graphs.graph import Graph


def create_graph_with_tkinter():
    interface = Tk()
    interface.title("Graph Creator")

    graph = Graph()

    button_add_node = Button(interface, text="Add Node", command=graph.add_new_node)
    button_add_node.pack()

    interface.mainloop()
