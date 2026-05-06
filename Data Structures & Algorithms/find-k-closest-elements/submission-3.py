class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        for right in range(left+k, len(arr)):
            if x - arr[left] > arr[right] - x:
                left += 1
        return arr[left:left+k]