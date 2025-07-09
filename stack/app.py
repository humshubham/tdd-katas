class Stack:
    def __init__(self):
        self.stack=[]

    def push(self):
        raise NotImplementedError
    
    def pop(self):
        raise NotImplementedError
    
    def is_empty(self):
        raise NotImplementedError
    
    def size(self) -> int:
        return len(self.stack)
    
    def peek(self):
        raise NotImplementedError
