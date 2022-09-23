from IU.BoardGrapher import BoardGrapher
import csv
import numpy

if __name__ == '__main__':
    reader = csv.reader(open("MazeExamples/maze_10x10.csv", "rt"), delimiter=",")
    x = list(reader)
    x = [ele for ele in x if ele != []]
    result = numpy.array(x)
    route = "IU"
    g = BoardGrapher(result, "Example2", route)
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


