class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.size=k
        self.q=collections.deque()
        self.busy=0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if len(self.q)<self.size:
            self.q.appendleft(value)
            return True
        else:
            return False
    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if len(self.q)<self.size:
            self.q.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if len(self.q)>0:
            self.q.popleft()
            return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if len(self.q)>0:
            self.q.pop()
            return True
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if len(self.q)>0:
            s=self.q[0]
            return s
        else:
            return -1
        

    def getRear(self) -> int:
        if len(self.q)>0:
            s=self.q[-1]
            return s
        else:
            return -1
        

    def isEmpty(self) -> bool:
        if len(self.q)==0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if len(self.q)==self.size:
            return True
        else:
            return False

      
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()