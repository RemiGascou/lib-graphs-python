# -*- coding: utf-8 -*-

from lib import *

g1 = Graph(["S", "A", "B", "C", "D", "T"], [["S", "A", 10], ["S", "C", 10], ["A", "B", 4], ["A", "D", 8], ["A", "C", 2], ["C", "D", 9], ["D", "B", 6], ["B", "T", 10], ["D", "T", 10]])

#g1.export("simple_ABC_Graph.png", fileformat='png')

for e in g1.get_edges():
    print(e)

a_ff = FordFulkersonAlgorithm(g1)   #
result = a_ff.run()                 # Returns result : Should be 19
