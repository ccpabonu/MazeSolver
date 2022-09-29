import numpy as np
from Algorithms.Models.Stack import Stack


class Iterative_Depth:
    def __init__(self,MAZE,gph):
        self.MAZE = MAZE
        self.gph = gph
        self.f_way = []
        self.explored = []
        self.Search_idfs()
        self.print_idfs()
        
    def print_idfs(self):
        for i in range(len(self.explored)):
            track = (self.explored[0:i+1])
            self.gph.printTrack(track, f"{i}")

        # for i in range(len(self.explored)):
        #     track = (self.f_way[0:i+1])
        #     self.gph.printTrack(track, f"{i}"+"final")

    def Search_idfs(self):
        START = [0,np.where((self.MAZE[0] == 'c'))[0][0]]
        GOAL = [self.MAZE.shape[0]-1,np.where((self.MAZE[self.MAZE.shape[0]-1] == 'c'))[0][0]]
        explored = []
        way = Stack()
        way.push(START)
        position = START
        explored.append(START)
        while GOAL != way.peek():
            if  GOAL == way.peek():
                break
            last_position = position
            while last_position == position :
                for next_step in "SEON":
                    if next_step == 'S' and (self.MAZE[position[0]+1][position[1]] != 'w') and ([position[0]+1, position[1]] not in explored) :
                        position = [position[0]+1, position[1]]
                        way.push(position)
                        break

                    elif next_step == 'E' and (self.MAZE[position[0]][position[1]+1] != 'w') and [position[0], position[1]+1] not in explored :
                        position = [position[0], position[1]+1]
                        way.push(position)
                        break

                    elif next_step == 'O' and (self.MAZE[position[0]][position[1]-1] != 'w') and [position[0],position[1]-1] not in explored :
                        position = [position[0],position[1]-1]
                        way.push(position)
                        break

                    elif next_step == 'N' and (self.MAZE[position[0]-1][position[1]] != 'w') and [position[0]-1,position[1]] not in explored :
                        position = [position[0]-1,position[1]]
                        way.push(position)
                        break

                if position not in explored:
                    explored.append(position)
                if position == last_position:
                    position = way.pop()
        array_way = []

        while way.peek():
            array_way.append(way.peek())
            way.pop()
        
        # print(f' explored :{explored} \n array way: {array_way}')
        
        self.explored = explored
