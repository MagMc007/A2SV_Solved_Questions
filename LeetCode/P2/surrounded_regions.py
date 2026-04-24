# https://leetcode.com/problems/surrounded-regions/description/
# 130. Surrounded Regions
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def isInbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def dfs(row, col):
            if not isInbound(row, col) or board[row][col] != "O":
                return 

            # protect the edge
            board[row][col] = "P"

            for c1, c2 in directions:
                new_row, new_col = row + c1, col + c2

                dfs(new_row, new_col)
            
        # go over all edges and coll dfs
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols -1)
        
        for j in range(cols):
            dfs(0, j)
            dfs(rows - 1, j)
        
        # change all unprotected O to X 
        # switch protected ones back to 0

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "P":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"