# -*- coding: utf-8 -*-

from lib import *

def test(g:Graph, AlgorithmClass, args, expectedresult):
    result = AlgorithmClass(g).run(args[0], args[1])
    try: assert(result == expectedresult)
    except AssertionError: print("FailedTest : (result=" + str(result) + ", expectedresult=" + str(expectedresult) + ")")


g1 = Graph(["S", "A", "B", "C", "D", "T"], [["S", "A", 10], ["S", "C", 10], ["A", "B", 4], ["A", "D", 8], ["A", "C", 2], ["C", "D", 9], ["D", "B", 6], ["B", "T", 10], ["D", "T", 10]])

args=["A", "B"]
test(g1, DijkstraAlgorithm, args, 19)
