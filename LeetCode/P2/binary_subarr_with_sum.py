# https://leetcode.com/problems/binary-subarrays-with-sum/description/
# 930. Binary Subarrays With Sum
from collections import Counter


class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        # use hash map to store the previous sums and remove
        hash = Counter()
        hash[0] = 1  # refering to empty array

        pref_sum = 0
        cnt = 0

        for i in nums:
            pref_sum += i

            # curr_sum - prev = goal
            # curr - goal = prev
            if pref_sum - goal in hash:
                cnt += hash[pref_sum - goal]
            
            hash[pref_sum] += 1
 
        return cnt
              
print(Solution().numSubarraysWithSum(nums = [1,0,1,0,1], goal = 2))