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