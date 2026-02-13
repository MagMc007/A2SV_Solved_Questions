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
        n =  cols - 1
        
        # will need 2 iterations
        # n//2 times for the outer and n - 1 time for the inner to make 
        # the rotation possible

        for i in range(cols//2):  # takes it in wards like constrict
            # for the rotation on a single row
            for j in range(cols - 1):
                # we do 4 swaps here
                temp = matrix[i][j]
                # swap1
                matrix[i + j][n - i], temp = temp, matrix[i + j][n - i]
                # swap 2
                matrix[n - i][n - i - j], temp = temp, matrix[n - i][n - i - j]
                # swap 3
                matrix[n - i - j][i], temp = temp, matrix[n - i - j][i]
                # swap 4
                matrix[i][i + j] = temp
            






        