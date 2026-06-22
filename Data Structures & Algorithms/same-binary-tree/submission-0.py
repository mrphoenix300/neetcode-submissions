# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        self.is_same = True

        def dfs(curr1, curr2):
            if not curr1 and not curr2:
                return
            elif not curr1:
                self.is_same = False
                return
            elif not curr2:
                self.is_same = False
                return 
            
            if curr1.val != curr2.val:
                self.is_same = False
                return
            
            dfs(curr1.left, curr2.left)
            dfs(curr1.right, curr2.right)
        
        dfs(p, q)
        return True if self.is_same else False
            


        