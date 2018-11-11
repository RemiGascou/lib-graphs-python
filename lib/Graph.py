# -*- coding: utf-8 -*-

import graphviz

from lib.Edge import *
from lib.Node import *

class Graph(object):
    """docstring for Graph."""
    def __init__(self, listOfNodeLabels=[], listOfEdges=[]):
        super(Graph, self).__init__()
        if len(listOfEdges) != 0:
            if type(listOfNodeLabels[0]) == str: nodes = [Node(labelstr) for labelstr in listOfNodeLabels if type(labelstr) == str]
            elif type(listOfNodeLabels[0]) == int: nodes = [Node(labelint) for labelint in listOfNodeLabels if type(labelint) == int]
            elif type(listOfNodeLabels[0]) == Node: nodes = [node for node in listOfNodeLabels if type(node) == Node]
            if len(nodes) == len(listOfNodeLabels): self.nodes = nodes
            else: self.nodes = []
        else: self.nodes = []

        if len(listOfEdges) != 0:
            edges = []
            if type(listOfEdges[0]) == Edge: edges = [edge for edge in listOfEdges if type(edge) == Edge]
            elif len(listOfEdges[0]) == 2 and type(listOfEdges[0]) == list and type(listOfEdges[0][0]) == str and type(listOfEdges[0][1]) == str:
                edges = []
                for edge in listOfEdges:
                    nodeStart = self.get_node_by_label(edge[0])
                    nodeDest  = self.get_node_by_label(edge[1])
                    if nodeStart != None and nodeDest != None : edges.append(Edge(nodeStart, nodeDest))
                if len(edges) == len(listOfEdges): self.edges = edges
            elif len(listOfEdges[0]) == 3 and type(listOfEdges[0]) == list and type(listOfEdges[0][0]) == str and type(listOfEdges[0][1]) == str and (type(listOfEdges[0][2]) == int or type(listOfEdges[0][2]) == float):
                edges = []
                for edge in listOfEdges:
                    nodeStart = self.get_node_by_label(edge[0])
                    nodeDest  = self.get_node_by_label(edge[1])
                    if nodeStart != None and nodeDest != None : edges.append(Edge(nodeStart, nodeDest, capacity=edge[2]))
                if len(edges) == len(listOfEdges): self.edges = edges
            elif len(listOfEdges[0]) == 4 and type(listOfEdges[0]) == list and type(listOfEdges[0][0]) == str and type(listOfEdges[0][1]) == str and (type(listOfEdges[0][2]) == int or type(listOfEdges[0][2]) == float) and (type(listOfEdges[0][3]) == int or type(listOfEdges[0][3]) == float):
                edges = []
                for edge in listOfEdges:
                    nodeStart = self.get_node_by_label(edge[0])
                    nodeDest  = self.get_node_by_label(edge[1])
                    if nodeStart != None and nodeDest != None : edges.append(Edge(nodeStart, nodeDest, capacity=edge[2], flow=edge[3]))
            else: self.edges = []
        else: self.edges = []

    def export(self, pathToFilename, fileformat='png'):
        if pathToFilename.endswith("."+fileformat):
            pathToFilename = pathToFilename[:len(pathToFilename)-len("."+fileformat)]
        dotfile = graphviz.Digraph(comment='Exported Graph')
        for node in self.nodes:
            dotfile.node(str(node.get_label()), str(node.get_description()))
        for edge in self.edges:
            dotfile.edge(str(edge.get_nodestart().get_label()), str(edge.get_nodedest().get_label()), constraint='false')
        dotfile.render(pathToFilename, format="png", view=False, cleanup=True)

# *----------------------------------Get Set---------------------------------- *

    def get_nodes (self):
        return self.nodes

    def get_node_by_label (self, label):
        for node in self.nodes:
            if node.get_label() == label:
                return node
        return None

    def get_edges (self):
        return self.edges

    def add_edges (self, nodeStart, nodeDest):
        self.edges.append(Edge(nodeStart, nodeDest))

    def add_node (self, nodeOrLabel):
        if type(nodeOrLabel) == Node:
            self.nodes.append(nodeOrLabel)
        elif type(nodeOrLabel) == str:
            self.nodes.append(Node(nodeOrLabel))

# *-----------------------------------Utils----------------------------------- *

    def __len__(self):
        return len(self.nodes), len(self.edges)
