class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum_subarray = 0
        left = 0
        min_subarray_length = len(nums)
        if sum(nums) < target:
            return 0

        for right in range(len(nums)):

            sum_subarray += nums[right]
            while sum_subarray >= target:
                sum_subarray -= nums[left]
                left += 1
            if left > 0:
                sum_subarray += nums[left - 1]
                left -= 1
                min_subarray_length = min(right - left + 1, min_subarray_length)

        return min_subarray_length
            

            



        