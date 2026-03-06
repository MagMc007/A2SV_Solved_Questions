# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/description/?envType=problem-list-v2&envId=prefix-sum
# 1413. Minimum Value to Get Positive Step by Step Sum

class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        strt = 0

        pref = 0

        for i in nums:
            pref += i

            # all that we need is to keep the curr_sum > 1
            if pref < 1:
                strt += 1 - pref
                pref = 1
        if not strt:
            return 1
        return strt


print(Solution().minStartValue([-3,2,-3,4,2]))

# time - O(n)
# space - O(1)