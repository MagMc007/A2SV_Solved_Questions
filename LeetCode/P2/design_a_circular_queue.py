# https://leetcode.com/problems/design-circular-deque/description/?envType=problem-list-v2&envId=queue
# 641. Design Circular Deque
class MyCircularDeque:
    def __init__(self, k: int):
        self.limit = k
        self.q = []

    def insertFront(self, value: int) -> bool:
        if len(self.q) < self.limit:
            self.q.insert(0, value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.q) < self.limit:
            self.q.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if self.q:
            self.q.pop(0)
            return True
        return False

    def deleteLast(self) -> bool:
        if self.q:
            self.q.pop()
            return True
        return False

    def getFront(self) -> int:
        if self.q:
            return self.q[0]
        return -1

    def getRear(self) -> int:
        if self.q:
            return self.q[-1]
        return -1

    def isEmpty(self) -> bool:
        if self.q:
            return False
        return True
        
    def isFull(self) -> bool:
        if len(self.q) == self.limit:
            return True
        return False
        
# btw  i could have resused is full and is empty on 4 occassions

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