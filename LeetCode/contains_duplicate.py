# https://leetcode.com/problems/contains-duplicate/description/
# 217. Contains Duplicate
from collections import Counter


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = Counter(nums)
        for value in nums.values():
            if value > 1:
                return True
        return False
        