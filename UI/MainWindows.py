import csv
import cv2

import numpy
from PyQt5 import uic, QtWidgets, QtGui, Qt
from PyQt5.QtGui import QImage

from PyQt5.QtWidgets import QMainWindow, QFileDialog

from UI.BoardGrapher import BoardGrapher


class MainWindows(QMainWindow):

    def __init__(self):
        self.routeMaze = ""
        self.matrix = None
        self.name = ""
        super(MainWindows, self).__init__()
        uic.loadUi("UI/UIQtDesigner/MainWindow.ui", self)
        self.pushButton.clicked.connect(self.cargarImagen)
        self.pushButton_2.clicked.connect(self.prueba)

    def cargarImagen(self):
        self.routeMaze = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        name = ""
        i=-1
        while(True):
            if(self.routeMaze[i] == "/"):
                break
            else:
                name = name+self.routeMaze[i]
                i=i-1
        name = name[::-1]
        self.name = name[:-4]
        self.matrix = self.CvsToMatrix()
        route = "UI"
        g = BoardGrapher(self.matrix, self.name, route)
        imagen = cv2.imread(f"UI/img/{self.name}-Walls.png")
        cv2.imshow(f'{self.name}-Walls.png',imagen)

    def setPhoto(self, image):
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        imagen = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        imagen = imagen.scaled(400, 400, Qt.KeepAspectRatio)
        self.label.setPixmap(QtGui.QPixmap.fromImage(imagen))

    def prueba(self):
        print("Funciona el boton")


    def CvsToMatrix(self):
        reader = csv.reader(open(self.routeMaze, "rt"), delimiter=",")
        x = list(reader)
        x = [ele for ele in x if ele != []]
        result = numpy.array(x)
        return result
