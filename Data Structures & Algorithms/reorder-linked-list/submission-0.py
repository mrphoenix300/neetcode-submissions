# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        s, f = head, head
        s_index = 0
        f_index = 0

        while s:

            while f.next and f.next.next:
                f = f.next
                f_index += 1
            if f_index == s_index:
                break
            tempNode = s.next
            s.next = f.next
            f.next.next = tempNode
            f.next = None
            s_index += 1
            f_index = s_index
            s = s.next.next
            f = s


