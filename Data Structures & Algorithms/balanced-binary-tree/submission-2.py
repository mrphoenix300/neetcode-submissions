# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        self.is_balanced = True

        def dfs(curr: Optinal[TreeNode]) -> int:
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            if abs(left - right) > 1:
                self.is_balanced = False

            return 1 + max(left, right)
        
        dfs(root)
        
        return True if self.is_balanced else False
        

        