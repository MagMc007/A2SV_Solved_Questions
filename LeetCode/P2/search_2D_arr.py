# https://leetcode.com/problems/search-a-2d-matrix/description/
# 74. Search a 2D Matrix
class Solution:
    def getCol(self, row, target):
        left = 0
        right = len(row) - 1

        while left <= right:
            mid = (left + right) // 2

            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

    def getRow(self, matrix, target):
        # looking for the right most element less than target
        up = 0
        down = len(matrix) - 1
        ans = 0

        while up <= down:
            mid = (up + down) // 2

            if matrix[mid][0] <= target:
                ans = mid
                up = mid + 1
            else:
                down = mid - 1
        
        return ans

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row = self.getRow(matrix, target)
        return self.getCol(matrix[row], target)
    

print(Solution().getCol([1, 3], 3))
# print(Solution().searchMatrix([[1, 3]], 3))
# print(Solution().getRow([[1],[2]], 2))
# print(Solution().getRow([[1],[2]], 2))