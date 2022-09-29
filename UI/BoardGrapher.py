import time

import matplotlib.image as image
import numpy as np
from PIL import Image
import imageio


class BoardGrapher:

    def __init__(self, matrix, name, route):
        self.route = route + "/"
        self.name = name
        self.matrix = matrix
        self.rows, self.columns = matrix.shape
        self.sPixels = int(600 / self.rows)
        self.img = np.ones((self.rows * self.sPixels, self.columns * self.sPixels, 3))
        self.colorWalls = [0, 0, 0]
        self.colorTrack = [0, 45, 187]
        self.filenames = []
        self.Gif = False
        self.printWalls()

    def printWalls(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.matrix[i][j] == "w":
                    self.printCell(i, j, self.colorWalls)
        self.printImage("Walls")

    def printImage(self, i):
        im = Image.fromarray(np.uint8(self.img * 255))
        self.filenames.append(self.route + f"img/{self.name}-{i}.png")
        im.save(self.route + f"img/{self.name}-{i}.png")

    def printCell(self, x0, y0, color):
        for x in range(int(x0) * self.sPixels, int(x0 + 1) * self.sPixels):
            for y in range(int(y0) * self.sPixels, int(y0 + 1) * self.sPixels):
                self.img[x][y] = np.array(color)

    def printTrack(self, track, i):
        for item in track:
            self.printCell(item[0], item[1], self.colorTrack)
        self.printImage(i)

    def printGif(self):
        images = []
        for filename in self.filenames:
            images.append(imageio.imread(filename))
        imageio.mimsave(f'UI/gif/{self.name}.gif', images, loop=1)
        self.filenames.clear()
