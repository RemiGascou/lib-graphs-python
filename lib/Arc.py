


class Arc(object):
    """docstring for Arc."""
    def __init__(self, nodestart:Node, nodedest:Node):
        super(Arc, self).__init__()
        self.nodestart = nodestart
        self.nodedest  = nodedest

    def get_nodestart(self):
        return self.nodestart

    def get_nodedest(self):
        return self.nodedest


    def __len__(self):
        pass
