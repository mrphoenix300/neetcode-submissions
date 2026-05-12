class MyQueue:

    def __init__(self):
        self.back = []
        self.front = deque()
        

    def push(self, x: int) -> None:
        self.back.append(x)
        self.front.appendleft(x)
        

    def pop(self) -> int:
        self.back.pop(0)
        return self.front.pop()
        

    def peek(self) -> int:
        return self.front[-1]
        

    def empty(self) -> bool:
        return True if not self.front else False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()