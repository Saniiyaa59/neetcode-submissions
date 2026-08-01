class MyStack:

    def __init__(self):
        self.q = []
        

    def push(self, x: int) -> None:
        self.q.append(x)
        n = len(self.q)
        while n > 1:
            self.q.append(self.q.pop(0))
            n-=1
        return

    def pop(self) -> int:
        if not self.q:
            return -1
        return self.q.pop(0)
        

    def top(self) -> int:
        if not self.q:
            return -1
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()