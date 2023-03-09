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
                    return self.node.append((state[0] + 1, state[1] + ',E,Stop', (i, j + 1), state[3].copy()))
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
        if state[1].count('Stop') == (np.count_nonzero(state[3] == 3) + np.count_nonzero(state[3] == 5)):
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
                    self.node.append((state[0] + 1, state[1] + ',W,Stop', (i, j - 1), state[3].copy()))
                # ->
                if state[3][i][j + 1] == 1:
                    state[3][i][j + 1] = -1
                    self.node.append((state[0] + 1, state[1] + ',E', (i, j + 1), state[3].copy()))
                    state[3][i][j + 1] = 1
                if state[3][i][j + 1] == 3:
                    state[3][i][j + 1] = 5
                    self.node.append((state[0] + 1, state[1] + ',E,Stop', (i, j + 1), state[3].copy()))
            if i > 0 and i <= state[3].shape[0] - 2:
                # ^
                if state[3][i - 1][j] == 1:
                    state[3][i - 1][j] = -1
                    self.node.append((state[0] + 1, state[1] + ',N', (i - 1, j), state[3].copy()))
                    state[3][i - 1][j] = 1
                if state[3][i - 1][j] == 3:
                     state[3][i - 1][j] = 5
                     self.node.append((state[0] + 1, state[1] + ',N,Stop', (i - 1, j), state[3].copy()))
                # v
                if state[3][i + 1][j] == 1:
                    state[3][i + 1][j] = -1
                    self.node.append((state[0] + 1, state[1] + ',S', (i + 1, j), state[3].copy()))
                    state[3][i + 1][j] = 1
                if state[3][i + 1][j] == 3:
                    state[3][i + 1][j] == 5
                    self.node.append((state[0] + 1, state[1] + ',S,Stop', (i + 1, j), state[3].copy()))

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