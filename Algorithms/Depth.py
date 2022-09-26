
import numpy as np
from Algorithms.Models.Stack import Stack

class Depth:
    def __init__(self,MAZE,gph):
        self.MAZE = MAZE
        self.gph = gph
        self.f_way = []
        self.explored = []
        self.Search()
        self.print_dfs()
        
    def print_dfs(self):

        # for i in range(len(self.explored)):
        #     track = (self.explored[0:i+1])
        #     self.gph.printTrack(track, f"{i}")

        for i in range(len(self.explored)):
            track = (self.f_way[0:i+1])
            self.gph.printTrack(track, f"{i}"+"final")

    def Search(self):
        START = [0,np.where((self.MAZE[0] == 'c'))[0][0]]
        GOAL = [self.MAZE.shape[0]-1,np.where((self.MAZE[self.MAZE.shape[0]-1] == 'c'))[0][0]]
        explored = []
        way = Stack()
        frontier = Stack()
        way.push(START)
        frontier.push(START)
        position = START
        last_for_positiom = position
        i = 0
        while frontier.peek() != False and GOAL != way.peek():
            if last_for_positiom == position:
                position = frontier.peek()
                explored.append(position)
                if frontier.peek() != START:
                    while frontier.peek() != way.peek():     
                        if way.peek() == frontier.peek() or way.peek() == False:
                            break
                        way.pop()
                    way.pop()
                    way.push(position)
            last_for_positiom = position
            i = i+1
            if  GOAL == way.peek():
                break
            count = 0
            array_way = []
            array_p = []
            for next_step in "SEON":
                if next_step == 'S' and (self.MAZE[last_for_positiom[0]+1][last_for_positiom[1]] != 'w') and ([last_for_positiom[0]+1, last_for_positiom[1]] not in explored) :
                    if count < 1:
                        position = [last_for_positiom[0]+1, last_for_positiom[1]]
                    else:
                        frontier.push(last_for_positiom)
                    count += 1
                elif next_step == 'E' and (self.MAZE[last_for_positiom[0]][last_for_positiom[1]+1] != 'w') and [last_for_positiom[0], last_for_positiom[1]+1] not in explored :
                    if count < 1:    
                        position = [last_for_positiom[0], last_for_positiom[1]+1]
                    else:
                        frontier.push(last_for_positiom)
                    count += 1
                elif next_step == 'O' and (self.MAZE[last_for_positiom[0]][last_for_positiom[1]-1] != 'w') and [last_for_positiom[0],last_for_positiom[1]-1] not in explored :
                    if count < 1:
                        position = [last_for_positiom[0],last_for_positiom[1]-1]
                    else:
                        frontier.push(last_for_positiom)
                    count += 1
                elif next_step == 'N' and (self.MAZE[last_for_positiom[0]-1][last_for_positiom[1]] != 'w') and [last_for_positiom[0]-1,last_for_positiom[1]] not in explored :
                    if count < 1:    
                        position = [last_for_positiom[0]-1,last_for_positiom[1]]
                    else:
                        frontier.push(last_for_positiom)
                    count += 1
                if position not in explored:
                        explored.append(position)

                if way.peek() == GOAL:
                    break
                if way.peek() != position:
                    way.push(position)

        while way.peek():
            array_way.append(way.peek())
            way.pop()

        self.explored = explored
        self.f_way = array_way

