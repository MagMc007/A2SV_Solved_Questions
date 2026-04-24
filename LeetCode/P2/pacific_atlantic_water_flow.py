# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
# 417. Pacific Atlantic Water Flow
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        # with out a doubt 2 can flow in
        ans = [[0, cols-1], [rows-1, 0]]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # i must start from the edges
        
