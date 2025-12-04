class MinStack:

    def __init__(self):
        self.stack=[]
        self.prefix=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.prefix:
            self.prefix.append(val)
        else :
            self.prefix.append(min(val, self.prefix[-1]))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.prefix.pop()
        else:
            print("stack is empty")
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else :
            return -1
        

    def getMin(self) -> int:
        return self.prefix[-1]
        
