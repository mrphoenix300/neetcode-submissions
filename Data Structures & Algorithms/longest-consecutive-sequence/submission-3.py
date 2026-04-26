from sortedcontainers import SortedSet

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_of_nums = SortedSet(nums)
        count_sequence = 0
        max_sequence = float('-inf')
        prev = None

        for num in set_of_nums:
            if prev is not None:
                if num == prev + 1:
                    count_sequence += 1
                else:
                    max_sequence = max(count_sequence, max_sequence)
                    count_sequence = 1
            else:
                count_sequence += 1
            prev = num

        return max(count_sequence, max_sequence)
            
            
        