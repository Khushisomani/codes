class MyCircularQueue:

    def __init__(self, k: int):
        self.q=collections.deque()
        self.s=k
      
    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if len(self.q)<self.s:
            self.q.append(value)
            return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if len(self.q)>0:
            self.q.popleft()
            return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if len(self.q)>0:
            return self.q[0]
        else:
            return -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if len(self.q)>0:
            return self.q[-1]
        else:
            return -1
    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if len(self.q)>0:
            return False
        else:
            return True
    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if len(self.q)==self.s:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()