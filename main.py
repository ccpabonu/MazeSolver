
from Algorithms.Models.TreeGenerator import TreeGenerator
import csv
import numpy
from anytree import Node, RenderTree
from anytree.exporter import DotExporter

from Algorithms.Width import Width
from UI.BoardGrapher import BoardGrapher

if __name__ == '__main__':
    reader = csv.reader(open("MazeExamples/maze_10x10.csv", "rt"), delimiter=",")
    x = list(reader)
    x = [ele for ele in x if ele != []]
    result = numpy.array(x)
    route = "UI"
    g = BoardGrapher(result, "maze_10x10", route)

    treeGen = TreeGenerator(result)
    tree = treeGen.getTree()
    print(RenderTree(tree))
    target = treeGen.getTarget()
    d = Width(tree, target, g)
    g.printGif()




    # g = BoardGrapher(result, "maze_5x5", route)
    # track = [[0, 1]]
    # g.printTrack(track, "1")
    # track = [[0, 1], [1, 1]]
    # g.printTrack(track, "2")
    # track = [[0, 1], [1, 1], [2, 1]]
    # g.printTrack(track, "3")
    # track = [[0, 1], [1, 1], [2, 1], [2, 2]]
    # g.printTrack(track, "4")
    # track = [[0, 1], [1, 1], [2, 1], [2, 2], [2, 3]]
    # g.printTrack(track, "5")
    # track = [[0, 1], [1, 1], [2, 1], [2, 2], [2, 3], [3, 3]]
    # g.printTrack(track, "6")
    # track = [[0, 1], [1, 1], [2, 1], [2, 2], [2, 3], [3, 3], [4, 3]]
    # g.printTrack(track, "7")

    # app = QApplication(sys.argv)
    # windows = MainWindows()
    # windows.show()
    # sys.exit(app.exec())



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




    # DotExporter(root).to_dotfile("root.dot")
    # from graphviz import render
    # render('dot', 'png', 'root.dot')