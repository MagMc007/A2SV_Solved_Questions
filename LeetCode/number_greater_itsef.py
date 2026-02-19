# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/
# 1365. How Many Numbers Are Smaller Than the Current Number
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_sorted = sorted(nums)
        
        output = []

        for i in nums:
            output.append(nums-sorted.index(i))