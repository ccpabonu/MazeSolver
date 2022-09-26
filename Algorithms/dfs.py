from __future__ import annotations
from re import S
from tkinter import E, N
from typing import TypeVar, Generic, List, Deque, Optional
import numpy as np
import csv

class Node_S():
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Stack: #LIFO
    def __init__(self):
        # Init stack
        self.top = None
        self.size = 0
    def push(self, data):
        # Push or insert nodes to stack
        node = Node_S(data, self.top)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size += 1
    def pop(self):
        # Pop or delete nodes to stack
        if self.top:
            data = self.top.data
            self.size -= 1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            return False
    def peek(self):
        # Retorn the head node
        return self.top.data if self.top else False
    def clear(self):
        # Clear all stack
        while self.top:
            self.pop()
    def search_element(self, data):
        if self.top:
            current = self.top
            while current:
                if current.data == data:
                    return (f'Elemet {data} founded')
                current = current.next
            return (f'Elemet {data} not founded')


# reader = csv.reader(open("MazeExamples/maze_10x10.csv", "rt"), delimiter=",")
# x = list(reader)
# x = [ele for ele in x if ele != []]
# result = np.array(x)
# print(result)

def dfs(MAZE):
    START = [0,np.where((MAZE[0] == 'c'))[0][0]]
    GOAL = [MAZE.shape[0]-1,np.where((MAZE[MAZE.shape[0]-1] == 'c'))[0][0]]
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
            if next_step == 'S' and (MAZE[last_for_positiom[0]+1][last_for_positiom[1]] != 'w') and ([last_for_positiom[0]+1, last_for_positiom[1]] not in explored) :
                if count < 1:
                    position = [last_for_positiom[0]+1, last_for_positiom[1]]
                else:
                    frontier.push(last_for_positiom)
                count += 1
            elif next_step == 'E' and (MAZE[last_for_positiom[0]][last_for_positiom[1]+1] != 'w') and [last_for_positiom[0], last_for_positiom[1]+1] not in explored :
                if count < 1:    
                    position = [last_for_positiom[0], last_for_positiom[1]+1]
                else:
                    frontier.push(last_for_positiom)
                count += 1
            elif next_step == 'O' and (MAZE[last_for_positiom[0]][last_for_positiom[1]-1] != 'w') and [last_for_positiom[0],last_for_positiom[1]-1] not in explored :
                if count < 1:
                    position = [last_for_positiom[0],last_for_positiom[1]-1]
                else:
                    frontier.push(last_for_positiom)
                count += 1
            elif next_step == 'N' and (MAZE[last_for_positiom[0]-1][last_for_positiom[1]] != 'w') and [last_for_positiom[0]-1,last_for_positiom[1]] not in explored :
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
    print('explored',explored)
    while way.peek():
        array_way.append(way.peek())
        way.pop()
    print('Final Way',array_way)
    while frontier.peek():
        array_p.append(frontier.peek())
        frontier.pop()
    print('Parents',array_p)
    return explored, array_way

# dfs(result)




    # explored, f_way = dfs(result)


    # for i in range(len(explored)):
    #     track = (explored[0:i+1])
    #     g.printTrack(track, f"{i}")

    # for i in range(len(explored)):
    #     track = (f_way[0:i+1])
    #     g.printTrack(track, f"{i}"+"final")




