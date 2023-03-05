import os 
import numpy as np
from termcolor import colored
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
    
#SingleFoodSearchProblem
class SingleFoodSearchProblem:
    def __init__(self) -> None:
        self.state = self.readMaze()
        self.node = list()
        self.initial_state = self.readMaze()

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

    def successor(self):
        for i in range(self.state.shape[0]):
            for j in range(self.state.shape[1]):
                if self.state[i][j] == 2:
                    if i > 0 and i < self.state.shape[0] - 2:
                        # <-
                        if self.state[i-1][j] == 1:
                            self.state[i-1][j] = 5
                            self.state[i][j] = -1
                            self.node.append(('W',self.state))
                        # ->
                        if self.state[i+1][j] == 1:
                            self.state[i+1][j] = 5
                            self.state[i][j] = -1
                            self.node.append(('E',self.state))
                        if j > 0 and j < self.state.shape[1] - 2:
                            # v
                            if self.state[i][j+1] == 1:
                                self.state[i][j+1] = 5
                                self.state[i][j] = -1
                                self.node.append(('S',self.state))
                            # ^
                            if self.state[i][j-1] == 1:
                                self.state[i][j-1] = 5
                                self.state[i][j] = -1
                                self.node.append(('N',self.state))

    def goalTest(self):


    def pathCost(self):

    
    def readMaze(self):
        i = 0
        number_of_cells = 0
        filename = r'C:\Users\QUANG\OneDrive\Máy tính\input.txt'
        if os.path.exists(filename):
            with open(filename) as f:
                for line in f:
                    col = len(line)
                    print('row =',col)
                    for char in line:
                        number_of_cells+=1
                        print(number_of_cells)
            col+=1
            number_of_cells+=1
            row = int (number_of_cells / col)   
            print('row =',row)     
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
            return matrix
    
    def printMaze(self):
        matrix_test = ''
        matrix = self.state
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if matrix[i][j] == 0:
                    matrix_test+=colored('%','white')
                if matrix[i][j] == 5:
                    matrix_test+=colored('-','red',attrs=['blink'])
                if matrix[i][j] == 2:
                    matrix_test+=colored('P','blue',attrs=['reverse','bold'])
                if matrix[i][j] == 3:
                    matrix_test+=colored('.','green',attrs=['reverse','bold'])
                if matrix[i][j] == 4:
                    matrix_test+='\n'
        print(matrix_test)

class SearchAgent(SingleFoodSearchProblem):
    def __init__(self) -> None:
        super().__init__()
    
    def bfs(self, problem: SingleFoodSearchProblem):
        src = problem.initial_state
        