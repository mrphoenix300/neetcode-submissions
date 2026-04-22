class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for index, value in enumerate(nums):
            indices[value] = index

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in indices and i != indices[difference]:
                return [i, indices[difference]]
            else:
                indices[difference] = i
        
        return []