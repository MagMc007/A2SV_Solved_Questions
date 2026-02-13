# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
# 1351. Count Negative Numbers in a Sorted Matrix
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negatives = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    negatives += 1

        return negatives