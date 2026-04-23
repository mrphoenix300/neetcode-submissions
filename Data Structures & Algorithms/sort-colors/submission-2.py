class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        size = 1
        while size < n:
            l = 0
            while l < n - 1:
                mid = min(l + size - 1, n - 1)
                h = min(l + 2 * size - 1, n - 1)
                self.merge(nums, l, mid, h)

                l += 2 * size
            size = 2 * size

    def merge(self, A: List[int], l: int, mid: int, h:int) -> List[int]:
        i = l
        j = mid + 1
        B = [0] * len(A)
        k = l
        

        while i <= mid and j <= h:
            if A[i] < A[j]:
                B[k] = A[i]
                i += 1
            else:
                B[k] = A[j]
                j += 1
            k += 1
        
        while i <= mid:
            B[k] = A[i]
            i += 1
            k += 1
        
        while j <= h:
            B[k] = A[j]
            j += 1
            k += 1

        for i in range(l, h + 1): A[i] = B[i]
        
        return A
        