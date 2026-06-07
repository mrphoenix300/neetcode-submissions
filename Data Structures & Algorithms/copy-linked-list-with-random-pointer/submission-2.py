"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        nodes = []
        all_nodes = {}

        dummy = Node(head.val)
        nodes.append(dummy)
        all_nodes[head] = dummy

        curr = head.next
        length = 1

        while curr:
            node = Node(curr.val)
            nodes.append(node)
            all_nodes[curr] = node
            curr = curr.next
            length += 1

        curr = head
        i = 0
        while i < length - 1:
            nodes[i].next = nodes[i + 1]
            if curr.random in all_nodes:
                nodes[i].random = all_nodes[curr.random]
            else:
                nodes[i].random = None
            curr = curr.next
            i += 1

        if curr:
            if curr.random in all_nodes:
                nodes[i].random = all_nodes[curr.random]
            else:
                nodes[i].random = None

        return dummy


