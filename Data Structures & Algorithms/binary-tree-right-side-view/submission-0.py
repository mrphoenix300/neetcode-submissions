# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        queue = deque([root])
        res = []

        while queue:
            right_side = None
            len_q = len(queue)

            for _ in range(len_q):
                node = queue.popleft()
                
                if node:
                    right_side = node
                    queue.append(node.left)
                    queue.append(node.right)

            if right_side:
                res.append(right_side.val)
        
        return res
