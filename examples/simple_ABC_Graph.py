# -*- coding: utf-8 -*-


from lib import *

g1 = Graph(["a", "b", "c"], [["a", "b"], ["b", "c"], ["c", "a"]])
g1.export("simple_ABC_Graph.png", fileformat='png')
