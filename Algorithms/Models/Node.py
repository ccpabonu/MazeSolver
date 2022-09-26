class Node:
    def __init__(self, name, parent=None, h=0):
        self.parent = parent
        self.name = name
        self.h = h
        self.children = []

    def insert(self, name):
        node = Node(name, self.name , self.h + 1)
        self.children.append(node)
        return node

    def value(self):
        return self.name

    def high(self):
        return self.h

    def numberChildren(self):
        return self.children.count()