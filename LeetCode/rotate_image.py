# https://leetcode.com/problems/rotate-image/description/
# 48. Rotate Image
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # we will do 4 swaps at once
        # we can complete it on a signle row
        cols = len(matrix[0])
        
        for c in range(cols - 1):
            for r in range()




        