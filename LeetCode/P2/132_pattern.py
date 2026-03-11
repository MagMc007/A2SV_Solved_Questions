# https://leetcode.com/problems/132-pattern/description/
# 456. 132 Pattern
class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        # but i'll use monotonic  || decreasing
        stack = []  # track the minimum along side the current elm
        min_ = nums[0]  # this will be the i

        for i in nums[1:]:
            while stack and i >= stack[-1][0]:
                stack.pop()

            if stack and stack[-1][1] < i:
                return True
            
            stack.append((i, min_))
            min_ = min(min_, i)
        return False
            
print(Solution().find132pattern([3,1,4,2]))