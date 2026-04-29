class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        i = 0
        j = 0
        merged_nums = [0] * len(nums1)
        k = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merged_nums[k] = nums1[i]
                i += 1
            else:
                merged_nums[k] = nums2[j]
                j += 1
            k += 1
        
        while i < m:
            merged_nums[k] = nums1[i]
            i += 1
            k += 1
        
        while j < n:
            merged_nums[k] = nums2[j]
            j += 1
            k += 1
        
        for i in range(len(nums1)): nums1[i] = merged_nums[i]
        