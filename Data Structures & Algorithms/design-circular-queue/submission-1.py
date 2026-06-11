class Node:

    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.front = None
        self.rear = None
        

    def enQueue(self, value: int) -> bool:
        if self.size == 0:
            self.front = Node(value)
            self.rear = self.front
            self.size += 1
            return True
        
        if self.size == self.capacity:
            return False

        self.rear.next = Node(value)
        self.rear = self.rear.next
        self.size += 1

        return True


    def deQueue(self) -> bool:
        if self.size == 0:
            return False

        if self.front == self.rear:
            self.rear = None
            self.front = None 
            self.size -= 1
            return True

        self.front = self.front.next
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        
        return self.front.val
        

    def Rear(self) -> int:
        if self.size == 0:
            return -1

        return self.rear.val    

    def isEmpty(self) -> bool:
        return True if self.size == 0 else False
        

    def isFull(self) -> bool:
        return True if self.size == self.capacity else False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()