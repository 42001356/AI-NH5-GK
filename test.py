import os
import numpy as np
from termcolor import colored
import time
import colorama
colorama.just_fix_windows_console()

# Stack
class Stack:
    def __init__(self) -> None:
        self.items = list()

    def empty(self):
        return len(self.items) == 0

    def push(self, state: tuple):
        self.items.append(state)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def contains(self, state: tuple):
        return state in self.items

    def __str__(self) -> str:
        return str(self.items)


# Queue
class Queue:
    def __init__(self) -> None:
        self.items = list()

    def empty(self):
        return len(self.items) == 0

    def enqueue(self, state: tuple):
        self.items.append(state)

    def dequeue(self):
        return self.items.pop(0)

    def front(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def contains(self, state: tuple):
        return state in self.items

    def __str__(self) -> str:
        return str(self.items)


# Priority Queue
class PriorityQueue:
    def __init__(self) -> None:
        self.items = list()

    def empty(self):
        return len(self.items) == 0

    def enqueue(self, state: tuple):
        self.items.append(state)
        self.items.sort()

    def dequeue(self):
        return self.items.pop(0)
    
    def getPriority(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def contains(self, state: tuple):
        return state in self.items

    def __str__(self) -> str:
        return str(self.items)


class SingleFoodSearchProblem:
    def __init__(self) -> None:
        self.state = tuple()
        self.node = list()
        self.initial_state = tuple()

    def getState(self):
        return self.state

    def getNode(self):
        return self.node

    def getInitialState(self):
        return self.initial_state

    def setState(self, state: tuple):
        self.state = state

    def setNode(self, node: list):
        self.node = node

    def setInitialState(self, initial_state: tuple):
        self.initial_state = initial_state

    def goalTest(self, state: tuple):
        return state[1][len(state[1]) - 4:] == 'Stop'

    def pathCost(self, state: tuple):
        if 'Stop' in state[1]:
            return state[0]
        return 'No path cost because no path to goal'

    def readMaze(self, filename):
        i = 0
        number_of_cells = 0
        if os.path.exists(filename):
            with open(filename) as f:
                for line in f:
                    col = len(line)
                    for char in line:
                        number_of_cells += 1
            col += 1
            number_of_cells += 1
            row = int(number_of_cells / col)
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
                        i += 1
            matrix = matrix.reshape(row, col)
            for i in range(matrix.shape[0]):
                for j in range(matrix.shape[1]):
                    if matrix[i][j] == 2:
                        self.initial_state = (0, 'Start', (i, j), matrix)
                        self.state = self.initial_state
                        return 0

    def successor(self, state):
        self.node = []
        self.state = state
        if state[1] != 'Stop':
            i = state[2][0]
            j = state[2][1]
            if j > 0 and j <= state[3].shape[1] - 2:
                # <-
                if state[3][i][j - 1] == 1:
                    state[3][i][j - 1] = -1
                    self.node.append((state[0] + 1, state[1] + ',W', (i, j - 1), state[3].copy()))
                    state[3][i][j - 1] = 1
                if state[3][i][j - 1] == 3:
                    return self.node.append((state[0] + 1, state[1] + ',W,Stop', (i, j - 1), state[3].copy()))
                # ->
                if state[3][i][j + 1] == 1:
                    state[3][i][j + 1] = -1
                    self.node.append((state[0] + 1, state[1] + ',E', (i, j + 1), state[3].copy()))
                    state[3][i][j + 1] = 1
                if state[3][i][j + 1] == 3:
                    return self.node.append((state[0] + 1, state[1] + ',E, Stop', (i, j + 1), state[3].copy()))
            if i > 0 and i <= state[3].shape[0] - 2:
                # ^
                if state[3][i - 1][j] == 1:
                    state[3][i - 1][j] = -1
                    self.node.append((state[0] + 1, state[1] + ',N', (i - 1, j), state[3].copy()))
                    state[3][i - 1][j] = 1
                if state[3][i - 1][j] == 3:
                    return self.node.append((state[0] + 1, state[1] + ',N,Stop', (i - 1, j), state[3].copy()))
                # v
                if state[3][i + 1][j] == 1:
                    state[3][i + 1][j] = -1
                    self.node.append((state[0] + 1, state[1] + ',S', (i + 1, j), state[3].copy()))
                    state[3][i + 1][j] = 1
                if state[3][i + 1][j] == 3:
                    return self.node.append((state[0] + 1, state[1] + ',S,Stop', (i + 1, j), state[3].copy()))

    def printMaze(self, state):
        matrix_test = ''
        matrix = state[3]
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if matrix[i][j] == 0:
                    matrix_test += '%'
                if matrix[i][j] == 1:
                    matrix_test += ' '
                if matrix[i][j] == -1:
                    matrix_test += colored('-', 'red')
                if i == self.initial_state[2][0] and j == self.initial_state[2][1]:
                    matrix_test += colored('P', 'blue', attrs=['reverse', 'bold'])
                if matrix[i][j] == 3:
                    matrix_test += colored('.', 'green', attrs=['reverse', 'bold'])
                if matrix[i][j] == 4:
                    matrix_test += '\n'
        
        print(matrix_test)


# BFS
def bfs(problem: SingleFoodSearchProblem):
    q = Queue()
    path = []
    turn = 0
    q.enqueue(problem.getInitialState())
    while True:
        if q.empty() or problem.goalTest(q.front()):
            for i in q.front()[1].split(","):
                path.append(i)
            return ('\n-----BFS-----\n',path, q.front(), problem.pathCost(q.front()), turn)
        problem.successor(q.dequeue())
        for state in problem.getNode():
            q.enqueue(state)
        turn+=1


# DFS
def dfs(problem: SingleFoodSearchProblem):
    s = Stack()
    path = []
    turn = 0
    s.push(problem.getInitialState())
    while True:
        if s.empty() or problem.goalTest(s.peek()):
            for i in s.peek()[1].split(","):
                path.append(i)
            return ('\n-----DFS-----\n',path, s.peek(), problem.pathCost(s.peek()), turn)
        problem.successor(s.pop())
        problem.getNode().reverse()
        for state in problem.getNode():
            s.push(state)
        turn+=1

# UCS
def ucs(problem: SingleFoodSearchProblem):
    pq = PriorityQueue()
    path = []
    turn = 0
    pq.enqueue(problem.getInitialState())
    while True:
        if pq.empty() or problem.goalTest(pq.getPriority()):
            for i in pq.getPriority()[1].split(","):
                path.append(i)
            return('\n-----UCS-----\n', path, pq.getPriority(), problem.pathCost(pq.getPriority()), turn)
        problem.successor(pq.dequeue())
        for i in problem.getNode():
            pq.enqueue(i)
        turn+=1


# main
problem = SingleFoodSearchProblem()
filename = r'C:\Users\QUANG\OneDrive\Máy tính\input.txt'
problem.readMaze(filename)
bfs = bfs(problem)
dfs = dfs(problem)
ucs = ucs(problem)
for name,path,state,cost,turn in [bfs,dfs,ucs]:
    print(name)
    problem.printMaze(state)
    print('\npath =',path)
    print('\ncost =',cost)
    print('\nTurn =',turn)

