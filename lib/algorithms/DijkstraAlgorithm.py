# -*- coding: utf-8 -*-

from lib.Graph import *

class DijkstraAlgorithm(object):
    """docstring for DijkstraAlgorithm."""
    def __init__(self, graph:Graph):
        super(DijkstraAlgorithm, self).__init__()
        self.graph = graph
        self.table = {}
        self.choices = {}

    def run(self, labelNodeStart, labelNodeDest):
        if self.isGraphPositive():
            #Init
            self.choices[labelNodeStart] = [0]
            for node in self.graph.get_nodes():
                if node.get_label() != labelNodeStart:
                    self.table[str(node.get_label())] = []
            #Processing
            labelselected = labelNodeStart
            while labelselected != labelNodeDest:
                print("labelselected : ", labelselected)
                ## Update table :
                for edge in self.graph.get_edges():
                    if edge.get_nodeStart().get_label() == labelselected:
                        if len(self.table[str(edge.get_nodeDest().get_label())]) == 0: self.table[str(edge.get_nodeDest().get_label())].append(edge.get_capacity())
                        else: self.table[str(edge.get_nodeDest().get_label())].append(self.table[str(edge.get_nodeDest().get_label())][-1] + edge.get_capacity())
                ## Seek minimum
                mini, labelmini = -1, ""
                for e in self.table:
                    if len(self.table[e]) != 0:
                        if mini == -1:
                            mini, labelmini = self.table[e][-1], e
                        elif self.table[e][-1] <= mini:
                            mini, labelmini = self.table[e][-1], e

                print("Old labelselected :", labelselected)
                if labelselected != labelNodeStart:
                    self.choices[str(labelselected)] = self.table[str(labelselected)][-1]
                labelselected = labelmini
                print("New labelselected :", labelselected)
                print("labelmini :", labelmini)
                print("self.table :", self.table)
                print("self.choices :", self.choices)
                print("\n")

            #Return
            if len(self.table[labelNodeStart]) == 0: return None
            else : return self.table[labelNodeStart][-1]
        else:
            return None

    def isGraphPositive(self):
        for edge in self.graph.get_edges():
            if edge.get_capacity() < 0:
                return False
        return True
