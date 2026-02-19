# https://leetcode.com/problems/largest-perimeter-triangle/description/
# 976. Largest Perimeter Triangle
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # There is a math theorem
        # for a traingle, the sums of any 2 sides must be 
        # greater than the other
        nums.sort()

        max_perim = 0

        for i in range(len(nums) - 2):
            side1 = nums[i]
            side2 = nums[i + 1]
            side3 = nums[i + 2]

            if side1 + side2 > side3:
                max_perim = side1 + side2 + side3
            
        return max_perim


