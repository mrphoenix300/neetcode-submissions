class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        freq_nums = Counter(nums)

        for key, value in freq_nums.items():
            if value > 1:
                return key


        