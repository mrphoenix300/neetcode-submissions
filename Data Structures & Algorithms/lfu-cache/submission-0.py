class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _insert(self, node: Node):
        prev_tail = self.tail.prev
        node.prev = prev_tail
        node.next = self.tail
        prev_tail.next = node
        self.tail.prev = node

    def _remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def is_empty(self) -> bool:
        return self.head.next == self.tail


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}       
        self.frequencies = {}  
        self.min_freq = 0      

    def _update(self, node: Node):
        old_freq = node.freq
        
        self.frequencies[old_freq]._remove(node)
        
        if old_freq == self.min_freq and self.frequencies[old_freq].is_empty():
            self.min_freq += 1
            
        node.freq += 1
        
        if node.freq not in self.frequencies:
            self.frequencies[node.freq] = DoublyLinkedList()
        self.frequencies[node.freq]._insert(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._update(node)
            return

        if len(self.cache) >= self.capacity:
            lru_list = self.frequencies[self.min_freq]
            node_to_delete = lru_list.head.next
            lru_list._remove(node_to_delete)
            del self.cache[node_to_delete.key]

        new_node = Node(key, value)
        new_node.freq = 1
        self.cache[key] = new_node
        
        if 1 not in self.frequencies:
            self.frequencies[1] = DoublyLinkedList()
        self.frequencies[1]._insert(new_node)
        
        self.min_freq = 1

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)