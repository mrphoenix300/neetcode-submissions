# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        queue = deque([root])
        res = []
        curr_level = 0

        while queue:
            len_q = len(queue)
            res.append([])

            for _ in range(len_q):
                node = queue.popleft()
                res[curr_level].append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            curr_level += 1
        
        return res
