import os
import numpy as np
from termcolor import colored
import time
import math
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

# SingleFoodSearchProblem
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
        return len(state[1].split(",")) - 1

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
                    return self.node.append((state[0] + 1, state[1] + ',Stop', (i, j - 1), state[3].copy()))
                # ->
                if state[3][i][j + 1] == 1:
                    state[3][i][j + 1] = -1
                    self.node.append((state[0] + 1, state[1] + ',E', (i, j + 1), state[3].copy()))
                    state[3][i][j + 1] = 1
                if state[3][i][j + 1] == 3:
                    return self.node.append((state[0] + 1, state[1] + ',Stop', (i, j + 1), state[3].copy()))
            if i > 0 and i <= state[3].shape[0] - 2:
                # ^
                if state[3][i - 1][j] == 1:
                    state[3][i - 1][j] = -1
                    self.node.append((state[0] + 1, state[1] + ',N', (i - 1, j), state[3].copy()))
                    state[3][i - 1][j] = 1
                if state[3][i - 1][j] == 3:
                    return self.node.append((state[0] + 1, state[1] + ',Stop', (i - 1, j), state[3].copy()))
                # v
                if state[3][i + 1][j] == 1:
                    state[3][i + 1][j] = -1
                    self.node.append((state[0] + 1, state[1] + ',S', (i + 1, j), state[3].copy()))
                    state[3][i + 1][j] = 1
                if state[3][i + 1][j] == 3:
                    return self.node.append((state[0] + 1, state[1] + ',Stop', (i + 1, j), state[3].copy()))

    def printMaze(self, matrix) -> None:
        matrix_text = ''
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if matrix[i][j] == 0:
                    matrix_text += '%'
                if matrix[i][j] == 1:
                    matrix_text += ' '
                if matrix[i][j] == -1:
                    matrix_text += colored('-', 'red')
                if i == self.initial_state[2][0] and j == self.initial_state[2][1]:
                    matrix_text += colored('P', 'blue', attrs=['reverse', 'bold'])
                if matrix[i][j] == 3:
                    matrix_text += colored('.', 'green', attrs=['reverse', 'bold'])
                if matrix[i][j] == 4:
                    matrix_text += '\n'
        
        print(matrix_text)
    
    def animate(self, action) -> None:
        action_matrix = self.initial_state[3].copy()
        i = self.initial_state[2][0]
        j = self.initial_state[2][1]
        for state in action:
            if state == 'W':
                action_matrix[i][j-1] = -1
                self.printMaze(action_matrix)
                j = j - 1
                enter = input()
                os.system('cls')
            if state == 'E':
                action_matrix[i][j+1] = -1
                self.printMaze(action_matrix)
                j = j + 1
                enter = input()
                os.system('cls')

            if state == 'N':
                action_matrix[i-1][j] = -1
                self.printMaze(action_matrix)
                i = i - 1
                enter = input()
                os.system('cls')
            if state == 'S':
                action_matrix[i+1][j] = -1
                self.printMaze(action_matrix)
                i = i + 1
                enter = input()
                os.system('cls')

