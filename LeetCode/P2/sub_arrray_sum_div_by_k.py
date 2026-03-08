# https://leetcode.com/problems/subarray-sums-divisible-by-k/description/
# 974. Subarray Sums Divisible by K
from collections import Counter


class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        # store the pref sum @ step and look them up 
        # as remainders
        hash = Counter()
        hash[0] = 1 

        pref = 0
        cnt = 0

        for right in range(len(nums)):
            pref += nums[right]

            if pref % k in hash:
                cnt += hash[pref % k]
            
            hash[pref % k] += 1
             
        return cnt
    

print(Solution().subarraysDivByK(nums = [4,5,0,-2,-3,1], k = 5))