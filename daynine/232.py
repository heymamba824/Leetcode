class MyQueue:

    def __init__(self):
        self.stackin = []
        self.stackout = []

    def push(self, x: int) -> None:
        self.stackin.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        if self.stackout:
            return self.stackout.pop()
        else:
            while self.stackin:
                self.stackout.append(self.stackin.pop())
            return self.stackout.pop()
    def peek(self) -> int:
        ans = self.pop()
        self.stackout.append(ans)
        return ans

    def empty(self) -> bool:
        if not self.stackin and not self.stackout:
            return True
