# -*- coding: utf-8 -*-

from lib import *

def test(g:Graph, AlgorithmClass, args, expectedresult):
    result = AlgorithmClass(g).run(args[0], args[1])
    try: assert(result == expectedresult)
    except AssertionError: print("FailedTest : (result=" + str(result) + ", expectedresult=" + str(expectedresult) + ")")

edges = [[1, 2, 1], [1, 3, 1], [1, 4, 1], [2, 3, 1], [2, 5, 1], [3, 4, 1], [3, 5, 1], [5, 6, 1], [5, 7, 1], [6, 3, 1], [6, 7, 1]]
g1 = Graph([1,2,3,4,5,6,7])

for e in edges:
    g1.add_edges(Node(e[0]), Node(e[1]))
    
paths = g1.findpaths(1, 7)

for p in paths :
    print(p)



