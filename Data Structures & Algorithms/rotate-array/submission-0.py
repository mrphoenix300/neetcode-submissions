class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        
        while k > 0:
            num = nums.pop()
            nums.insert(left, num)
            k -= 1
        
        

        