from anytree import Node, RenderTree
from anytree.exporter import DotExporter


class TreeGenerator:
    def __init__(self, matrix):
        self.matrix = matrix
        self.m, self.n = self.matrix.shape
        self.root = Node(f"{0},{1}")
        self.createTree(self.root)

    def createTree(self, root, parent=None):
        x, y = root.name.split(',')
        if parent is None:
            xp, yp = -1, -1
        else:
            xp, yp = parent.name.split(',')
        x, y, xp, yp = int(x), int(y), int(xp), int(yp)

        if y - 1 >= 0:
            if self.matrix[x][y - 1] == 'c' and (x != xp or y - 1 != yp):
                child = Node(f"{x},{y - 1}", root)
                self.createTree(child, root)

        if x - 1 >= 0:
            if self.matrix[x-1][y] == 'c' and (x - 1 != xp or y != yp):
                child = Node(f"{x-1},{y}", root)
                self.createTree(child, root)

        if y + 1 < self.m:
            if self.matrix[x][y+1] == 'c' and (x != xp or y + 1 != yp):
                child = Node(f"{x},{y+1}", root)
                self.createTree(child, root)

        if x + 1 < self.n:
            if self.matrix[x+1][y] == 'c' and (x + 1 != xp or y != yp):
                child = Node(f"{x+1},{y}", root)
                self.createTree(child, root)

    def getTree (self):
        return self.root

    def getTarget(self):
        return str(self.n-1)+','+str(self.m-2)
