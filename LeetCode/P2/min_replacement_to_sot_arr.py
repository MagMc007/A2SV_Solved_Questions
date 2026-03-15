# https://leetcode.com/problems/minimum-replacements-to-sort-the-array/description/
# 2366. Minimum Replacements to Sort the Array
from math import ceil

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        # start from the back
        n = len(nums)
        splits = 0

        # track what the next number must be == or less
        max_min = nums[-1]

        for j in range(n-2, -1, -1): # we do not touch the last, it is the biggest
            # divide to parts
            parts = ceil(nums[j] / max_min)
            splits += parts - 1
            
            if parts == 0:
                continue
            # what to compare to next
            max_min = nums[j] // parts

        return splits
