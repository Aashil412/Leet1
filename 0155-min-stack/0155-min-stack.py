class MinStack:

    def __init__(self):
        self.stack = []
        self.MinStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.MinStack or val < self.MinStack[-1]:
            self.MinStack.append(val)
        else:
            self.MinStack.append(self.MinStack[-1])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        if self.MinStack:
            self.MinStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.MinStack:
            return self.MinStack[-1] 


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()