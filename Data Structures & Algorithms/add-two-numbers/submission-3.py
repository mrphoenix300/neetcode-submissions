# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1 = 0
        multi1 = 1
        curr = l1
        while curr:
            num1 += (multi1 * curr.val)
            multi1 *= 10
            curr = curr.next
        
        num2 = 0
        multi2 = 1
        curr = l2
        while curr:
            num2 += (multi2 * curr.val)
            multi2 *= 10
            curr = curr.next
        
        num = num1 + num2
        
        head = ListNode(0)
        curr = head

        while num != 0:
            last_digit = num % 10
            curr.val = last_digit
            num //= 10
            if num != 0:
                curr.next = ListNode(0)
                curr = curr.next
            
        
        return head



        