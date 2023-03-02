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
    

