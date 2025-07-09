class Stack:
    def __init__(self):
        self.stack=[]

    def push(self, element):
        self.stack.insert(0, element)
    
    def pop(self):
        return self.stack.pop()
    
    def is_empty(self):
        return self.size() == 0
    
    def size(self) -> int:
        return len(self.stack)
    
    def peek(self):
        return self.stack[0]
