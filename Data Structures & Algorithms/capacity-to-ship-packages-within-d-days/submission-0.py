class Solution:
    def canShip(self, weights, capacity, days):
        days_used = 1
        sum_of_weights = 0
        i = 0
        while i < len(weights):
            if sum_of_weights + weights[i] <= capacity:
                sum_of_weights += weights[i]
            else:
                sum_of_weights = weights[i]
                days_used += 1
            i += 1
        
        if days_used <= days:
            return True
        else:
            return False



    def shipWithinDays(self, weights: List[int], days: int) -> int:

        low, high = max(weights), sum(weights)
        res = high

        while low <= high:
            mid = (low + high) // 2

            can_ship = self.canShip(weights, mid, days)

            if can_ship:
                res = min(res, mid)
                high = mid - 1
            else:
                low = mid + 1
        
        return res

        