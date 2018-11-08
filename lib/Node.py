# -*- coding: utf-8 -*-

class Node(object):
    """docstring for Node."""
    def __init__(self, label):
        super(Node, self).__init__()
        self.label       = label
        self.description = ''

    def get_label(self):
        return self.label

    def get_description(self):
        if len(self.description) != 0:
            return self.description
        elif len(self.description) == 0:
            return self.label

    def __str__(self):
        return str(self.label)
