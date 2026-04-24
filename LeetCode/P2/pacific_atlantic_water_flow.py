# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
# 417. Pacific Atlantic Water Flow
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        ans = []

        # we will have 2 dxns
        # up or left
        pacific = [(0, -1), (-1, 0)]
        # right or down
        atlantic = [(0, 1), (1, 0)]
        