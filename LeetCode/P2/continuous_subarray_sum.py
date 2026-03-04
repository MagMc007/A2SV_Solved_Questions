# https://leetcode.com/problems/continuous-subarray-sum/description/
# 523. Continuous Subarray Sum
from collections import defaultdict


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # record remainder at each index of the prefix sum        
        hash = defaultdict(int)
        prefix_sum = 0
        
        # the theory is if 2 different numbers have the same remaider when
        # divided by k, then their difference would be div by k
        for i, num in enumerate(nums):
            prefix_sum += num
            rem = prefix_sum % k
            
            if rem == 0 and i >= 1:
                return True
            
            if rem in hash:
                # it is in the hash so the one in between is div by k
                if i - hash[rem] >= 2:
                    return True
            else:
                hash[rem] = i
        
        return False