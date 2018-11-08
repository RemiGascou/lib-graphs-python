# -*- coding: utf-8 -*-

import graphviz

from lib.Arc import *
from lib.Node import *

class Graph(object):
    """docstring for Graph."""
    def __init__(self, listoflabels:list):
        super(Graph, self).__init__()
        if type(listoflabels[0]) == str: nodes = [Node(labelstr) for labelstr in listoflabels if type(labelstr) == str]
        elif type(listoflabels[0]) == int: nodes = [Node(labelint) for labelint in listoflabels if type(labelint) == int]
        elif type(listoflabels[0]) == Node: nodes = [node for node in listoflabels if type(node) == Node]

        if len(nodes) == len(listoflabels): self.nodes = nodes
        else: self.nodes = []
        self.arcs = []

    def get_nodes (self):
        return self.nodes

    def get_arcs (self):
        return self.arcs

    def add_arcs (self, nodestart:Node, nodedest:Node):
        self.arcs.append(Arc(nodestart, nodedest))

    def add_node (self, nodeorlabel):
        if type(nodeorlabel) == Node:
            self.nodes.append(nodeorlabel)
        elif type(nodeorlabel) == str:
            self.nodes.append(Node(nodeorlabel))

    def export(self, pathtofilename:str):
        if not pathtofilename.endswith(".png"):
            pathtofilename =+ ".png"
        dotfile = graphviz.Digraph(comment='Exported Graph')
        for n in self.nodes:
            dotfile.node(str(n.get_label()), str(n.get_description()))
        for a in self.arcs:
            dotfile.edge(a.get_nodestart().get_label(), a.get_nodedest().get_label(), constraint='false')
        dotfile.render(pathtofilename, view=True)

    def __len__(self):
        return len(self.nodes)
