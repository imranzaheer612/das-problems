class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    """
    Push value to the stack
    Push the crosponding min value in the minStack
    """
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)  

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(3)
obj.push(4)
obj.push(1)
obj.push(5)
print("getMin()", obj.getMin())
print("pop ->", obj.pop())
print("top():", obj.top())
print("getMin()", obj.getMin())

print(obj.stack)
print(obj.minStack)