# MultiFoodSearchProblem
class MultiFoodSearchProblem:
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
        return state[1].count('Stop') == (np.count_nonzero(state[3] == 3) + np.count_nonzero(state[3] == 5))

    def pathCost(self, state: tuple):
        return len(state[1].split(",")) - 1

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

    def successor(self, state: tuple):
        self.node = []
        self.state = state
        if state[1].count('Stop') <= (np.count_nonzero(state[3] == 3) + np.count_nonzero(state[3] == 5)):
            i = state[2][0]
            j = state[2][1]
            if j > 0 and j <= state[3].shape[1] - 2:
                # <-
                if state[3][i][j - 1] == 1:
                    state[3][i][j - 1] = -1
                    self.node.append((state[0] + 1, state[1] + ',W', (i, j - 1), state[3].copy()))
                    state[3][i][j - 1] = 1
                if state[3][i][j - 1] == 3:
                    state[3][i][j-1] = 5
                    self.node.append((state[0] + 1, state[1] + ',Stop', (i, j - 1), state[3].copy()))
                # ->
                if state[3][i][j + 1] == 1:
                    state[3][i][j + 1] = -1
                    self.node.append((state[0] + 1, state[1] + ',E', (i, j + 1), state[3].copy()))
                    state[3][i][j + 1] = 1
                if state[3][i][j + 1] == 3:
                    state[3][i][j + 1] = 5
                    self.node.append((state[0] + 1, state[1] + ',Stop', (i, j + 1), state[3].copy()))
            if i > 0 and i <= state[3].shape[0] - 2:
                # ^
                if state[3][i - 1][j] == 1:
                    state[3][i - 1][j] = -1
                    self.node.append((state[0] + 1, state[1] + ',N', (i - 1, j), state[3].copy()))
                    state[3][i - 1][j] = 1
                if state[3][i - 1][j] == 3:
                     state[3][i - 1][j] = 5
                     self.node.append((state[0] + 1, state[1] + ',Stop', (i - 1, j), state[3].copy()))
                # v
                if state[3][i + 1][j] == 1:
                    state[3][i + 1][j] = -1
                    self.node.append((state[0] + 1, state[1] + ',S', (i + 1, j), state[3].copy()))
                    state[3][i + 1][j] = 1
                if state[3][i + 1][j] == 3:
                    state[3][i + 1][j] == 5
                    self.node.append((state[0] + 1, state[1] + ',Stop', (i + 1, j), state[3].copy()))

    def printMaze(self, matrix) -> None:
        matrix_text = ''
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if matrix[i][j] == 0:
                    matrix_text += '%'
                if matrix[i][j] == 1:
                    matrix_text += ' '
                if matrix[i][j] == -1:
                    matrix_text += colored('-', 'red')
                if i == self.initial_state[2][0] and j == self.initial_state[2][1]:
                    matrix_text += colored('P', 'blue', attrs=['reverse', 'bold'])
                if matrix[i][j] == 3 or matrix[i][j] == 5:
                    matrix_text += colored('.', 'green', attrs=['reverse', 'bold'])
                if matrix[i][j] == 4:
                    matrix_text += '\n'
        
        print(matrix_text)
    
    def animate(self, action) -> None:
        action_matrix = self.initial_state[3].copy()
        i = self.initial_state[2][0]
        j = self.initial_state[2][1]
        for state in action:
            if state == 'W':
                action_matrix[i][j-1] = -1
                self.printMaze(action_matrix)
                j = j - 1
                enter = input()
                os.system('cls')
            if state == 'E':
                action_matrix[i][j+1] = -1
                self.printMaze(action_matrix)
                j = j + 1
                enter = input()
                os.system('cls')

            if state == 'N':
                action_matrix[i-1][j] = -1
                self.printMaze(action_matrix)
                i = i - 1
                enter = input()
                os.system('cls')
            if state == 'S':
                action_matrix[i+1][j] = -1
                self.printMaze(action_matrix)
                i = i + 1
                enter = input()
                os.system('cls')

