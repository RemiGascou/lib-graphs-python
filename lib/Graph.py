# -*- coding: utf-8 -*-

import graphviz

from lib.Edge import *
from lib.Node import *

class Graph(object):
    """docstring for Graph."""
    def __init__(self, listofnodelabels=[], listofedges=[]):
        super(Graph, self).__init__()
        if len(listofedges) != 0:
            if type(listofnodelabels[0]) == str: nodes = [Node(labelstr) for labelstr in listofnodelabels if type(labelstr) == str]
            elif type(listofnodelabels[0]) == int: nodes = [Node(labelint) for labelint in listofnodelabels if type(labelint) == int]
            elif type(listofnodelabels[0]) == Node: nodes = [node for node in listofnodelabels if type(node) == Node]
            if len(nodes) == len(listofnodelabels): self.nodes = nodes
            else: self.nodes = []
        else: self.nodes = []


        if len(listofedges) != 0:
            if type(listofedges[0]) == Edge: edges = [edge for edge in listofedges if type(edge) == Edge]
            elif len(listofedges[0]) == 2 and type(listofedges[0]) == list and type(listofedges[0][0]) == str and type(listofedges[0][1]) == str:
                edges = []
                for ledge  in listofedges:
                    nodestart = self.get_node_by_label(ledge[0])
                    nodedest  = self.get_node_by_label(ledge[1])
                    if nodestart != None and nodedest != None : edges.append(Edge(nodestart, nodedest))
            if len(edges) == len(listofedges): self.edges = edges
            else: self.edges = []
        else: self.edges = []


    def get_nodes (self):
        return self.nodes

    def get_node_by_label (self, label):
        for node in self.nodes:
            if node.get_label() == label:
                return node
        return None

    def get_Edges (self):
        return self.Edges

    def add_Edges (self, nodestart:Node, nodedest:Node):
        self.Edges.append(Edge(nodestart, nodedest))

    def add_node (self, nodeorlabel):
        if type(nodeorlabel) == Node:
            self.nodes.append(nodeorlabel)
        elif type(nodeorlabel) == str:
            self.nodes.append(Node(nodeorlabel))

    def export(self, pathtofilename:str, fileformat='png'):
        if pathtofilename.endswith("."+fileformat):
            pathtofilename = pathtofilename[:len(pathtofilename)-len("."+fileformat)]
            print(pathtofilename)
        dotfile = graphviz.Digraph(comment='Exported Graph')
        for n in self.nodes:
            dotfile.node(str(n.get_label()), str(n.get_description()))
        for a in self.edges:
            dotfile.edge(str(a.get_nodestart().get_label()), str(a.get_nodedest().get_label()), constraint='false')
        dotfile.render(pathtofilename, format="png", view=False, cleanup=True)
    def __len__(self):
        return len(self.nodes)
