class StockSpanner:

    def __init__(self):
        self.prices = []
        

    def next(self, price: int) -> int:
        
        consecutive_days = 1
        
        while self.prices and self.prices[-1][0] <= price:
            consecutive_days += self.prices[-1][1]
            self.prices.pop()
        
        self.prices.append((price, consecutive_days))

        return consecutive_days



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)