# -*- coding: utf-8 -*-

from lib.Node import *

class Edge(object):
    """docstring for Edge."""
    def __init__(self, nodestart:Node, nodedest:Node):
        super(Edge, self).__init__()
        self.nodestart = nodestart
        self.nodedest  = nodedest

    def get_nodestart(self):
        return self.nodestart

    def get_nodedest(self):
        return self.nodedest


    def __len__(self):
        pass
