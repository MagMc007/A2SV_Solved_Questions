# https://leetcode.com/problems/minimum-moves-to-reach-target-score/description/
# 2139. Minimum Moves to Reach Target Score
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        left = target

        # would be optimal if i choose the half and check whether 
        # it is a perfect double or not
        for _ in range(maxDoubles):
            if left == 1:
                return moves
            
            val = left // 2
            moves += 1 + (left % 2)
            left = val
        
        if left == 1:
            return moves
    
        moves += left - 1
        return moves

print(Solution().minMoves(1, 0))