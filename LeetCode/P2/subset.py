# https://leetcode.com/problems/subsets/description/
# 78. Subsets
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        array = []

        def backtrack(idx, comp):
            array.append(comp.copy())

            for i in range(idx, len(nums)):
                comp.append(nums[i])
                backtrack(i+1, comp)
                comp.pop()

        backtrack(0, [])
        return array


        