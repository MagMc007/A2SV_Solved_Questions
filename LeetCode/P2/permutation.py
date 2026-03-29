# https://leetcode.com/problems/permutations/description/
# 46. Permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(idx, permutation):
            # base case
            if len(permutation) == len(nums):
                ans.append(permutation[:])
                return 

            for i in nums:
                if i in permutation:
                    continue

                permutation.append(i)
                backtrack(idx+1, permutation)
                permutation.pop()
            
        backtrack(0, [])
        return ans
    
'''
time: O(n*n!) # for each numbers the branching will be n!
space: O(n*n!) # at each step in n! i am storing n elements into ans 
'''