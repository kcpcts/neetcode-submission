class MinStack:

    def __init__(self):
        self.stack = []
        self.pmin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.pmin:
            val = min(val,self.pmin[-1])
        

        self.pmin.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.pmin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.pmin[-1]
        
        
