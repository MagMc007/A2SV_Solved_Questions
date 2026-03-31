# https://leetcode.com/problems/subsets-ii/description/
# 90. Subsets II
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subset = []

        def backtrack(idx, subs):
            if idx == len(nums):
                subset.append(subs[:])
                return
            
            # choose, no choose
            # chose
            subs.append(nums[idx])
            backtrack(idx+1, subs)
            subs.pop()

            # no choose
            while idx + 1 < len(nums) and nums[idx] == nums[idx+1]:
                idx += 1
            
            backtrack(idx+1, subs)
            
        backtrack(0, [])
        return subset