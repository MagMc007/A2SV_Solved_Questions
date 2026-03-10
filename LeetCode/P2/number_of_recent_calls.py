# https://leetcode.com/problems/number-of-recent-calls/description/
# 933. Number of Recent Calls
from collections import deque

class RecentCounter:
    def __init__(self):
        self.q = deque()
        
    def ping(self, t: int) -> int:
        self.q.append(t)
        low_bound = t - 3000

        while self.q[0] < low_bound:
            self.q.popleft()
                
        return len(self.q)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)