class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0
        while left < right:
            current_height = min(heights[left], heights[right])
            current_width = right - left
            max_area = max(current_height * current_width, max_area)
            if current_height == heights[left]:
                left += 1
            else:
                right -= 1
        return max_area
        

        