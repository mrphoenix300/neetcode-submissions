# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        i = 1
        f = head
        while f and f.next:
            i += 1
            f = f.next

        if i == 1:
            head = None
            return head
        
        if i == n:
            return head.next

        prev, curr = None, head
        target_index = i - n % i
        j = 0

        while curr:
            if j == target_index:
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next
                break
            prev = curr
            curr = curr.next
            j += 1

        return head






        

        

        
        
        