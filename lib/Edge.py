# -*- coding: utf-8 -*-

from lib.Node import *

class Edge(object):
    """docstring for Edge."""
    def __init__(self, nodeStart, nodeDest):
        super(Edge, self).__init__()
        self.nodeStart = nodeStart
        self.nodeDest  = nodeDest

    def get_nodeStart(self):
        return self.nodeStart

    def get_nodedest(self):
        return self.nodeDest

    def __len__(self):
        pass
