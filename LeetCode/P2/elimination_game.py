# https://leetcode.com/problems/elimination-game/description/
# 390. Elimination Game
class Solution:
    def lastRemaining(self, n: int) -> int:
        if n == 1:
            return 1
        
        return 2 * ((n // 2 + 1) - self.lastRemaining(n//2))
    
# time: O(logn) it halves at every step
# space: O(1)