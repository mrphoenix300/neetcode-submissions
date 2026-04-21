class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for value in nums:
            if nums.count(value) > 1:
                return True
        return False
        