# https://leetcode.com/problems/subsets/
# 78. Subsets
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = [[], ]

        def backtrack(idx, subs):
            # base case
            if idx == len(nums):
                return 
        
            for i in range(idx, len(nums)):
                subs.append(nums[i])
                subset.append(subs[:])
                backtrack(i+1, subs)
                subs.pop()
 
        backtrack(0, [])
        return subset


# time: O(n * (2**n))
# space: O(n * (2**n)) 
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i):          
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)
            
        subset = []
        res = []
        dfs(0)
        return res
'''

# 