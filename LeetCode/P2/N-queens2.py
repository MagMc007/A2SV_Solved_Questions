# https://leetcode.com/problems/n-queens-ii/description/
# 52. N-Queens II
class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = [False] * n
        posDiag = [False] * (2*n - 1)  # r - c + (n-1)
        negDiag = [False] * (2*n - 1)  # r + c
        
        # board = [["."] * n for _ in range(n)]
        result = 0

        def backtrack(r):
            nonlocal result
            # base case
            if r == n:
                result += 1
                return
            
            for c in range(n):
                posD = r - c + (n - 1)
                negD = r + c
                
                if cols[c] or posDiag[posD] or negDiag[negD]:
                    continue
                
                # place queen
                cols[c] = posDiag[posD] = negDiag[negD] = True
                # board[r][c] = "Q"
                
                backtrack(r + 1)
                
                # remove queen (backtrack)
                cols[c] = posDiag[posD] = negDiag[negD] = False
                # board[r][c] = "."

        backtrack(0)
        return result