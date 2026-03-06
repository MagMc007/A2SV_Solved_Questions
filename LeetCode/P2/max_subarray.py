# https://leetcode.com/problems/maximum-subarray/
# 53. Maximum Subarray
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_ = float("-inf")

        pref = 0

        for i in range(len(nums)):
            pref += nums[i]
            max_ = max(pref, max_)

            # if the current pref lessthan 0, then it contributes
            # nothing to the next except making it smaller
            # so ignore it
            if pref < 0:
                pref = 0
                
        return max_

print(Solution().maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))