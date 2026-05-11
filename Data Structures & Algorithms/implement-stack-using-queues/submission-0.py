class MyStack:

    def __init__(self):
        self.elements = deque()
        

    def push(self, x: int) -> None:
        self.elements.appendleft(x)
        

    def pop(self) -> int:

        if not self.elements:
            raise IndexError("Stack is Empty")
        
        return self.elements.popleft()
        

    def top(self) -> int:
        return self.elements[0]

        

    def empty(self) -> bool:
        if not self.elements:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()