# search Agents
class searchAgents:
    # BFS
    def bfs(problem):
        
        q = Queue()
        path = []
        turn = 0
        q.enqueue(problem.getInitialState())
        while True:
            if q.empty():
                raise 'No path because cant find goal'
            if problem.goalTest(q.front()):
                for i in q.front()[1].split(","):
                    path.append(i)
                return ('\n-----BFS-----\n',path, q.front(), problem.pathCost(q.front()), turn)
            problem.successor(q.dequeue())
            for state in problem.getNode():
                q.enqueue(state)
            turn+=1


    # DFS
    def dfs(problem):
        
        s = Stack()
        path = []
        turn = 0
        s.push(problem.getInitialState())
        while True:
            if s.empty():
                raise 'No path because cant find goal'
            if problem.goalTest(s.peek()):
                for i in s.peek()[1].split(","):
                    path.append(i)
                return ('\n-----DFS-----\n',path, s.peek(), problem.pathCost(s.peek()), turn)
            problem.successor(s.pop())
            problem.getNode().reverse()
            for state in problem.getNode():
                s.push(state)
            turn+=1

    # UCS
    def ucs(problem):
       
        pq = PriorityQueue()
        path = []
        turn = 0
        pq.enqueue(problem.getInitialState())
        while True:
            if pq.empty():
                raise 'No path because cant find goal'
            if problem.goalTest(pq.getPriority()):
                for i in pq.getPriority()[1].split(","):
                    path.append(i)
                return('\n-----UCS-----\n', path, pq.getPriority(), problem.pathCost(pq.getPriority()), turn)
            problem.successor(pq.dequeue())
            for state in problem.getNode():
                pq.enqueue(state)
            turn+=1

    # Heuristic Manhattan Single
    def heuristicManhattanSingle(state):
        matrix = problem.getInitialState()[3]
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if matrix[i][j] == 3:
                    return abs(state[2][0] - i) + abs(state[2][1] - j)

        
    # Heuristic Euclid Single
    def heuristicEuclidSingle(state):
        matrix = problem.getInitialState()[3]
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if matrix[i][j] == 3:
                    return math.sqrt((state[2][0] - i) ** 2 + (state[2][1] - j) ** 2)
    
    
    # Heuristic Manhattan Multi
    def heuristicManhattanMulti(state):
        matrix = state[3]
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if matrix[i][j] == 3:
                    return abs(state[2][0] - i) + abs(state[2][1] - j)


    # Heuristic Euclid Multi
    def heuristicEuclidMulti(state):
        matrix = state[3]
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if matrix[i][j] == 3:
                    return math.sqrt((state[2][0] - i) ** 2 + (state[2][1] - j) ** 2)
    
    # A*
    def astar(problem, fn_heuristic):
        
        pq = PriorityQueue()
        path = []
        turn = 0
        pq.enqueue(problem.getInitialState())
        while True:
            if pq.empty():
                raise 'No path because cant find goal'
            if problem.goalTest(pq.getPriority()):
                for i in pq.getPriority()[1].split(","):
                    path.append(i)
                return('\n-----A*-----\n', path, pq.getPriority(), problem.pathCost(pq.getPriority()), turn)
            problem.successor(pq.dequeue())
            for state in problem.getNode():
                state = list(state)
                state[0] = fn_heuristic(state) + problem.pathCost(state)
                state = tuple(state)
                pq.enqueue(state)
            turn+=1
    
    # GBFS
    def gbfs(problem, fn_heuristic):
        pq = PriorityQueue()
        path = []
        turn = 0
        pq.enqueue(problem.getInitialState())
        while True:
            if pq.empty():
                raise 'No path because cant find goal'
            if problem.goalTest(pq.getPriority()):
                for i in pq.getPriority()[1].split(","):
                    path.append(i)
                return('\n-----GBFS-----\n', path, pq.getPriority(), problem.pathCost(pq.getPriority()), turn)
            problem.successor(pq.dequeue())
            for state in problem.getNode():
                state = list(state)
                state[0] = fn_heuristic(state)
                state = tuple(state)
                pq.enqueue(state)
            turn+=1

# main
problem = MultiFoodSearchProblem()
filename = r'C:\Users\QUANG\OneDrive\Máy tính\input.txt'
problem.readMaze(filename)
bfs = searchAgents.bfs(problem)
dfs = searchAgents.dfs(problem)
ucs = searchAgents.ucs(problem)
astar = searchAgents.astar(problem,searchAgents.heuristicEuclidMulti)
gbfs = searchAgents.gbfs(problem,searchAgents.heuristicEuclidMulti)
for name,path,state,cost,turn in [bfs,dfs,ucs,astar,gbfs]:
    print(name)
    problem.printMaze(state[3])
    print('\npath =',path)
    print('\ncost =',cost)
    print('\nturn =',turn)
        

