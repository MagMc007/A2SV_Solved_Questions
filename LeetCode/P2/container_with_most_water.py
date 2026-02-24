# https://leetcode.com/problems/container-with-most-water/description/
# 11. Container With Most Water
class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0
        j = len(height) - 1
        max_area = 0

        while i < j:
            area = min(height[i], height[j]) * (j - i)
            max_area = max(area, max_area)

            if height[j] < height[i]:
                j -= 1
            else:
                i += 1
                
        return max_area