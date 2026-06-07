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
        dummy = head

        map_of_nodes = {}
        while dummy:
            map_of_nodes[dummy] = Node(dummy.val)
            dummy = dummy.next
        
        dummy = head
        while dummy:
            new_node = map_of_nodes[dummy]
            new_node.next = map_of_nodes.get(dummy.next, None)
            new_node.random = map_of_nodes.get(dummy.random, None)
            dummy = dummy.next
        
        return map_of_nodes.get(head, None)


