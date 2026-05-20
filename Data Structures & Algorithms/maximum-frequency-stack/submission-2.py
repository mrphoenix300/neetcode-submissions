class FreqStack:

    def __init__(self):
        self.freq_of_val = {}
        self.stack = collections.defaultdict(list)
        self.max_freq = 0
        

    def push(self, val: int) -> None:
        self.freq_of_val[val] = self.freq_of_val.get(val, 0) + 1
        cur = self.freq_of_val[val]
        self.stack[cur].append(val)
        self.max_freq = max(self.max_freq, cur)

    def pop(self) -> int:
        while self.max_freq != 0 and not self.stack[self.max_freq]: 
            self.max_freq -= 1
        removed_value = self.stack[self.max_freq].pop()
        self.freq_of_val[removed_value] -= 1

        return removed_value
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()