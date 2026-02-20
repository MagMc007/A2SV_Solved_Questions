# https://leetcode.com/problems/majority-element-ii/description/
# 229. Majority Element II
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority = len(nums) // 3
        nums = Counter(nums)
        answer = []

        for num, num_count in nums.items():
            if num_count > majority:
                answer.append(num)
        return answer