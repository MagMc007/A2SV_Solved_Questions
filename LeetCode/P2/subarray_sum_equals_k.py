# https://leetcode.com/problems/subarray-sum-equals-k/description/
# 560. Subarray Sum Equals K
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # no 2 ptr no sliding window, the constraint
        # says there will be -ves

        # store the prefixes before a current pref
        hash = defaultdict(int) 

        cnt = 0
        pref = 0

        for i in range(len(nums)):
            pref += nums[i]

            # the current pref may be equal
            if pref == k:
                cnt += 1

            # from the current pref, we remove a previous
            # pref to get k
            if hash[pref-k]:
                cnt += hash[pref-k]

            hash[pref] += 1
        
        return cnt
    

soln = Solution()
print(soln.subarraySum(nums = [1,1,-1,1,1,1], k = 3))


# time: O(n)
# space: O(n)





