class MyStack:

    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    def push(self, x: int) -> None:
        while self.stk1:
            self.stk2.append(self.stk1.pop())
        self.stk2.append(x)
        while self.stk2:
            self.stk1.append(self.stk2.pop())

    def pop(self) -> int:
        return self.stk1.pop(0)

    def top(self) -> int:
        return self.stk1[0]
    
    def empty(self) -> bool:
        return len(self.stk1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()