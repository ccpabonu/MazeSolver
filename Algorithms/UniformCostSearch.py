from queue import PriorityQueue
import numpy as np

class UniformCostSearch:
    def __init__(self,MAZE,gph):
        self.MAZE = MAZE
        self.gph = gph
        self.explored = []
        self.f_way = self.explored[::-1]
        self.UniformCostSearch_f()
        self.print_UniformCostSearch()

    def print_UniformCostSearch(self):
        '''
        This function print the images 
        '''
        for i in range(len(self.explored)):
            track = (self.explored[0:i+1])
            self.gph.printTrack(track, f"{i}")
    
    def generate_cost(self, MAZE):
        g_score = {}
        for i in range(len(MAZE)):
            for j in range(len(MAZE)):
                g_score[i,j] = float('inf')
        return g_score

        
    def UniformCostSearch_f(self):
        START = [0,np.where((self.MAZE[0] == 'c'))[0][0]]
        GOAL = [self.MAZE.shape[0]-1,np.where((self.MAZE[self.MAZE.shape[0]-1] == 'c'))[0][0]]
        g_cost_d = self.generate_cost(self.MAZE) #Dictionary of vaule's cost
        g_cost_d[tuple(START)] = 1
        f_cost_d = self.generate_cost(self.MAZE) #Dictionary of vaule's cost
        f_cost_d[tuple(START)] = 1
        queue_a = PriorityQueue()
        queue_a.put( (1,1,tuple(START)) )
        way = {}
        way_array = []
        while not queue_a.empty():
            position = queue_a.get()[2]
            if position == tuple(GOAL):
                way_array.append(position)
                break
            for next_step in "SEON":
                if next_step == 'S' and (self.MAZE[position[0]+1][position[1]] != 'w') :
                    last_position = (position[0]+1, position[1])
                if next_step == 'E' and (self.MAZE[position[0]][position[1]+1] != 'w'):
                    last_position = (position[0], position[1]+1)
                if next_step == 'O' and (self.MAZE[position[0]][position[1]-1] != 'w'):
                    last_position = (position[0],position[1]-1)
                if next_step == 'N' and (self.MAZE[position[0]-1][position[1]] != 'w'):
                    last_position = (position[0]-1,position[1])
                tg_cost_d = g_cost_d[position]+1 #
                tf_cost_d = tg_cost_d+0
                if position == tuple(GOAL):
                    break
                if tf_cost_d < f_cost_d[last_position]:
                    g_cost_d[last_position]=tg_cost_d
                    f_cost_d[last_position]=tf_cost_d
                    queue_a.put( (tf_cost_d,1,last_position))
                    way[last_position]=position
                    way_array.append(position)
        way_array_l = []
        for i in (way_array):
            way_array_l.append([i[0],i[1]])
        
        self.explored = way_array_l









