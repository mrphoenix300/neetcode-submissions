class FreqStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> int:
        freq_dict = Counter(self.stack)
        max_freq = max(freq_dict.values())
        max_elem = [k for k, v in freq_dict.items() if v == max_freq]

        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] in max_elem:
                return self.stack.pop(i)

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()