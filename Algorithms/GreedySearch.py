import time
from queue import PriorityQueue
import numpy as np


class GreedySearch:
    def __init__(self, MAZE, gph):
        self.MAZE = MAZE
        self.gph = gph
        self.explored = []
        self.f_way = self.explored[::-1]
        st = time.time_ns()
        self.Greedy_Search_f()
        et = time.time_ns()
        self.elapsed_time = et - st
        self.print_A_Star()

    def print_A_Star(self):
        '''
        This function print the images 
        '''
        for i in range(len(self.explored)):
            track = (self.explored[0:i + 1])
            self.gph.printTrack(track, f"{i}")

    def generate_cost(self, MAZE):
        g_score = {}
        for i in range(len(MAZE)):
            for j in range(len(MAZE)):
                g_score[i, j] = float('inf')
        return g_score

    def distance(self, position, problem, distance_type='E'):
        if distance_type == 'E':
            "The Euclidean distance heuristic for a PositionSearchProblem"
            xy1 = position
            xy2 = problem
            return ((xy1[0] - xy2[0]) ** 2 + (xy1[1] - xy2[1]) ** 2) ** 0.5
        else:
            "The Manhattan distance heuristic for a PositionSearchProblem"
            xy1 = position
            xy2 = problem
            return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])

    def Greedy_Search_f(self):

        START = [0, np.where((self.MAZE[0] == 'c'))[0][0]]
        GOAL = [self.MAZE.shape[0] - 1, np.where((self.MAZE[self.MAZE.shape[0] - 1] == 'c'))[0][0]]
        g_cost_d = self.generate_cost(self.MAZE)
        g_cost_d[tuple(START)] = 0
        h_cost_d = self.generate_cost(self.MAZE)
        h_cost_d[tuple(START)] = self.distance(START, GOAL)
        queue_a = PriorityQueue()
        queue_a.put((self.distance(START, GOAL), self.distance(START, GOAL), tuple(START)))
        way = {}
        way_array = []
        while not queue_a.empty():
            position = queue_a.get()[2]
            if position == tuple(GOAL):
                way_array.append(position)
                break
            for next_step in "SEON":
                if next_step == 'S' and (self.MAZE[position[0] + 1][position[1]] != 'w'):
                    last_position = (position[0] + 1, position[1])
                if next_step == 'E' and (self.MAZE[position[0]][position[1] + 1] != 'w'):
                    last_position = (position[0], position[1] + 1)
                if next_step == 'O' and (self.MAZE[position[0]][position[1] - 1] != 'w'):
                    last_position = (position[0], position[1] - 1)
                if next_step == 'N' and (self.MAZE[position[0] - 1][position[1]] != 'w'):
                    last_position = (position[0] - 1, position[1])
                tg_cost_d = 0
                th_cost_d = tg_cost_d + self.distance(last_position, tuple(GOAL))
                if position == tuple(GOAL):
                    break
                if th_cost_d < h_cost_d[last_position]:
                    g_cost_d[last_position] = tg_cost_d
                    h_cost_d[last_position] = th_cost_d
                    queue_a.put((th_cost_d, self.distance(last_position, GOAL), last_position))
                    way[last_position] = position
                    way_array.append(position)
        way_array_l = []
        for i in (way_array):
            way_array_l.append([i[0], i[1]])

        self.explored = way_array_l
