# -*- coding: utf-8 -*-

class Node(object):
    """docstring for Node."""
    def __init__(self, label):
        super(Node, self).__init__()
        self.label = label

    def get_label(self):
        return self.label

    def get_description(self):
        return self.get_description

    def __str__(self):
        return str(self.label)
