# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.pre_order_dfs(root)

        return root
    
    def pre_order_dfs(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        dummy = root.left
        root.left = root.right
        root.right = dummy

        self.pre_order_dfs(root.left)
        self.pre_order_dfs(root.right)


        