# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/
# 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # for each element we do an increasing and monotonic
        # decreasing queues
        mon_inc = deque() 
        mon_dec = deque()
        left = 0
        ans = 0

        for right in range(len(nums)):
            # make the increasing monotone
            while mon_dec and mon_inc and mon_inc[-1] < nums[right]:
                mon_inc.pop()
            
            mon_inc.append(nums[right])

            # make the decresing monotone
            while mon_dec[-1] > nums:
                mon_dec.pop()
            
            mon_dec.append(nums[right])

            # now we have the smallest and the biggest element
            # of the subarray
            diff = abs(mon_dec[0] - mon_inc[0])

            if diff > limit:
                if mon_dec[0] == nums[left]:
                    mon_dec.popleft()
                else:
                    mon_inc.popleft()
                
                left += 1
            
            ans = max(ans, right - left + 1)
        return ans


