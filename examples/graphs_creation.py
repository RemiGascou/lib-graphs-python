# -*- coding: utf-8 -*-


from lib import *


g1 = Graph(["a", "b", "c", "d", "e"], [["a", "b"], ["b", "c"], ["d", "e"], ["b", "e"], ["c", "a"]]) #list of node labels of the same type.
g1.export("graph.png", fileformat='png')

g2 = Graph([c for c in "abcdefghijkl"])

g3 = Graph([0, 1, 2, 3, 4])

g4 = Graph(list(range(5)))
