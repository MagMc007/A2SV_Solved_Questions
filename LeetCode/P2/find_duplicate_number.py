# https://leetcode.com/problems/find-the-duplicate-number/
# 287. Find the Duplicate Number
from collections import Counter


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # no soring at all
        # double for loop would work O(n**2)
        cnt = Counter(nums)
        for k, v in cnt.items():
            if v > 1:
                return k


# time: O(n)
# space: O(n)

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # fast and slow pointer from linked list
        # floyd
        slow, fast = 0, 0

        # till they intersect
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow
        
# time: O(n)
# space: O(1)