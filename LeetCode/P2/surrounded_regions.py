# https://leetcode.com/problems/surrounded-regions/description/
# 130. Surrounded Regions
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        toMod = []

        # to check if it is inbound
        def isInbound(row, col):
            return 0 <= row < rows and 0 <= col < cols
        
        def isOnEdge(row, col):
            return row == 0 or col == 0 or row == rows - 1 or col == cols - 1
        
        # in the dfs we look for any connected region that is on the edge
        # use return true/false to check that
        def dfs(row, col):
            visited.add((row, col))

            if isOnEdge(row, col):
                return False
            
            stat = True  # in false from the 4 dxns will invalidate this

            for c1, c2 in directions:
                new_row, new_col = row + c1, col + c2
                
                if isInbound(new_row, new_col) and (new_row, new_col) not in visited and board[new_row][new_col] == "O":
                    stat = stat and dfs(new_row, new_col)

            # in all 4 dxns not on edge
            if stat:
                toMod.append((row, col))
                return True
            return False
                    
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and not isOnEdge(i, j):
                    visited = set()
                    dfs(i, j)
        for i,j in toMod:
            board[i][j] = "X"        
        print(board)

Solution().solve( [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]])


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