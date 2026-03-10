# https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/description/
# 2526. Find Consecutive Integers from a Data Stream
from collections import deque
class DataStream:
    def __init__(self, value: int, k: int):
        # must be of size k at all times
        # keep only vals = value
        self.value = value
        self.len = k
        self.q = deque()
        
    def consec(self, num: int) -> bool:
        if num != self.value:
            self.q = deque()
            return False

        self.q.append(num)

        while len(self.q) > self.len:
            self.q.popleft()
        
        if len(self.q) == self.len:
            return True
        
        return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)