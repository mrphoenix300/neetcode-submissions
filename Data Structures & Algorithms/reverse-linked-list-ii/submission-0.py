# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        prev, curr = None, head
        for i in range(1, left):
            prev = curr
            curr = curr.next
        connection = prev
        tail = curr

        for i in range(left, right + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        tail.next = curr
        
        if connection:
            connection.next = prev
            return head
        else:
            return prev
                
        



        