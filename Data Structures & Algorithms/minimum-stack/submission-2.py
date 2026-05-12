class MinStack:

    def __init__(self):
        self.stack = []
        self.minElements = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minElements:
            if val <= self.minElements[-1]:
                self.minElements.append(val)
        else:
            self.minElements.append(val)
            
        

    def pop(self) -> None:
        removed_element = self.stack.pop()
        if removed_element == self.minElements[-1]:
            self.minElements.pop()

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        print(self.minElements)   
        return self.minElements[-1]
        
