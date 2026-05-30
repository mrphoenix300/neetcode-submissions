class Solution:

    def canSplit(self, nums: List[int], mid: int, k: int) -> bool:

        chunks = 1
        current_sum = 0

        for num in nums:
            if current_sum + num <= mid:
                current_sum += num
            else:
                chunks += 1
                current_sum = num
        
        return True if chunks <= k else False

    def splitArray(self, nums: List[int], k: int) -> int:

        left, right = max(nums), sum(nums)
        min_sum = right

        while left <= right:
            mid = (left + right) // 2

            can_split = self.canSplit(nums, mid, k)
            if can_split:
                min_sum = min(mid, min_sum)
                right = mid - 1
            else:
                left = mid + 1
        
        return min_sum

        