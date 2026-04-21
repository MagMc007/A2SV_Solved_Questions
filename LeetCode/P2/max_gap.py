# https://leetcode.com/problems/maximum-gap/description/
# 164. Maximum Gap
class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return 0
        
        mx = max(nums)
        mn = min(nums)
        bucket = [0] * (mx + 1)

        
        # mark the indices that exist
        for i in nums:
            bucket[i] = 1
        prev = mn
        max_ = 0

        for i in range(mn, mx + 1):
            if bucket[i]:
                # print(i - prev)
                # record the difference
                max_ = max(i - prev, max_)
                prev = i

        return max_

print(Solution().maximumGap([2,2,2, 1]))