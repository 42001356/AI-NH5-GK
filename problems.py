import os 
import numpy as np
class SingleFoodSearchProblem:
    def __init__(self) -> None:
        self.sate = 0
        self.node = list()
        self.initial_state = 0
        self.matrix = self.readMaze()
    def successor(self):
        
    
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
        matrix = self.matrix
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if matrix[i][j] == 0:
                    matrix_test+='%'
                if matrix[i][j] == 1:
                    matrix_test+=' '
                if matrix[i][j] == 2:
                    matrix_test+='P'
                if matrix[i][j] == 3:
                    matrix_test+='.'
                if matrix[i][j] == 4:
                    matrix_test+='\n'
        print(matrix_test)
    