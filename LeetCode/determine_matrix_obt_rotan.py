# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/description/
# 1886. Determine Whether Matrix Can Be Obtained By Rotation
class Solution:
    def rotate(self, matrix):
        # 4 swaps
        # how many times?? nxn so n // 2 times
        cols = len(matrix[0])
        times = cols // 2
        n = cols - 1

        for i in range(times):
            for j in range(cols - 1):
                # we do 4 swaps here
                temp = matrix[i][i + j]
                # swap1
                matrix[i + j][n - i], temp = temp, matrix[i + j][n - i]
                # swap 2
                matrix[n - i][n - i - j], temp = temp, matrix[n - i][n - i - j]
                # swap 3
                matrix[n - i - j][i], temp = temp, matrix[n - i - j][i]
                # swap 4
                matrix[i][i + j] = temp

            cols -= 2 # @ a time we complete swapping of 2 cols
        return matrix
    
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        if mat == target:
            return True
        
        # we only need to rotate a max of 3x 
        for _ in range(3):
            mat = self.rotate(mat)
            if mat == target:
                return True
        return False

soln = Solution()
print(soln.rotate([[0,1],[1,0]]))