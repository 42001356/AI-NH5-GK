import os
import numpy as np
from termcolor import colored
import time
#Stack
class Stack:
    def __init__(self) -> None:
        self.items = list()
    
    def empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def contains(self, item):
        return item in self.items
    
    def __str__(self) -> str:
        return str(self.items)

#Queue
class Queue:
    def __init__(self) -> None:
        self.items = list()

    def empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0)
    
    def front(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)
    
    def contains(self, item):
        return  item in self.items
    
    def __str__(self) -> str:
        return str(self.items)

#Priority Queue    
class PriorityQueue:
    def __init__(self) -> None:
        self.items = list()
    
    def empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
        self.items.sort()
    
    def getPriority(self, vertice):
        for w,v in self.items:
            if v == vertice:
                return w
        raise 'Key Error'
    
    def updatePriority(self, v):
        p_w = self.getPriority(v)
        self.items.remove((p_w, v))

    def size(self):
        return len(self.items)
    
    def contains(self, item):
        return item in self.items
    
    def __str__(self) -> str:
        return str(self.items)
    


class SingleFoodSearchProblem:
    def __init__(self) -> None:
        self.state = tuple()
        self.node = list()
        self.initial_state = tuple()
    
    def setMatrix(self, matrix):
        self.matrix = matrix
    
    def getMatrix(self):
        return self.matrix
    
    def getState(self):
        return self.state
    
    def getNode(self):
        return self.node
    
    def getInitialState(self):
        return self.initial_state
    
    def setState(self, state):
        self.state = state
    
    def setNode(self, node):
        self.node = node
    
    def setInitialState(self, initial_state):
        self.initial_state = initial_state
    
    def goalTest(self,expanded: list):
        return expanded[-1] == 'Stop'
    
    def pathCost(self,expanded: list):
        if self.goalTest(expanded):
            self.setNode([])
            path = []
            path.append(expanded[-1])
            cost = 0
            curr = expanded.pop(-1)
            while expanded:
                node_check = expanded.pop(-1)
                self.successor(node_check)
                for state in self.getNode():
                   if state[1] == curr[1]:
                       print('state[1] =',state[1])
                       print('curr[1] =',curr[1])
                       path.append(node_check)
                       cost+=1
                       curr = expanded.pop(-1)
                self.setNode([])    
            path.reverse()
            
            return path
        return 'No path cost because no path to goal'
    
    def readMaze(self):
        i = 0
        number_of_cells = 0
        filename = r'C:\Users\QUANG\OneDrive\Máy tính\input.txt'
        if os.path.exists(filename):
            with open(filename) as f:
                for line in f:
                    col = len(line)
                    for char in line:
                        number_of_cells+=1
            col+=1
            number_of_cells+=1
            row = int (number_of_cells / col)      
            matrix = np.arange(number_of_cells)
            matrix[-1] = 4
            with open(filename) as f:
                for line in f:
                    for char in line:
                        if char == ' ':
                            matrix[i] = 1
                        elif char == 'P':
                            matrix[i] = 2
                        elif char == '.':
                            matrix[i] = 3
                        elif char == '\n':
                            matrix[i] = 4
                        else:
                            matrix[i] = 0
                        i+=1
            matrix = matrix.reshape(row,col)
            for i in range(matrix.shape[0]):
                for j in range(matrix.shape[1]):
                    if matrix[i][j] == 2:
                        self.initial_state = ('Start',(i,j),matrix)
                        self.state = self.initial_state
                        return 0
        
    def successor(self,state):
        self.node = []
        self.state = state
        if state[0] != 'Stop':
            i = state[1][0]
            j = state[1][1]
            
            if j > 0 and j <= state[2].shape[1] - 2:
                # <-
                if state[2][i][j-1] == 1:
                    state[2][i][j-1] = -1
                    
                    self.node.append(('Trái',(i,j-1),state[2]))
                    
                    
                    
                if state[2][i][j-1] == 3:
                    return self.node.append(('Stop',(i,j-1),state[2]))
                # ->
                if state[2][i][j+1] == 1:
                    state[2][i][j+1] = -1
                   
                    self.node.append(('Phải',(i,j+1),state[2]))
                    
                    
                    
                if state[2][i][j+1] == 3:
                    return self.node.append(('Stop',(i,j+1),state[2]))
                        
            if i > 0 and i <= state[2].shape[0] - 2:
                # v
                if state[2][i+1][j] == 1:
                    state[2][i+1][j] = -1
                    
                    self.node.append(('Xuống',(i+1,j),state[2]))
                    
                    
                if state[2][i+1][j] == 3:
                    
                    return self.node.append(('Stop',(i+1,j),state[2]))
                # ^
                if state[2][i-1][j] == 1:
                    state[2][i-1][j] = -1
                    
                    self.node.append(('Lên',(i-1,j),state[2]))
                        
                        
                if state[2][i-1][j] == 3:
                    
                    return self.node.append(('Stop',(i-1,j),state[2]))

    def printMaze(self,state):
        
        matrix_test = ''
        matrix = state[2]
        
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if matrix[i][j] == 0:
                    matrix_test+=colored('%','white')
                if matrix[i][j] == 1:
                    matrix_test+=' '
                if matrix[i][j] == -1:
                    matrix_test+=colored('-','red')
                if i == self.initial_state[1][0] and j == self.initial_state[1][1]:
                    matrix_test+=colored('P','blue',attrs=['reverse','bold'])
                if matrix[i][j] == 3:
                    matrix_test+=colored('.','green',attrs=['reverse','bold'])
                if matrix[i][j] == 4:
                    matrix_test+='\n'
        
        
        print(matrix_test)

q = Queue()    
sfsp = SingleFoodSearchProblem()
sfsp.readMaze()
expanded = []
q.enqueue(sfsp.getInitialState())
expanded.append('Start')
while True:
    if q.empty() or sfsp.goalTest(expanded):
        sfsp.printMaze(q.front())
        
        break
    
    sfsp.printMaze(q.front())
    sfsp.successor(q.dequeue())
    for state in sfsp.getNode():
        
        q.enqueue(state)
        expanded.append(state[0])
    print(expanded)
    
    