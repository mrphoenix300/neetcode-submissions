class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        missing_number = 1
        for i in range(len(nums)):
            if missing_number not in nums:
                break
            else:
                missing_number += 1
        
        return missing_number