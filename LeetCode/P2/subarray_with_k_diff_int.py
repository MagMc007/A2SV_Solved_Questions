# https://leetcode.com/problems/subarrays-with-k-different-integers/
# 992. Subarrays with K Different Integers
from collections import Counter


class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        # keep count of each number in a subarray
        cnt = Counter()
        total = 0

        # it will be a sliding window with 3 ptrs
        far_left = 0
        near_left = 0
        
        for right in range(len(nums)):
            cnt[nums[right]] += 1
            
            # track new numbers that are making it extra 
            while len(cnt) > k:
                cnt[nums[near_left]] -= 1

                # near_left is out of bound of good subarray
                if cnt[nums[near_left]] == 0:
                    cnt.pop(nums[near_left])

                near_left += 1
                far_left = near_left
            
            # if there is extra count, then subarray will still be good
            while cnt[nums[near_left]] > 1:
                cnt[nums[near_left]] -= 1
                near_left += 1
                
            if len(cnt) == k:
                total += near_left - far_left + 1

        return total

       
soln = Solution()
print(soln.subarraysWithKDistinct(nums=[1,2,1,2,3], k=2))
