class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)
    
    def merge(self, leftList: List[int], rightList: List[int]) -> List[int]:
        i = 0
        j = 0

        mergeList = []

        while i < len(leftList) and j < len(rightList):
            if leftList[i] < rightList[j]:
                mergeList.append(leftList[i])
                i += 1
            else:
                mergeList.append(rightList[j])
                j += 1
        
        while i < len(leftList):
            mergeList.append(leftList[i])
            i += 1
        
        while j < len(rightList):
            mergeList.append(rightList[j])
            j += 1
        
        return mergeList

        