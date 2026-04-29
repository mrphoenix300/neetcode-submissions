class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count_boats = 0
        left = 0
        right = len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                count_boats += 1
                left += 1
                right -= 1
            else:
                count_boats += 1
                right -= 1
        
        return count_boats
        