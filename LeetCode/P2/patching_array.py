# https://leetcode.com/problems/patching-array/description/
# 330. Patching Array
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        miss = 1

        i = 0

        while miss <= n:
            # no gap
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else: # there is a gap
                miss += miss
                patches += 1
        return patches