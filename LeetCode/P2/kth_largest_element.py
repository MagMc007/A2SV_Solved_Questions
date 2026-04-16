# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
# 215. Kth Largest Element in an Array
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums.sort(reverse=True)

        for i in nums:
            k -= 1
            
            if not k:
                return i
            
# print(Solution().findKthLargest(nums = [3,2,3,1,2,4,5,5,6,6], k = 2))
