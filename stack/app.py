class Stack:
    def __init__(self):
        self.stack=[]

    def push(self, element):
        self.stack.insert(0, element)
    
    def pop(self):
        raise NotImplementedError
    
    def is_empty(self):
        raise NotImplementedError
    
    def size(self) -> int:
        return len(self.stack)
    
    def peek(self):
        raise NotImplementedError
