import sys

from PyQt5.QtWidgets import QApplication

from Algorithms.Models.Node import Node
from TreeGenerator import TreeGenerator
from UI.BoardGrapher import BoardGrapher
import csv
import numpy

from UI.MainWindows import MainWindows

if __name__ == '__main__':
    reader = csv.reader(open("MazeExamples/maze_5x5.csv", "rt"), delimiter=",")
    x = list(reader)
    x = [ele for ele in x if ele != []]
    result = numpy.array(x)


    route = "UI"
    g = BoardGrapher(result, "maze_5x5", route)
    track = [[0, 1]]
    g.printTrack(track, "1")
    track = [[0, 1], [1, 1]]
    g.printTrack(track, "2")
    track = [[0, 1], [1, 1], [2, 1]]
    g.printTrack(track, "3")
    track = [[0, 1], [1, 1], [2, 1], [2, 2]]
    g.printTrack(track, "4")
    track = [[0, 1], [1, 1], [2, 1], [2, 2], [2, 3]]
    g.printTrack(track, "5")
    track = [[0, 1], [1, 1], [2, 1], [2, 2], [2, 3], [3, 3]]
    g.printTrack(track, "6")
    track = [[0, 1], [1, 1], [2, 1], [2, 2], [2, 3], [3, 3], [4, 3]]
    g.printTrack(track, "7")

    # app = QApplication(sys.argv)
    # windows = MainWindows()
    # windows.show()
    # sys.exit(app.exec())

    from anytree import Node, RenderTree
    from anytree.exporter import DotExporter


    # ceo = Node("CEO")  # root
    # vp_1 = Node("VP_1", parent=ceo)
    # vp_2 = Node("VP_2", parent=ceo)
    # gm_1 = Node("GM_1", parent=vp_1)
    # gm_2 = Node("GM_2", parent=vp_2)
    # m_1 = Node("M_1", parent=gm_2)
    # DotExporter(ceo).to_dotfile("ceo.dot")
    #
    # from graphviz import render
    #
    # render('dot', 'png', 'ceo.dot')

    #tree =TreeGenerator(result)
    #root = Node(f"{0},{1}")
    #print(root)
    #tree.createTree(root)