# -*- coding: utf-8 -*-

from lib import *

def test(g:Graph, AlgorithmClass, args, expectedresult):
    result = AlgorithmClass(g).run(args[0], args[1])
    try: assert(result == expectedresult)
    except AssertionError: print("FailedTest : (result=" + str(result) + ", expectedresult=" + str(expectedresult) + ")")


g1 = Graph([c for c in "ABCDEFGH"], [["A", "B", 12], ["A", "D", 14], ["B", "G", 16], ["B", "H", 21], ["B", "F", 9], ["G", "H", 11], ["F", "H", 11], ["E", "C", 13], ["E", "F", 16], ["E", "H", 10], ["C", "F", 10]])

args=["A", "H"]
test(g1, DijkstraAlgorithm, args, 32)
