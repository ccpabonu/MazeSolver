import sys


class Width:
    def __init__(self, tree, target, grapher):
        self.grapher = grapher
        self.tree = tree
        self.target = target
        self.queue = [self.tree]
        a = self.tree.name.split(',')
        self.track = [[int(x) for x in a]]
        self.count = 1
        sys.setrecursionlimit(2000)
        self.searchWithImg()

    def searchWithImg(self):
        self.grapher.printTrack(self.track, f"{self.count}")
        self.count = self.count + 1
        nodo = self.queue.pop(0)
        if nodo.name != self.target:
            self.queue = self.queue + list(nodo.children)
            for child in nodo.children:
                a = child.name.split(',')
                self.track.append([int(x) for x in a])
            self.searchWithImg()

    def search(self):
        self.count = self.count + 1
        nodo = self.queue.pop(0)
        if nodo.name != self.target:
            self.queue = self.queue + list(nodo.children)
            self.search()
