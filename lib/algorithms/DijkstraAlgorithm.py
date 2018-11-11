# -*- coding: utf-8 -*-

from lib.Graph import *

class DijkstraAlgorithm(object):
    """docstring for DijkstraAlgorithm."""
    def __init__(self, graph:Graph):
        super(DijkstraAlgorithm, self).__init__()
        self.graph = graph
        self.table = {}

    def run(self, labelNodeStart, labelNodeDest):
        if self.isGraphPositive():
            #Init
            self.table[labelNodeStart] = []
            for node in self.graph.get_nodes():
                if node.get_label() != labelNodeStart:
                    self.table[str(node.get_label())] = []
            print(self.table)
            #Processing
            labelselected = labelNodeStart
            del self.table[labelselected]
            while labelselected != labelNodeDest:
                ## Update table :
                for edge in self.graph.get_edges():
                    if edge.get_nodeStart().get_label() == labelselected:
                        self.table[str(edge.get_nodeDest().get_label())].append(edge.get_capacity())
                ## Seek minimum
                # mini, labelmini = -1, ""
                # for e in self.table:
                #     if mini == -1 and len(self.table[e]) != 0: mini, labelmini = self.table[e][-1], e
                #     elif self.table[e][-1] < mini: mini, labelmini = self.table[e][-1], e
                #
                # labelselected = labelmini
                print(self.table)
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
