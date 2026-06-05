# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        previous, current = None, slow
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        left, right = head,previous
        while right.next:
            temp1,temp2 = left.next, right.next
            left.next = right
            right.next = temp1
            left,right = temp1, temp2