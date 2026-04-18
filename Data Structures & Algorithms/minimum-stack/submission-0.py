class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStk=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStk:
            self.minStk.append(val)
        else:
            self.minStk.append(min(self.minStk[-1],val))

    def pop(self) -> None:
        self.stack.pop()
        self.minStk.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStk[-1]
