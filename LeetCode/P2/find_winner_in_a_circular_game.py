# https://leetcode.com/problems/find-the-winner-of-the-circular-game/
# 1823. Find the Winner of the Circular Game
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        def get_winner(n, k):
            if n == 0:
                return 0
            
            return (get_winner(n-1, k) + k) % k
        
        return get_winner(n, k) + 1
    
'''
    time: O(n)
    space: O(n) cos of the call stack
'''