# https://leetcode.com/problems/transpose-matrix/submissions/1533539874/?utm_source=chatgpt.com
# 867. Transpose Matrix
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # inintialize the empty transpose
        row = len(matrix)
        col = len(matrix[0])
        transpose_matrix = [[0] * row for _ in range(col)]

        # push into the transpose 
        for r in range(row):
            for c in range(col):
                # if it is a square matrix 
                if row == col:
                    transpose_matrix[r][c] = matrix[c][r]
                else:
                    transpose_matrix[c][r] = matrix[r][c]

        return transpose_matrix