# https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/
# 1589. Maximum Sum Obtained of Any Permutation
class Solution:
    def maxSumRangeQuery(self, nums: list[int], requests: list[list[int]]) -> int:
        nums.sort(reverse=True)
        # compute the repetition of the indices in requests
        reqs = [0] * (len(nums) + 1)

        for l, r in requests:
            reqs[l] += 1
            reqs[r + 1] -= 1
        
        # compute pref sum of reqs
        pref_req = []
        curr_sum = 0

        for i in reqs:
            curr_sum += i
            pref_req.append(curr_sum)
        
        pref_req.sort(reverse=True)

        max_ = 0
        for i in range(len(nums)):
            max_ += pref_req[i] * nums[i]
        
        return max_ % (7 + 10**9)
    

print(Solution().maxSumRangeQuery(nums = [1,2,3,4,5], requests = [[1,3],[0,1]]))