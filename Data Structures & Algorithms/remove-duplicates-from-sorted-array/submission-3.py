class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while True:
            target_left = nums[left % len(nums)]
            while left  < len(nums) and nums.count(target_left) > 1:
                nums.remove(target_left)
                left += 1
            if left >= len(nums):
                left = left % len(nums)
            else:
                left += 1
            if right >= len(nums):
                right = len(nums) - 1
            target_right = nums[right]
            while right > 0 and nums.count(target_right) > 1:
                nums.remove(target_right)
                right -= 1
            right -= 1
            if len(nums) == len(set(nums)):
                break
        return len(nums)