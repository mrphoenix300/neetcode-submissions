class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        i = 0
        while i < len(nums):
            removed = nums.pop(i)
            product_elements = math.prod(nums)
            output.append(product_elements)
            nums.insert(i, removed)
            i += 1
        
        return output
                

        