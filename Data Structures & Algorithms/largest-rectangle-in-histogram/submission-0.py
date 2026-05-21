class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        max_area = 0

        for i in range(len(heights)):
            if stack:
                right_boundary = i
                while stack and heights[stack[-1]] > heights[i]:
                    current_height = heights[stack.pop()]
                    if stack:
                        left_boundary = stack[-1]
                    else:
                        left_boundary = -1
                    width = right_boundary - left_boundary - 1
                    area = width * current_height
                    max_area = max(max_area, area)
                else:
                    stack.append(i)
            else:
                stack.append(i)
        
        if stack:
            right_boundary = len(heights)
            while stack:
                current_height = heights[stack.pop()]
                if stack:
                    left_boundary = stack[-1]
                else:
                    left_boundary = -1
                width = right_boundary - left_boundary - 1
                area = width * current_height
                max_area = max(max_area, area)
        
        return max_area
        