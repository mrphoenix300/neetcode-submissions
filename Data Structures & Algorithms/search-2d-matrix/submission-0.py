class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left_row = 0
        right_row = len(matrix) - 1

        while left_row <= right_row:
            left_col = 0
            right_col = len(matrix[left_row]) - 1
            mid_row = (left_row + right_row) // 2
            while left_col <= right_col:
                mid_col = (left_col + right_col) // 2
                
                if matrix[mid_row][mid_col] == target:
                    return True
                elif matrix[mid_row][mid_col] > target:
                    right_row = mid_row - 1
                    right_col = mid_col - 1
                else:
                    left_row = mid_row + 1
                    left_col = mid_col + 1
        
        return False
        