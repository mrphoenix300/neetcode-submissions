class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0
        min_buy = prices[0]

        for right in range(len(prices)):
            sell = prices[right]

            while left < right:
                min_buy = min(prices[left], min_buy)
                max_profit = max(sell - min_buy, max_profit)
                left += 1

        return max_profit


        