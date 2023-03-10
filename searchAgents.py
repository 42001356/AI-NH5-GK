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