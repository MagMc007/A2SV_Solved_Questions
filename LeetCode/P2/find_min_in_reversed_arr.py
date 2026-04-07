# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
# 153. Find Minimum in Rotated Sorted Array
class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1 

        # rotation forces the smallest to be to the right always
        # if not it the left that means it was rotated n times
        while left < right:
            mid = (left + right) // 2

            if nums[right] > nums[mid]:
                # search to the left
                right = mid
            else:
                left = mid + 1

        return nums[left]

print(Solution().findMin([3,1,2]))