class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        for row in board:
            filtered = [v for v in row if v != "."]
            if len(filtered) != len(set(filtered)):
                return False

        for col in zip(*board):
            filtered = [v for v in col if v != "."]
            if len(filtered) != len(set(filtered)):
                return False
        
        for box_row in range(0, 9, 3):           # 0, 3, 6
            for box_col in range(0, 9, 3):       # 0, 3, 6
                box = []
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        box.append(board[r][c])
                # now `box` is a flat list of 9 cells from one real 3x3 region
                filtered = [v for v in box if v != "."]
                if len(filtered) != len(set(filtered)):
                    return False

        return True 

        