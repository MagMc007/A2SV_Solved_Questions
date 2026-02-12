# https://leetcode.com/problems/set-matrix-zeroes/description/
# 73. Set Matrix Zeroes
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # iterate over each and record the row and columns there is 0 at
        # iterate again and change the elements to 0

        row_0 = set()
        col_0 = set()
        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    row_0.add(row)
                    col_0.add(col)
        
        for row in range(rows):
            for col in range(cols):
                if row in row_0 or col in col_0:
                    matrix[row][col] = 0

soln = Solution()
print(soln.setZeroes(matrix = [[1,1,1],[1,0,1],[1,1,1]]))