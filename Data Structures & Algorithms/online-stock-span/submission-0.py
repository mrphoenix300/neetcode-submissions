class StockSpanner:

    def __init__(self):
        self.prices = []
        

    def next(self, price: int) -> int:
        
        stack = [p for p in self.prices]
        consecutive_days = 1

        while stack:
            if stack[-1] <= price:
                consecutive_days += 1
                stack.pop()
            else:
                break
        
        self.prices.append(price)

        return consecutive_days



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)