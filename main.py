import sys

from PyQt5.QtWidgets import QApplication

from Algorithms.Depth import Depth
from Algorithms.Models.TreeGenerator import TreeGenerator
import csv
import numpy
from anytree import Node, RenderTree
from anytree.exporter import DotExporter
from UI.BoardGrapher import BoardGrapher
from UI.MainWindows import MainWindows

from Algorithms.Width import Width
from Algorithms.Depth import Depth
from Algorithms.GreedySearch import Greedy_Search
from Algorithms.IterativeDepth import Iterative_Depth
from Algorithms.AStar import A_Star
from Algorithms.UniformCostSearch import UniformCostSearch

if __name__ == '__main__':
    reader = csv.reader(open("MazeExamples/maze_10x10.csv", "rt"), delimiter=",")
    x = list(reader)
    x = [ele for ele in x if ele != []]
    result = numpy.array(x)
    route = "UI"
    g = BoardGrapher(result, "maze_10x10", route)

    #Width
 
    # h = BoardGrapher(result, "maze_10x10", route)
    # DF_Search = Depth(result,h) #Depth First Searc
    # h.printGif()

    # i = BoardGrapher(result, "maze_10x10", route)
    # Greedy_Search_f = Greedy_Search(result,i)
    # i.printGif()

    # j = BoardGrapher(result, "maze_10x10", route)
    # IDFS = Iterative_Depth(result,j)
    # j.printGif()

    # k = BoardGrapher(result, "maze_10x10", route)
    # A_Star_f = A_Star(result,k)
    # k.printGif()

    # l = BoardGrapher(result, "maze_10x10", route)
    # UCSearch = UniformCostSearch(result,l) #Unifom_cost_search
    # l.printGif()


    # app = QApplication(sys.argv)
    # windows = MainWindows()
    # windows.show()
    # sys.exit(app.exec())


    # from graphviz import render
    #
    # render('dot', 'png', 'ceo.dot')

    # DotExporter(root).to_dotfile("root.dot")
    # from graphviz import render
    # render('dot', 'png', 'root.dot')