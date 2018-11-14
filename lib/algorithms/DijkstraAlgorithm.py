# -*- coding: utf-8 -*-

from lib.Graph import *

class DijkstraAlgorithm(object):
    """docstring for DijkstraAlgorithm."""
    def __init__(self, graph:Graph):
        super(DijkstraAlgorithm, self).__init__()
        self.graph   = graph
        self.table   = {}
        self.choices = {}

    def run(self, labelNodeStart, labelNodeDest):
        if self.isGraphPositive():
            nodes, edges           = self.graph.get_nodes(), self.graph.get_edges()
            nodeStart, nodeDest    = self.graph.get_node_by_label(labelNodeStart), self.graph.get_node_by_label(labelNodeDest)
            distances, nodes_seen  = {}, []
            infvalue               = sum([e.get_capacity() for e in edges])

            if nodeStart == None or nodeDest == None: return None

            for node in nodes: distances[node.get_label()] = infvalue
            distances[nodeStart.get_label()] = 0


            while len(nodes_seen) <= len(nodes) :
                currentNode = self.__get_minimum_node(distances)
                nodes_seen.append(currentNode)
                if currentNode == nodeDest: return None

                for edge in edges:
                    print("distances :",distances)
                    if edge.get_nodeStart() == currentNode:
                        dist = distances[currentNode.get_label()] + edge.get_capacity()
                        if dist < distances[edge.get_nodeDest().get_label()]:
                            distances[edge.get_nodeDest().get_label()] = dist

            return None

    def __get_minimum_node(self, distances):
        mini, nodemini = -1, None
        for node in self.graph.get_nodes():
            if mini == -1: mini, nodemini = distances[node.get_label()], node
            elif distances[node.get_label()] <= mini: mini, nodemini = distances[node.get_label()], node
        return nodemini


    # def run(self, labelNodeStart, labelNodeDest):
    #     if self.isGraphPositive():
    #         #Init
    #         self.choices[labelNodeStart] = [0]
    #         for node in self.graph.get_nodes():
    #             if node.get_label() != labelNodeStart:
    #                 self.table[str(node.get_label())] = []
    #         #Processing
    #         labelselected = labelNodeStart
    #         while labelselected != labelNodeDest:
    #             print("labelselected : ", labelselected)
    #             ## Update table :
    #             for edge in self.graph.get_edges():
    #                 if edge.get_nodeStart().get_label() == labelselected:
    #                     if len(self.table[str(edge.get_nodeDest().get_label())]) == 0: self.table[str(edge.get_nodeDest().get_label())].append(edge.get_capacity())
    #                     else: self.table[str(edge.get_nodeDest().get_label())].append(self.table[str(edge.get_nodeDest().get_label())][-1] + edge.get_capacity())
    #             ## Seek minimum
    #             mini, labelmini = -1, ""
    #             for e in self.table:
    #                 if len(self.table[e]) != 0:
    #                     if mini == -1:
    #                         mini, labelmini = self.table[e][-1], e
    #                     elif self.table[e][-1] <= mini:
    #                         mini, labelmini = self.table[e][-1], e
    #
    #             print("Old labelselected :", labelselected)
    #             if labelselected != labelNodeStart:
    #                 self.choices[str(labelselected)] = self.table[str(labelselected)][-1]
    #             labelselected = labelmini
    #             print("New labelselected :", labelselected)
    #             print("labelmini :", labelmini)
    #             print("self.table :", self.table)
    #             print("self.choices :", self.choices)
    #             print("\n")
    #
    #         #Return
    #         if len(self.table[labelNodeStart]) == 0: return None
    #         else : return self.table[labelNodeStart][-1]
    #     else:
    #         return None

    def isGraphPositive(self):
        for edge in self.graph.get_edges():
            if edge.get_capacity() < 0:
                return False
        return True
