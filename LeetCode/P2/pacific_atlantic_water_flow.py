# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
# 417. Pacific Atlantic Water Flow
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def inBound(r, c):
            return 0 <= r < rows and 0 <= c < cols
        
        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]
        
        # separately tackle those that reach pacific starting from 
        # atlantic

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(r, c, ocean):
            ocean[r][c] = True
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # inbound, not visited, heigh must opposite
                if (inBound(nr, nc) and
                    not ocean[nr][nc] and
                    heights[nr][nc] >= heights[r][c]):
                    
                    dfs(nr, nc, ocean)

        # Pacific (top row to left column)
        for c in range(cols):
            dfs(0, c, pacific)
        for r in range(rows):
            dfs(r, 0, pacific)
        
        # Atlantic (bottom row to right column)
        for c in range(cols):
            dfs(rows - 1, c, atlantic)
        for r in range(rows):
            dfs(r, cols - 1, atlantic)

        result = []
        for r in range(rows):
            for c in range(cols):
                if pacific[r][c] and atlantic[r][c]:
                    result.append([r, c])
        
        return result
        
