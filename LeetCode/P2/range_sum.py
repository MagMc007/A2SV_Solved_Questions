# https://leetcode.com/problems/range-sum-query-2d-immutable/description/
# 304. Range Sum Query 2D - Immutable
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # one more row and col at the beggining
        self.pref = [[0] * (len(matrix[0]) + 1) for _ in range(1 + len(matrix))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # above, to its left and then remove diagonal, then add the number from the original arr
                #                       left            above               diagonal             
                self.pref[i+1][j+1] = self.pref[i][j+1] + self.pref[i+1][j] - self.pref[i][j] + matrix[i][j]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # take the whole to [r2][c2] then remove the ones above and the ones beside
        # [r2][c2] - [r2][c1-1] - [r1-1][c2] + [r1][c1]
        ans = self.pref[row2 + 1][col2 + 1] - self.pref[row2 + 1][col1] - self.pref[row1][col2 + 1] + self.pref[row1][col1]
        
        return ans

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)