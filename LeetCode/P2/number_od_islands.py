# https://leetcode.com/problems/number-of-islands/description/
# 200. Number of Islands
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def isInbound(row, col):
            return 0 <= row < rows and 0 <= col < cols
        
        # star movt
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                    #   (1, 1), (-1, -1), (1, -1), (-1, 1)]
      
        islands = 0
        # turn the visited islands into 0 to mark it is connected 
        # to another island
        # those not connected will be found later

        def dfs(row, col):
            grid[row][col] = "0"

            for c1, c2 in directions:
                new_row = row + c1
                new_col = col + c2

                # must be in bound and must be connected to the island
                if isInbound(new_row, new_col) and grid[new_row][new_col] != "0":
                    dfs(new_row, new_col)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    islands += 1
                    # mark those connected to it as 0
                    dfs(i, j)

        return islands

print(Solution().numIslands(
    [["0", "1"],["1", "0"]]
))