import csv
import sys
import tkinter as tk
import cv2

import numpy
from PyQt5 import uic, QtWidgets, QtGui, Qt
from PyQt5.QtGui import QImage

from PyQt5.QtWidgets import QMainWindow, QFileDialog
from anytree import RenderTree
from anytree.exporter import DotExporter
from graphviz import render

from Algorithms.AStar import AStar
from Algorithms.Depth import Depth
from Algorithms.GreedySearch import GreedySearch
from Algorithms.IterativeDepth import IterativeDepth
from Algorithms.Models.Enums.Search import Search
from Algorithms.Models.TreeGenerator import TreeGenerator
from Algorithms.UniformCostSearch import UniformCostSearch
from Algorithms.Width import Width
from UI.BoardGrapher import BoardGrapher
from UI.LoadingGif import ImageLabel


class MainWindows(QMainWindow):

    def __init__(self):
        self.root = tk.Tk()
        self.routeMaze = ""
        self.matrix = None
        self.name = ""
        self.g = None
        self.tree = None
        self.target = None
        self.row = 0
        self.time = 0
        self.memory = 0

        super(MainWindows, self).__init__()
        uic.loadUi("UI/UIQtDesigner/MainWindow.ui", self)

        self.tableWidget.setColumnWidth(2, 161)
        self.tableWidget.setColumnWidth(3, 161)
        self.pushButton.clicked.connect(self.loadImage)
        self.pushButton_2.clicked.connect(self.solveMaze)

    def loadImage(self):
        self.routeMaze = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        name = ""
        i = -1
        while True:
            if self.routeMaze[i] == "/":
                break
            else:
                name = name + self.routeMaze[i]
                i = i - 1
        name = name[::-1]
        self.name = name[:-4]
        self.matrix = self.CvsToMatrix()
        route = "UI"
        self.g = BoardGrapher(self.matrix, self.name, route)
        image = cv2.imread(f"UI/img/{self.name}-Walls.png")
        cv2.imshow(f'{self.name}-Walls.png', image)

        treeGen = TreeGenerator(self.matrix)
        self.tree = treeGen.getTree()
        print(RenderTree(self.tree))
        self.target = treeGen.getTarget()
        DotExporter(self.tree).to_dotfile(f"UI/tree/{self.name}.dot")

        render('dot', 'png', f"UI/tree/{self.name}.dot")

        imagen2 = cv2.imread(f"UI/tree/{self.name}.dot.png")
        cv2.imshow(f'{self.name}-tree.png', imagen2)

    def setPhoto(self, image):
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        image = image.scaled(400, 400, Qt.KeepAspectRatio)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))

    def solveMaze(self):

        selected = self.comboBox.currentText()

        if self.root.children.__len__() != 0 :
            self.root.destroy()
            self.root = tk.Tk()

        if selected == Search.Depth.value:
            self.g.name = self.name + "-Depth"
            self.solveDepth()
        elif selected == Search.Width.value:
            self.g.name = self.name + "-Width"
            self.solveWidth()
        elif selected == Search.UniformCostSearch.value:
            self.g.name = self.name + "-UniformCost"
            self.solveUniformCostSearch()
        elif selected == Search.AStar.value:
            self.g.name = self.name + "-AStar"
            self.solveAStar()
        elif selected == Search.Greedy.value:
            self.g.name = self.name + "-Greedy"
            self.solveGreedy()
        elif selected == Search.InteractiveDepth.value:
            self.g.name = self.name + "-Interactive"
            self.solveInteractiveDepth()

        self.tableWidget.insertRow(self.row)
        self.tableWidget.setItem(self.row, 0, QtWidgets.QTableWidgetItem(self.name))
        self.tableWidget.setItem(self.row, 1, QtWidgets.QTableWidgetItem(selected))
        self.tableWidget.setItem(self.row, 2, QtWidgets.QTableWidgetItem(str(self.time)))
        self.tableWidget.setItem(self.row, 3, QtWidgets.QTableWidgetItem(str(self.memory)))
        self.row = self.row + 1

        lbl = ImageLabel(self.root)
        lbl.pack()
        lbl.load(f"UI/gif/{self.g.name}.gif")
        self.root.mainloop()


    def CvsToMatrix(self):
        reader = csv.reader(open(self.routeMaze, "rt"), delimiter=",")
        x = list(reader)
        x = [ele for ele in x if ele != []]
        result = numpy.array(x)
        return result

    def solveDepth(self):
        d = Depth(self.matrix, self.g)
        self.time = d.elapsed_time
        self.memory = sys.getsizeof(d)
        self.g.printGif()

    def solveWidth(self):
        w = Width(self.tree, self.target, self.g)
        self.time = w.elapsed_time
        self.memory = sys.getsizeof(w)
        self.g.printGif()

    def solveUniformCostSearch(self):
        u = UniformCostSearch(self.matrix, self.g)
        self.time = u.elapsed_time
        self.memory = sys.getsizeof(u)
        self.g.printGif()

    def solveAStar(self):
        a = AStar(self.matrix, self.g)
        self.time = a.elapsed_time
        self.memory = sys.getsizeof(a)
        self.g.printGif()

    def solveGreedy(self):
        g = GreedySearch(self.matrix, self.g)
        self.time = g.elapsed_time
        self.memory = sys.getsizeof(g)
        self.g.printGif()

    def solveInteractiveDepth(self):
        i = IterativeDepth(self.matrix, self.g)
        self.time = i.elapsed_time
        self.memory = sys.getsizeof(i)
        self.g.printGif()
