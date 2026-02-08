# https://leetcode.com/problems/single-number/description/
# 136. Single Number
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # count and identify the ones with count > 1
        ctr = Counter(nums) 

        for k,v in ctr.items():
            if v == 1:
                return k