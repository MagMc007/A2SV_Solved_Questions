# https://leetcode.com/problems/sort-colors/description/
# 75. Sort Colors
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # insertion sort
        n = len(nums)
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]