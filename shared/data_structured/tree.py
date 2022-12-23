class Node:
    def __init__(self, data, children=None):
        self.data = data
        self.children = None
        self.parent = None
        self.weight = None
        self.set_children(children)

    def set_children(self, children):
        self.children = children
        if children is not None:
            for h in self.children:
                h.parent = self

    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

    def is_equal(self, nodo):
        return self.get_data() == nodo.get_data()

    def in_list(self, list_nodes):
        for node in list_nodes:
            if self.is_equal(node):
                return True
        return False

    def __str__(self):
        return str(self.get_data())
