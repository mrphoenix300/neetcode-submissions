# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visitedNode = {}

        tail = head
        i = 0

        while tail:
            if tail not in visitedNode:
                visitedNode[tail] = i
                i += 1
            else:
                break
            tail = tail.next
        
        return False if tail is None else True