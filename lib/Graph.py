# -*- coding: utf-8 -*-

import graphviz

from lib.Arc import *
from lib.Node import *

class Graph(object):
    """docstring for Graph."""
    def __init__(self, listoflabels=[], listofarcs=[]):
        super(Graph, self).__init__()
        if type(listoflabels[0]) == str: nodes = [Node(labelstr) for labelstr in listoflabels if type(labelstr) == str]
        elif type(listoflabels[0]) == int: nodes = [Node(labelint) for labelint in listoflabels if type(labelint) == int]
        elif type(listoflabels[0]) == Node: nodes = [node for node in listoflabels if type(node) == Node]

        if len(nodes) == len(listoflabels): self.nodes = nodes
        else: self.nodes = []
        
        if type(listofarcs[0]) == Arc: arcs = [arc for arc in listofarcs if type(arc) == Arc]
        elif len(listofarcs[0]) == 2 and type(listofarcs[0]) == list and type(listofarcs[0][0]) == str and type(listofarcs[0][1]) == str:
            arcs = []
            for larc in listofarcs:
                nodestart = self.get_node_by_label(larc[0])
                nodedest  = self.get_node_by_label(larc[1])
                if nodestart != None and nodedest != None : arcs.append(Arc(nodestart, nodedest))

        if len(arcs) == len(listofarcs): self.arcs = arcs
        else: self.arcs = []


    def get_nodes (self):
        return self.nodes

    def get_node_by_label (self, label):
        for node in self.nodes:
            if node.get_label() == label:
                return node
        return None

    def get_arcs (self):
        return self.arcs

    def add_arcs (self, nodestart:Node, nodedest:Node):
        self.arcs.append(Arc(nodestart, nodedest))

    def add_node (self, nodeorlabel):
        if type(nodeorlabel) == Node:
            self.nodes.append(nodeorlabel)
        elif type(nodeorlabel) == str:
            self.nodes.append(Node(nodeorlabel))

    def export(self, pathtofilename:str, fileformat='png'):
        if not pathtofilename.endswith(".png"):
            pathtofilename =+ ".png"
        dotfile = graphviz.Digraph(comment='Exported Graph')
        for n in self.nodes:
            dotfile.node(str(n.get_label()), str(n.get_description()))
        for a in self.arcs:
            dotfile.edge(str(a.get_nodestart().get_label()), str(a.get_nodedest().get_label()), constraint='false')
        dotfile.render(pathtofilename, format="png", view=True)

    def __len__(self):
        return len(self.nodes)
