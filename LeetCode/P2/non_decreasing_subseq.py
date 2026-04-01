# https://leetcode.com/problems/non-decreasing-subsequences/description/?envType=problem-list-v2&envId=backtracking
# 491. Non-decreasing Subsequences
class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        ans = []

        def backtrack(idx, arr):
            if len(arr) >= 2:
                ans.append(arr[:])

            used = set()

            for i in range(idx, len(nums)):
                if nums[i] in used:
                    continue

                if not arr or nums[i] >= arr[-1]:
                    used.add(nums[i])
                    arr.append(nums[i])
                    backtrack(i+1, arr)
                    arr.pop()
                
        backtrack(0, [])

        return ans

print(Solution().findSubsequences([4,4,3,2,1]))